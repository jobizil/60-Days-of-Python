# Exercise
# Create a script that will resize all images in a folder to 3 different sizes (300x300, 600x600, 900x900).
# Note: Some images have been provided in the wallpaper folder.


#  Solution

from PIL import Image
import os

# Open the wallpaper folder
#  Loop through the files and check if the files are of .jpg extensions
# Split the files and extension and then create diffferent thumbnails of images and append file name to the image size and save into the file size respective folders.

size_300 = (300,300)
size_600 = (1200,640)
size_900 = (900,900)

for file in os.listdir('./images/wallpaper'):
    if file.endswith('.jpg'):
        image = Image.open(f'./images/wallpaper/{file}')
        print(image.size)
        file_name, extension = os.path.splitext(file)

        # Perform file size manipulation

        # Create a folder if no existing 
        if not os.path.exists('./images/x300'):
            os.mkdir('./images/x300')
            print('Creating a new path....')
        # Resize and Save Image
        image.thumbnail(size_300)
        print(image.size)
        image.save(f'./images/x300/{file_name}{size_300}{extension}')  
        
        if not os.path.exists('./images/x600'):
            os.mkdir('./images/x600')
            print('Creating a new path....')
        # Resize and Save Image
        image.thumbnail(size_600)
        print(image.size)
        image.save(f'./images/x600/{file_name}{size_600}{extension}')

