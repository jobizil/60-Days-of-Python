"""
IMAGE PROCESSING
To get started with image processing, we need to install a required libraries and the most commonly used one is Pillow. 
Pillow is a fork of the Python Imaging Library (PIL). It is a library that adds support for opening, manipulating, and saving many different image file formats.


To install Pillow, we can use pip:
pip install Pillow

To use Pillow, we need to import it:
from PIL import Image

We can then open an image using the Image.open() function:
img = Image.open('image.jpg')

We can then use the show() function to display the image:
img.show()

We can also save the image using the save() function:
img.save('image.png')

We can also use the dir() function to see all the methods and attributes available to the Image object:
print(dir(img))

The Pillow library has many methods and attributes that we can use to manipulate images. Some of the most commonly used methods are:
- img.size: returns the width and height of the image in pixels
- img.format: returns the format of the image
- img.mode: returns the mode of the image
- img.show(): opens the image in a preview mode
- img.save('image.png'): saves the image as a png file
- img.rotate(90): rotates the image 90 degrees clockwise
- img.convert('L'): converts the image to black and white
- img.convert('RGB'): converts the image to RGB
- img.thumbnail((400, 400)): resizes the image to a 400x400 thumbnail

We can also use the ImageFilter module to apply filters to images:
from PIL import Image, ImageFilter

img = Image.open('image.jpg')
img.filter(ImageFilter.BLUR).save('blur.jpg')
img.filter(ImageFilter.CONTOUR).save('contour.jpg')
img.filter(ImageFilter.DETAIL).save('detail.jpg')


"""


# # Opens Image we intend to mainpulate/processs
# img = Image.open('./pokedex/squirtle.jpg')
# print(dir(img) )
# # img.show() # This opens the image in a preview mode
# img.save('squirtle.png') #  Change file extension 

# # Rotate image 90 degrees clockwise
# img.rotate(90).save('squirtle90.png')


# Processing Multiple Images
# We can use the os module to loop through all the images in a directory and process them.
# We can use the os.listdir() function to get a list of all the files in a directory:


from PIL import Image
import os

# Resize all images to 300x300
size_300 = (300, 300)
size_700 = (700, 700)

for file in os.listdir('./pokedex'):
    """
    Loop through all the files in the pokedex directory and check if they end with a .jpg extension.
    """
    # Checks if file ends with a .jpg extension
    if file.endswith('.jpg'):
        #  Make an image object from the file
        img = Image.open(f'./pokedex/{file}')
        #  Split the file name and extension
        filename,extension = os.path.splitext(file)

        #  Resize the image
        
        if not os.path.exists('./300'):  # Creates a folder called 300 if it doesn't exist
            os.makedirs('300')
            img.thumbnail(size_300)
        img.save(f'./300/{filename}_300{extension}')

        if not os.path.exists('700'):
            new_path = os.makedirs('700')
            img.thumbnail(size_700)
        img.save(f'./700/{filename}_700{extension}')

        #  Save the image to a new file with the same name and .png extension
        if not os.path.exists('pngs'):
            os.mkdir('pngs')
        img.save(f'./pngs/{filename}.png')  

print('all done!')
