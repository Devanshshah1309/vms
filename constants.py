from enum import Enum

# default constants
DEFAULT_BLUR_KERNEL_SIZE = (11, 11)
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
    FULLSCREEN_ORIGINAL = ord('1')
    FULLSCREEN_GRAYSCALE = ord('2')
    FULLSCREEN_BLUR = ord('3')
    FULLSCREEN_EDGE_DETECT = ord('4')

class FullScreenMode(Enum):
    ORIGINAL = 0
    GRAYSCALE = 1
    BLUR = 2
    EDGE_DETECT = 3