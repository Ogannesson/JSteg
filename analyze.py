# analyze.py

import matplotlib.pyplot as plt
import jpeglib


def plot_dct_histogram(image_path):
    img = jpeglib.read_dct(image_path)
    dct = img.Y

    plt.subplot(2, 1, 1)
    plt.title("DCT Coefficients Histogram")
    plt.hist(dct.ravel(), bins=50, density=True)
    plt.show()
