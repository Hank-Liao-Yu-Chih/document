# ch5_8.py
import cv2
import numpy as np
 
height = 160                                # 影像高
width = 280                                 # 影像寬
# 建立BGR影像陣列
image = np.zeros((height, width, 3), np.uint8)
blue_image = image.copy()
blue_image[:,:,0] = 255                     # 建立 B 通道像素值
cv2.imshow("blue image", blue_image)        # 顯示blue image影像

green_image = image.copy()
green_image[:,:,1] = 255                    # 建立 G 通道像素值
cv2.imshow("green image", green_image)      # 顯示green image影像

red_image = image.copy()
red_image[:,:,2] = 255                      # 建立 R 通道像素值
cv2.imshow("red image", red_image)          # 顯示red image影像

cv2.waitKey(0)
cv2.destroyAllWindows()




 
