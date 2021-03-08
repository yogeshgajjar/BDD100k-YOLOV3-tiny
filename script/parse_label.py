#!/usr/bin/python

f = open("image_label_txt", "w+")
import json
import csv


json_data = open('/home/yogesh/Git/BDD100K-YOLOV3/bdd100k_labels/labels/bdd100k_labels_images_train.json')
print("----- LOADING JSON -----")
data = json.load(json_data)

# Construct a dictionary
class_dict = {}

num_of_images = len(data)
# initialze current_index
latest_class_label = 0 #Only add one when it is a new class

# List of category that need to be ignorded
list_of_category_to_ignore = ["drivable area", "lane"]


# Fill out the dictionary
for i in range(num_of_images):
    print("[STEP 1] =============  image number i: ", i)
    print("latest_class_label: " , latest_class_label)
    current_image = data[i]
    image_name = current_image['name']
    print("image_name: ", image_name)
    # Create a Text file for each image
    image_label_txt = str(image_name[:-4]) + ".txt"
    print("image_label_txt: ", image_label_txt)



    num_of_object_in_image = len(current_image['labels']) # In the type of dict

    print('num_of_object_in_image: ' , num_of_object_in_image)
    # For each object in the current image
    for j in range(num_of_object_in_image):
        print("[STEP 2] ============== object number: ", j)
        current_object = current_image['labels'][j]
        current_object_label = current_object['category']
        print("current_object_label:   ", current_object_label)

        if current_object_label in list_of_category_to_ignore:
            print("The current object label is in the ignore list")
        else:
            # Get the X-Y info
            y1 = current_object['box2d']['y1']
            x2 = current_object['box2d']['x2']
            x1 = current_object['box2d']['x1']
            y2 = current_object['box2d']['y2']
            image_width = 1280
            image_height = 720

            # x-y => Center of the box2d
            bbox_x = (x1 + x2)/2
            bbox_y = (y1 + y2)/2

            bbox_x_normalized = bbox_x / image_width
            bbox_y_normalized = bbox_y / image_height

            bbox_width = abs(x1-x2)
            bbox_height = abs(y1-y2)

            bbox_width_normalized = bbox_width / image_width
            bbox_height_normalized = bbox_height / image_height

            print("Center X-Y & Width-Height")
            print(bbox_x, bbox_y, bbox_width, bbox_height)
            print("NORMALIZED Center X-Y & Width-Height")
            print(bbox_x_normalized, bbox_y_normalized, bbox_width_normalized, bbox_height_normalized)


            # Check if current_object_label is already in the dictionary (Add )
            if class_dict.has_key(current_object_label):
                print("current_object_label is already in the class_dict")
                # show current size of class_dict
                print("len(class_dict):  ", len(class_dict))
            else:
                print("New Class: add to class_dict")
                print("label_to_be_added: ", current_object_label)
                class_dict[current_object_label] = latest_class_label
                # Update label count
                latest_class_label = latest_class_label + 1
                # show current size of class_dict
                print("len(class_dict):  ", len(class_dict))

            # Get the corresponding label from the class dict
            class_label_code = class_dict[current_object_label]
            print("class_label_code: ", class_label_code)
            # Prepare the line to be written down to txt file
            line_to_be_written = str(class_label_code) + " " + str(bbox_x_normalized) + " " + str(bbox_y_normalized) + " " + str(bbox_height_normalized) + " " + str(bbox_width_normalized)
            print("line_to_be_written: ", line_to_be_written)
            f.write(line_to_be_written + "\n")


    f.close()
    print("=== Show current Class Dict Collection ====")
    print(class_dict.items())
    #input("Press Enter to continue...")



print(" --- END OF CLASS DICT CONSTRUCT ---")
print(class_dict.items())

# Save class dictionary to text file
f = open("class_dict.txt","w")
f.write( str(class_dict) )
f.close()

# Save class dictionary to csv file
w = csv.writer(open("class_dict.csv", "w"))
for key, val in class_dict.items():
    w.writerow([key, val])