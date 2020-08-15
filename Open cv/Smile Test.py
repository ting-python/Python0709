import cv2

# 匯入辨識檔
face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_alt.xml')
smile_cascade = cv2.CascadeClassifier('./xml/haarcascade_smile.xml')

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    # print(ret, frame)
    # 取得灰階圖樣
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # 偵測臉
    faces = face_cascade.detectMultiScale(
        gray,  # 待檢測圖片，一般為灰度圖像加快檢測速度
        scaleFactor=1.1,  # 檢測粒度 scaleFactor 。更大的粒度將會加快檢測的速度，但是會對檢測準確性產生影響。相反的，一個更小的粒度將會影響檢測的時間，但是會增加準確性。
        minNeighbors=5,  # 每個目標至少檢測到幾次以上，才可被認定是真數據。
        minSize=(30, 30),  # 設定數據搜尋的最小尺寸 ，如 minSize=(30,30)
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    print(faces)

    # 繪製臉的範圍
    for(x, y, w, h) in faces:  # (x,y)座標 / w,h長寬
        # 獲取人臉矩形的興趣區域
        roi_gray = gray[y:y + h, x:x + w]
        smile = smile_cascade.detectMultiScale(
            gray,  # 待檢測圖片，一般為灰度圖像加快檢測速度
            scaleFactor=1.1,  # 檢測粒度 scaleFactor 。更大的粒度將會加快檢測的速度，但是會對檢測準確性產生影響。相反的，一個更小的粒度將會影響檢測的時間，但是會增加準確性。
            minNeighbors=5,  # 每個目標至少檢測到幾次以上，才可被認定是真數據。
            minSize=(30, 30),  # 設定數據搜尋的最小尺寸 ，如 minSize=(30,30)
            flags=cv2.CASCADE_SCALE_IMAGE
        )

    for(sx, sy, sw, sh) in smile:
        cv2.rectangle(frame, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 5)

    # 顯示影像
    cv2.imshow('Tuan', frame)

    # 按下 q 離開迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()