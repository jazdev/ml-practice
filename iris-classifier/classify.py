from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']

plength = features[:, 2] # petal length

is_setosa = (target == 0) # if target == setosa

max_setosa =plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()

print('Maximum of setosa: {0}.'.format(max_setosa))
print('Minimum of others: {0}.'.format(min_non_setosa))

#
# a very simple model that separates the Iris Setosa flowers from the other two species 
#
for e in features[:,2]:
	if e <= max_setosa: 
		print 'Iris Setosa'
	else: 
		print 'Iris Virginica or Iris Versicolour'
 

#select only the non-Setosa features and labels
target = target[~is_setosa]
virginica = (target == 2) # if target == setosa

#
# a better prediction model 
#
best_acc = -1.0
for fi in xrange(features.shape[1]):
	# We are going to generate all possible threshold for this feature
	thresh = features[:,fi].copy()
	thresh.sort()
	# Now test all thresholds:
	for t in thresh:
		pred = (features[:,fi] > t)
		print pred
		tmp = (pred == virginica)
		print tmp
		acc = tmp.mean()
		if acc > best_acc:
			best_acc = acc
			best_fi = fi
			best_t = t

print best_fi
print best_t