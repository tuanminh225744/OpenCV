import cv2 as cv

# Đọc ảnh
img = cv.imread("image/anhto1.jpg")

# Hiển thị ảnh
cv.imshow("Anh", img)
cv.waitKey(0)
cv.destroyAllWindows()
