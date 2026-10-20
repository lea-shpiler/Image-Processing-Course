import numpy as np
x = np.array([100, 200, 250], dtype=np.uint8)

#1
#([110 210 4])
print(x + 10)
#([200 44 94])
print(x + 100)
#([206 50 100])
print(x - 150)
#([200 144 244])
print(x * 2)
#([200 300 350])
print(x.astype(np.int16) + 100)
#([150 300 375])
print(x * 1.5)
#float64
print((x * 1.5).dtype)

#2
#print(x + 300)
#Error because 300 is outside the range of uint8.

#3
def add_safe(x, b):
    x = x.astype(np.int16)
    result = x + b
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)
    
x = np.array([100, 200, 250], dtype=np.uint8)
print(add_safe(x, 100))
print(add_safe(x, -150))

#4
#First, 100 is added to x.
# This can cause overflow before np.clip is applied, so the result may be incorrect.

#5
#The range of `int8` is -128 to 127.
#so 127+1 = -128 
