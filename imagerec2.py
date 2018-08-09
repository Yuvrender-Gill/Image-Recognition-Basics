from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Open the  image file
i = Image.open('images/dotndot.png')


## opens the image as a numpy array of pixel values
iar = np.asarray(i)

## Each image file is represented by an array
## Each pixel is represented as a list of four values in one row
## of the array. So there are four values of each pixel in a list.

if __name__ == '__main__':
    print(iar)
    plt.imshow(iar)
    plt.show()