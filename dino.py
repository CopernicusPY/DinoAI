
import cv2 as cv
import pyautogui
import numpy as np
#As of now this script captures data from screen that can be customized by the user, and uses image annotation to display the pixel value that the user is interested in to the screen.
#I may turn this into a class for a more user friendly expirience when the AI is done.
#Image Manipulation-Related Functions
def threshold(v1, v2, region):
    screenshot = pyautogui.screenshot(region = region)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    (thresh, src) = cv2.threshold(screenshot,v1,v2,cv2.THRESH_BINARY)
    return (thresh, src)
def show_pixel_val(text_pos, pixel):
    cv2.putText(img,str(img[pixel[0],pixel[1]),(text_pos[0], text_pos[1]), cv2.FONT_HERSHEY_PLAIN, 2, (83,83,83), 2)
while True:
    threshold(127, 255, (51,226,375,202))
    show_pixel_val((141,78),(0,200))
                            
    cv2.imshow("Capture:", src) 

    if cv2.waitKey(1) == ord("q"):
        cv2.destroyAllWindows()
        break
