import os

def list_files(src):
    images = []
    #directory = os.path + "data"

    for dirpath, _, filenames in os.walk(src):
        for filename in [f for f in filenames if f.lower().endswith(".heic")]:
            images.append( (os.path.join(dirpath, filename), filename) )
    
    print("%d .heic images found in \"%s\"" % (len(images), src))

    return images



            