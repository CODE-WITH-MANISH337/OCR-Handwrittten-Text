import cv2
import matplotlib.pyplot as plt
import numpy as np
import easyocr


# image_path='images/surf.jpeg'
reader=easyocr.Reader(['en'])
video=cv2.VideoCapture(0, cv2.CAP_DSHOW)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:    
    ret, frame = video.read()  
    result=reader.readtext(frame)
    for detection in result:
        top_left = tuple(map(int, detection[0][0]))
        bottom_right = tuple(map(int, detection[0][2]))
        text=detection[1]
        img=cv2.rectangle(frame,top_left,bottom_right,(255,0,0),1)
        cv2.putText(frame,text,top_left,font,1,(255,0,0),2,cv2.LINE_AA)  
    cv2.imshow('window',frame)
    if cv2.waitKey(1)==ord('x'):
        break
cv2.destroyAllWindows()    




