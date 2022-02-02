#As of now this script captures data from screen that can be customized by the user, and uses image annotation to display the pixel value that the user is interested in to the screen.
#Day/Night detection added. This will help later for the cactus-detection system.
#Image Manipulation-Related Functions

import cv2 as cv
import pyautogui
import numpy as np

def threshold(v1, v2, region):
    screenshot = pyautogui.screenshot(region = region)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    (thresh, src) = cv2.threshold(screenshot,v1,v2,cv2.THRESH_BINARY)
    return (thresh, src)
def show_pixel_val(img,text_pos, pixel):
    cv2.putText(img,str(img[pixel[0],pixel[1]),(text_pos[0], text_pos[1]), cv2.FONT_HERSHEY_PLAIN, 2, (83,83,83), 2)
def is_day(img, x, y):
    if img[x, y] == 225:
        return True
    else:
        return False
while True:
    img = threshold(127, 255, (51,226,375,202))
    show_pixel_val(img,(141,78),(0,200))
    is_day(img, 0, 159)
                            
    cv2.imshow("Window Capture:", img) 

    if cv2.waitKey(1) == ord("q"):
        cv2.destroyAllWindows()
        break
