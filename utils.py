import os
import tempfile
from pdf2image import convert_from_path

def convert_single_file(filename, target, first_page, last_page):
    with tempfile.TemporaryDirectory() as path:
         images_from_path = convert_from_path(filename, output_folder=path, last_page=last_page, first_page=first_page)
    
    base_filename = os.path.splitext(os.path.basename(filename))[0] + '.jpg'     
    
    for page in images_from_path:
        page.save(os.path.join(target, base_filename), 'JPEG')