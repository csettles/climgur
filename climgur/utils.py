from __future__ import print_function

from six.moves import input

_album_fields = ['title', 'description', 'privacy', 'layout']
_advanced_options = """privacy: public | hidden | secret (users only)
                       layout: blog | grid | horizontal | vertical
                    """


def save_config(config):
    '''Save changes to auth.ini'''
    with open('auth.ini', 'w') as configfile:
        config.write(configfile)


def get_metadata(album=False):
    '''Prompts the user for information about the upload.
    Extra fields if user is uploading an album'''

    print("""All fields are optional. Please enter desired values:""")

    if album:
        print(_advanced_options)
        data = {field: input('Enter {}\n>\t'.format(field))
                for field in _album_fields}
    else:
        data = {field: input('Enter {}\n>\t'.format(field))
                for field in _album_fields[:2]}
    return data

if __name__ == '__main__':
    print(get_metadata())
