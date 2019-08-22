# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 12:50:40 2019

@author: lione
"""

def detect_label(img):

    client = vision.ImageAnnotatorClient()

    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    

    response = client.label_detection(image=image)
    labels = response.label_annotations
            
    return([response, labels])
    
  
def detect_obj(img):

    client = vision.ImageAnnotatorClient()
    
    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)    
    objects = client.object_localization(
        image=image).localized_object_annotations

    return(objects)

def detect_land(img):


    client = vision.ImageAnnotatorClient()

    ###with open(face_file, "rb") as imageFile:
        ###im = base64.b64encode(imageFile.read())
    ###content = Image.open(face_file)
    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    
    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations
    print('Landmarks:')

    for landmark in landmarks:
        print(landmark.description)
        for location in landmark.locations:
            lat_lng = location.lat_lng
            print('Latitude {}'.format(lat_lng.latitude))
            print('Longitude {}'.format(lat_lng.longitude))
            
    return([response, landmarks])
    
from google.cloud import vision   
 



def detect_text(img):

    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    ###with open(face_file, "rb") as imageFile:
        ###im = base64.b64encode(imageFile.read())
    ###content = Image.open(face_file)
    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)    
    response = client.document_text_detection(image=image)
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))

                    for symbol in word.symbols:
                        print('\tSymbol: {} (confidence: {})'.format(
                            symbol.text, symbol.confidence))    
    
    return(response)