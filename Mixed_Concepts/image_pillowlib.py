from PIL import Image, ImageFilter
import sys
import os

# img = Image.open('./JPG/pikachu.jpg')
# print(img) #<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x640 at 0x234C5B31950>
# print(img.format) # JPEG
# print(img.size) # (640, 640)
# print(img.mode) # RGB
# print(dir(img))

# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save("./SavedFiles/blur.png", "png")

# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img.save("./SavedFiles/smooth.png", "png")

# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img.save("./SavedFiles/sharpen.png", "png")

# filtered_img = img.convert('L')
''' 
The current version supports all possible conversions between
 "L", "RGB" and "CMYK". The ``matrix`` argument only supports "L"
 and "RGB".
'''
# it converts the image to grey scale, that is Black and White. Similarly, RGB = Red Green Blue
# filtered_img.save("./SavedFiles/grey.png", "png")

# filtered_img.show()    # this opens the image in the default player

# rotated_img = img.rotate(45)
# rotated_img.save("./SavedFiles/rotated.png", "png")

# resized_img = img.resize((80,50)) # but this can ruin the aspect ratio hence we use thumbnail method
# resized_img.save("./SavedFiles/resized.png", "png")

# box = (100,100,400,400)
# cropped_img = filtered_img.crop(box)
# cropped_img.save("./SavedFiles/cropped_img.png", "png")

# filtered_img.thumbnail((50,50))
# # it will keep max. 50*50 aspect ratio, it can be like 30*50, but it won't exceed 50 pixels
# filtered_img.save("./SavedFiles/thumbnailed.png", "png")

# --------------JPG to PNG------------
source_path = sys.argv[1]
target_path = sys.argv[2]

# print(source_path,target_path)

if not os.path.exists(target_path):
    os.makedirs(target_path)

for file in os.listdir(source_path):
    img = Image.open(f'{source_path}{file}')
    # new_file = file.replace(".jpg", ".png")    # we can do this or the below command
    new_filename = os.path.splitext(file)[0]    # this keeps the file name without the extension
    # and splitext make the result in tuple
# # added the / in case user doesn't enter it. You may want to check for this and add or remove it.
    img.save(f"{target_path}/{new_filename}.png", "png")
print('all done!')

