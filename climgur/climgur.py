from __future__ import print_function
import argparse
import sys
import os
from glob import glob
import webbrowser
from datetime import datetime

from auth import get_anon_client, log_in
from utils import get_metadata

# file extensions accepted by imgur
file_extensions = ['.png', '.jpg', '.gif', '.tif',
                   '.bmp', '.tiff', '.pdf', '.xcf']


class Uploader:

    """A class that interacts with imgur's api in order to
    upload local images to imgur.com from the command line.
    """

    def __init__(self, args):
        self.args = args
        self.metadata = dict(title=self.args.title,
                             description=self.args.description)
        self.init_client()

    def init_client(self):
        """Sets ImgurClient scope based on user preference"""
        self.client = get_anon_client()
        if self.args.user:
            self.client = log_in(self.client)

    def upload_pic(self, path, data, album_id=None):
        # as of now, does not check for valid file extension
        anon = self.client.auth is None
        if album_id:
            data['album'] = album_id
        image = self.client.upload_from_path(path, data, anon)

        self.log_upload(image)

        return image['id']  # return image if more data is needed

    def upload_album(self):
        album_data = get_metadata(
            True) if self.args.metadata else self.metadata
        album = self.client.create_album(album_data)
        print('Created album named "{}"'.format(album_data.get('title')))
        self.log_upload(album)

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

    def log_upload(self, entity):
        """Record time of upload and deletion links of upload in
        local file log.txt
        """
        with open('log.txt', 'a+') as f:
            deletehash = entity['deletehash']
            link = 'http://imgur.com/delete/{}'.format(deletehash)
            record = '{} {}'.format(datetime.now().strftime('%c'), link)
            f.write(record+'\n')
        return link

    def main(self):
        args = self.args
        if args.screenshot:
            if args.path.endswith('.png') or args.path.endswith('.bmp'):
                from screenshot import take_screenshot
                take_screenshot(args.path, args.delay)
                pic_id = self.upload_pic(args.path, self.metadata)
                print('Upload complete.')
                webbrowser.open(self.client.get_image(pic_id).link)
            else:
                sys.exit('File must be saved as a bitmap or png.')

        elif os.path.isfile(args.path):
            pic_id = self.upload_pic(args.path, self.metadata)
            print('Upload complete.')
            webbrowser.open(self.client.get_image(pic_id).link)

        elif os.path.isdir(self.args.path):
            album_id = self.upload_album()
            print('Upload complete.')
            webbrowser.open(self.client.get_album(album_id).link)

        else:
            sys.exit("\nWhat you are trying to upload does not exist")


if __name__ == "__main__":
    description = """A command line wrapper for imgur's api"""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('path', action='store',
                        help='path to file or folder to upload')
    parser.add_argument('-t', '--title',
                        action='store', help='title of upload')
    parser.add_argument('-d', '--description',
                        action='store', help='upload description')
    parser.add_argument('-u', '--user', action='store_true',
                        help='upload to stored user account')
    parser.add_argument('-m', '--metadata', action='store_true',
                        help='add data to images when uploading album')
    parser.add_argument('-s', '--screenshot', action='store_true',
                        help='take screenshot and upload it')
    parser.add_argument('--delay', default=3, type=int,
                        help='delay (s) before taking screenshot')
    args = parser.parse_args()
    Uploader(args=args).main()
