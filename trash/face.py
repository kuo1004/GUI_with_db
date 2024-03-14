import cv2

def detect_faces(image_path):
    # 加载人脸检测器
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 加载图像
    image = cv2.imread(image_path)

    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_sBGR2GRAY)

    # 使用人脸检测器检测人脸
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 返回检测到的人脸位置
    return faces

# 测试图片路径
image_path = "summary/family.jpg"

# 检测人脸
face_locations = detect_faces(image_path)

# 绘制人脸框
image = cv2.imread(image_path)
for (x, y, w, h) in face_locations:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# 显示结果
cv2.imshow("Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()