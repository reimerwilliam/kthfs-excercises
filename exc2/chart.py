import Tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Chart(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.display_grid = tk.IntVar()
        self.__create_chart()
        self.__create_grid_control()   

    def __create_chart(self):
        self.figure = Figure(dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.chart_type = FigureCanvasTkAgg(self.figure, self)
        self.chart_type.get_tk_widget().grid(row=0, column=0)

    def draw(self):
        self.figure.canvas.draw()

    def __create_grid_control(self):
        def handleCheck():
            self.ax.grid(bool(self.display_grid.get()))
            self.draw()

        checkbutton = tk.Checkbutton(self, text='Show grid', variable=self.display_grid, command=handleCheck)
        checkbutton.grid(row=1, column=0)


    