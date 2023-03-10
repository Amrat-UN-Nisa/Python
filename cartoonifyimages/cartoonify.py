import cv2  # for image processing
import numpy as np  # to store image


import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

top = tk.Tk()   # create the root window as  we have initialized root as an object for Tk() class for creating a root window.
top.geometry('400x400')   # dislay size of the window
top.title('Cartoonify Your Image !') # title of the window that display on the left side of the window
top.configure(background='white')  # window background colour
label = Label(top, background='#CDCDCD', font=('calibri', 20, 'bold')) #  label is used to provide a single-line caption


# """ fileopenbox opens the box to choose file
# and help us store file path as string ""

def upload():
    ImagePath = "E:/MachineLearning/CartoonifyImage/cartoonifyimages/download.png"
    # fileopenbox() is the method in easyGUI module which returns the path of the chosen file as a string.
    cartoonify(ImagePath)


def cartoonify(ImagePath):
    # read the image
    # Imread is a method in cv2 which is used to store images in the form of numbers.The image is read as a numpy array,
    # in which cell values depict R, G, and B values of a pixel.
    originalmage = cv2.imread(ImagePath)
    # cvtColor(image, flag) is a method in cv2 which is used to transform an image into the colour-space mentioned as ‘flag’.
    originalmage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2RGB)
    # cvtColor(image, flag) is a method in cv2 which is used to transform an image into the colour-space mentioned as ‘flag’.
    # Here, our first step is to convert the image into grayscale.Thus, we use the BGR2GRAY flag. This returns the image in grayscale
    print(originalmage)  # image is stored in form of numbers

    # # confirm that image is chosen
    if originalmage is None:
        print("Can not find any image. Choose appropriate file")
        sys.exit()
    ReSized1 = cv2.resize(originalmage, (960, 540))
    #plt.imshow(ReSized1, cmap='gray')

    # converting an image to grayscale
    grayScaleImage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2GRAY)
    ReSized2 = cv2.resize(grayScaleImage, (960, 540))
    # plt.imshow(ReSized2, cmap='gray')
    # After each transformation, we resize the resultant image using the resize() method in cv2 and display it using imshow() method.
    # This is done to get more clear insights into every single transformation step.

    # applying median blur to smoothen an image
    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
    ReSized3 = cv2.resize(smoothGrayScale, (960, 540))
    # plt.imshow(ReSized3, cmap='gray')

    # retrieving the edges for cartoon effect
    # by using thresholding technique
    getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 9, 9)

    ReSized4 = cv2.resize(getEdge, (960, 540))
    # plt.imshow(ReSized4, cmap='gray')

    # applying bilateral filter to remove noise
    # and keep edge sharp as required
    colorImage = cv2.bilateralFilter(originalmage, 9, 300, 300)
    ReSized5 = cv2.resize(colorImage, (960, 540))
    # plt.imshow(ReSized5, cmap='gray')

    # masking edged image with our "BEAUTIFY" image
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)

    ReSized6 = cv2.resize(cartoonImage, (960, 540))
    # plt.imshow(ReSized6, cmap='gray')

    # Plotting the whole transition
    images = [ReSized1, ReSized2, ReSized3, ReSized4, ReSized5, ReSized6]

    fig, axes = plt.subplots(3, 2, figsize=(8, 8), subplot_kw={'xticks': [], 'yticks': []},
                             gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')

    save1 = Button(top, text="Save cartoon image", command=lambda: save(ReSized6, ImagePath), padx=30, pady=5)
    save1.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
    save1.pack(side=TOP, pady=50)

    plt.show()


def save(ReSized6, ImagePath):
    # saving an image using imwrite()
    newName = "cartoonified_Image"
    path1 = os.path.dirname(ImagePath)
    extension = os.path.splitext(ImagePath)[1]
    path = os.path.join(path1, newName + extension)
    cv2.imwrite(path, cv2.cvtColor(ReSized6, cv2.COLOR_RGB2BGR))
    I = "Image saved by name " + newName + " at " + path
    tk.messagebox.showinfo(title=None, message=I)


upload = Button(top, text="Cartoonify an Image", command=upload, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
upload.pack(side=TOP, pady=50)

top.mainloop()
