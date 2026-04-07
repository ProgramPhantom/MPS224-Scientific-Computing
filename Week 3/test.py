import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

xs = np.linspace(0, 1, 1000)  # x coordinates of points on the graph
fs = xs * (1 - xs)                   # y coordinates of points on the graph
gs = xs * (1 - xs) * (1 - 2*xs)

ax.set_title("Two functions")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.plot(xs, fs, label=r"f(x)", linewidth=3)
ax.plot(xs, gs, label=r"g(x)", linewidth=4)

ax.legend()