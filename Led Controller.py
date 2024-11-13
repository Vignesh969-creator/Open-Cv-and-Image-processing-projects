import cv2
import mediapipe as mp
#import controller as cnt
img=cv2.VideoCapture(0)
hand_draw=mp.solutions.hands.Hands()
tipsIDS=[4,8,12,16,20]
drawing_utils=mp.solutions.drawing_utils
hand_connections = mp.solutions.hands.HAND_CONNECTIONS
while True:
    ret,frame=img.read()
    height,width,_=frame.shape
    rgb_img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    lmlist=[]
    OUTPUT=hand_draw.process(rgb_img)
    hands=OUTPUT.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand,hand_connections)
            landmarks=hand.landmark
            for id,landmark in enumerate(landmarks):
                x=int(landmark.x*width)
                y=int(landmark.y*height)
                lmlist.append((id, x, y))

    fingers=[]
    if(len(lmlist)!=0):
        if (lmlist[tipsIDS[0]][1] > lmlist[tipsIDS[0] - 1][1]):

            fingers.append(1)
        
        else:
            fingers.append(0)

        for id in range(1,5):
            if(lmlist[tipsIDS[id]][2] < lmlist[tipsIDS[id] - 2][2]):
                fingers.append(1)
            else:
                fingers.append(0)
        total=fingers.count(1)
        #cnt.led(total)
        if total==0:
            cv2.rectangle(frame, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, "0", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
            cv2.putText(frame, "LED", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
        elif total==1:
            cv2.rectangle(frame, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, "1", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
            cv2.putText(frame, "LED", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
        elif total==2:
            cv2.rectangle(frame, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, "2", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
            cv2.putText(frame, "LED", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
        elif total==3:
            cv2.rectangle(frame, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, "3", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
            cv2.putText(frame, "LED", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
        elif total==4:
            cv2.rectangle(frame, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, "4", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
            cv2.putText(frame, "LED", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
        elif total==5:
            cv2.rectangle(frame, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, "5", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
            cv2.putText(frame, "LED", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
 
        
    
        
    
    cv2.imshow("FRAME",frame)

    if(cv2.waitKey(1)==ord("q")):
        break


img.release()
cv2.destroyAllWindows()
