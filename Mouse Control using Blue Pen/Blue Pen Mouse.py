"""
Created on Fri Aug 24 06:12:57 2018

@author: Udbhav
"""
try:
    import cv2
    try:
        import numpy as np
        try:
            import pyautogui as mouse
            try:
                screen_x,screen_y = mouse.size()
                cap = cv2.VideoCapture(0)
                mouse.FAILSAFE = False
                _,f= cap.read()
                window_x,window_y,c = f.shape
                f_x = screen_x/window_x
                f_y = screen_y/window_y
                while(1):
                    ret,frame = cap.read()
                    if ret:
                        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
                        lower_blue = np.array([100,100,100])
                        upper_blue = np.array([140,255,255])
                        mask = cv2.inRange(hsv, lower_blue, upper_blue)
                        mask = np.flip(mask,1)
                        median = cv2.medianBlur(mask,25)
                        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(median)
                        cv2.imshow('Mask',mask)
                        cv2.circle(median, maxLoc, 5, (255, 255, 255), 2)
                        cv2.imshow('Median Blur',median)
                        (x,y) = maxLoc
                        mouse.moveTo(f_x*x,f_y*y)
                        k = cv2.waitKey(5) & 0xFF
                        if k == 27:
                            break
                    else:
                        print("---CHECK RENDERING DEVICE AND/OR WEBCAM PORT WRONG---")
                        break
                cv2.destroyAllWindows()
                cap.release()
                print("---EXITING---")
            except:
                print("---ERROR---")
        except:
            print("---UNABLE TO LOAD PYAUTOGUI---")
    except:
        print("---UNABLE TO LOAD NUMPY---")
except:
    print("---UNABLE TO LOAD OPENCV---")