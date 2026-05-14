import numpy as np
a=np.arange(1,21)
print("Array: ",a)
b=a.reshape(4,5)
print("Reshaped array:\n",np.array(b))
print("shape of array: ",b.shape)
print("Dimension of array: ",b.ndim)
