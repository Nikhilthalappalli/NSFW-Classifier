import os
from django.conf import settings
from django.shortcuts import render

# Create your views here.
def home(request):
   return render(request,'home.html') 

import tensorflow as tf
import numpy as np
import matplotlib.image as mpimg

def setup_models():
    path = os.path.join(settings.BASE_DIR,'files','vgg16.h5') 
    model = tf.keras.models.load_model(path)
    return model

def predict_class(image):
    model = setup_models()
    classes = ['Drawing','Hentai','Neutral','Porn','Sexual']
    img = mpimg.imread(image)
    resize = tf.image.resize(img,(224,224))
    result = model.predict(np.expand_dims(resize/255,0))
    result = np.argmax(result)
    if result in [1,3,4]:
        m=1
    else:
        m=0
    return classes[result],m

def imagefile(request):
    img = request.FILES["img"]
    result,m = predict_class(img)
    return render(request,'home.html',{'result':result,'m':m})  