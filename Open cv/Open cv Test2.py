# 若跑不出資料可重插 USB

import cv2

cap = cv2.VideoCapture(0)  # 0代表camera的順序
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 寬度
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 高度

while True:
    ret, frame = cap.read()
    print(ret, frame)
    cv2.imshow('ATOM', frame)
    # 按下Q離開迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
