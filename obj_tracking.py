import cv2
import numpy as np
from 



capture = cv2.VideoCapture("/Users/ramahalharbi/Desktop/projectComputerVision/source_code/los_angeles.mp4")

while True:
    _, frame = capture.read()

    cv2. imshow("Fream", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

capture.release()
cv2.destroyAllWindows()