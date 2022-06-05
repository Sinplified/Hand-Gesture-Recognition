from tensorflow.keras.models import model_from_json
from cv2 import flip,cvtColor,COLOR_BGR2RGBA,COLOR_BGR2GRAY,GaussianBlur,adaptiveThreshold,ADAPTIVE_THRESH_GAUSSIAN_C,THRESH_BINARY_INV,threshold,THRESH_BINARY_INV,THRESH_OTSU,resize
from numpy import argmax


class Model:
    def __init__(self):
        self.json_file = open("model-bw.json", "r")
        self.model_json = self.json_file.read()
        self.json_file.close()
        self.loaded_model = model_from_json(self.model_json)
        self.loaded_model.load_weights("model-bw.h5")
    


    def predict(self,test_image):
        # test_image = test_image[10:320,10:320]  #ROI
        test_image = flip(test_image,1)

        # cv2image = cvtColor(test_image, COLOR_BGR2RGBA)
        gray = cvtColor(test_image,COLOR_BGR2GRAY)
        blur = GaussianBlur(gray,(5,5),2)
        th3 = adaptiveThreshold(blur,255,ADAPTIVE_THRESH_GAUSSIAN_C,THRESH_BINARY_INV,11,2)
        ret, res = threshold(th3, 70, 255,THRESH_BINARY_INV+THRESH_OTSU)

        res = resize(res, (128,128))
        result = self.loaded_model.predict(res.reshape(1, 128, 128, 1))
        result = argmax(result)

        if result!=0:
            prediction = chr(ord('A') + result -1)
        else: 
            prediction = 'Blank'

        return prediction