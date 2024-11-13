import cv2
import mediapipe as mp
import pyautogui
img=cv2.VideoCapture(0)
my_hand=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
x1=y1=x2=y2=0


while True:
    ret,frame=img.read()
    frame=cv2.flip(frame,1)
    height,width,_=frame.shape
    rgb_img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    OUTPUT=my_hand.process(rgb_img)
    hands=OUTPUT.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks=hand.landmark
            
            for id,landmark  in enumerate(landmarks):
                x=int(landmark.x*width)
                y=int(landmark.y*height)
                if(id==8):
                    cv2.circle(frame,(x,y),8,(255,0,0),5)
                    x1=x
                    y1=y
                if(id==4):
                    cv2.circle(frame,(x,y),8,(0,255,0),5)
                    x2=x
                    y2=y
    distance=((x2-x1)**2 +(y2-y1)**2)**(0.5)//4
    cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),10)
    
    if(distance>50):
      pyautogui.press("volumeup")
    else:
      pyautogui.press("volumedown")

 
    cv2.imshow("frame",frame) 
    if cv2.waitKey(1) == ord('q'):
        break


   
      

img.release()
cv2.destroyAllWindows()