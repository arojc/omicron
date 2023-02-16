from matplotlib import style, pyplot as plt, animation as animation
from pingonizer import Pingonizer
import threading

class Drawer :

    xs = []
    ys = []
    p = None

    def __init__(self, l) :
        for i in range(l) :
            self.ys.append(0)
        self.xs = range(l)
        self.p = Pingonizer()

    def animate(self, i, ax1):

        self.ys.pop(0)
        self.ys.append(self.p.ping_with_pythonping("192.168.4.90"))

        ax1.clear()
        ax1.plot(self.xs, self.ys)

    def draw (self) :
        style.use('fivethirtyeight')

        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)

        ani = animation.FuncAnimation(fig, self.animate, fargs=[ax1,], interval=1000)
        plt.show()

    def draw_wrapper (self) :
        t = threading.Thread(target=self.draw)
        t.start()

