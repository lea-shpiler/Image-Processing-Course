import numpy as np

a = np.array([[10, 100, 200],
              [50, 150, 250]], dtype=np.uint8)

print(a.dtype, a.shape, a.ndim, a.size, a.nbytes,a[1, 2],a[0, 1],a.max()) 

print("a + 10:")
print(a + 10)

print("a - 20:")
print(a - 20)

print("a * 2:")
print(a * 2)

print("a.max(axis=0):")
print(a.max(axis=0))

print("a.max(axis=1):")
print(a.max(axis=1))