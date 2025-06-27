import numpy as np
a= np.array([1,2,3], dtype='int16')
print(a)
b=np.array([[2.0,3.0,5.0],[4.0,1.0,6.0]])
print(b)
#get dimension
print(b.ndim)
print(b.shape)
print(a.dtype)
print(a.itemsize)
print(a.nbytes)#(no of item*byte per item)