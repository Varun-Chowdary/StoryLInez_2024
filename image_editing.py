image editing
import cv2
from PIL import Image
"""
Image Editing:
-save image in different formats: .jpeg, .json
-cropping (entire image, one part of the image), flipping
-opacity
-insert text
-adding image
"""

#save image in diff formats
def convert_image_format(input_image_path, output_image_path, output_format):
    try:
        # Open the image file
        img = Image.open(input_image_path)
        
        # Save it in the desired format
        img.save(output_image_path, format=output_format)
        
        print(f"Image saved successfully as {output_image_path} in {output_format} format.")
    except IOError:
        print(f"Unable to save image as {output_image_path} in {output_format} format.")
"""
    JPEG: 'JPEG' or 'JPG'
    PNG: 'PNG'
    BMP: 'BMP'
    GIF: 'GIF'
    TIFF: 'TIFF' or 'TIF'
    WebP: 'WebP'
    ICO: 'ICO'
    PPM/PGM/PBM: 'PPM', 'PGM', 'PBM'
    PDF: 'PDF'
    EPS: 'EPS'
"""
#Crop the base image
def crop_image(image_path, x, y, width, height):
    #x, y = pos on img, width/height tells how the crop should go
    img = cv2.imread(image_path)
    cropped_img = img[y:y+height, x:x+width]
    # Display the original and cropped images (optional)
    cv2.imshow('Original Image', cv2.imread(image_path))
    cv2.imshow('Cropped Image', cropped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return cropped_img
#flip the image
def flip_img(image_path, direction):
    #0 means around x axis, 1 means y axis
    flipped_img = cv2.imread(image_path, 1)
    flipped_img = cv2.flip(flipped_img, direction)
    cv2.imshow('Original Image', cv2.imread(image_path))
    cv2.imshow('Flipped Image', flipped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#insert text
# need to add parameters on where to add the text
def add_text(image_path, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    height = 500
    input_img = cv2.imread(image_path, 1)
    text_img = cv2.putText(input_img, text, (200, height -10), font, 4, [0,0,0], 5, cv2.LINE_AA)
    cv2.imshow('Original Image', cv2.imread(image_path))
    cv2.imshow('Image with text', text_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#adding an image
def add_image_overlay(background_image_path, overlay_image_path, x, y):
    # Read the background and overlay images
    background = cv2.imread(background_image_path)
    overlay = cv2.imread(overlay_image_path, -1)  # Use -1 to include alpha channel if present
    
    x_offset = y_offset = 50
    background[y_offset:y_offset+overlay.shape[0], x_offset:x_offset+overlay.shape[1]] = overlay
    # Display the result (optional)
    cv2.imshow('Result Image', background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return background

# Example usage:
background_image_path = 'assets/image_3.jpg'  # Replace with your background image path
overlay_image_path = 'assets/image_5.jpg'  # Replace with your overlay image path
x, y = 100, 50  # Position where overlay image will be placed

# Add overlay image onto the background image
#result_image = add_image_overlay(background_image_path, overlay_image_path, x, y)

def menu():
    print("1. Convert")
    print("2. Crop Image")
    print("3. Flip Image")
    print("4. Add text")
    print("5. Add image overlay")
    choice = input("Enter the number of your choice ")
    
    if choice == '1':# Convert
        print("You chose Option 1")
        img_path = input("what is the path of the image ")
        save_type = input("what type do you want to save it as ")
        output_path = input("what do you want to call it ")
        convert_image_format(img_path, output_path, save_type)
    elif choice == '2':# Crop
        print("You chose Option 2")
        img_path = input("what is the path of the image ")
        x = int(input("x coord "))
        y = int(input("y coord "))
        height = int(input("hieght of crop "))
        width = int(input("width of crop "))
        crop_image(img_path, x, y, width, height)
        #x, y, width, height = 100, 50, 300, 200 
    elif choice == '3':# Flip
        print("You chose Option 3")
        img_path = input("what is the path of the image ")
        direction = int(input("0 for x axis, 1 for y axis "))
        flip_img(img_path, direction)
    elif choice == '4':# Text
        print("You chose Option 4")
        img_path = input("what is the path of the image ")
        text = input("what text do you want it to say")
        add_text(img_path, text)
    elif choice == '5':# Overlay
        print("You chose Option 5")
        background_image_path = input("background image path ")
        overlay_image_path = input("overlay image ")
        x = int(input("x coord"))
        y = int(input("y coord"))
        result_image = add_image_overlay(background_image_path, overlay_image_path, x, y)
    elif choice == '0':
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please enter a number from 1 to 5 or 0 to exit.")


if __name__ == "__main__":
    menu()
