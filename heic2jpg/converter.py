from PIL import Image, UnidentifiedImageError
import os
import shutil

def converter(images, dst, length):

    # path of the folder containg .jpg photos
    directory = os.path.join(dst)

    counter = 0

    for path, filename in images:

        try:
            # image conversion
            image = Image.open(path)

        except UnidentifiedImageError:
            
            print(f"{filename} cannot be converted, it will be copied to the \"not converted images\" folder")

            # creating "not created" directory 
            not_converted_path = os.path.join(dst, "not converted images")
            if not (os.path.exists(not_converted_path)):
                os.mkdir(not_converted_path)

            # copying the not converted file to the directory
            shutil.copy(src=path, dst=not_converted_path)

            continue

        # saving the filename
        filename_no_extension, _ = os.path.splitext(filename)

        # saving metadata
        exif = image.getexif()

        # if image not in RGB mode, converts it
        if not (image.mode == 'RGB'):
            image = image.convert('RGB')

        # converting/saving the image
        image.save(f"{directory}/{filename_no_extension}.jpg", quality=95, exif=exif, format="JPEG")

        counter += 1
        print("%d/%d file(s) converted: %s" % ( counter, length, filename))

        

    print("")
    print("finished, all %d photo(s) have been converted to .jpg:)" %(counter))