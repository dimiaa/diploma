import numpy
# import xarray
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import animation
from openpyxl import Workbook
import pandas as pd

import karaushev3d
# from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Расчет разбавления сточных вод")
#
#         button = QPushButton("Press Me!")
#
#
#         self.setCentralWidget(button)
#
#
# def start_application():
#     app = QApplication()
#     window = MainWindow()
#     window.show()
#     app.exec()


# def animate(i):
#     print("animation running...")
#     x, step = 0, 0
#     while x < distance:
#         arr, _x = t.calculate_iteration(x, step)
#         im, cbar = t.heatmap(arr, [], [], ax=ax,
#                            cmap="YlGn", cbarlabel="Концентрация вещества")
#         texts = t.annotate_heatmap(im, valfmt="{x:.1f}")
#         txt_title.set_text('Тепловая карта: x = {0:4d} step={0:4d}')
#         x += _x
#         step += 1
#         fig.clear()



if __name__ == "__main__":
    book = Workbook()
    sheet = book.active

    t = karaushev3d.Karaushev3d(224.7, 25.3, 2.44, 100, 0, 6.4, 16, 50.7,150)
    start_arr, dx = t.pre_calculate()

    sheet['A1'] = f"Kарта распространения вещества: x = 0, step = 0, deltaZ = deltaY = {round(t.deltaZ, 2)}"

    arr_list = start_arr.tolist()

    row_count = 1
    for row in arr_list:
        sheet.append(row)
        row_count += 1

    # df = pd.DataFrame(start_arr)
    # df.to_excel('file.xlsx', index=False, header=False)

    fig, ax = plt.subplots()
    plt.xlabel("Ось y")
    plt.ylabel("Ось z")
    xticklabels = []
    yticklabels = []

    i = 0
    labels = 0
    delta = t.deltaZ
    while i < t.countZ:
        yticklabels.append(labels)
        labels += delta
        labels = round(labels, 2)
        i += 1

    i = 0
    labels = 0
    while i < t.countX:
        xticklabels.append(labels)
        labels += delta
        labels = round(labels, 2)
        i += 1

    txt_title = ax.set_title(f'Kарта распространения вещества: x = 0, step = 0\n'
                             f'deltaZ = deltaY = {round(t.deltaZ, 2)}')
    im, cbar = t.heatmap(start_arr, yticklabels, xticklabels, ax=ax,
                         cmap="Purples", cbarlabel="Концентрация вещества")
    texts = t.annotate_heatmap(im, valfmt="{x:.1f}")
    fig.tight_layout()
    plt.show()
    plt.clf()
    x, step = dx, 1
    row_count += 1
    while x < t.length + t.deltaX:
        tmp_x, tmp_step = x, step
        arr, x, step = t.calculate_iteration(x, step)

        sheet.cell(row=row_count, column=1).value = f'x = {tmp_x:.2f}, step = {tmp_step}'
        row_count += 1
        arr_list = arr.tolist()

        for row in arr_list:
            sheet.append(row)
            row_count += 1

        fig, ax = plt.subplots()
        plt.xlabel("Ось y")
        plt.ylabel("Ось z")
        txt_title = ax.set_title(f'Kарта распространения вещества: x = {tmp_x:.2f}, step = {tmp_step}')
        im, cbar = t.heatmap(arr, yticklabels, xticklabels, ax=ax,
                           cmap="Purples", cbarlabel="Концентрация вещества")
        texts = t.annotate_heatmap(im, valfmt="{x:.1f}")
        fig.tight_layout()
        plt.show()
        plt.clf()

    book.save('file.xlsx')
