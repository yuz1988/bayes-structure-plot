from matplotlib import pyplot as plt
import numpy as np

dataName = 'hepar2'
tree = np.loadtxt(dataName + '/tree.txt', dtype=float)

tree_global_2 = np.loadtxt(dataName + '/tree-global-2.txt', dtype=float)
tree_global_4 = np.loadtxt(dataName + '/tree-global-4.txt', dtype=float)
tree_global_8 = np.loadtxt(dataName + '/tree-global-8.txt', dtype=float)

tree_local_2 = np.loadtxt(dataName + '/tree-local-2.txt', dtype=float)
tree_local_4 = np.loadtxt(dataName + '/tree-local-4.txt', dtype=float)
tree_local_8 = np.loadtxt(dataName + '/tree-local-8.txt', dtype=float)

tree_uniform_2 = np.loadtxt(dataName + '/tree-uniform-2.txt', dtype=float)
tree_uniform_4 = np.loadtxt(dataName + '/tree-uniform-4.txt', dtype=float)
tree_uniform_8 = np.loadtxt(dataName + '/tree-uniform-8.txt', dtype=float)

x = range(100, 1001*100, 100)

plt.figure(figsize=(8, 5))

plt.plot(x, tree)

plt.plot(x, tree_global_2)
plt.plot(x, tree_global_4)
plt.plot(x, tree_global_8)

plt.plot(x, tree_local_2)
plt.plot(x, tree_local_4)
plt.plot(x, tree_local_8)

plt.plot(x, tree_uniform_2)
plt.plot(x, tree_uniform_4)
plt.plot(x, tree_uniform_8)

plt.xlim(0, 14000)

legend_labels = ['w/o sampling', 'global-2', 'global-4', 'global-8', 'local-2', 'local-4', 'local-8',
                 'uniform-2', 'uniform-4', 'uniform-8']

plt.xlabel('number of training instances (alarm)')
plt.ylabel('KL-Divergence (relative to ground truth)')
plt.legend(legend_labels)
plt.savefig('graph/' + dataName + '-vertical-sampling.png')