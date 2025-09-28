import cv2 as cv
import numpy as np  # Thư viện dùng để sử lý mảng

blank = np.zeros(
    (500, 500, 3), dtype="uint8"
)  # Tạo ảnh đen, truyền vào chiều dài, rộng, số kênh màu


# cv.imshow("anhden", blank)
# blank[:] = 0, 255, 0  # Đặt mãu màu xanh cho ảnh
# cv.imshow("anhxanh", blank)
# blank[200:300, 300:400] = 0, 0, 255  # Cài vị trí màu của ảnh
# cv.imshow("anhdo", blank)


# # vẽ hình chữ nhật
# cv.rectangle(
#     blank, (0, 0), (250, 250), (0, 255, 0), thickness=2
# )  # Tạo hình chữ nhật, truyền vào ảnh, tọa độ đầu cuối, màu, độ dày
# cv.rectangle(
#     blank, (0, 0), (250, 250), (0, 255, 0), thickness=cv.FILLED
# )  # Tạo hình chữ nhật được tô bên trong, có thể thay cv.FILLED=-1
# cv.rectangle(
#     blank,
#     (0, 0),
#     (blank.shape[1] // 2, blank.shape[0] // 2),
#     (0, 255, 0),
#     thickness=cv.FILLED,
# )  # Tạo hình chữ nhật kích thước bằng 1/2 kich thước gốc
# cv.imshow("hinh chu nhat", blank)


# # Vẽ hình tròn
# cv.circle(
#     blank, (250, 250), 40, (0, 255, 0), thickness=2
# )  # Tạo hình tròn, truyền vào ảnh, tâm, bán kính, độ dày
# cv.imshow("hinh tron", blank)


# # Vẽ đường thẳng
# cv.line(
#     blank, (0, 0), (250, 250), (0, 255, 0), thickness=2
# )  # Tạo đường thẳng, truyền vào ảnh, điểm đầu cuối, màu, độ dày
# cv.imshow("duong thang", blank)


# Viết text
cv.putText(
    blank,
    "hello",
    (255, 255),  # điểm viết
    cv.FONT_HERSHEY_TRIPLEX,  # font
    1.0,  # scale
    (255, 255, 255),  # màu
    thickness=2,
)
cv.imshow("chu", blank)

cv.waitKey(0)
cv.destroyAllWindows()
