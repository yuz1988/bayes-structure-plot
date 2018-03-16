from matplotlib import pyplot as plt


def f(a):
    return a**2


plt.figure(figsize=(8, 5))
x = range(124, 824, 100)
x = list(map(f, x))
y = [0.961, 3.745, 8.915, 16.483, 26.901, 40.547, 55.966]
plt.plot(x, y, marker='o')
plt.xlabel('square of variables')
plt.ylabel('training time per 100 instances (sec)')
plt.savefig('lineplot.png')