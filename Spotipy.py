# Testing Spotify API

import spotipy
import spotipy.util as util

import credentials

# Set up credentials for token
username = credentials.username
scope = credentials.scope
client_id = credentials.client_id
secret = credentials.secret
redirect = credentials.redirect

# Get authorisation from user
token = util.prompt_for_user_token(username,scope,client_id,secret,redirect)

# Create our spotifyObject
sp = spotipy.Spotify(auth=token)

# Get playlists for user
playlists = sp.user_playlists(username)
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
