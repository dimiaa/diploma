import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
class Karaushev3d:

    """
    Keyword arguments:
    Qe -- расход воды в потоке выше выпуска сточных вод
    Qst -- расход сточных вод
    Vsr -- средняя скорость течения
    Sst -- концентрация вещества
    Se -- фоновая концентрация
    H -- средняя глубина водного объекта
    B -- ширина водного объекта
    D -- коэффициент турбулентной диффузии
    C -- коэффициент Шези
    M -- коэффициент Маннинга
    """
    def __init__(self, Qe, Qst, Vsr, Sst, Se, H, B, C, length):
        self.Qe = Qe
        self.Qst = Qst
        self.Vsr = Vsr
        self.Sst = Sst
        self.Se = Se
        self.H = H
        self.B = B
        self.D = None
        self.C = C
        self.M = None
        self.g = 9.81
        self.length = length
        self.arr = None
        self.deltaZ = None
        self.deltaX = None
        self.countZ = None
        self.countX = None

    def pre_calculate(self):

        if self.C <= 60:
            self.M = 0.7 * self.C + 6
        else:
            self.M = 48

        self.D = self.g * self.H * self.Vsr / (self.M * self.C)

        delta = self.Qst / self.Vsr
        self.deltaZ = self.Qst / (self.H * self.Vsr)
        self.deltaZ = round(self.deltaZ, 1)
        deltaY = self.deltaZ

        self.deltaX = (0.25 * self.Vsr * self.deltaZ * self.deltaZ) / self.D
        # deltaOmega = self.deltaZ * deltaY
        # Nz - количество загрязненных клеток
        # Nz = math.ceil(delta / deltaOmega)
        # N - общее количество клеток
        # N = math.ceil((self.B * self.H) / deltaOmega)

        self.countX = math.ceil(self.length / self.deltaX)
        self.countZ = math.ceil(self.H / self.deltaZ)

        self.arr = np.zeros((self.countZ, self.countX))
        self.arr[:] = self.Se

        self.arr[0][0] = self.Sst

        # print(f"deltaZ = deltaY = {self.deltaZ}, deltaX = {self.deltaX}, x = {0}, step = {0}")
        # print(self.arr)
        return self.arr, self.deltaX

    def calculate_iteration(self, x, step):
        tmp = np.zeros((self.countZ, self.countX))
        for i in range(self.countZ):
            for j in range(self.countX):
                tmp[i][j] = (self.get(self.arr, i, j + 1) + self.get(self.arr, i, j - 1) +
                             self.get(self.arr, i + 1, j) + self.get(self.arr, i - 1, j)) / 4
        self.arr = tmp

        # print(f"x = {x}, step = {step}")
        # print(self.arr)
        x += self.deltaX
        step += 1
        return self.arr, x, step

    def get(self, arr, i, j):
        if i >= len(arr):
            i = len(arr) - 1
        if j >= len(arr[0]):
            j = len(arr[0]) - 1

        if i < 0:
            i = 0
        if j < 0:
            j = 0

        return arr[i][j]
