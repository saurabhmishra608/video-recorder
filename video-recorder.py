import numpy as np
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', required=True)
args = parser.parse_args()


cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(args.path,fourcc, 20.0, (640,480))

while(cap.isOpened()):


    ret, frame = cap.read()
    cv2.imshow("frame",frame)
    out.write(frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()