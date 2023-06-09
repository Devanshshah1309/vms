# :camera: Video Management System (VMS)

## Dependencies

- `opencv-python`
- `numpy`

## Examples

### Grid View

![grid](Resources/grid.png)

### Edge Detection (Full Screen)

![edgedetect](Resources/edgedetect.png)

### Grayscale (Full Screen)

![grayscale](Resources/grayscale.png)

## Features

The VMS is designed to allow users to process videos using the keyboard (for efficiency purposes). All the commands are made as intuitive as possible by using commonly used key-bindings.

When the application starts, the user is prompted for a path to the file, which is then opened and a `2 x 2` grid of video streams are shown - original, grayscale, blurred, and edge detection.

The following are the features:

- Enter fullscreen mode (show only 1 video on the window): Press the number (either 1, 2, 3 or 4) to make that stream full screen.
- Toggle fullscreen mode: `f` (by default, original video is chosen to be displayed)
- Rewind by 5 seconds: `a`
- Fast-forward by 5 seconds: `d`
- Exit the application: `q`
- Pause and Play the video: `space`

## Developer Guide

The code is divided into 3 files - `utils.py`, `vms.py` and `constants.py`.

- `utils.py`: contains all the `cv2`-related code (image processing, stacking images, resizing images, etc.) so that we maintain a clean abstraction between the logic of the code and the underlying implementation
- `vms.py`: contains the actual business logic of the main program.
- `constants.py`: contains the constants (default values, enums, etc.) used in the application.

### Design Decisions

This section explains some of the thought-processes I had when designing this application - please feel free to reach out in case you have any other questions :smile:

- Rewinding and forwarding is allowed only for a fixed number of seconds - This is similar to many applications such as YouTube, Netflix, etc. and hence is quite intuitive to use. It would be quite simple to allow the user to enter the number of seconds to rewind/forward by at the start and use that value dynamically, but I felt this wasn't that important because it's possible to rewind/forward by a larger amount by pressing the key multiple times, if it's really needed.
- "Fullscreen Mode" only fills up original window size - I felt this would make more sense rather than forcing the entire window size to fill up the monitor size and then the video to fill the window. Also, `opencv` does not provide a neat way to do this (i.e., to access the current window size), at least to my best knowledge.
- Logging is done for easy debugging and tracking errors
- Using named constants is always better than using magic numbers as it makes code easier to read and understand (even for myself later). This can be seen in the `vms.py` code as well.
- We use type hints in python as much as possible to make it easier to reason about code (mainly used in `utils.py`) and reduce the possibility of type-related bugs. Type aliases are also used to improve abstraction - e.g. `Image` instead of `cv2.Mat` makes it much easier to understand what a function is doing.
- All functions in `vms.py` have proper documentation. Functions in `utils.py` don't need documentation because they're generally quite straightforward implementations (and their names provide sufficient context as to what the function might be doing). This also taught me that not every function needs a documentation - sometimes, it's much better (and economical in terms of time) to name functions better (maybe even have long, descriptive names which don't need any additional explanations) rather than spending a lot of time writing documentation for a simple function.
- Although global variables are generally not a good practice, here, they can be used since they manage the state of the application and are closely coupled with the logic of the program too. An alternative would be to use the return values from functions to change the state but that would get quite messy too (e.g. if the `change_settings` function returns a `2`, change `video_is_ended` to `True`, etc.) - however, it would allow us to move all these functions to a separate file, further increasing modularity. The trade-off made here was to allow more coupling in order to reduce complexity. This would have to be reconsidered while scaling the system.
- I've tried to modularise the code as much as possible by abstracting the common logic into functions to make it easier to add new functionality to this VMS (e.g. the `change_settings` and `handle_pause_play` functions). Adding a new functionality would just involve creating a new handler for that command and including it in the `change_settings` (or wherever appropriate, depending on the actual implementation).
- A good way to further improve abstraction (a possible extenstion) by using Object Oriented Programming (OOP) would be to create a `VMS` class and store all the video related information inside it (including file path, current settings, etc). I eventually decided not to do this because the current code is at a sufficient level of abstraction for its size. In future, if more features were to be added, this could be a possible consideration - since the logic itself remains intact, the refactoring wouldn't be too difficult.
- Currently only 1 video input is supported (with 3 extra streams created for it) but it would be possible to support multiple video inputs. A possible way to do this would be to arrange all 4 streams for each input video in a row and then just stack all the streams for different videos on top of each other (i.e., the grid would be `n x 4` where `n` is the number of video inputs)
- A possible extension is to be able to allow the user to specify the guassian kernel size, canny thresholds, and other processing parameters so that they have greater control over the video streams. This can be easily implemented by asking the user for input at the start of the program and using the parameters dynamically.
