# real time systems
# Lab1
# author: Roman Myronenko
# group: IO-72
# var: 18

import matplotlib.pyplot as plt
from algs import signal, get_m, get_D

# option values
n = 10
omega = 1100
N = 256

range_min = 0
range_max = 1

s_gen = signal(n, omega, N, range_min, range_max)
s = [s_gen(i) for i in range(N)]
m = get_m(s)
D = get_D(s, m)
print(f'm: {m}\nD: {D}')

plt.plot(range(N), s)
plt.show()
