import jpeglib
import numpy as np


def embed_message(cover_path, stego_path, message):
    cover = jpeglib.read_dct(cover_path)
    dct_y = cover.Y  # 获取亮度DCT系数
    message_length = len(message)

    # 将DC系数置0并找出绝对值大于1的非DC系数位置
    valid_ac_locations = [(i, j, u, v) for i in range(dct_y.shape[0]) for j in range(dct_y.shape[1])
                          for u in range(8) for v in range(8)
                          if (u != 0 or v != 0) and np.abs(dct_y[i, j, u, v]) > 1]

    if len(valid_ac_locations) < message_length:
        raise ValueError("Message too long for the cover image")

    # 嵌入信息
    for i, loc in enumerate(valid_ac_locations):
        if i >= message_length:
            break
        x, y, u, v = loc
        message_bit = message[i]
        if dct_y[x, y, u, v] > 0:
            dct_y[x, y, u, v] = dct_y[x, y, u, v] - dct_y[x, y, u, v] % 2 + message_bit
        else:
            dct_y[x, y, u, v] = dct_y[x, y, u, v] - (dct_y[x, y, u, v] + 1) % 2 + message_bit

    cover.Y = dct_y
    cover.write_dct(stego_path)
