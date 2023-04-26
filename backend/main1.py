# Importing Necessary modules
import shutil
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, File, UploadFile
import numpy as np

import tensorflow as tf
from tensorflow import  keras
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import load_img,img_to_array

# Declaring our FastAPI instance

app = FastAPI()


# templating the HTML file

templates = Jinja2Templates(directory="templates")



test_datagen= ImageDataGenerator(
    rescale=1./255
)

# Defining path operation for root endpoint

@app.get('/')
def main(request : Request):
     return templates.TemplateResponse("index.html",{"request":request})

# Defining path operation for /name endpoint
@app.post('/')
async def predict(request: Request,img : UploadFile = File(...)):
    print("hello")
    
    print(img.filename)
    
    path='./images/test1.jpg'
    
    with open(path,"wb") as buffer:
            shutil.copyfileobj(img.file, buffer)
   

    #preprocessing the image
            
    test_img=load_img('./images/test1.jpg',target_size=(256,256))
    test_img_array=img_to_array(test_img)
    test_img_array=test_img_array.reshape((1,)+test_img_array.shape)
    batch=test_datagen.flow(test_img_array,batch_size=1)
    
    #loading the model and predicting the image 
    model=tf.keras.models.load_model('../best_model-47-0.65.hdf5')
    result=model.predict(batch)
    predicted_class=np.argmax(result)
    print(predicted_class)
    print(result)                                           
     
    # classes of diseases 
    label = ['acene and rosacea','actinic','eczema','warts molluscam']
    
    classification = '%s (%.2f%%)' % (label[predicted_class],result[0][predicted_class]*100)
    return templates.TemplateResponse("index.html",{"request":request,"prediction": classification})
	
    	
