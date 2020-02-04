import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class extractFace():
    def __init__(self,img):
        self.img = cv2.imread(img,1)
    
    def extract(self):
        
#        dst = cv2.fastNlMeansDenoisingColored(self.img,None,10,10,7,21)
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        ret, thresh1 = cv2.threshold(gray, 190, 220,cv2.THRESH_BINARY_INV) 
        
        kernel = np.ones((5,5), np.uint8)
        img_dilation = cv2.dilate(thresh1, kernel, iterations=3) 
        img_erosion = cv2.erode(img_dilation, kernel, iterations=3)
        
        contours,hierarchy = cv2.findContours(img_erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        if len(contours) != 0:
            # draw in blue the contours that were founded
            cv2.drawContours(img_erosion, contours, -1, 255, 3)
        
            #find the biggest area
            c = max(contours, key = cv2.contourArea)
        
            x,y,w,h = cv2.boundingRect(c)
            # draw the book contour (in green)    
            val = cv2.rectangle(self.img,(x,y),(x+w,y+h),(23,255,21),0)
            face = self.img[y:y+h,x:x+w]
#        plt.imshow(face)
        return face
    
    def getface(self):
        face_cascade = cv2.CascadeClassifier('face.xml')
        letter = self.extract()
        dt = cv2.cvtColor(letter, cv2.COLOR_BGR2GRAY)
#        plt.imshow(dt)
        aces = face_cascade.detectMultiScale(dt, 1.3, 5)
        for (x,y,w,h) in aces:  
            val = cv2.rectangle(letter,(x-25,y-15),(x+w+6,y+h+5),(255,0,0),0)
            fc = letter[y-15:y+h+5,x-25:x+w+6]
        fc = cv2.fastNlMeansDenoisingColored(fc,None,10,10,7,21)
        return fc;
    
    def show_face(self,img):
        cv2.imshow("face",img)
        cv2.waitKey(0)
        cv2.destroyWindow("face window")

if __name__ == "__main__":
    c = extractFace("pan.jpg")
    c.show_face(c.getface())
    
        