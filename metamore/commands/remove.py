import piexif
import click
import os


@click.command()
@click.argument('target', type=click.Path(exists=True))
@click.option('-d', '--dir', is_flag=True, help='Target is a directory. Remove EXIF data from all files in target '
                                                'directory.')
def cli(target, dir):
    """Remove EXIF metadata from file(s)"""
    if dir:
        directory = os.fsencode(target)
        no_jpg_found = True
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".jpg") or filename.endswith(".jpeg"):
                no_jpg_found = False
                piexif.remove(target + '/' + filename)
        if no_jpg_found is True:
            print("Error: No JPG/JPEG files found in the target directory")

    else:
        piexif.remove(target)
