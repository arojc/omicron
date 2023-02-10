import os
import subprocess
import threading
import time
import pythonping

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


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
        t = threading.Thread(target=self.run_the_batch, args=(path,))
        t.start()

    def run_the_batch(self, path) :
        subprocess.run([path])

    def ping_directly(self, hostname, parameters):
        command = "ping " + hostname
        for key in parameters:
            command += " -" + key + " " + parameters[key]
        response = os.system(command)
        print(response)

    def animate(ax1, i):
        graph_data = open('example.txt', 'r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(float(x))
                ys.append(float(y))
        ax1.clear()
        ax1.plot(xs, ys)

    def draw_a_live_graph(self, address):
        style.use('fivethirtyeight')

        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)

        self.animate(ax1)

        ani = animation.FuncAnimation(fig, self.animate, interval=1000)
        plt.show()

    def measure_rtt(self, address):
        while True :
            time.sleep(0.2)
            x = self.ping_with_pythonping(address)
            print("%0.5f - %0.5f" % (x, 1000*x))

    def ping_with_pythonping(self, address):
        response = pythonping.ping(address, verbose=False)
        return response.rtt_avg

    def run_the_thread_directly(self, hostname):
        t = threading.Thread(target=self.ping_directly, args=(hostname,))
        t.start()





#write_the_files(1000)

#p = Pingonizer()
#parameters = {"w" : "3000", "l" : "1000", "n" : "1"}
#p.measure_rtt("192.168.4.90")
#p.draw_a_live_graph("192.168.4.90")




style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('example.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines[0:i]:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))

    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()


