import sys 
import cv2 
import numpy as np 

cap = cv2.VideoCapture(sys.argv[1]) 

while(cap.isOpened()) : 
    ret, frame = cap.read() 
    if ret == True : 
        Z = frame.reshape((-1,3)) 
        Z = np.float32(Z)

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 50, 0.1) 
        K = 3
        ret, label, center = cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_PP_CENTERS)

        center = np.uint8(center)
#        ravel = label.ravel()==0
#        print(ravel.shape)
#        label = label.flatten()
#        label[label==0]=255
#        label[label!=255]=0
#        label = label.reshape((int(cap.get(4)), int(cap.get(3))))
#        label = np.uint8(label)
#        
#        print(label)
#        print(label.flatten())
        
        res = center[label.flatten()] 
#        res = Z[label.ravel()==0]
        res2 = res.reshape((frame.shape)) 
        print(label)   
#        print(center[label.flatten()])
#        print(res2.shape)
        cv2.imshow('res2',res2) 
        if cv2.waitKey(1) & 0XFF == ord('q') :
            break
    else : 
        break

cap.release()
cv2.destroyAllWindows()
