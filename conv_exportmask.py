import sys
import cv2 
import numpy as np 

# get video and image path from argument
cap = cv2.VideoCapture(sys.argv[1])  

vidWidth = int(cap.get(3)) 
vidHeight = int(cap.get(4))

#export obj
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(sys.argv[2],fourcc, 30.0, (vidWidth,vidHeight), True) 

while(cap.isOpened()): 
    ret, frame = cap.read()
    if ret == True: 

#       ORIGINAL GREEN
#        lw = np.array([65,60,60]) 
#        up = np.array([80,255,255])

        lw = np.array([40,30,60])   #40 30 60
        up = np.array([80,255,255])

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lw, up)
        mask_blur = cv2.medianBlur(mask, 5)
        mask_blur = cv2.cvtColor(mask_blur, cv2.COLOR_GRAY2RGB)
#        mask_inv = cv2.bitwise_not(mask_blur)
       
        out.write(mask_blur)

        cv2.imshow('res',mask_blur)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    else: 
        break

cap.release()
out.release()
cv2.destroyAllWindows()
