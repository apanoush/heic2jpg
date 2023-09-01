# heic2jpg

searches for `.heic` photos in the `--src` folder, convert all of them to `.jpg` photos and saves them in the `--dst` folder.
if an image can't converted, it will be copied to the `--dst/not converted images` folder

## why

apple icloud photos (through their website) only accepts `.jpg` photos while google photos export photos taken on an iphone with the `.heic` format

## usage

`python main.py --src path --dst path`

- `--src`: folder where are stored the `.heic` photo, **optional**, default is "`data`"
- `--dst`: folder that will be created where the `.jpg` photos will be stored, **optional**, default is "`jpgs`"


## dependencies

uses `Pillow`.
you can install it using `pip install Pillow`