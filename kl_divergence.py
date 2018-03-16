from matplotlib import pyplot as plt
import numpy as np


graph = np.loadtxt('data/graph.txt', dtype=float)
tree = np.loadtxt('data/tree.txt', dtype=float)
tree_1 = np.loadtxt('data/tree-0.1.txt', dtype=float)
tree_5 = np.loadtxt('data/tree-0.5.txt', dtype=float)
tree_9 = np.loadtxt('data/tree-0.9.txt', dtype=float)
x = range(100, 1001*100, 100)

plt.figure(figsize=(8, 5))
# plt.plot(x, graph)
plt.plot(x, tree_1)
plt.plot(x, tree_5)
plt.plot(x, tree_9)
plt.plot(x, tree)
plt.plot(x, graph)
plt.xlim(0, 14000)

legend_labels = ['sample=0.1', 'sample=0.5', 'sample=0.9', 'sample=1 (full data size)', 'non-tree']

plt.xlabel('number of training instances')
plt.ylabel('KL-Divergence (relative entropy distance)')
plt.legend(legend_labels)
plt.savefig('nontree-vs-tree.png')