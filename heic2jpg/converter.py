from PIL import Image
import os

def converter(images, dst):

    # path of the folder containg .jpg photos
    directory = os.path.join(dst)

    counter = 0

    for path, filename in images:

        # image conversion
        image = Image.open(path)

        # saving the filename
        filename_no_extension, _ = os.path.splitext(filename)

        # saving metadata
        exif = image.getexif()

        # converting/saving the image
        image.save(f"{directory}/{filename_no_extension}.jpg", quality=95, exif=exif)

        counter += 1
        print("%d file(s) converted: %s" % ( counter, filename) , end="\r")

    print("")
    print("finished, all %d photo(s) have been converted to .jpg:)" %(counter))