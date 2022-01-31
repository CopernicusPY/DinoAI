import cv2 as cv
import pyautogui

def threshold(v1, v2, region):
    screenshot = pyautogui.screenshot(region = region)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    (thresh, src) = cv2.threshold(screenshot,v1,v2,cv2.THRESH_BINARY)
    return (thresh, src)
    

while True:
    threshold(127, 255, (51,226,375,202))
    cv2.imshow("Capture:", src) 

    if cv2.waitKey(1) == ord("q"):
        cv2.destroyAllWindows()
        break
