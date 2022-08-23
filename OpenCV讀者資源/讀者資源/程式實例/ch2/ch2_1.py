# ch2_1.py
import cv2

img = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)   # 灰階讀取
print("列印灰階影像的屬性")
print(f"shape = {img.shape}")
print(f"size  = {img.size}")
print(f"dtype = {img.dtype}")




 
