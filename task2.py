import matplotlib.pyplot as plt
import math
import numpy as np
import copy as c

def add_noise(img, rate=5):
    img[::rate, ::rate, :] = 1;

def Kernel(sigma, radius):
    sigma = 2 * sigma * sigma;
    kernel = np.zeros((3, 3));
    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            kernel[i + radius][j + radius] = math.exp(-(i * i + j * j) / sigma) / math.sqrt(sigma * math.pi);
    return kernel;

def FilterByGauss(img):
    img2 = np.zeros_like(img);
    radius = 1;
    kernel = Kernel(5, radius);

    for k in range(img.shape[2]): # foreach color channel
        for i in range(radius, img.shape[0] - radius): # foreach row
            for j in range(radius, img.shape[1] - radius): # foreach column
                window = img[i - radius:i + radius + 1, j - radius : j + radius + 1, k];
                img2[i,j,k] = (kernel * window).sum();
    return img2;

def main():
    img = plt.imread("shava.jpg")[:, :, :3];
    img = c.copy(img);
    add_noise(img);
    img2 = FilterByGauss(img);
    fig, axs = plt.subplots(1,2);
    axs[0].imshow(img);
    axs[1].imshow(img2);
    plt.show();

if __name__ == "__main__":
    main();