import cv2

cap = cv2.VideoCapture('kadıkoy.mp4')  # capture frames from a video

car_detection = cv2.CascadeClassifier(
    'cars.xml')  # Trained XML classifiers describes some features of some object we want to detect

while True:
    ret, frames = cap.read()  # reads frames from a video

    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)  # convert to gray scale of each frames

    cars = cars_detection = car_detection.detectMultiScale(gray, 1.1, 1)  # Detects cars of different sizes in the
    # input image

    for (x, y, w, h) in cars:
        cv2.rectangle(frames, (x, y), (x + w, y + h), (28, 255, 66), 2)  # 28,255,66 RGB COLOR GREEN 2 Thickness

    cv2.namedWindow('video', cv2.WND_PROP_FULLSCREEN)  # FULLSCREEN WINDOWS

    cv2.imshow('video', frames)  # Display frames in a window

    if cv2.waitKey(33) == 13:  # Wait for Enter key to stop
        break
cv2.destroyAllWindows()
