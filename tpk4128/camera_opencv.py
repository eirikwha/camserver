import numpy as np
import cv2 as cv



class Camera(object):

    def __init__(self):

        # Implement this constructor that opens a webcam and stores it in self._camera

        self._camera = cv.VideoCapture(0)  # Prepare the camera...
        print("Camera warming up ...")



    def capture(self):

        # Implement this function that grabs an image from the webcam and returns a numpy array

        s , img = self._camera.read()

        if s:  # frame captures without errors...
            pass

        print('Length',len(img.tostring()))
        print('Data type',img.dtype)
        print('Image shape',img.shape)
        print("Reading image ...")

        return img

    def __del__(self):
        # Implement this destructor. Remember to free the camera.
        
        print("Releasing ...")

        self._camera.release()
        self._camera = cv.destroyAllWindows()
