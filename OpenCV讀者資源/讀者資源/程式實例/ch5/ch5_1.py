# ch5_1.py
import cv2
import numpy as np
 
height = 160                # 影像高
width = 280                 # 影像寬
# 建立GRAY影像陣列
image = np.zeros((height, width), np.uint8)
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()




 
