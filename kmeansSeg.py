import sys 
import cv2 
import numpy as np 

cap = cv2.VideoCapture(sys.argv[1]) 

while(cap.isOpened()) : 
    ret, frame = cap.read() 
    if ret == True : 
        Z = frame.reshape((-1,3)) 
        Z = np.float32(Z)

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 0.1) 
        K = 3
        ret, label, center = cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_PP_CENTERS)

        center = np.uint8(center)

#        lw = np.array([40,30,60])
#        up = np.array([80,255,255])

        num = np.array([np.count_nonzero(label==0), np.count_nonzero(label==1), np.count_nonzero(label==2)])
        dom_clr = np.argmax(num, axis=0) 
        center[dom_clr] = np.multiply(center[dom_clr], 0)

        # here we go stupid code 
        if dom_clr == 0 :
            center[1] = [255,255,255] 
            center[2] = [255,255,255] 
        elif dom_clr == 1 : 
            center[0] = [255,255,255] 
            center[2] = [255,255,255] 
        else: 
            center[1] = [255,255,255] 
            center[2] = [255,255,255]

        print(num)
        print(center)


        res = center[label.flatten()] 
        res = res.reshape((frame.shape)) 
#        res = cv2.medianBlur(res, 5)

#        kernel = np.ones((15,15), np.float32)/225 
#        smoothed = cv2.filter2D(res,-1,kernel)

        blur = cv2.GaussianBlur(res, (15,15), 0)

#        print(res2)   
#        print(center[label.flatten()])
#        print(res2.shape)
        cv2.imshow("output", blur) 
        if cv2.waitKey(1) & 0XFF == ord('q') :
            break
    else : 
        break

cap.release()
cv2.destroyAllWindows()
