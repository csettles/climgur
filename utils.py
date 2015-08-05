from __future__ import print_function

album_fields = ['title', 'description', 'privacy', 'layout']


# def get_config():
#     '''Create config parser for auth.ini'''
#     try:
#         import ConfigParser
#         return ConfigParser.ConfigParser()
#     except ImportError:
#         import configparser
#         return configparser.ConfigParser()


# def get_input(string):
#     '''Makes getting input compatible with python2/3'''
#     try:
#         return raw_input(string)
#     except NameError:
#         return input(string)


def save_config(config):
    '''Save changes to auth.ini'''
    with open('auth.ini', 'w') as configfile:
        config.write(configfile)


def get_metadata(album=False):
    '''Prompts the user for information about the upload.
    Extra fields if user is uploading an album'''

    print("""All fields are optional. Please enter desired values:""")

    if album:
        print("""privacy: public | hidden | secret (users only)
        layout: blog | grid | horizontal | vertical""")
        data = {field: get_input('Enter {}\n>\t'.format(field))
                for field in album_fields}
    else:
        data = {field: get_input('Enter {}\n>\t'.format(field))
                for field in album_fields[:2]}
    return data

if __name__ == '__main__':
    print(get_metadata())
