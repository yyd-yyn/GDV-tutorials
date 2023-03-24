import numpy as np
import cv2

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

result = A @ B
print(result, end="\n\n")

result = A * B
print(result, end="\n\n")

A = np.array([[1, 2, 3]])
B = np.array([[5, 6, 7]])

result = A @ np.transpose(B)
print(result, end="\n\n")

result = np.transpose(A) @ B
print(result, end="\n\n")

result = A * B
print(result, end="\n\n")


# load image
img = cv2.imread('data/images/Bumbu_Rawon.jpg', cv2.IMREAD_GRAYSCALE)

img_crop = img[3:8, 3:8]
img5x5 = cv2.resize(img, (5, 5))
eye5x5 = np.identity(5, np.uint8)

print(img5x5, img_crop, eye5x5)

print(img_crop * eye5x5)  # element-wise
print(img_crop @ eye5x5)  # matrix multiplication

col = cv2.getGaussianKernel(5, 1.0)
col = np.zeros((5, 1), np.uint8)
col[0] = 1
col[1] = 2
col[2] = 3
col[3] = 4
col[4] = 5
print('##############################')
print('col', col)
row = np.transpose(col)
print('row', row)
print('\n col * row', col * row)
print('\n row * col', row * col)
print('col @ row', col @ row)
print('row @ col', row @ col)
