from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png', 'png')
converted_img = img.convert('L')
converted_img.save('converted.png', 'png')
converted_img.show()

print(img.format)
