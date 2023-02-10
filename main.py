import os
import subprocess
import threading
import time


def write_the_files(N) :
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop\pings')
    paths = []
    for i in range(N) :
        paths.append(desktop + "\omicron_script" + str(i) + ".bat")
        print(paths[i])
        f = open(paths[i], "w")
        command = "ping 192.168.4.90 -w 3000 -n 4 -l " + str(60000+i)
        f.write(command)
        f.close();

class Pingonizer :

    def run_the_thread (self, n) :
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop\pings')
        path = desktop + "\omicron_script" + str(n) + ".bat"
        t = threading.Thread(target=self.run_the_process, args=(path,))
        t.start()

    def run_the_process(self, path) :
        subprocess.run([path])





write_the_files(1000)

p = Pingonizer()
p.run_the_thread(1)
p.run_the_thread(2)
p.run_the_thread(3)
p.run_the_thread(4)
p.run_the_thread(5)