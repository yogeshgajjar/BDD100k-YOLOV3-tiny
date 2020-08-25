import argparse
import json


def label2txt(frames, det_path):
    """
    This function converts the labels into a .txt file with the same name as the image. It extracts the bounding box, class info from the 
    .json file and converts it into the darknet format. 

    The darknet format is 
        <object id> <x> <y> <width> <height> 

    :params 
        frames : each image with labeled information in the .json file.  
        det_path : The path to output detection file. 
    """

    for frame in frames:
        img_name = frame['name']
        frame_name = img_name[:-4]

        #Creates, opens, and adds to a txt file with the name of each image.jpg
        f = open(det_path + frame_name + ".txt","w+")

        #For each sub label of each image, get the box2d variable
        #Get the relative center point compared to the image size 1280/720
        for label in frame['labels']:
            if 'box2d' not in label:
                continue
            xy = label['box2d']
            if xy['x1'] >= xy['x2'] or xy['y1'] >= xy['y2']:
                continue
            X = xy['x1']/1280
            Y = xy['y1']/720
            MX = ((xy['x1'] + xy['x2']) / 2)/1280
            MY = ((xy['y1'] + xy['y2']) / 2)/720
            W = xy['x2']/1280
            H = xy['y2']/720
            if X > W or Y > H:
                continue
            lbl = -1

            #provide a number corresponding to the category of sub label for darknet format.
            if(label['category'] == "bike"):
                lbl = 0
            if(label['category'] == "bus"):
                lbl = 1
            if(label['category'] == "car"):
                lbl = 2
            if(label['category'] == "motor"):
                lbl = 3
            if(label['category'] == "person"):
                lbl = 4
            if(label['category'] == "rider"):
                lbl = 5 
            if(label['category'] == "traffic light"):
                lbl = 6
            if(label['category'] == "traffic sign"):
                lbl = 7
            if(label['category'] == "train"):
                lbl = 8
            if(label['category'] == "truck"):
                lbl = 9
            f.write(repr(lbl) + " " + repr(MX) + " " + repr(MY) + " " + repr(W-X) + " " + repr(H-Y) + '\n')

def convert_labels(label_path, det_path):
    """
    Intermediate method called to pass the argument in to the label2txt folder. 

    :params 
        label_path  : The path where image labels are present. Basically the .json file 
        det_path    : The path for the output detection file   
    """
    
    frames = json.load(open(label_path, 'r'))
    det = label2txt(frames, det_path)
    # json.dump(det, open(det_path, 'w'), indent=4, separators=(',', ': '))


def main():

    ap = argparse.ArgumentParser()
    ap.add_argument('-l', '--label_path', help='path to the label dir')
    ap.add_argument('-d', '--det_path', help='path to output detection file')
    # ap.add_argument('-n', '--folder_name', help='name of the label folder') 
    args = ap.parse_args()

    convert_labels(args.label_path, args.det_path)


if __name__ == '__main__':
    main()  