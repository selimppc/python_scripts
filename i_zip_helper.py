import os
import sys
import shutil
import pyminizip


def iZip(source_dir, output):
    """zip"""
    shutil.make_archive(output, 'zip', source_dir)
    return True


def remove(source):
    """remove file """
    try:
        os.remove(source)
        return True
    except OSError as e:
        print("Error: %s : %s" % (source, e.strerror))
        return e.strerror


def rename(old_name, new_name):
    """rename file"""
    try:
        os.rename(old_name, new_name)
        return True
    except OSError as e:
        print("Error: %s : %s" % (old_name, e.strerror))
        return e.strerror


def mini_zipper():
    """mini zipper"""
    if sys.argv[1] and sys.argv[2] and sys.argv[3]:
        source_dir = 'image'  # sys.argv[1]  # dir name
        output = 'com_zip'  # sys.argv[2]  # dir name // 'image_zip.zip'
        password = b'pass'  # sys.argv[3]  # password

        # create zip file
        iZip(source_dir, output)

        # create password for zipFile
        pyminizip.compress(output + '.zip', None, output + '_.zip', password, int(5))

        # remove zip file
        new_name = output + '.zip'
        if remove(new_name) is True:
            old_name = output + '_.zip'

            # rename password protected zip
            rename(old_name, new_name)

        return True
    else:
        return 'Invalid Params'


if __name__ == '__main__':
    mini_zipper()
