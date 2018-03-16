from matplotlib import pyplot as plt
import numpy as np

dataName = '1Mdata'
tree = np.loadtxt(dataName + '/tree.txt', dtype=float)

tree_uniform_8 = np.loadtxt(dataName + '/tree-uniform-8.txt', dtype=float)
tree_uniform_16 = np.loadtxt(dataName + '/tree-uniform-16.txt', dtype=float)
tree_uniform_18 = np.loadtxt(dataName + '/tree-uniform-18.txt', dtype=float)

x = range(1000, 1001*1000, 1000)

plt.figure(figsize=(8, 5))

plt.plot(x, tree, '-')

plt.plot(x, tree_uniform_8)
plt.plot(x, tree_uniform_16)
plt.plot(x, tree_uniform_18, ':')

plt.xlim(0, )

legend_labels = ['tree w/o sampling', 'uniform-8', 'uniform-16', 'uniform-18']

plt.xlabel('number of training instances (1M alarm data)')
plt.ylabel('KL-Divergence (relative to ground truth)')
plt.legend(legend_labels)
plt.savefig('graph/' + dataName + '-uniform-vs-nosample.png')