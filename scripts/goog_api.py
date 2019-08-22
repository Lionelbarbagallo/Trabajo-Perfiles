# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:04:23 2019

@author: lione
"""
from google.cloud import vision
from google.cloud.vision import types
import io
from PIL import Image, ImageDraw

client = vision.ImageAnnotatorClient()

def detect_label(img):

    global client

    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    

    response = client.label_detection(image=image)
    labels = response.label_annotations
            
    return([response, labels])
    
  
def detect_obj(img):

    global client
    
    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)    
    objects = client.object_localization(
        image=image).localized_object_annotations

    return(objects)