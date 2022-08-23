# ch2_7.py
import cv2

img = cv2.imread("jk.jpg")      # 彩色讀取
cv2.imshow("Before the change", img)
for y in range(img.shape[0]-50, img.shape[0]):
    for x in range(img.shape[1]-50, img.shape[1]):
        img[y, x] = [255, 255, 255]
cv2.imshow("After the change", img)
cv2.waitKey(0)
cv2.destroyAllWindows()









 
