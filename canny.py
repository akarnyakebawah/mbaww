import sys 
import cv2 
import numpy as np 

cap = cv2.VideoCapture(sys.argv[1]) 
width = int(cap.get(3))
height = int(cap.get(4))

while(cap.isOpened()) : 
    ret, frame = cap.read() 
    if ret == True :
            
        edges = cv2.Canny(frame,height,width) 

        
        cv2.imshow('res2',edges) 
        if cv2.waitKey(1) & 0XFF == ord('q') :
            break
    else : 
        break

cap.release()
cv2.destroyAllWindows()
