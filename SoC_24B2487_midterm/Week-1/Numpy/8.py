import numpy as np
a=np.ones([3,2])
b=np.full([2,3],3)
print(np.matmul(a,b))
#find det
c=np.identity(3)
print(np.linalg.det(c))
