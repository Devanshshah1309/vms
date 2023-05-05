# Video Management System (VMS)

### Dependencies

- `opencv-python`
- `numpy`

### Features

The VMS is designed to allow users to process videos using the keyboard (for efficiency purposes). All the commands are made as intuitive as possible by using commonly used key-bindings.

When the application starts, the user is prompted for a path to the file, which is then opened and a `2 x 2` grid of video streams are shown - original, blurred, edge detection and grayscale.

The following are the features:

- Enter fullscreen mode (show only 1 video on the window): Press the number (either 1, 2, 3 or 4) to make that stream full screen.
- Toggle fullscreen mode: `f` (by default, original video is chosen to be displayed)
- Rewind by 5 seconds: `a`
- Fast-forward by 5 seconds: `d`
- Exit the application: `q`
- Pause and Play the video: `space`

## Developer Guide

The code is divided into 2 files - `utils.py` and `vms.py`.

- `utils.py`: contains all the `cv2`-related code (image processing, stacking images, resizing images, etc.) so that we maintain a clean abstraction between the logic of the code and the underlying implementation
- `vms.py`: contains the actual business logic of the main program.

### Design Decisions

- Rewinding and forwarding is allowed only for a fixed number of seconds - This is similar to many applications such as YouTube, Netflix, etc. and hence is quite intuitive to use. It would be quite simple to allow the user to enter the number of seconds to rewind/forward by at the start and use that value dynamically, but I felt this wasn't that important because it's possible to rewind/forward by a larger amount by pressing the key multiple times, if it's really needed.
- "Fullscreen Mode" only fills up original window size - I felt this would make more sense rather than forcing the entire window size to fill up the monitor size and then the video to fill the window. Also, `opencv` does not provide a neat way to do this (i.e., to access the current window size), at least to my best knowledge.
- Logging is done for easy debugging and tracking errors
- Using named constants is always better than using magic numbers as it makes code easier to read and understand (even for myself later). This can be seen in the `vms.py` code as well.
- Although global variables are generally not a good practice, here, they can be used since they manage the state of the application and are closely coupled with the logic of the program too.
- I've tried to modularise the code as much as possible by abstracting the common logic into functions to make it easier to add new functionality to this VMS (e.g. the `change_settings` and `handle_pause_play` functions). Adding a new functionality would just involve creating a new handler for that command and including it in the `change_settings` (or wherever appropriate, depending on the actual implementation).
- A good way to further improve abstraction (a possible extenstion) by using Object Oriented Programming (OOP) would be to create a `VMS` class and store all the video related information inside it (including file path, current settings, etc). I eventually decided not to do this because the current code is at a sufficient level of abstraction for its size. In future, if more features were to be added, this could be a possible consideration - since the logic itself remains intact, the refactoring wouldn't be too difficult.
- Currently only 1 video input is supported (with 3 extra streams created for it) but it would be possible to support multiple video inputs. A possible way to do this would be to arrange all 4 streams for each input video in a row and then just stack all the streams for different videos on top of each other (i.e., the grid would be `n x 4` where `n` is the number of video inputs)
- A possible extension is to be able to allow the user to specify the guassian kernel size, canny thresholds, and other processing parameters so that they have greater control over the video streams. This can be easily implemented by asking the user for input at the start of the program and using the parameters dynamically.
