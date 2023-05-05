import cv2
import numpy as np

Image = cv2.Mat # alias for cv2 Mat type

def resize(img, width_scale, height_scale) -> Image:
    return cv2.resize(img, (int(img.shape[1] * width_scale), int(img.shape[0] * height_scale)))

def blur(img: Image, kernel_size: tuple[int]) -> Image:
    return cv2.GaussianBlur(img, kernel_size, 0)

def edge_detect(img: Image, min_threshold: int, max_threshold: int) -> Image:
    return convert_to_3_channels(cv2.Canny(img, min_threshold, max_threshold))

def grayscale(img: Image) -> Image:
    # maintains 3 channels for compatibility with other kinds of images
    return convert_to_3_channels(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

def convert_to_3_channels(img: Image) -> Image:
    return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

def hstack(imgs: list[Image]) -> Image:
    return np.concatenate(imgs, axis=1)

def vstack(imgs: list[Image]) -> Image:
    return np.concatenate(imgs, axis=0)

def grid(imgs: list[Image], grid_cols: int) -> Image:
    return np.concatenate([np.concatenate(imgs[i:i+grid_cols], axis=1) for i in range(0, len(imgs), grid_cols)], axis=0)

def show(img, window_name: str) -> None:
    cv2.imshow(window_name, img)

def get_fullscreen_image(img, grid_cols: int, grid_rows: int) -> Image:
    return resize(img, grid_cols, grid_rows)

def get_gray_blur_edgedetect_image(img: Image, kernel_size: tuple[int], min_threshold: int, max_threshold: int):
    return grid([img, grayscale(img), blur(img, kernel_size), edge_detect(img, min_threshold, max_threshold)], 2)