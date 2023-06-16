import cv2
import os
from os import getcwd

def GetFileList(mypath):
    return [f for f in listdir(mypath) if isfile(join(mypath, f))]

def start():
    path = getcwd()
    indir = path + "\\box\\"
    outdir = path + "\\box\\"

    blur = int(input('    Blur Amount? (1 - 100):'))
    if (blur % 2 == 0):
        blur += 1
    blur_images_in_folder(indir, blur)
    print("\n    Done!")

def blur_images_in_folder(folder_path, blur_amount):
    path = getcwd()
    indir = path + "\\box\\"
    outdir = path + "\\box\\"

    # Iterate through the files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Load the image
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)

            # Apply Gaussian blur
            blurred_image = cv2.GaussianBlur(image, (blur_amount, blur_amount), 0)

            # Save the blurred image
            output_path = os.path.join(folder_path, 'blurred_' + filename)
            cv2.imwrite(output_path, blurred_image)

            print(f"    Blurred image saved: {output_path}")