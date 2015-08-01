# climgur

Climgur (command line imgur) is a fork of the imgurup repo, but instead uses argparse and imgurpython. Actually, almost 100% of the original code is gone as I got a little carried away (woops).
Current features:
* Upload anonymously or as a registered user
* Upload single image
* Upload local folder as album
* Set title, description, album type, privacy setting depending on upload type

## Setup

In order to run climgur, you must create an auth.ini file in the main directory.

Provide your client_id and client_secret by [adding an imgur client](http://api.imgur.com/oauth2/addclient) (requires an imgur account). Leave the access and refresh token fields blank.
```
[credentials]
client_id=
client_secret=
access_token=
refresh_token=
```

## Use
Only use the -m argument when the path argument points to a folder. Single file uploads can use the -t and -d arguments to add relavent metadata. Please note that using the -m argument will overwrite -t and -d arguments.

*By default, all uploads are anonymous.* If you want to associate an upload with a user account, use the -u argument.

 ```
 positional arguments:
  path                  path to file or folder to upload

optional arguments:
  -h, --help            show this help message and exit
  -t TITLE, --title TITLE
                        title of upload
  -d DESCRIPTION, --description DESCRIPTION
                        upload description
  -u, --user            upload to a user account
  -m, --metadata        add information to individual images when uploading an album
```

## Requirements
climgur uses [requests](https://pypi.python.org/pypi/requests) and [imgurpython](https://github.com/Imgur/imgurpython) to upload images from the command line.
To install any dependences, cd into the main directory and type into the command line:
```
$ pip install -r requirements.txt
```

## Licence
Licenced under the [WTFPL](http://www.wtfpl.net/).
