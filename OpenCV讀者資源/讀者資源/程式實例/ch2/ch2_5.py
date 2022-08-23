# ch2_5.py
import cv2

pt_y = 169
pt_x = 118
img = cv2.imread("jk.jpg")      # 彩色讀取
blue = img[pt_y, pt_x, 0]       # 讀 B 通道值
green = img[pt_y, pt_x, 1]      # 讀 G 通道值
red = img[pt_y, pt_x, 2]        # 讀 R 通道值
print(f"BGR = {blue}, {green}, {red}")





 
