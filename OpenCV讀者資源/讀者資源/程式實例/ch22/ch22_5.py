# ch22_5.py
import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread('opencv_coin.jpg',cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src,cv2.COLOR_BGR2RGB)       
# 二值化
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)
# 執行膨脹操作
sure_bg = cv2.dilate(opening,kernel,iterations=3)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening,cv2.DIST_L2,5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst,0.7*dst.max(),255,0)  # 前景圖案
# 計算未知區域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
# 標記
ret, markers = cv2.connectedComponents(sure_fg)
# 先複製再標記修訂
sure_fg_copy = sure_fg.copy()
ret, markers_new = cv2.connectedComponents(sure_fg_copy)
markers_new += 1                                        # 標記修訂
markers_new[unknown==255] = 0
plt.subplot(131)
plt.title("未知區域")
plt.imshow(unknown)
plt.axis('off')
plt.subplot(132)
plt.title("標記區")
plt.imshow(markers, cmap="jet")
plt.axis('off')
plt.subplot(133)
plt.title("標記修訂區")
plt.imshow(markers_new, cmap="jet")
plt.axis('off')
plt.show()






