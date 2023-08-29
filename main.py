import os
import heic2jpg.converter
import heic2jpg.list_files
import argparse

def main(args):

    # checks if data folder exists
    if not (os.path.exists(args.src)):
        raise Exception("not folder called \"%s\" found" %(args.src))

    # creates jpgs directory where converted photos will be stored
    if not (os.path.exists(args.dst)):
        os.mkdir(args.dst)

    images = heic2jpg.list_files.list_files(args.src)

    if (len(images) == 0): 
        raise Exception("no .heic photo found in %s" %(args.src))

    heic2jpg.converter.converter(images, args.dst)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='converting .heic photos to .jpg')
    parser.add_argument('--src', default="data", type=str, help="folder where are stored the .heic photos")
    parser.add_argument('--dst', default="jpgs", type=str, help="folder that will be created where the .jpg photos will be stored")
    args = parser.parse_args()
    main(args)