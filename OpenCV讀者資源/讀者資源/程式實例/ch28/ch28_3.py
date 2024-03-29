# ch28_3.py
import cv2
import os

if not os.path.exists("ch28_3"):                # 如果不存在ch28_3資料夾
    os.mkdir("ch28_3")                          # 就建立ch28_3
name = input("請輸入英文名字 : ")
faceName = "ch28_3\\" + name + ".jpg"           # 人臉影像
pictPath = r'C:\opencv\data\haarcascade_frontalface_alt2.xml'
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識檔案物件
cap = cv2.VideoCapture(0)                       # 開啟攝影機
while(cap.isOpened()):                          # 攝影機有開啟就執行迴圈   
    ret, img = cap.read()                       # 讀取影像
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
            minNeighbors = 3, minSize=(20,20))
    for (x, y, w, h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  # 藍色框住人臉
    cv2.imshow("Photo", img)                    # 顯示影像在OpenCV視窗
    if ret == True:                             # 讀取影像如果成功
        key = cv2.waitKey(200)                  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            imageCrop = img[y:y+h,x:x+w]                    # 裁切
            imageResize = cv2.resize(imageCrop,(160,160))   # 重製大小
            cv2.imwrite(faceName, imageResize)  # 儲存人臉影像           
            break
cap.release()                                   # 關閉攝影機

cv2.waitKey(0)
cv2.destroyAllWindows()


