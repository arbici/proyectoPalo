import numpy as np

###################################################
# Modeling: What we want to compute
# points = [(np.array([2]), 4), (np.array([4]), 2)]
# d = 1

# Generate artificial data
true_w = np.array([1, 2, 3, 4, 5])
d = len(true_w)
points = []

for i in range(1000):
    x = np.random.randn(d)
    y = true_w.dot(x) + np.random.randn()
    # print(x, y)
    points.append((x, y))
    # print(points)
    # print(len(points))


def f(w):
    return sum((w.dot(x) - y) ** 2 for x, y in points) / len(points)


def df(w):
    return sum(2 * (w.dot(x) - y) * x for x, y in points) / len(points)

###################################################
# Algorithms: How we compute it


def gradient_descent(f, df, d):
    # Gradient descent
    w = np.zeros(d)
    eta = 0.01
    for t in range(1000):
        value = f(w)
        gradient = df(w)
        w = w - eta * gradient
        print('iteration {}: w = {}, f(w) = {}'.format(t, w, value))


gradient_descent(f, df, d)