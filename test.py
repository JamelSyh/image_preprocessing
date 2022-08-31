from internship import *
import cv2 as cv


def path(name):
    return "./images/{}.png".format(name)


def show(img):
    cv.imshow("img", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def read(img):
    image_path = path(img)
    image = cv.imread(image_path)
    return image


def write(img, name):
    image_path = path(name)
    cv.imwrite(image_path, img)


def readShow(img):
    image = read(img)
    show(image)
    return image


def writeShow(img, name):
    write(img, name)
    show(img)


im = read("image")


# change the constractors parameter to get the disaired results
result = Processing(im, Binarization.multi).result()

show(result)
# write(result, "test")
