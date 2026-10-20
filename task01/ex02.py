import numpy as np
#1
black=np.zeros((100, 200), dtype=np.uint8)

#2
white=np.full((100, 200), 255, dtype=np.uint8)

#3
red=np.full((100, 200,3), (255, 0, 0), dtype=np.uint8)

#4
print(black.shape, black.ndim, black.size, black.nbytes)
print(white.shape, white.ndim, white.size, white.nbytes)
print(red.shape, red.ndim, red.size, red.nbytes)

#5
#1920*1080*3 = 6220800
print("Memory usage for a 1920x1080 RGB image:", 1920*1080*3, "bytes")
#12000000*3
print("Memory usage for a 12000000 pixel image:", 12000000*3, "bytes")
color = np.zeros((1080, 1920, 3), dtype=np.uint8)
print(color.nbytes, "bytes")
color12 = np.zeros((3000, 4000, 3), dtype=np.uint8)
print(color12.nbytes, "bytes")

#6
b = np.arange(12).reshape(3, 4)
print(b)
print(b.sum())
print(b.sum(axis=0))
print(b.sum(axis=1))
print(b[2, 3], b[-1, -1])
#- `axis=0`: Calculates the sum of each column.
#-`axis=1`: Calculates the sum of each row.