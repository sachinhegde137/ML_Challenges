import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


if __name__ == '__main__':
    F, N = map(int, input().split())

    x = []
    y = []

    for _ in range(N):
        data = list(map(float, input().split()))
        x.append(data[:-1])
        y.append(data[-1])

    T = int(input())
    x_test = []
    for _ in range(T):
        data = list(map(float, input().split()))
        x_test.append(data)

    poly = PolynomialFeatures(degree=3)
    x_poly = poly.fit_transform(x)
    x_testpoly = poly.transform(x_test)

    model = LinearRegression()
    model.fit(x_poly, y)

    predicted = model.predict(x_testpoly)

    for p in predicted:
        print(f"{p:.2f}")