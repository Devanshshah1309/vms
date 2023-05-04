import cv2
import numpy as np
from enum import Enum
import utils

# default constants
DEFAULT_BLUR_KERNEL_SIZE = (5, 5)
DEFAULT_CANNY_MIN_THRESHOLD = 200
DEFAULT_CANNY_MAX_THRESHOLD = 300
DEFAULT_VIDEO_PATH = "Resources/Bowling strike.mp4"
DEFAULT_WINDOW_NAME = "Video Analysis"
END_OF_VIDEO = "No more frames left!"
DEFAULT_GRID_ROWS = 2
DEFAULT_GRID_COLS = 2

# define keybinding options
class OPTIONS(Enum):
    PAUSE_OR_PLAY = ord(' ') 
    QUIT = ord('q')
    FULLSCREEN = ord('f')

# settings/control variables
video_is_paused = False
video_is_fullscreen = False
video_is_ended = False

def change_settings(key):
    if key == -1: # -1 => no key pressed
        return
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

def handle_pause_play():
    global video_is_paused
    key = cv2.waitKey(0)
    change_settings(key)
    if video_is_ended:
        return False
    if key == OPTIONS.PAUSE_OR_PLAY.value:
        return True
    return handle_pause_play() # recursively call until valid key is pressed

# main video manipulation loop

def process_video(video_path = DEFAULT_VIDEO_PATH):
    cap = cv2.VideoCapture(video_path)
    while True:
        if video_is_paused:
            handle_pause_play()
        if video_is_ended:
            break
        success, img = cap.read()
        display_image = None
        if not success:
            print("End of Video!")
            break
        if video_is_fullscreen:
            display_image = utils.get_fullscreen_image(img, DEFAULT_GRID_COLS, DEFAULT_GRID_ROWS)
        else:
            display_image = utils.get_gray_blur_edgedetect_image(img, DEFAULT_BLUR_KERNEL_SIZE,
                                DEFAULT_CANNY_MIN_THRESHOLD, DEFAULT_CANNY_MAX_THRESHOLD)
        
        utils.show(display_image, DEFAULT_WINDOW_NAME)
        
        key = cv2.waitKey(1)
        change_settings(key)
    # clean up
    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    print("-" * 20)
    print("Welcome to Devansh's Video Manipulation System!")
    print("-" * 20)
    video_path = input("Enter your video's path: ")
    if video_path == "": process_video()
    else: process_video(video_path)