import numpy as np
import cv2
#read the existing image
#img=cv2.imread("/Users/chauhanabhishek/Downloads/Abhi.jpeg",1)

#creating the image using numpy
img=np.zeros([512,512,3],np.uint8)

#line function
img=cv2.line(img,(0,0),(1000,1500),(0,0,0),15)


#ArrowLine Function
img=cv2.arrowedLine(img,(50,0),(50,1000),(0,0,255),15)

#Rectangle function
img=cv2.rectangle(img,(255,255),(800,800),(0,0,0),15)

#circle function
img=cv2.circle(img,(555,555),400,(255,0,0),20)

#Put the text into the picture
font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,"Hey Im Abhi",(0,255),font,4,(100,100,100),10,cv2.LINE_AA)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()