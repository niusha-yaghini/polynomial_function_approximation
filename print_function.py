import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def f1(x):
    return 4*(x**4) + 3*(x**3) + 2*(x**2) + x

# def f2(x):
    

x = np.linspace(-10, 10, 100)

plt.plot(x, f1(x), color='red')
# plt.plot(x, f2(x), color='blue')

plt.show()