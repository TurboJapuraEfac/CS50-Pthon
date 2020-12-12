from PIL import Image, ImageFilter

# pip install Pillow to install PIL

# Importing Image and ImageFilter module from PIL package
from PIL import Image, ImageFilter

# creating a image object
im1 = Image.open(r"C:\Users\nimes\OneDrive\Desktop\New folder\Semester 7.jpeg")
# applying the blur filter
im2 = im1.filter(ImageFilter.BLUR)
im2.show()

before = Image.open(r"C:\Users\nimes\OneDrive\Desktop\New folder\Semester 7.jpeg")
after = before.filter(ImageFilter.BoxBlur(1))
after.save("out.bmp")
