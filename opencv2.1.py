import cv2
import numpy as np
import epydoc
#make a black window
windowname='drawing'
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow(windowname)
#mouse callback function
def draw_shape(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),40,(255,0,0),thickness=5,lineType=-1)
    if event==cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img,(x,y),(x*2,y*2),(200,0,156),thickness=2)
cv2.setMouseCallback(windowname,draw_shape)
def main():
    while (True):
        cv2.imshow(windowname,img)
        if cv2.waitKey(20)==27:
            break
    cv2.destroyAllWindows()
if __name__=="__main__":
    main()