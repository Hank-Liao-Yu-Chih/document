# ch4_12_1.py
import cv2 
 
image = cv2.imread('street.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hsv, saturation, value = cv2.split(hsv_image)
hsv.fill(200)                                      # 修訂 hsv 內容
hsv_image = cv2.merge([hsv, saturation, value])    # 依據H S V順序合併
new_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR) # HSV 轉 BGR

cv2.imshow("The Image", image)
cv2.imshow("The New Image", new_image)

cv2.waitKey(0)
cv2.destroyAllWindows() 









 
