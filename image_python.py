from PIL import Image
import os

image_path = "hi.jpeg"
if os.path.exists(image_path):
    try:  
        div = Image.open(image_path)
        divi = div.rotate(0)
        divi.show()
        div.show()
        print("Original Image Size:", div.size)
        print("Rotated Image Size:", divi.size)
    except Exception as e:
        print("Error:", e)
else:
    print("Image file not found at the specified path.")
