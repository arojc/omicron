import os

from pingonizer import Pingonizer
from drawer import Drawer
from spoofer import Spoofer


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


#write_the_files(1000)

#p = Pingonizer()
#parameters = {"w" : "3000", "l" : "1000", "n" : "1"}
#p.measure_rtt("192.168.4.90")
#p.draw_a_live_graph("192.168.4.90")


def fill_the_file_with_fibbonacci () :
    graph_data = open('example.txt','w')
    graph_data.close()
    target = 13

    x = range(1,target)
    y = [0, 1]
    for i in range(2, target) :
        y.append(y[i-1] + y[i-2])

    graph_data = open('example.txt','a')
    for i in y:
        graph_data.write(str(y.index(i)) + "," + str(i) + "\n")

    graph_data.close()



#d = Drawer()
#d.draw()

#style.use('fivethirtyeight')

#fig = plt.figure()
#ax1 = fig.add_subplot(1, 1, 1)

#ani = animation.FuncAnimation(fig, animate, interval=1000)
#plt.show()

#p = Pingonizer()
#for i in range(10) :
    #p.run_the_thread_directly("192.168.4.90", i, 3)

#p = Pingonizer()
#for i in range(100) :
    #p.run_the_thread_directly("192.168.4.90", 50000+i, 30)

#d = Drawer(10)
#d.draw_wrapper()

s = Spoofer()
s.find_all_new_ips()



