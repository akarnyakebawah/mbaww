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
        center_reshape = center.reshape((1, K, 3))

        lw = np.array([40,30,60])
        up = np.array([80,255,255])

#        lw = np.array([36,0,0]) 
#        up = np.array([70,255,255])

        center_reshape_hsv = cv2.cvtColor(center_reshape, cv2.COLOR_BGR2HSV) 
        center_reshape_hsv_green = cv2.inRange(center_reshape_hsv, lw, up) 
        center_reshape_hsv_green = center_reshape_hsv_green / 255
#        print(center_reshape_hsv_green[0][0])
#        print(center[0])


        for x in range(0,(K-1)) :
            center[x] = np.multiply(center[x],center_reshape_hsv_green[0][x])
        
        print(center)

        res = center[label.flatten()] 
        res2 = res.reshape((frame.shape)) 

#        print(res2)   
#        print(center[label.flatten()])
#        print(res2.shape)
        cv2.imshow("output", res2) 
        if cv2.waitKey(1) & 0XFF == ord('q') :
            break
    else : 
        break

cap.release()
cv2.destroyAllWindows()
