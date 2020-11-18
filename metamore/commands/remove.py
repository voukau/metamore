import piexif
import click


@click.command()
@click.argument('target', type=click.Path(exists=True))
@click.option('-a', '--all', is_flag=True, help='Remove all EXIF data from a file.')
# @click.option('-k', '--key', type=click.Choice(['0th', 'Exif', 'GPS', 'Interop', '1st'],case_sensitive=False, help='Remove EXIF data stored in particular key.')
def cli(target, all):
    """Remove EXIF metadata from file(s)"""

    if all:
        piexif.remove(target)
