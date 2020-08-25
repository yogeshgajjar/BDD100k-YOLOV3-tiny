import argparse
import glob
import os 

def missing_image(image_path, label_path):
    """
    This function removes the images from the train folder if the correspining labels are not found in the .txt file. 
    NOTE - Make sure you perform the conversion from the label to txt. 
    The code performs the following function, 

    - Takes the input dataset folder path, searches if the images with label information are present. 
    - If not found, removes the image. 

    :params
        image_path  - The directory where the training images are present 
        label_path  - The directory where .txt file correspinding to each image is present. 

    """

    for image in os.listdir(image_path):
        if image.endswith('jpg'):
            image_name = os.path.splitext(image)[0]

            # Corresponding label file name
            label_name = image_name + '.txt'
            if os.path.isfile(label_path + '/' + label_name) == False:
                print(" -- DELETE IMAGE [Label file not found -- ]")
                image_path = image_path + '/' + image_name + '.jpg'
                os.remove(image_path)

def main():

    ap = argparse.ArgumentParser()
    ap.add_argument('-l', '--label_path', help='path to the label dir')
    ap.add_argument('-d', '--image_path', help='path to output detection file') 
    args = ap.parse_args()

    missing_image(args.image_path, args.label_path)

if __name__ == "__main__":
    main()