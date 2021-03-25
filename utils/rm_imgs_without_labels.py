import argparse
import os
from pathlib import Path

import logging


def missing_image(image_path: Path, label_path: Path):
    """
    This function removes the images from the train folder if the correspining labels
    are not found in the .txt file.

    NOTE - Make sure you perform the conversion from the label to txt.
    The code performs the following function,

    - Takes the input dataset folder path, searches if the images with label information
      are present.
    - If not found, removes the image.

    :params
        image_path  - The directory where the training images are present
        label_path  - The directory where .txt file correspinding to each image is
                      present.
    """

    for image in image_path.iterdir():
        if image.suffix == ".jpg":
            # Corresponding label file name
            label = label_path / (image.stem + ".txt")
            if not label.is_file():
                logging.warning("Label not found: {}".format(label))
                logging.warning("Deleting file:   {}".format(image))
                os.remove(image)


def main():

    ap = argparse.ArgumentParser()
    ap.add_argument("-l", "--label_path", help="path to the label dir")
    ap.add_argument("-d", "--image_path", help="directory with images")
    args = ap.parse_args()

    image_path = Path(args.image_path).absolute()
    label_path = Path(args.label_path).absolute()

    assert image_path.is_dir(), "Image directory needs to exist"
    assert label_path.is_dir(), "Label directory needs to exist"

    missing_image(image_path, label_path)


if __name__ == "__main__":
    main()
