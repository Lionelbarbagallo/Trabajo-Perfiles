# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:34:43 2019

@author: lione
"""

import argparse
import io

from google.cloud import vision
from google.cloud.vision import types

###esta función realiza la busqueda web. tira buenas Labels, pero hay que garpar y no parece ser mejor a los otros servicios
###recordar establecer la variable global con la Key, eso está en otro script

def annotate(img):
    """Returns web annotations given the path to an image."""
    client = vision.ImageAnnotatorClient()
    

    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    web_detection = client.web_detection(image=image).web_detection

    return web_detection

###lo que sigue no sé que es, no lo analicé...quedará para el futuro!

def report(annotations):
    """Prints detected features in the provided web annotations."""
    if annotations.pages_with_matching_images:
        print('\n{} Pages with matching images retrieved'.format(
            len(annotations.pages_with_matching_images)))

        for page in annotations.pages_with_matching_images:
            print('Url   : {}'.format(page.url))

    if annotations.full_matching_images:
        print('\n{} Full Matches found: '.format(
              len(annotations.full_matching_images)))

        for image in annotations.full_matching_images:
            print('Url  : {}'.format(image.url))

    if annotations.partial_matching_images:
        print('\n{} Partial Matches found: '.format(
              len(annotations.partial_matching_images)))

        for image in annotations.partial_matching_images:
            print('Url  : {}'.format(image.url))

    if annotations.web_entities:
        print('\n{} Web entities found: '.format(
              len(annotations.web_entities)))

        for entity in annotations.web_entities:
            print('Score      : {}'.format(entity.score))
            print('Description: {}'.format(entity.description))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    path_help = str('The image to detect, can be web URI, '
                    'Google Cloud Storage, or path to local file.')
    parser.add_argument('image_url', help=path_help)
    args = parser.parse_args()

    report(annotate(args.image_url))