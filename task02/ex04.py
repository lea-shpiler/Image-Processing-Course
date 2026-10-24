import sys
import cv2


if len(sys.argv) != 2:
    print("Usage: python ex04.py <string>")
    exit(1)

print(f"image file: {sys.argv[1]}")

img = cv2.imread(sys.argv[1])
if img is None:
    print("failed to read image")
    exit(1)

print(f"Image type: {type(img)}")
print(f"Image dtype: {img.dtype}")
print(f"Image shape: {img.shape}")