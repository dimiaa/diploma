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
        deltaOmega = self.deltaZ * deltaY
        # Nz - количество загрязненных клеток
        Nz = math.ceil(delta / deltaOmega)
        # N - общее количество клеток
        N = math.ceil((self.B * self.H) / deltaOmega)

        self.countX = math.ceil(self.length / self.deltaX)
        self.countZ = math.ceil(self.H / self.deltaZ)

        self.arr = np.zeros((self.countZ, self.countX))
        self.arr[:] = self.Se


        self.arr[0][0] = self.Sst
        self.arr[1][0] = self.Sst
        self.arr[0][1] = self.Sst
        self.arr[1][1] = self.Sst

        print(f"deltaZ = deltaY = {self.deltaZ}, deltaX = {self.deltaX}, x = {0}, step = {0}")
        print(self.arr)
        return self.arr, self.deltaX

    def calculate_iteration(self, x, step):
        tmp = np.zeros((self.countZ, self.countX))
        for i in range(self.countZ):
            for j in range(self.countX):
                tmp[i][j] = (self.get(self.arr, i, j + 1) + self.get(self.arr, i, j - 1) +
                             self.get(self.arr, i + 1, j) + self.get(self.arr, i - 1, j)) / 4
        self.arr = tmp

        print(f"x = {x}, step = {step}")
        print(self.arr)
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

    def heatmap(self, data, row_labels, col_labels, ax=None,
                cbar_kw=None, cbarlabel="", **kwargs):

        if ax is None:
            ax = plt.gca()

        if cbar_kw is None:
            cbar_kw = {}

        im = ax.imshow(data, **kwargs)

        cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
        cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

        ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
        ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

        ax.tick_params(top=True, bottom=False,
                       labeltop=True, labelbottom=False)

        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
                 rotation_mode="anchor")

        # Turn spines off and create white grid.
        ax.spines[:].set_visible(False)

        ax.set_xticks(np.arange(data.shape[1] + 1) - .5, minor=True)
        ax.set_yticks(np.arange(data.shape[0] + 1) - .5, minor=True)
        ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
        ax.tick_params(which="minor", bottom=False, left=False)

        return im, cbar

    def annotate_heatmap(self, im, data=None, valfmt="{x:.2f}",
                         textcolors=("black", "white"),
                         threshold=None, **textkw):

        if not isinstance(data, (list, np.ndarray)):
            data = im.get_array()

        if threshold is not None:
            threshold = im.norm(threshold)
        else:
            threshold = im.norm(data.max()) / 2.

        kw = dict(horizontalalignment="center",
                  verticalalignment="center")
        kw.update(textkw)

        if isinstance(valfmt, str):
            valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

        texts = []
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
                text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
                texts.append(text)

        return texts



