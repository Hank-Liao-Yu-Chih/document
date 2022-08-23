# ch2_6.py
import cv2

pt_y = 169
pt_x = 118
img = cv2.imread("jk.jpg")      # 彩色讀取
px = img[pt_y, pt_x]            # 讀取 px 點
print(f"更改前BGR = {px}")
px = [255, 255, 255]            # 修改 px 點     
print(f"更改後BGR = {px}")








  
