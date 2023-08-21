import cv2 
from pyzbar.pyzbar import decode 

cap = cv2.VideoCapture(0)

while True :
    st,frame = cap.read()
    
    d =decode(frame)
    if len(d)>0 :
        
        for code in d :
            print(code.data.decode("UTF-8"))
      
    cv2.imshow("QR Reader", frame)
    
    cv2.waitKey(60)
    
