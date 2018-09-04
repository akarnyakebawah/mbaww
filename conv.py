import sys
import cv2 
import numpy as np 

# get video and image path from argument
cap = cv2.VideoCapture(sys.argv[1])  
selImg = cv2.imread(sys.argv[2])

# get dimension of selected video 
vidWidth = int(cap.get(3))
vidHeight = int(cap.get(4))

# resize selected image
# height, width = selImg.shape[:2] 
selImgRes = cv2.resize(selImg,(vidWidth,vidHeight), interpolation = cv2.INTER_CUBIC) 

#export obj
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.VideoWriter_fourcc('X','2','6','4')
out = cv2.VideoWriter(sys.argv[3],fourcc, 30.0, (vidWidth,vidHeight), True) 

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
#        mask_blur = cv2.GaussianBlur(mask, (5,5), 0)
        mask_blur = cv2.medianBlur(mask, 5)
        mask_inv = cv2.bitwise_not(mask_blur)
       
        #add blackout
        twibbonMasked = cv2.bitwise_and(frame, frame, mask = mask_inv)
        selImgMasked = cv2.bitwise_and(selImgRes,selImgRes, mask=mask_blur)  
        
        #add two img 
        result = cv2.add(twibbonMasked,selImgMasked) 
        out.write(result)

        # cv2.imshow('res',result)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    else: 
        break

cap.release()
out.release()
cv2.destroyAllWindows()
