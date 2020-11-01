#!/usr/bin/env python

import random
import numpy as np
from matplotlib import pyplot as plt


def timeSuffix():
    from datetime import datetime
    timeformat = "%d%m%Y_%H-%M-%S"
    return datetime.now().strftime(timeformat)

class Continuous_uniform():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.timeformat = "%d%m%Y_"

    def f(self, x):
        return 1 / (self.b - self.a)

    def F(self, x):
        return (self.b - self.a)*x + self.a
    
    def random(self):
        y = random.random()
        return self.F(y)

def plot_histogram(a, b, data, func, beans=20, fig_name=None):
    if (fig_name is None):
        from datetime import date
        fig_name = "histogram_{}.png".format(timeSuffix())
        
    plt.hist(data, beans, density=True)
    plt.plot(np.linspace(a, b, 50), [func(x) for x in np.linspace(a, b, 50)])
    plt.savefig(fig_name)

a, b = 0, 10
samples=10000
cu = Continuous_uniform(a, b)
data = [cu.random() for x in range(samples)]
plot_histogram(a, b, data, cu.f, fig_name='test.png')

# plt.hist(data)
# plt.plot(np.linspace(0, 10), [cu.F(x) for x in np.linspace(0, 10)])
# plt.savefig('test.png')

# x = np.random.randn(1000)
# fig = plt.figure()
# ax = fig.add_subplot()
# n, bins, rectangles = ax.hist(x, 50, density=True)
# fig.canvas.draw()
# plt.savefig('test.png')

