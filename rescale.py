import cv2 as cv

# Hàm rescale
# Nhận vào frame video hoặc ảnh, trả về frame, ảnh đã được scale
def rescaleFrame(frame, scale=1.2):
    # Có thể thay đổi kích thước của image, video, live video
    width=int(frame.shape[1]*scale) 
    height=int(frame.shape[0]*scale)
    dimentions=(width,height)

    return cv.resize(frame,dimentions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    # Chỉ có thể thay đổi live video
    cap.set(3,width)
    cap.set(4,height)


# # Đọc ảnh
# img = cv.imread("image/anhto1.jpg")
# imgRescale=rescaleFrame(img)

# # Hiển thị ảnh
# cv.imshow("Anh", img)
# cv.imshow("Anh rescale", imgRescale)
# cv.waitKey(0)
# cv.destroyAllWindows()

# Đọc hình
cap=cv.VideoCapture('video/videoplayback.mp4')
while True:
    isTrue, frame= cap.read() # Đọc từng khung hình, trả về false nếu hết video
    frameRescale=rescaleFrame(frame)

    cv.imshow('video',frame) # Hiển thị từng khung hình
    cv.imshow('video rescale',frameRescale)


    if cv.waitKey(20) & 0xFF==ord('q'): # Chờ 20ms để hiện khung hình tiếp theo, nếu bấm Q thì thoát màn hình
        break

cap.release() # Xóa con trỏ lưu tới video
cv.destroyAllWindows() # Tắt màn hình