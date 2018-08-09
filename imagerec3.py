from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Open the  image file
i = Image.open('images/numbers/0.1.png')


## opens the image as a numpy array of pixel values
iar = np.asarray(i)

## This tutorial is to demonstrate the different color values of the pixel.
## The importance of understanding the color scheme is the key to character
## recognition.

if __name__ == '__main__':
    print(iar)
    plt.imshow(iar)
    plt.show()