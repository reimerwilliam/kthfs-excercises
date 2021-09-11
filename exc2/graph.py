import matplotlib.pyplot as plt
import numpy as np

class Graph:
    def __init__(self):
        self.x_list = np.linspace(-10, 10, 1000)

    def _lambda(self, t):
        return 5 * np.sin(2 * np.pi * 1 * t)

    def h(self, t):
        return 3 * np.pi * np.exp(-self._lambda(t))

    def show(self):
        y_list = self.h(self.x_list)
        plt.plot(self.x_list, y_list, '-r', label='h(t)')
        plt.title('Graph of h(t)')
        plt.xlabel('t', color='#1C2833')
        plt.ylabel('h', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        plt.show()
