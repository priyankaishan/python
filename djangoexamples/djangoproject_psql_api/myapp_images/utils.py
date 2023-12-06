""" # utils.py
import base64

def convert_image_to_bytea(image_path):
    with open(image_path, 'rb') as image_file:
        image_data = base64.b64encode(image_file.read())
    return image_data
 """