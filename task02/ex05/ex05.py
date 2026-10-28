
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    print("Usage: python ex05.py <image file>")
    sys.exit(1)

filename = sys.argv[1]

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Failed to read image")
    sys.exit(1)


def add_safe(x, b):
    x = x.astype(np.int16)
    result = x + b
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)


# Part 1
def brighten(img, b, method):
    if method == "np":
        return img + b
    elif method == "cv2":
        if b >= 0:
            return cv2.add(img, b)
        else:
            return cv2.subtract(img, -b)
    elif method == "clip":
        return add_safe(img, b)
    else:
        raise ValueError("Unknown method")


# Part 2
img_np = brighten(img, 100, "np")
img_cv2 = brighten(img, 100, "cv2")
img_clip = brighten(img, 100, "clip")

plt.figure(figsize=(16, 5))

plt.subplot(1, 4, 1)
plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.title("Original")

plt.subplot(1, 4, 2)
plt.imshow(img_np, cmap="gray", vmin=0, vmax=255)
plt.title("NumPy")

plt.subplot(1, 4, 3)
plt.imshow(img_cv2, cmap="gray", vmin=0, vmax=255)
plt.title("OpenCV")

plt.subplot(1, 4, 4)
plt.imshow(img_clip, cmap="gray", vmin=0, vmax=255)
plt.title("add_safe")

plt.savefig("ex05.png")
plt.show()


# Part 3
# Explanation is written in ex05.md


# Part 4
try:
    img_np_dark = brighten(img, -100, "np")
except OverflowError:
    img_np_dark = None
    print("NumPy: OverflowError")

img_cv2_dark = brighten(img, -100, "cv2")
img_clip_dark = brighten(img, -100, "clip")


# Part 5
plt.figure(figsize=(16, 5))

plt.subplot(1, 4, 1)
plt.imshow(img, cmap="gray")
plt.title("Original")

plt.subplot(1, 4, 2)
plt.imshow(img_np, cmap="gray")
plt.title("NumPy")

plt.subplot(1, 4, 3)
plt.imshow(img_cv2, cmap="gray")
plt.title("OpenCV")

plt.subplot(1, 4, 4)
plt.imshow(img_clip, cmap="gray")
plt.title("add_safe")

plt.savefig("ex05_no_vmin.png")
plt.show()
