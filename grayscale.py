import numpy as np
from load import load, save 

'''
converting RGB image to grayscale image, 
is done converting the 3 channel color into a single channel color using weighted sum of the RGB values

average method or the weighted luminosity method 
'''

image = load('input/butterfly.png')

T1 = np.array([0.299, 0.587, 0.114])
T2 = np.array([0.216, 0.7152, 0.0722])
T3 = np.array([1/3, 1/3, 1/3])

height, width, _ = image.shape

new_image = np.zeros((height, width), dtype=np.uint8)
new_image2 = np.zeros((height, width), dtype=np.uint8)
new_image3 = np.zeros((height, width), dtype=np.uint8)


for i in range(height):
    for j in range(width):
        pixel = image[i, j]

        new_image[i, j] = int(T1 @ pixel)
        new_image2[i, j] = int(T2 @ pixel)
        new_image3[i, j] = int(T3 @ pixel)

save(new_image, 'output/grayscale/average_greyscale.png')
save(new_image2, 'output/grayscale/weighted_luminosity_greyscale.png')
save(new_image3, 'output/grayscale/uniform_greyscale.png')