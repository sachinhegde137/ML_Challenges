
class LeastSquaresRegressionLine:
    def __init__(self):
        self.slope = None
        self.intercept = None

    def fit(self, x_values, y_values):
        n = len(x_values)
        sum_x = sum(x_values)
        sum_y = sum(y_values)
        sum_xy = sum([x*y for x, y in zip(x_values, y_values)])
        sum_x2 = sum([x*x for x in x_values])

        numerator = n * sum_xy - (sum_x * sum_y)
        denominator = n * sum_x2 - (sum_x ** 2)

        self.slope = numerator / denominator
        self.intercept = (sum_y / n) - (self.slope * (sum_x / n))

    def predict(self, x_value):
        if self.slope and self.intercept:
            return self.slope * x_value + self.intercept
        else:
            raise ModuleNotFoundError("predict is not found, call fit() before predict")


if __name__ == '__main__':
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))

    model = LeastSquaresRegressionLine()
    model.fit(x_list, y_list)

    x_test = int(input())
    y_value = model.predict(x_test)
    print(f"The value of y is: {y_value:.1f}")