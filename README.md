# heic2jpg

searches for `.heic` photos in the `--src` folder, convert all of them to `.jpg` photos and saves them in the `--dst` folder

## why

apple icloud photos (through their website) only accepts `.jpg` photos while google photos export photos taken on an iphone with the `.heic` format

## usage

`python main.py --src path --dst path`

- `--src`: folder where are stored the `.heic` photo, **optional**, default is "`data`"
- `--dst`: folder that will be created where the `.jpg` photos will be stored, **optional**, default is "`jpgs`"
