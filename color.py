import cv2 as cv

img = cv.imread("image/anh1.jpg")
cv.imshow("Anh", img)

# Chuyển ảnh sang màu xám
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("Gray", gray)

# Làm mờ ảnh
blur = cv.GaussianBlur(
    img, (3, 3), cv.BORDER_DEFAULT
)  # Thông số thứ 2(k-size) phải có giá trị là 2 số lẻ
cv.imshow("Blur", blur)

# Hiển thị cạnh của ảnh
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

# Giãn kích thước cạnh trắng của ảnh
dilated = cv.dilate(canny, (7, 7), iterations=1)
cv.imshow("Dilated", dilated)

# Co kích thước cạnh trắng của ảnh
eroded = cv.erode(dilated, (7, 7), iterations=1)
cv.imshow("Eroded", eroded)


cv.waitKey(0)
cv.destroyAllWindows()
