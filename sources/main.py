from sources import karaushev3d, LinearRegression
from utils import XLSXHelper
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    data = XLSXHelper.read_excel("../dataset.xlsx")

    d = data.copy()
    cols = [0, 11]
    d.drop(d.columns[cols], axis=1, inplace=True)

    X = d.copy()
    X.drop(X.columns[9], axis=1, inplace=True)
    Y = d.copy()
    cols = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    Y.drop(Y.columns[cols], axis=1, inplace=True)

    x_train, x_test, y_train, y_test = train_test_split(X.values, Y.values, train_size=40)
    y_train = y_train.reshape(40, 1)
    # print(x_train)
    # y_train = y_train.T
    # print(y_train)
    # y_test = y_test.T

    lr = LinearRegression.LinReg()
    lr.fit(x_train, y_train)

    for i in range(1, 40):

        t = karaushev3d.Karaushev3d(d.values[i][0], d.values[i][1], d.values[i][2], d.values[i][3], d.values[i][4],
                                    d.values[i][5], d.values[i][6], d.values[i][7], d.values[i][8])

        start_arr, dx = t.pre_calculate()
        # rc = XLSXHelper.write_excel("output.xlsx", start_arr.tolist(), 0, 0, t.deltaZ)
        length = 0
        x, step = 0.0, 0
        # xticklabels = HeatmapPlotter.gen_xticklabels(t.countX, t.deltaX)
        # ticklabels = HeatmapPlotter.gen_yticklabels(t.deltaZ, t.countZ)

        # HeatmapPlotter.heatmap(start_arr, yticklabels, xticklabels, step, cmap="Purples", cbarlabel="Концентрация вещества")

        while x < t.length + dx:
            tmp_x, tmp_step = x, step
            arr, x, step = t.calculate_iteration(x, step)
            # rc = XLSXHelper.write_excel("output.xlsx", arr.tolist(), x, step, t.deltaZ, rc)
            # HeatmapPlotter.heatmap(arr, yticklabels, xticklabels, step, cmap="Purples", cbarlabel="Концентрация вещества")

        print(f"i={i} Полученное методом Караушева значение = {t.arr[0][0]}")
        testX = [[d.values[i][0], d.values[i][1], d.values[i][2], d.values[i][3], d.values[i][4],
                d.values[i][5], d.values[i][6], d.values[i][7], d.values[i][8]]]
        print(f"i{i} Полученной с помощью регрессии = {lr.predict(testX)}")





    #
    # regr = RangomForest.RandomForest()
    # regr.fit(x_train, y_train)
    # # p = Perceptron.model(x_train, y_train)
    #
    # k = karaushev3d.Karaushev3d(224.7, 25.3, 2.44, 100, 0, 6.4, 16, 50.7, 150)
    # # k = karaushev3d.Karaushev3d(27.72, 3.28, 3.40, 326.00, 0.01, 3.20, 50.00, 2.16, 168.00)
    # plot_x = []
    # plot_y = []
    # start_arr, dx = k.pre_calculate()
    # plot_x.append(0)
    # plot_y.append(start_arr[0][0])
    # x, step = 0.0, 0
    # while x < k.length + dx:
    #     tmp_x, tmp_step = x, step
    #     arr, x, step = k.calculate_iteration(x, step)
    #     plot_x.append(x)
    #     plot_y.append(arr[0][0])
    #
    # gr = GraphPlotter.GraphPlotter(plot_x, plot_y)
    # gr.plot()
    #
    #
    # # testX = [[224.7, 25.3, 2.44, 100, 0, 6.4, 16, 50.7, 150]]
    # testX = [[27.72, 3.28, 3.40, 326.00, 0.01, 3.20, 50.00, 2.16, 168.00]]
    # print(f"Linear Reg predict = {lr.predict(x_pred=testX)}")
    # # print(f"Perceptron predict = {p.predict(testX)}")
    # print(f"Rangom Forest Regression = {regr.predict(x_pred=testX)}")
    # print(f"Karaushev predict = {k.arr[0][0]}")
    #
    # testLinReg = LinReg.predict(X)
    # print(testLinReg)
