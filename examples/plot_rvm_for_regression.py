#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=========================================================
RVM for regression
=========================================================
from https://github.com/ctgk/PRML
"""
print(__doc__)

# Authors: X
# License: BSD 3 clause

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.metrics import mean_squared_error, r2_score
from sklearn_rvm import RVR


def create_toy_data(n=10):
    x = np.linspace(0, 1, n)
    t = np.sin(2 * np.pi * x) + np.random.normal(scale=0.1, size=n)
    return x, t


x_train, y_train = create_toy_data(n=50)
x = np.linspace(0, 1, 100)

model = RVR(kernel='rbf')
model.fit(x_train[:, None], y_train)

y, y_std = model.predict(x[:, None], return_std=True)

plt.scatter(x_train, y_train, facecolor="none", edgecolor="g", label="training")
plt.scatter(x[:, None],y, s=100, facecolor="none", edgecolor="b", label="relevance vector")
plt.plot(x[:, None], y, color="r", label="predict mean")
plt.fill_between(x, y - y_std, y + y_std, color="pink", alpha=0.2, label="predict std.")
plt.legend(loc="best")
plt.show()