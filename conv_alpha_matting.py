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
selImgResRGBA = cv2.cvtColor(selImgRes, cv2.COLOR_RGB2RGBA).astype(float)
#export obj
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.VideoWriter_fourcc('X','2','6','4')
#out = cv2.VideoWriter(sys.argv[3],fourcc, 30.0, (vidWidth,vidHeight), True) 

while(cap.isOpened()): 
    ret, frame = cap.read()
    if ret == True: 

#       ORIGINAL GREEN
#        lw = np.array([65,60,60]) 
#        up = np.array([80,255,255])

        lw = np.array([40,30,60])   #40 30 60
        up = np.array([80,255,255])

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        alpha = cv2.inRange(hsv, lw, up)
#        mask_blur = cv2.GaussianBlur(mask, (5,5), 0)
        alpha_blur = cv2.medianBlur(alpha, 5)
        alpha_inv = cv2.bitwise_not(alpha_blur)
       
        #add blackout
#        twibbonMasked = cv2.bitwise_and(frame, frame, mask = mask_inv)
 #       selImgMasked = cv2.bitwise_and(selImgRes,selImgRes, mask=mask_blur)  
        
        #add two img 
  #      result = cv2.add(twibbonMasked,selImgMasked) 
 #       out.write(result)
        
#        alpha_inv_rgba = cv2.cvtColor(alpha_inv, cv2.COLOR_RGB2RGBA)
#        alpha_data = alpha_inv.astype(float)/255 
#        alpha_data_rgba = cv2.cvtColor(alpha_data, cv2.COLOR_RGB2RGBA)
#       frame_rgba = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA) 
#        frame_rgba[:, :, 3] = alpha_data  
#        foreground = cv2.multiply(alpha, frame_rgba.astype(float))

        frameRGBA = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)
        frameRGBAas = frameRGBA.astype(float)
        alphaInvRGB = cv2.cvtColor(alpha_inv, cv2.COLOR_GRAY2RGB) 
        alphaInvRGBA = cv2.cvtColor(alphaInvRGB, cv2.COLOR_RGB2RGBA).astype(float)/255

        foreground = cv2.multiply(alphaInvRGBA,frameRGBAas) 
        background = cv2.multiply(1.0-alphaInvRGBA, selImgResRGBA) 
        outImage = cv2.add(foreground, background)/255 
#        outImageRGB = cv2.cvtColor(outImage, cv2.COLOR_RGBA2RGB) 

        print(frameRGBA.dtype)
        print(frameRGBAas.dtype)
        print(outImage.shape)
        cv2.imshow('res', outImage)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    else: 
        break

cap.release()
#out.release()
cv2.destroyAllWindows()
