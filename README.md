# climgur

Climgur (command line imgur) is a fork of the imgurup repo, but instead uses argparse and imgurpython. Actually, almost 100% of the original code is gone as I got a little carried away (oops).
Current features:
* Upload anonymously or as a registered user
* Upload single image
* Upload local folder as album
* Take screenshot and upload from command line
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

## Requirements

To install any dependences, cd into the main directory and type into the command line:
```
$ pip install -r requirements.txt
```

AutoPy is not required to run climgur, only to take screenshots.
**_If you receive errors installing autopy, please look below for installation instructions_**

#### Linux / Os x
You need to install libpng and zlib before you try to run climgur.
```
$ sudo apt-get update
$ sudo apt-get install libpng-dev zlib1g-dev libxtst-dev
$ sudo apt-get install python-dev -y
$ sudo apt-get install <autopy or autopy3>
```

#### Windows
If you get errors through pip, go [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#autopy) and download the relevant .whl file. The .whl files are named like so:
`autopy-<pkg version>-cp<python version>-none-<architecture>.whl`.
32 bit architecture is denoted by win32, while 64 bit is by win_amd64.
Install the downloaded file by changing into its directory and typing `pip install <filename>.whl`

## Use
Only use the -m argument when the path argument points to a folder. Single file uploads can use the -t and -d arguments to add relavent metadata. Please note that using the -m argument will overwrite -t and -d arguments.

*By default, all uploads are anonymous.* If you want to associate an upload with a user account, use the -u argument.

Taking a screenshot will save to the path argument. It will overwrite if the image already exists.

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
  -m, --metadata        add data to individual images when uploading album
```

## To-Do
* Add support for >1 account

## Licence
Licenced under the [WTFPL](http://www.wtfpl.net/).
