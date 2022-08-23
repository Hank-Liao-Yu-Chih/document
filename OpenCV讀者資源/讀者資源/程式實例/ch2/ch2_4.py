# ch2_4.py
import cv2

pt_y = 169
pt_x = 118
img = cv2.imread("jk.jpg")      # 彩色讀取
px = img[pt_y, pt_x]            # 讀px點
print(type(px))
print(f"BGR = {px}")





 
