#from scapy.all import *
import threading

import pythonping
import scapy.all as scapy
import socket
import subprocess
import ifcfg
import ipaddress
import ifcfg
import json
import re
import datetime
import time

class Spoofer :
    def get_my_ipconfig (self) :
        data = subprocess.check_output(['ipconfig', '/all']).decode('utf-8')
        data = data.strip('\r\n')
        list1 = data.split('\r\n\r\n')
        dict1 = {list1[i] : list1[i+1] for i in range(0, len(list1), 2)}
        dict2 = {}

        for key in dict1.keys() :
            dict2[key] = dict1[key].replace(' ', '').replace('..', '').replace('.:', ':').split('\r\n')

        for x in dict2.values() :
            ip = ""
            mask = ""
            for y in x :
                if("IPv4Address" in y):
                    ip = re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', y)[0]
                if("SubnetMask" in y):
                    mask = re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', y)[0]
                l1 = len(ip)
                l2 = len(mask)
                if(l1 * l2 > 0) :
                    return ip, mask

        return None, None

    def find_all_active_ips_around_me (self) :
        my_ip, my_mask = self.get_my_ipconfig()
        network = my_ip + "/" + my_mask
        my_lan = ipaddress.ip_network(network, False)

        list = []

        for ip in my_lan :
            t = threading.Thread(target=self.check_ip_address, args=(list, ip.exploded, ))
            t.start()

        list.sort()
        #print(list)

        return list

    def write_all_active_ips(self):
        list = self.find_all_active_ips_around_me()

        active_ips = open('list_of_ips.txt', 'w')
        active_ips.write(','.join(list))
        active_ips.close()

    def find_all_new_ips(self):

        list2 = self.find_all_active_ips_around_me()

        active_ips = open('list_of_ips.txt', 'r')
        list1 = active_ips.read().split(",")
        active_ips.close()

        set1 = set(list1)
        set2 = set(list2)

        set3 = set2 - set1
        new_ips = list(set3)
        new_ips.sort()

        new_ips_file = open('new_ips.txt', 'a')
        new_ips_file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        new_ips_file.write("\n")
        new_ips_file.write(','.join(new_ips))
        new_ips_file.write("\n")
        new_ips_file.write("\n")
        active_ips.close()

        new_ips = open('list_of_ips.txt', 'w')
        new_ips.write(','.join(list2))
        active_ips.close()

    def monitor(self):
        #self.write_all_active_ips()
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Started: {date}")

        while True :
            time.sleep(60)
            self.find_all_new_ips()
            print("New round")


    def check_ip_address(self, list, ip_address):
        #print(f"Start for IP {ip_address}")
        response = pythonping.ping(ip_address, verbose=False)
        if(response.stats_packets_lost < 4) :
            list.append(ip_address)
        #print(f"Finish for IP {ip_address}")

    def spoof (self) :
        A = "192.168.1.254" # spoofed source IP address
        B = "192.168.1.105" # destination IP address
        C = scapy.RandShort() # source port
        D = 80 # destination port
        payload = "yada yada yada" # packet payload

        while True:
            spoofed_packet = scapy.IP(src=A, dst=B) / scapy.TCP(sport=C, dport=D) / payload
            scapy.send(spoofed_packet)

#s = Spoofer()
#s.get_my_ipconfig()
