import numpy as np

print "numpy version = ", np.version.full_version

###############################################
print "============\nCreating arrays"

a = np.array([0,1,2,3,4,5])

print "a = ", a

print "a.ndim = ", a.ndim

print "a.shape = ", a.shape

###############################################
print "============\nReshaping arrays"

print "Reshaping a and saving to b"

b = a.reshape((3,2))

print "b = ", b

print "b.ndim = ", b.ndim

print "b.shape = ", b.shape

###############################################
print "============\nDeep-copying arrays"

print "Reshaping a and copy() to c"

c = a.reshape((3,2)).copy()

print "c = ", c

###############################################
print "============\nOperations on arrays"

print "a*2 = ", a*2 #operations can be propogated to inner elements

print "c = a**2 = ", a**2

###############################################
print "============\nIndexing Operations"

c=a**2

print "c[np.array([2,3,4])] = ", c[np.array([2,3,4])]

###############################################
print "============\nAccessing data"

print "c > 4 = ", c>4

print "c[c > 4] = ", c[c>4]

###############################################
print "============\nTrimming outliers with clip()"

print "c.clip(0,4) --> ", c.clip(0,4)

###############################################
print "============\nHandling nan's"

d = np.array([1,2,np.NAN,3,4])

print "d = ",d

print "np.isnan(d) --> ", np.isnan(d)

###############################################
print "============\nRemoving nan's"

print "d[- np.isnan(d)] --> ", d[-np.isnan(d)]

###############################################
print "============\nMean of an array"

print "np.mean(d[- np.isnan(d)]) --> ", np.mean(d[- np.isnan(d)])

###############################################
print "============\nDatatypes"

print "d.dtype --> ", d.dtype

###############################################
print "============\nMore basic operations"

e = np.arange(15).reshape(3, 5)

print "e = ", e

print "e.ndim = ", e.ndim

print "e.shape = ", e.shape

print "e.size = ", e.size

print "e.dtype = ", e.dtype

print "e.itemsize = ", e.itemsize

print "e.data = ", e.data

print "type(e) --> ", type(e)

###############################################
print "============\nCreating advanced arrays"














