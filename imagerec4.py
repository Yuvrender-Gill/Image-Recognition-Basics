from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

# Open the  image file
i = Image.open('images/dotndot.png')

# opens the image as a numpy array of pixel values
iar = np.array(i)


def threshold(image_array):

    """
    Finds the average colour of the image array
    :param image_array:
    :return:
    """

    balance_array = []
    new_array = image_array

    for row in image_array:
        for pixel in row:
            # add first three values of pixel that define the colour of the pixel
            # then divide by 3
            average_colour = reduce(lambda x, y: x + y, pixel[:3])/len(pixel[:3])
            # add the average colour value to the balance array
            balance_array.append(average_colour)
    # take the average of average colour value of each pixel.
    balance = reduce(lambda x, y: x + y, balance_array)/len(balance_array)

    # perform thresholding
    for row in new_array:
        for pixel in row:
            if reduce(lambda x, y: x + y, pixel[:3])/len(pixel[:3]) > balance:
                for i in range(4):
                    pixel[i] = 255
            else:
                for i in range(3):
                    pixel[i] = 0
                pixel[3] = 255

    return new_array


if __name__ == '__main__':

    threshold(iar)
    plt.show()
