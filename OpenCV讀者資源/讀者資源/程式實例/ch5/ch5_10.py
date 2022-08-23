# ch5_10.py
import cv2
import numpy as np
 
height = 150                # 影像高
width = 300                 # 影像寬
image = np.zeros((height,width,3),np.uint8)
image[0:50,:,0] = 255       # blue
image[50:100,:,1] = 255     # green
image[100:150,:,2] = 255    # red
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()




 
