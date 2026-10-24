import numpy as np
x = np.array([100, 200, 250], dtype=np.uint8)

# Part 1

print(x + 10)

print(x + 100)

print(x - 150)

print(x * 2)

print(x.astype(np.int16) + 100)

print(x * 1.5)

print((x * 1.5).dtype)

# Part 2
try:
    print(x + 300)
except (OverflowError, TypeError) as error:
    print(type(error).__name__ + ":", error)

# Part 3
def add_safe(x, b):
    x = x.astype(np.int16)
    result = x + b
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)
    
x = np.array([100, 200, 250], dtype=np.uint8)
print(add_safe(x, 100))
print(add_safe(x, -150))

# Part 4
#First, 100 is added to x.
# This can cause overflow before np.clip is applied, so the result may be incorrect.

# Part 5 

x_int8 = np.array([100, 120, 127], dtype=np.int8)
print("int8 x + 10:")
print(x_int8 + 10)
print("int8 x + 100:")
print(x_int8 + 100)
print("int8 x - 150:")
print(x_int8 - 150)
print("int8 x * 2:")
print(x_int8 * 2)
print("int8 x.astype(np.int16) + 100:")
print(x_int8.astype(np.int16) + 100)
print("int8 x * 1.5:")
print(x_int8 * 1.5)
print("(int8 x * 1.5).dtype:")
print((x_int8 * 1.5).dtype)
print("int8 127 + 1:")
print(np.array([127], dtype=np.int8) + 1)
