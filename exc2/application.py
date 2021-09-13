import Tkinter as tk
from chart import Chart
from result_chart import ResultChart
import numpy as np

class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid(row=0, column=0)
        self.create_h_graph()
        self.create_result_chart()

    def create_h_graph(self):
        def _lambda(t):
            return 5 * np.sin(2 * np.pi * 1 * t)

        def h(t):
            return 3 * np.pi * np.exp(-_lambda(t))

        x_list = np.linspace(-10, 10, 1000)
        y_list = h(x_list)

        chart = Chart(self)
        chart.ax.plot(x_list, y_list)
        chart.ax.set_title('Graph of h(t)')
        chart.grid(row=0, column=0)

    def create_result_chart(self):
        chart = ResultChart(self)
        chart.grid(row=0, column=1)

root = tk.Tk()
app = Application(root)
app.mainloop()