import numpy as np
from cv2 import adaptiveThreshold, INTER_LINEAR, cvtColor, COLOR_BGR2GRAY, resize, THRESH_BINARY, \
    ADAPTIVE_THRESH_GAUSSIAN_C

def preprocess_image(img):
    gray = cvtColor(np.array(img), COLOR_BGR2GRAY)
    resized = resize(gray, None, fx=1.5, fy=1.5, interpolation=INTER_LINEAR)
    processed_img = adaptiveThreshold(
        resized,
        255,
        ADAPTIVE_THRESH_GAUSSIAN_C,
        THRESH_BINARY,
        61,
        11
    )
    return processed_img