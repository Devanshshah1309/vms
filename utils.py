import cv2
import numpy as np

# define utility functions to help with video manipulation
# abstract all cv2 and numpy related functions into this file
# so that the main file only contains the logic of the program (not the implementation)
def resize(img, width_scale, height_scale):
    return cv2.resize(img, (int(img.shape[1] * width_scale), int(img.shape[0] * height_scale)))

def blur(img, kernel_size):
    return cv2.GaussianBlur(img, kernel_size, 0)

def edge_detect(img, min_threshold, max_threshold):
    return convert_to_3_channels(cv2.Canny(img, min_threshold, max_threshold))

def grayscale(img):
    # maintains 3 channels for compatibility with other kinds of images
    return convert_to_3_channels(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

def convert_to_3_channels(img):
    return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

def hstack(imgs):
    return np.concatenate(imgs, axis=1)

def vstack(imgs):
    return np.concatenate(imgs, axis=0)

def grid(imgs, grid_cols):
    return np.concatenate([np.concatenate(imgs[i:i+grid_cols], axis=1) for i in range(0, len(imgs), grid_cols)], axis=0)

def show(img, window_name):
    cv2.imshow(window_name, img)

def get_fullscreen_image(img, grid_cols, grid_rows):
    return resize(img, grid_cols, grid_rows)

def get_gray_blur_edgedetect_image(img, kernel_size, min_threshold, max_threshold):
    return grid([img, grayscale(img), blur(img, kernel_size), edge_detect(img, min_threshold, max_threshold)], 2)