import numpy as np
import matplotlib
import matplotlib.pyplot as plt


class GraphPlotter:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plot(self):
        plt.plot(self.x, self.y, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)
        plt.title("График распределения концентрации")
        plt.xlabel("Расстояние (м)")
        plt.ylabel("Концентрация (г/м^3)")
        plt.show()
