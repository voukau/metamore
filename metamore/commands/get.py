import piexif
import click
import os


@click.command()
@click.argument('target', type=click.Path(exists=True))
@click.option('-o', '--out', is_flag=True, help='Save output to file.')
@click.option('--no-thumbnail', 'nothumb', is_flag=True, help='Ignore thumbnail data.')
def cli(target, out, nothumb):
    """Get EXIF metadata from file(s)"""
    exif_dict = piexif.load(target)

    if nothumb:
        del exif_dict["thumbnail"]

    if out:
        with open(os.path.splitext(target)[0]+'_meta.txt', 'w') as f:
            print(exif_dict, file=f)
    else:
        print(exif_dict)
