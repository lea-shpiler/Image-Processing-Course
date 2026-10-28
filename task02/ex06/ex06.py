
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    print("Usage: python ex06.py <image file>")
    sys.exit(1)

filename = sys.argv[1]

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Failed to read image")
    sys.exit(1)


# Part 1
result = img * 1.5

print("Original dtype:", img.dtype)
print("Result dtype:", result.dtype)
print("Original maximum:", img.max())
print("Result maximum:", result.max())

# Part 2
result_uint8 = np.clip(result, 0, 255).astype(np.uint8)

# plt.figure(figsize=(10, 5))

# plt.subplot(1, 2, 1)
# plt.imshow(img, cmap="gray", vmin=0, vmax=255)
# plt.title("Original")

# plt.subplot(1, 2, 2)
# plt.imshow(result_uint8, cmap="gray", vmin=0, vmax=255)
# plt.title("Contrast x 1.5")

# plt.savefig("ex06.png")
# plt.show()


# Part 3
result2 = img * 2

print("Integer multiplication dtype:", result2.dtype)
print("Integer multiplication maximum:", result2.max())

# Part 4
result_half = img * 0.5

print("Half multiplication dtype:", result_half.dtype)
print("Half multiplication maximum:", result_half.max())

# Convert results to valid uint8 images
result2_uint8 = result2
result_half_uint8 = np.clip(result_half, 0, 255).astype(np.uint8)


# Part 5 - Bonus
m = img.mean()

result_contrast = (img.astype(np.float64) - m) * 1.5 + m

result_contrast_uint8 = np.clip(
    result_contrast, 0, 255
).astype(np.uint8)

print("Image mean:", m)
print("Contrast result dtype:", result_contrast.dtype)

# Display all images
plt.figure(figsize=(16, 5))

plt.subplot(1, 5, 1)
plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.title("Original")

plt.subplot(1, 5, 2)
plt.imshow(result_uint8, cmap="gray", vmin=0, vmax=255)
plt.title("Multiply by 1.5")

plt.subplot(1, 5, 3)
plt.imshow(result2_uint8, cmap="gray", vmin=0, vmax=255)
plt.title("Multiply by 2")

plt.subplot(1, 5, 4)
plt.imshow(result_half_uint8, cmap="gray", vmin=0, vmax=255)
plt.title("Multiply by 0.5")

plt.subplot(1, 5, 5)
plt.imshow(result_contrast_uint8, cmap="gray", vmin=0, vmax=255)
plt.title("Contrast x 1.5")

plt.tight_layout()
plt.savefig("ex06.png")
plt.show()