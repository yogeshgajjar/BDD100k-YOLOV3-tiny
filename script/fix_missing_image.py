import glob, os

label_dir = '/home/san/Dev/dataset/bdd100k_data/bdd100k/labels/100k/train'
image_dir = '/home/san/Dev/dataset/bdd100k_data/bdd100k/images/100k/train'

for label in os.listdir(label_dir):
    if label.endswith('.txt'):
        label_name = os.path.splitext(label)[0]

        # Corresponding label file name
        image_name = label_name + '.jpg'
        if os.path.isfile(image_dir + '/' + image_name) == False:
            print(" -- DELETE LABEL [Image file not found -- ]")
            label_path = label_dir + '/' + label_name + '.txt'
            os.remove(label_path)