from __future__ import print_function
import argparse
import sys
import os
from glob import glob
import webbrowser

from auth import get_anon_client, log_in
from helpers import get_metadata

# file extensions accepted by imgur
file_extensions = ['.png', '.jpg', '.gif', '.apng',
                   '.bmp', '.jpeg', '.tiff', '.pdf', '.xcf']


class CLUploader:

    def __init__(self, args):
        self.args = args
        self.metadata = dict(title=self.args.title,
                             description=self.args.description)
        self.initialize()

    def initialize(self):
        """Sets ImgurClient scope based on user preference"""
        if not args.user:
            self.client = get_anon_client()
        else:
            self.client = log_in(get_anon_client())

    def upload_pic(self, path, data, album_id=None):
        anon = self.client.auth is None
        if album_id:
            data['album'] = album_id
        image = self.client.upload_from_path(path, data, anon)

        return image['id']  # return image if more data is needed

    def upload_album(self):
        album_data = get_metadata(
            True) if self.args.metadata else self.metadata
        album = self.client.create_album(album_data)
        print('Created album named "{}"'.format(album_data.get('title')))
        album_id = album['id'] if self.client.auth else album['deletehash']

        # get all images in the folder with approved file extensions
        files = [glob(os.path.join(self.args.path, '*' + ext))
                 for ext in file_extensions]
        files = sum(files, [])  # ugly way to flatten list

        for f in files:
            print('Uploading {}'.format(os.path.basename(f)))
            img_data = get_metadata() if self.args.metadata else dict()
            self.upload_pic(f, img_data, album_id)

        return album['id']  # return album if more data is needed

    def main(self):
        if os.path.isfile(self.args.path):
            pic_id = self.upload_pic(self.args.path, self.metadata)
            print('Upload complete.')
            webbrowser.open(self.client.get_image(pic_id).link)
        elif os.path.isdir(self.args.path):
            album_id = self.upload_album()
            print('Upload complete.')
            webbrowser.open(self.client.get_album(album_id).link)
        else:
            sys.exit("\nWhat you are trying to upload does not exist")


if __name__ == "__main__":
    description = "A command line wrapper for imgur's api"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        'path', action='store', help="path to file or folder to upload")
    parser.add_argument(
        '-t', '--title', action='store', help="title of upload")
    parser.add_argument(
        '-d', '--description', action='store', help='upload description')
    parser.add_argument(
        '-u', '--user', action='store_true', help="upload to a user account")
    parser.add_argument('-m', '--metadata', action='store_true',
                        help="add data to individual images when uploading album")
    args = parser.parse_args()
    CLUploader(args=args).main()
