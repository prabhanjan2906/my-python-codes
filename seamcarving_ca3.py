__author__ = 'prabhanjan'

from pylab import imread
from pylab import figure
from pylab import gray
from pylab import imshow
from pylab import subplot
from pylab import show
from pylab import title
from pylab import inf
from skimage import img_as_float
import numpy as np
from skimage import filter


class SeamCarving():
    def __init__(self, image_name):
        img = imread(image_name)
        self.img = img_as_float(img)
        self.w, self.h = self.img.shape[:2]
        self.image_to_show_seam_carving = np.copy(self.img)
        self.image_to_manipulate = self.img
        figure()
        gray()

    def display(self):
        print "Original Image Size: rows=" + str(self.w) + " columns=" + str(self.h)
        print "Seam Carved Image Size: rows=" + str(self.image_to_manipulate.shape[0]) + " columns=" + str(self.image_to_manipulate.shape[1])
        subplot(3,1,1); imshow(self.img); title("Actual Image")
        subplot(3,1,2); imshow(self.image_to_show_seam_carving); title("Seam Carving Along Columns")
        subplot(3,1,3); imshow(self.image_to_manipulate); title("Seam Carved Image")
        show()

    def dual_gradient_energy(self, img):
        horizontal_gradient = filter.hsobel(img)
        horizontal_gradient = np.square(horizontal_gradient)
        vertical_gradient = filter.vsobel(img)
        vertical_gradient = np.square(vertical_gradient)
        energy = horizontal_gradient + vertical_gradient
        return energy

    def findShortestPath(self, img, seam, BeginRow , lastRow, lastCol, SeamBeginColumn):
        if(BeginRow == lastRow):
            return

        leastElement, column = img[BeginRow+1][SeamBeginColumn], SeamBeginColumn

        if( (leastElement > img[BeginRow+1][SeamBeginColumn-1])):
            leastElement = img[BeginRow+1][SeamBeginColumn - 1]
            column = SeamBeginColumn - 1

        if((SeamBeginColumn < lastCol) and (leastElement > img[BeginRow+1][SeamBeginColumn+1])):
            leastElement = img[BeginRow+1][SeamBeginColumn + 1]
            column = SeamBeginColumn + 1

        seam.append(column)
        self.findShortestPath(img, seam, BeginRow+1, lastRow, lastCol, column)

    def find_seam(self, img):
        rows = img.shape[0]
        cols = img.shape[1]
        verticalSeam = []

        for r in range(1, rows):
            for c in range(1,cols-1):
                if(c == 1):
                    img[r][c] = img[r][c] + min(img[r-1][c], img[r-1][c+1])
                    continue

                if(c==cols-2):
                    img[r][c] = img[r][c] + min(img[r-1][c-1], img[r-1][c])
                    continue

                img[r][c] = img[r][c] + min(img[r-1][c-1], img[r-1][c], img[r-1][c+1])

        minimum, BeginColumn = inf, 0
        for c in range(1,cols-1):
            if(minimum > img[1][c]):
                minimum = img[1][c]
                BeginColumn = c

        verticalSeam.append(BeginColumn)
        verticalSeam.append(BeginColumn)
        self.findShortestPath(img,verticalSeam,1,rows-1, cols-1 ,BeginColumn)
        return verticalSeam

    def plot_seam(self, img, seam):
        row = 0
        for i in range(len(seam)):
            img[i][seam[i]] = [255, 0, 0]

    def remove_seam(self, img, seam):
        img_as_list = img.tolist()
        for i in range(0,img.shape[0]):
            del img_as_list[i][seam[i]]

        newimg = np.array(img_as_list)
        return newimg

    def findGradient(self, color_image):
        energy_red = self.dual_gradient_energy(color_image[:,:,0])  # Red
        energy_green = self.dual_gradient_energy(color_image[:,:,1])  # Green
        energy_blue = self.dual_gradient_energy(color_image[:,:,2])  # blue

        totalEnergy = energy_red + energy_blue + energy_green
        return totalEnergy

    def resize_image(self):
        totalEnergy = self.findGradient(self.image_to_manipulate)
        seam = self.find_seam(totalEnergy)
        self.plot_seam(self.image_to_show_seam_carving, seam)
        newImg = self.remove_seam(self.image_to_manipulate, seam)
        self.image_to_manipulate = newImg

    def resize_image_to(self, number_of_colums_to_remove):
        for i in range(number_of_colums_to_remove):
            self.resize_image()
        self.display()
