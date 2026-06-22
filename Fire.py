import cv2
import numpy as np import playsound as ps

fire_reported = 0
alarm_status = False

def play_audio():
    ps.playsound("C:\\Users\\Ranjiv\\PycharmProjects\\demo1\\alram.mp3")
    video = cv2.VideoCapture("video.mov.mp4")
    while True:
        ret, frame = video.read()
        frame = cv2.resize(frame,(1000,500))
        blur = cv2.GaussianBlur(frame,(15,15),0)
        hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
        lower = [18,50,50]
        upper = [35,255,255]
        lower = np.array(lower,dtype="uint8") 
        upper = np.array(upper,dtype="uint8")
        mask = cv2.inRange(hsv,lower,upper)
        output = cv2.bitwise_and(frame,hsv,mask=mask)
        no_of_total = cv2.countNonZero(mask)
        if int(no_of_total)>15000:
            print('fire detected') 
            if ret == False:
                break 
            cv2.imshow("output", output)
            if cv2.waitKey(10000) & 0xff == ord("q"): 
                break
            play_audio()
            break;
        '''if int(no_of_total) > 15000: fire_reported = fire_reported + 1 if fire_reported >= 1:
            if alarm_status == False: play_audio() alarm_status = True'''
        if ret == False: 
            break
        cv2.imshow("output",output)
        if cv2.waitKey(1) & 0xff == ord("q"):
            break
    cv2.destroyAllWindows()
    video.release()