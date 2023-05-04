import cv2
import numpy as np
from enum import Enum

# Constants
BLUR_KERNEL_SIZE = (5, 5)
CANNY_MIN_THRESHOLD = 200
CANNY_MAX_THRESHOLD = 300
VIDEO_PATH = "Resources/Bowling strike.mp4"
WINDOW_NAME = "Video Analysis"
END_OF_VIDEO = "No more frames left!"
GRID_ROWS = 2
GRID_COLS = 2

# define keybinding options
class OPTIONS(Enum):
    PAUSE_OR_PLAY = ord(' ') 
    QUIT = ord('q')
    FULLSCREEN = ord('f')

# set up video capture
cap = cv2.VideoCapture(VIDEO_PATH)
img_width, img_height  = cap.get(3), cap.get(4)

# settings/control variables
video_is_paused = False
video_is_fullscreen = False
video_is_ended = False

def change_settings(key):
    global video_is_paused, video_is_fullscreen, video_is_ended
    if key == OPTIONS.PAUSE_OR_PLAY.value:
        video_is_paused = not video_is_paused
    elif key == OPTIONS.FULLSCREEN.value:
        video_is_fullscreen = not video_is_fullscreen
    elif key == OPTIONS.QUIT.value:
        video_is_ended = True
    else:
        print("Invalid key pressed")
        return
    print("Settings changed")
    print("Paused" if video_is_paused else "Playing")
    print("Fullscreen" if video_is_fullscreen else "Not fullscreen")

# main video manipulation loop
while True:
    if video_is_paused:
        key = cv2.waitKey(0)
        if key == OPTIONS.QUIT.value:
            break
        if key == OPTIONS.PAUSE_OR_PLAY.value:
            video_is_paused = False
        else:
            continue
    success, img = cap.read()
    if not success:
        print(END_OF_VIDEO)
        break
    if video_is_fullscreen:
        print("Entered full screen mode")
        img = cv2.resize(img, (int(img_width) * GRID_COLS, int(img_height) * GRID_ROWS))
        cv2.imshow(WINDOW_NAME, img)
    else:
        imgGray = cv2.cvtColor(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)
        imgBlur = cv2.GaussianBlur(img, BLUR_KERNEL_SIZE, 0)
        imgEdgeDetect = cv2.cvtColor(cv2.Canny(img, CANNY_MIN_THRESHOLD, CANNY_MAX_THRESHOLD), cv2.COLOR_GRAY2BGR)
        all = np.concatenate((np.concatenate((img, imgGray), axis=1), np.concatenate((imgBlur, imgEdgeDetect), axis=1)), axis=0)
        cv2.imshow(WINDOW_NAME, all)
    key = cv2.waitKey(1)
    if key == OPTIONS.QUIT.value:
        break
    if key == OPTIONS.PAUSE_OR_PLAY.value:
        video_is_paused = not video_is_paused
        key = cv2.waitKey(-1)
        if key == OPTIONS.QUIT.value:
            break
        if key == OPTIONS.PAUSE_OR_PLAY.value:
            video_is_paused = not video_is_paused
            continue
    elif key == OPTIONS.FULLSCREEN.value:
        video_is_fullscreen = not video_is_fullscreen

# clean up
cv2.destroyAllWindows()
cap.release()