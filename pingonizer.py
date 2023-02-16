import os
import threading
import time

import pythonping


class Pingonizer :

    def ping_directly(self, hostname, parameters):
        command = "ping " + hostname
        for key in parameters:
            command += " -" + key + " " + parameters[key]
        response = os.system(command)
        #print(response)

    def run_the_thread_directly(self, hostname, size, number_of):
        parameters = {
            "n": str(number_of),
            "l": str(size)
        }
        t = threading.Thread(target=self.ping_directly, args=(hostname, parameters))
        t.start()

    def measure_rtt(self, address):
        while True :
            time.sleep(0.2)
            x = self.ping_with_pythonping(address)
            print("%0.5f - %0.5f" % (x, 1000*x))

    def ping_with_pythonping(self, address):
        response = pythonping.ping(address, verbose=False)
        return response.rtt_avg



