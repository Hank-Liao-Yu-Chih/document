# ch3_5_1.py
import cv2
import numpy as np

fig = np.ones((50, 200), dtype=np.uint8) * 255    
print(fig)
cv2.imshow("fig", fig)

cv2.waitKey(0)
cv2.destroyAllWindows()














 
