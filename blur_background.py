import cv2
import time
import numpy as np

cam = cv2.VideoCapture(0)

last_time = time.time()

while True:
    _, frame = cam.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, (255, 0, 255), (255, 255, 255))
    mask_3d = np.repeat(mask[:, :, np.newaxis], 3, axis=2)

    blurred = cv2.GaussianBlur(frame, (15, 15), 0)
    frame = np.where(mask_3d == (255, 255, 255), frame, blurred)
    text = f"FPS: {int(1 / (time.time() - last_time))}"

    last_time = time.time()
    cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (0, 255, 0), 2)

    cv2.imshow("Blurring", frame)

    if cv2.waitKey(1) == ord('q'):
        print("file saved")
        break
cam.release()
cv2.destroyAllWindows()

