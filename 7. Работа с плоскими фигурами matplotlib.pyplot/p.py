import numpy as np
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt


class Figure:
    fig, ax = plt.subplots()
    patches = []
    resolution = 50  # the number of vertices'

    def __init__(self, *coordinates, r=0, fig_type='polygon'):
        self.coordinates = coordinates
        self.fig_type = fig_type
        self.r = r

    def draw(self):
        for i in self.coordinates:
            figure = Polygon(i)
            Figure.patches.append(figure)
        p = PatchCollection(Figure.patches, alpha=0.4)
        Figure.ax.add_collection(p)
        Figure.ax.plot(10, 10)

    @staticmethod
    def show():
        plt.show()

    @staticmethod
    def gen_rectangle():
        k = 0
        for i in range(100):
            figure = Polygon(([0+k*1.2, 0], [0+k*1.2, 1], [1+k*1.2, 1], [1+k*1.2, 0]))
            Figure.patches.append(figure)
            k += 1
        p = PatchCollection(Figure.patches, alpha=0.4)
        Figure.ax.add_collection(p)
        Figure.ax.plot(10, 10)

    @staticmethod
    def gen_triangle():
        k = 0
        for i in range(100):
            figure = Polygon(([0 + k * 1.2, 1.5], [0.5 + k * 1.2, 2], [1 + k * 1.2, 1.5]))
            Figure.patches.append(figure)
            k += 1
        p = PatchCollection(Figure.patches, alpha=0.4)
        Figure.ax.add_collection(p)
        Figure.ax.plot(10, 10)

    @staticmethod
    def gen_hexagon():
        k = 0
        for i in range(100):
            figure = Polygon(([1 + k * 1.5, 3], [1 + k * 1.5, 3.4], [1.3 + k * 1.5, 3.7], [1.7 + k * 1.5, 3.7], [2 + k * 1.5, 3.4], [2 + k * 1.5, 3], [1.7 + k * 1.5, 2.7], [1.3 + k * 1.5, 2.7]))
            Figure.patches.append(figure)
            k += 1
        p = PatchCollection(Figure.patches, alpha=0.4)
        Figure.ax.add_collection(p)
        Figure.ax.plot(10, 10)


np.random.seed(19680801)

# pol = Figure(([0, 0], [0, 1], [1, 1], [1, 0]), ([3, 3], [0, 6], [3, 6], [9, 5], [9, 4]))
# pol.draw()
Figure.gen_rectangle()
Figure.gen_triangle()
Figure.gen_hexagon()
Figure.show()


