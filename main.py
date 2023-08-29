import os
import heic2jpg.converter
import heic2jpg.list_files
import argparse

def main(args):

    # checks if --src folder exists
    if not (os.path.exists(args.src)):
        raise Exception("not folder called \"%s\" found, it should contain all .heic photos to be converted" %(args.src))

    # creates --dst directory (if it doesn't exist already) where converted photos will be stored
    if not (os.path.exists(args.dst)):
        os.mkdir(args.dst)

    # finds all .heic photos in --src
    images = heic2jpg.list_files.list_files(args.src)

    # if no .heic file found raise an error
    if (len(images) == 0): 
        raise Exception("no .heic photo found in %s" %(args.src))

    # converts all these photos to .jpg and saves them in --dst
    heic2jpg.converter.converter(images, args.dst)

if __name__ == "__main__":
    # all arguments
    parser = argparse.ArgumentParser(description='converting .heic photos to .jpg')
    parser.add_argument('--src', default="data", type=str, help="folder where are stored the .heic photos")
    parser.add_argument('--dst', default="jpgs", type=str, help="folder that will be created where the .jpg photos will be stored")
    args = parser.parse_args()
    main(args)