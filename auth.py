# auth setup taken from imgurpython's example files
from imgurpython import ImgurClient
import webbrowser # for convenience

from six.moves.configparser import ConfigParser
from six.moves import input

from utils import save_config


def get_anon_client():
    '''Simple ImgurClient that is not tied to a user account'''
    config = ConfigParser()
    config.read('auth.ini')
    client_id = config.get('credentials', 'client_id')
    client_secret = config.get('credentials', 'client_secret')
    # removed for compatibility with python 2.7
    # client_id = config.get('credentials', 'CLIENT_ID', fallback=None)
    # client_secret = config.get('credentials', 'CLIENT_SECRET', fallback=None)
    return ImgurClient(client_id, client_secret)


def log_in(client):
    '''Ties ImgurClient with a user account so uploads will be remembered'''
    config = ConfigParser() 
    config.read('auth.ini')
    access_token = config.get('credentials', 'access_token')
    refresh_token = config.get('credentials', 'refresh_token')
    if len(access_token) > 0 and len(refresh_token) > 0:
        client.set_user_auth(access_token, refresh_token)
        return client

    authorization_url = client.get_auth_url('pin')
    webbrowser.open(authorization_url)
    pin = input('Please input your pin\n>\t')

    credentials = client.authorize(pin)  # grant_type default is 'pin'

    access_token = credentials['access_token']
    refresh_token = credentials['refresh_token']

    config.set('credentials', 'access_token', access_token)
    config.set('credentials', 'refresh_token', refresh_token)

    save_config(config)
    client.set_user_auth(access_token, refresh_token)
    return client
