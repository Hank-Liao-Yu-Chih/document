# ch5_9.py
import cv2
import numpy as np
 
height = 160                # 影像高
width = 280                 # 影像寬
# 使用random.randint()建立GRAY影像陣列
image = np.random.randint(256,size=[height,width,3],dtype=np.uint8)
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()




 
