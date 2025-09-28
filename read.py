import cv2 as cv

# Đọc ảnh
img = cv.imread("image/anhto1.jpg")

# Hiển thị ảnh
cv.imshow("Anh", img)
cv.waitKey(0)
cv.destroyAllWindows()


# # Đọc hình
# cap=cv.VideoCapture('video/videoplayback.mp4')
# while True:
#     isTrue, frame= cap.read() # Đọc từng khung hình, trả về false nếu hết video
#     cv.imshow('video',frame) # Hiển thị từng khung hình

#     if cv.waitKey(20) & 0xFF==ord('q'): # Chờ 20ms để hiện khung hình tiếp theo, nếu bấm Q thì thoát màn hình
#         break

# cap.release() # Xóa con trỏ lưu tới video
# cv.destroyAllWindows() # Tắt màn hình