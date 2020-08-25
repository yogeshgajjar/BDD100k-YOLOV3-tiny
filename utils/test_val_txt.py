import pickle
import os, argparse
from os import listdir, getcwd
from os.path import join


def create_train(train_img_path):
    """
    Creates the .txt file which contains the entire path of the training image file. This file is required to be added in the 
    .data file 

    :params 
        train_img_path : The path of the training images 

    """

    f = open("train.txt", "w+")
    for subdirs, dirs, files in os.walk(train_img_path):
        for filename in files:
            if filename.endswith(".jpg"):
                train_image_path = os.path.join(train_img_path, filename)
                print(train_image_path)
                f.write(train_image_path + "\n")
    f.close()

def create_val(val_img_path):
    """
    Creates the .txt file which contains the entire path of the validation image file. This file is required to be added in the 
    .data file 

    :params 
        val_img_path : The path of the validation images  

    """

    f = open("val.txt", "w+")
    for subdirs, dirs, files in os.walk(val_img_path):
        for filename in files:
            if filename.endswith(".jpg"):
                val_image_path = os.path.join(val_img_path, filename)
                print(val_image_path)
                f.write(val_image_path + "\n")
    f.close()


def main():

    ap = argparse.ArgumentParser()
    ap.add_argument('-l', '--train_image_path', help='path to the label dir')
    ap.add_argument('-d', '--val_image_path', help='path to output detection file') 
    args = ap.parse_args()

    create_train(args.train_image_path)
    create_val(args.val_image_path)

if __name__ == "__main__":
    main()



