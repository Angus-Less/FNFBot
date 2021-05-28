
import time
import numpy as np
import cv2

from mss import mss
from pynput.keyboard import Key, Controller

# MACROS
keyboard = Controller()
UP_KEY = Key.up
DOWN_KEY = Key.down
RIGHT_KEY = Key.right
LEFT_KEY = Key.left


# todo: implement system where it updates and checks for use afterwards.

bounding_box = {"top": 350, "left": 1300, "width": 500, "height": 180}

sct = mss()

while True:
    sct_img = sct.grab(bounding_box)
    screen = np.array(sct_img)
    cv2.imshow('screen', screen)

    FirstButton = int(screen.shape[0] / 4)
    halfwayVertical = int(screen.shape[0] / 2)


    halfwayHorizontal = int(screen.shape[1] / 2)

    # Default grey is [135, 163, 173]

    for n, rgbValues in enumerate(screen[halfwayVertical]):
        #print(n)
        #print(rgbValues)
        #screen[halfwayVertical][n] = [255, 0, 0]

        if n == halfwayVertical:
            screenValues = screen[halfwayVertical][n]
            if screenValues[0] != 135 and screenValues[1] != 163 and screenValues[2] != 173:
                print("LEFT BUTTON")
                keyboard.press(LEFT_KEY)
                time.sleep(0.01)
                keyboard.release(LEFT_KEY)

        if n == halfwayVertical * 4.5:
            screenValues = screen[halfwayVertical][n]
            if screenValues[0] != 135 and screenValues[1] != 163 and screenValues[2] != 173:
                print("RIGHT BUTTON")
                keyboard.press(RIGHT_KEY)
                time.sleep(0.01)
                keyboard.release(RIGHT_KEY)


        if n == halfwayVertical * 2:
            screenValues = screen[halfwayVertical][n]
            if screenValues[0] != 135 and screenValues[1] != 163 and screenValues[2] != 173:
                print("DOWN BUTTON")
                keyboard.press(DOWN_KEY)
                time.sleep(0.01)
                keyboard.release(DOWN_KEY)


        if n == halfwayVertical * 3.4:
            screenValues = screen[halfwayVertical][n]
            if screenValues[0] != 135 and screenValues[1] != 163 and screenValues[2] != 173:
                print("UP BUTTON")
                keyboard.press(UP_KEY)
                time.sleep(0.01)
                keyboard.release(UP_KEY)

        # keyboard.release(LEFT_KEY)
        # keyboard.release(UP_KEY)
        # keyboard.release(DOWN_KEY)
        # keyboard.release(RIGHT_KEY)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break