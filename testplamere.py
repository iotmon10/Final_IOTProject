import os
import pprint
import sys
import json
import spotipy
import spotipy.util as util
import setenv

#if len(sys.argv) > 3:
 #   username = sys.argv[1]
  #  playlist_id = sys.argv[2]
   # track_ids = sys.argv[3:]
#else:
 #   print("Usage: %s username playlist_id track_id ..." % (sys.argv[0],))
  #  sys.exit()

username = 'adaptiveplayer'
client_id = os.environ['SPOTIPY_CLIENT_ID']
client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
redirect = os.environ['SPOTIPY_REDIRECT_URI']


scope = 'playlist-modify-public '
token = util.prompt_for_user_token(username, scope,client_id,client_secret,redirect)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = True
    genre = sp.recommendation_genre_seeds()
    print(json.dumps(genre,indent=4)) 

else:
    print("Can't get token for", username)
