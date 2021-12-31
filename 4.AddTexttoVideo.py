import cv2
import datetime
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text="Width: "+str(cap.get(3)) +" Height: "+ str(cap.get(4))
        datte=str(datetime.datetime.now())

        cv2.putText(frame,datte,(10,50),font,1,(0,0,0),3,cv2.LINE_AA )
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",gray)

        if cv2.waitKey(1) & 0xFF==ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
