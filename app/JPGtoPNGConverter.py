import sys
import os
from PIL import Image

# grab first and second argument
source_folder = sys.argv[1]
target_folder = sys.argv[2]

# check if new/ exists, if not create it
if not os.path.isdir(target_folder):
    os.mkdir(target_folder)

# loop through Pokedex,
for file in os.listdir(source_folder):
    img = Image.open(f'./{source_folder}/{file}')
    clean_name = os.path.splitext(file)[0]
    # convert images do png
    # save to the new folder
    img.save(f'./{target_folder}/{clean_name}.png', 'png')
    # converted_img.show()
