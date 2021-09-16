import Tkinter as tk
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
        self.control_panel = tk.Frame(self)
        self.control_panel.grid(row=2, column=0)
        self.start_button()
        self.stop_button()
        self.reset_button()

    def read_file(self):
        with open(os.path.join(os.path.dirname(__file__), '../exc1/data.csv'), 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                self.rows.append(row)

        # remove headers
        self.rows.pop(0)

    def start_anim(self):
        # If there is an animation already, start it
        if hasattr(self, 'anim'):
            return self.anim.event_source.start()
        
        # Otherwise create a new animation
        def animate(i):
            raw, by_q = (s.strip() for s in self.rows[i])
            self.list_raw.append(float(raw))
            self.list_by_q.append(float(by_q))
            self.list_x.append(i)
            self.ax.plot(self.list_x, self.list_raw, label='Raw value', color='#000000')
            self.ax.plot(self.list_x, self.list_by_q, label="Divided by q", color="#007bff")
            self.ax.legend()

        anim = animation.FuncAnimation(self.figure, animate, interval=1000, frames=len(self.rows))
        self.anim = anim
        self.draw()

    def stop_anim(self):
        if hasattr(self, 'anim'):
            self.anim.event_source.stop()

    def reset_anim(self):
        self.stop_anim()

        self.ax.lines = []
        self.list_x = []
        self.list_raw = []
        self.list_by_q = []
        
        if hasattr(self, 'anim'):
            delattr(self, 'anim')

        self.draw()

    def start_button(self):
        btn = tk.Button(self.control_panel, text='Start', command=self.start_anim)
        btn.grid(row=0, column=0)

    def stop_button(self):
        btn = tk.Button(self.control_panel, text='Stop', command=self.stop_anim)
        btn.grid(row=0, column=1)
    
    def reset_button(self):
        btn = tk.Button(self.control_panel, text='Reset', command=self.reset_anim)
        btn.grid(row=0, column=2)