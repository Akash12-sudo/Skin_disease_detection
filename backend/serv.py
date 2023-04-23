from flask import Flask,render_template,request
import numpy as np
#import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import  keras
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import load_img,img_to_array

model=tf.keras.models.load_model('../model-09-0.55.hdf5')
test_datagen= ImageDataGenerator(
    rescale=1./255
)


app=Flask(__name__)

@app.route('/',methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def predict():
    print("hello")
    img=request.files['img']
    path='./images/test1.jpg'
    img.save(path)

    #preprocessing the image
    
    test_img=load_img('./images/test1.jpg',target_size=(256,256))
    test_img_array=img_to_array(test_img)
    test_img_array=test_img_array.reshape((1,)+test_img_array.shape)
    batch=test_datagen.flow(test_img_array,batch_size=1)
    
    #predicting the image 

    result=model.predict(batch)
    predicted_class=np.argmax(result)
    print(predicted_class)
    print(result)
 
    label = ['acene and rosacea','actinic','eczema','warts molluscam']
    
    classification = '%s (%.2f%%)' % (label[predicted_class],result[predicted_class]*100)
    return render_template('index.html',prediction=classification)

if __name__== '__main__':
    app.run(port=3000,debug=True)