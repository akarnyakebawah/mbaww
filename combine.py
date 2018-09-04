import sys 
import cv2
import numpy as np

cap1 = cv2.VideoCapture(sys.argv[1])
cap2 = cv2.VideoCapture(sys.argv[2])
img_r  = cv2.imread(sys.argv[3]) 

vidWidth = int(cap1.get(3))
vidHeight = int(cap1.get(4)) 

img_p = cv2.resize(img_r,(vidWidth, vidHeight), interpolation = cv2.INTER_CUBIC) 

while (cap1.isOpened()):
    ret, frame = cap1.read()
    mask_ret, mask = cap2.read() 

    if ret == True:

        retval, binary = cv2.threshold(mask, 127,255,cv2.THRESH_BINARY)
        redMask, greenMask, blueMask = cv2.split(binary)
        print(redMask)

        mask_inv = cv2.bitwise_not(redMask) 

        foreground = cv2.bitwise_and(frame,frame, mask = mask_inv)
        background = cv2.bitwise_and(img_p, img_p, mask = redMask)
        result = cv2.add(foreground, background) 

        cv2.imshow('sd',result)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    else:
        break 

cap1.release()
cap2.release()
cv2.destroyAllWindows()
