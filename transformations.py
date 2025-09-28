import cv2 as cv
import numpy as np

# Đọc ảnh
img = cv.imread("image/anh4.jpg")
cv.imshow("Anh", img)

# Thay đổi kích thước khung hình
resized = cv.resize(img, (400, 500))  # Chiều rộng, dài
cv.imshow("Resize", resized)

# Cắt ảnh
cropped = img[50:150, 50:150]
cv.imshow("Cropped", cropped)


# Hàm dịch chuyển ảnh
# x -> right
# -x -> left
# y -> down
# -y -> up
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


translated = translate(img, 100, 100)
cv.imshow("translated", translated)


# Hàm quay ảnh
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:  # Nếu không truyền rotPoint thì lấy tâm ảnh làm tâm xoay
        rotPoint = (width // 2, height // 2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)  # Tạo ma trận xoay 2D
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45)
cv.imshow("rotated", rotated)


# Hàm lật ảnh
# 0 → lật theo trục X (lật dọc, trên ↔ dưới).
# 1 → lật theo trục Y (lật ngang, trái ↔ phải).
# -1 → lật cả hai trục (trên ↔ dưới và trái ↔ phải, tức là xoay 180°).
flipped = cv.flip(img, 0)
cv.imshow("flip", flipped)


cv.waitKey(0)
cv.destroyAllWindows()
