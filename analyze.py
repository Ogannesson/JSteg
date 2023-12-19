# analyze.py

import matplotlib.pyplot as plt
import jpeglib
import numpy as np


def plot_dct_histogram(image_path):
    img = jpeglib.read_dct(image_path)
    dct = img.Y

    plt.figure()
    plt.title("DCT Coefficients Histogram")
    plt.hist(dct.ravel(), bins=np.arange(-5, 5, 0.4), color='blue', alpha=0.7, density=True)
    plt.xlim(-10, 10)
    plt.xlabel('DCT Coefficient Value')
    plt.ylabel('Probability')
    plt.grid(True)
    plt.show()
