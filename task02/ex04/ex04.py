import sys
import cv2
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    print("Usage: python ex04.py <image file>")
    exit(1)

print(f"image file: {sys.argv[1]}")

img = cv2.imread(sys.argv[1])

# Part 2
if img is None:
    print("failed to read image")
    exit(1)

# Part 1
print(f"Image type: {type(img)}")
print(f"Image dtype: {img.dtype}")
print(f"Image shape: {img.shape}")
print(f"Pixel value at (0, 0): {img[0, 0]}")  

# Part 3
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Without conversion")

plt.subplot(1, 2, 2)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title("With RGB conversion")

plt.show()

# Part 4
# Part 4
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title("Original image")

plt.subplot(2, 2, 2)
plt.imshow(img[:, :, 0], cmap="gray")
plt.title("Blue channel")

plt.subplot(2, 2, 3)
plt.imshow(img[:, :, 1], cmap="gray")
plt.title("Green channel")

plt.subplot(2, 2, 4)
plt.imshow(img[:, :, 2], cmap="gray")
plt.title("Red channel")

plt.savefig("ex04.png")
plt.show()


# Part 5
img_gray = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)

print(f"Grayscale image shape: {img_gray.shape}")