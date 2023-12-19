import jpeglib
import numpy as np


def extract_message(stego_path, message_length):
    stego = jpeglib.read_dct(stego_path)
    dct_y = stego.Y  # 获取亮度DCT系数

    # 选择非DC且绝对值大于1的DCT系数位置
    valid_ac_locations = [(i, j, u, v) for i in range(dct_y.shape[0]) for j in range(dct_y.shape[1])
                          for u in range(8) for v in range(8)
                          if (u != 0 or v != 0) and np.abs(dct_y[i, j, u, v]) > 1]

    if len(valid_ac_locations) < message_length:
        raise ValueError("Message length exceeds the number of available AC coefficients")

    # 提取信息
    message = []
    for i in range(message_length):
        x, y, u, v = valid_ac_locations[i]
        dct_val = dct_y[x, y, u, v]
        if dct_val > 0:
            message_bit = dct_val % 2
        else:
            message_bit = (dct_val + 1) % 2
        message.append(message_bit)

    return message
