from sklearn.linear_model import LinearRegression


class LinReg:
    def __init__(self):
        self.reg = LinearRegression()

    def fit(self, X, Y):
        self.reg.fit(X, Y)

    def predict(self, x_pred):
        return self.reg.predict(x_pred)


# class LinearRegression:
#     def __init__(self, learning_rate, number_of_iterations):
#         self.learning_rate = learning_rate
#         self.number_of_iterations = number_of_iterations
#
#     def fit(self, X, Y):
#         self.m, self.n = X.shape
#         self.w = np.zeros((self.n, 1))
#         self.b = 0
#         self.X = X
#         self.Y = Y
#
#         for i in range(self.number_of_iterations):
#             self.update_weights()
#
#     def update_weights(self):
#         Y_prediction = self.predict(self.X)
#
#         dw = -(self.X.T).dot(self.Y - Y_prediction) / self.m
#
#         db = -np.sum(self.Y - Y_prediction) / self.m
#
#         self.w = self.w - self.learning_rate * dw
#         self.b = self.b - self.learning_rate * db
#
#     def predict(self, X):
#         return X.dot(self.w) + self.b
#
#     def print_weights(self):
#         print('Weights for the respective features are :')
#         print(self.w)
#         print()
#
#         print('Bias value for the regression is ', self.b)
