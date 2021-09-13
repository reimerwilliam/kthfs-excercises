from chart import Chart
import os
import matplotlib.animation as animation
import csv

class ResultChart(Chart):
    def __init__(self, master):
        Chart.__init__(self, master)
        self.rows = []
        self.list_x = []
        self.list_raw = []
        self.list_by_q = []
        self.ax.set_title('Live graph of topic: "/kthfs/result"')
        self.read_file()
        self.start_anim()
        self.ax.legend()

    def read_file(self):
        with open(os.path.join(os.path.realpath('.'), '../exc1/data.csv'), 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                self.rows.append(row)

        # remove headers
        self.rows.pop(0)

    def start_anim(self):
        def animate(i):
            raw, by_q = (s.strip() for s in self.rows[i])
            self.list_raw.append(float(raw))
            self.list_by_q.append(float(by_q))
            self.list_x.append(i)
            self.ax.plot(self.list_x, self.list_raw, label='Raw value', color='#000000')
            self.ax.plot(self.list_x, self.list_by_q, label="Divided by q", color="#007bff")
    
        anim = animation.FuncAnimation(self.figure, animate, interval=1000, frames=len(self.rows))
        self.draw()