import cv2
import numpy as np
from enum import Enum
import utils
import logging

# default constants
DEFAULT_BLUR_KERNEL_SIZE = (5, 5)
DEFAULT_CANNY_MIN_THRESHOLD = 200
DEFAULT_CANNY_MAX_THRESHOLD = 300
DEFAULT_VIDEO_PATH = "Resources/2022 Reel.mp4"
DEFAULT_WINDOW_NAME = "Video Analysis"
END_OF_VIDEO = "No more frames left!"
DEFAULT_GRID_ROWS = 2
DEFAULT_GRID_COLS = 2
DEFAULT_REWIND_FAST_FORWARD_SECONDS = 5

# define keybinding options
class Options(Enum):
    PAUSE_OR_PLAY = ord(' ') 
    QUIT = ord('q')
    FULLSCREEN = ord('f')
    REWIND = ord('a')
    FAST_FORWARD = ord('d')

logging.basicConfig(level=logging.DEBUG)

# settings/control variables
video_is_paused = False
video_is_fullscreen = False
video_is_ended = False

def change_settings(key):
    # rewind and fast forward are handled in the main loop because they affect the video itself
    # not just the display
    if key == -1: # -1 => no key pressed
        return
    global video_is_paused, video_is_fullscreen, video_is_ended
    if key == Options.PAUSE_OR_PLAY.value:
        logging.info("Toggling pause/play.")
        video_is_paused = not video_is_paused
    elif key == Options.FULLSCREEN.value:
        logging.info("Toggling fullscreen.")
        video_is_fullscreen = not video_is_fullscreen
    elif key == Options.QUIT.value:
        logging.info("Ending video.")
        video_is_ended = True
    else:
        logging.warning("Invalid key pressed.")
        return

def handle_pause_play():
    global video_is_paused
    key = cv2.waitKey(0)
    change_settings(key)
    if video_is_ended:
        return False
    if key == Options.PAUSE_OR_PLAY.value:
        return True
    return handle_pause_play() # recursively call until valid key is pressed

def get_frames_offset(fps):
    return fps * DEFAULT_REWIND_FAST_FORWARD_SECONDS


# main video manipulation loop
def process_video(video_path = DEFAULT_VIDEO_PATH):
    cap = cv2.VideoCapture(video_path)
    logging.info("Video opened successfully.")
    fps = cap.get(cv2.CAP_PROP_FPS)
    current_frame = 0
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

        # handle rewind and fast forward
        if key == Options.REWIND.value:
            logging.info("Rewinding.")
            offset = get_frames_offset(fps)
            current_frame = max(0, current_frame - offset)
            cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
        elif key == Options.FAST_FORWARD.value:
            logging.info("Fast forwarding.")
            offset = get_frames_offset(fps)
            current_frame = min(cap.get(cv2.CAP_PROP_FRAME_COUNT), current_frame + offset)
            cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
    # clean up
    logging.info("Cleaning up.")
    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    print("-" * 20)
    print("Welcome to Devansh's Video Manipulation System!")
    print("-" * 20)
    video_path = input("Enter your video's path: ")
    if video_path == "": process_video()
    else: process_video(video_path)