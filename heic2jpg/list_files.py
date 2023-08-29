import os

def list_files(src):

    # all paths and filenames of .heic photos will be added in this array
    images = []

    # searching
    for path, _, filenames in os.walk(src):
        for filename in [f for f in filenames if f.lower().endswith(".heic")]:
            images.append( (os.path.join(path, filename), filename) )
    
    print("%d .heic images found in \"%s\"" % (len(images), src))

    return images