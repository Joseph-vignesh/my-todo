import zipfile
import pathlib  # zipfile: This module provides tools for creating, reading, writing, and extracting ZIP files.
#                  pathlib: This module offers classes to handle filesystem paths in an object-oriented way.


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname= filepath.name)


# if __name__ == __"main"__:
#     make_archive()