import argparse
import glob
import os 

'''
Sometimes your image data set might not match with your label data set.
This code does the folowing
(1) Go through your image data set
(2) Search if the corresponding label file exist in the label data set. 
(3) If not, remove current image
'''

def missing_image(image_path, label_path):
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