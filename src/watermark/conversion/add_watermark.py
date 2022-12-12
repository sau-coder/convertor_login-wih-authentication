import base64

import cv2
import numpy as np


def stream_to_cv2(contents: bytes):
    np_arr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    return img


class Watermark_Adder:
    def __init__(self, image, watermark):
        self.image = stream_to_cv2(image)
        self.watermark = stream_to_cv2(watermark)

    def add_watermark(self):
        percent_of_scaling = 20
        new_width = int(self.image.shape[1] * percent_of_scaling / 100)
        new_height = int(self.image.shape[0] * percent_of_scaling / 100)
        new_dim = (new_width, new_height)
        resized_img = cv2.resize(self.image, new_dim, interpolation=cv2.INTER_AREA)

        wm_scale = 40
        wm_width = int(self.watermark.shape[1] * wm_scale / 100)
        wm_height = int(self.watermark.shape[0] * wm_scale / 100)
        wm_dim = (wm_width, wm_height)
        resized_wm = cv2.resize(self.watermark, wm_dim, interpolation=cv2.INTER_AREA)

        h_img, w_img, _ = resized_img.shape
        center_y = int(h_img / 2)
        center_x = int(w_img / 2)
        h_wm, w_wm, _ = resized_wm.shape
        top_y = center_y - int(h_wm / 2)
        left_x = center_x - int(w_wm / 2)
        bottom_y = top_y + h_wm
        right_x = left_x + w_wm
        roi = resized_img[top_y:bottom_y, left_x:right_x]

        result = cv2.addWeighted(roi, 1, resized_wm, 0.3, 0.3)

        resized_img[top_y:bottom_y, left_x:right_x] = result

        _, buffer = cv2.imencode(".jpg", resized_img)
        return base64.b64encode(buffer)
