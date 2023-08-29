from PIL import Image
import os

def converter(images, dst):
    directory = os.path.join(dst)
    counter = 0
    for e in images:
        image = Image.open(e)
        #jpg = image.replace('.HEIC', '.jpg')
        #image.save(f"{directory}/{image}.jpg", "JPEG")
        image.save('test.jpg', quality=100)
        counter += 1
        print("%d file(s) converted: %s" % ( counter, image) , end="\r")

    print("finished, all %d photos have been converted to .jpg:)" %(counter))