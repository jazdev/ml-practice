import numpy as np

print "numpy version = ", np.version.full_version

###############################################
a = np.array([0,1,2,3,4,5])

print "a = ", a

print "a.ndim = ", a.ndim

print "a.shape = ", a.shape

###############################################
print "Reshaping a and saving to b"

b = a.reshape((3,2))

print "b = ", b

print "b.ndim = ", b.ndim

print "b.shape = ", b.shape

###############################################
print "Reshaping a and copy() to c"

c = a.reshape((3,2)).copy()

print "c = ", c

###############################################
print "a*2 = ", a*2

print "a**2 = ", a**2

###############################################

