#import urllib3
#import certifi
import requests,json
import sys,os
import spotipy
import spotipy.util as util
import pprint
import subprocess
import setenv
#urllib3.disable_warnings()

scope = 'user-library-read playlist-modify-private playlist-modify-public'

### https requests verification###

#http = urllib3.PoolManager(
  #  cert_reqs='CERT_REQUIRED', # Force certificate check.
 #   ca_certs=certifi.where(),  # Path to the Certifi bundle.
#)

# You're ready to make verified HTTPS requests.
#try:
#    r = http.request('GET', 'https://example.com/')
#except urllib3.exceptions.SSLError as e:
    # Handle incorrect certificate error.

playlist_id =""

def show_tracks(results):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print "   %d %32.32s %s" % (i, track['artists'][0]['name'],track['name'])
	#print(track['id'])
	

#if len(sys.argv) > 1:
#    username = sys.argv[1]
#else:
#    print "Usage: %s username" % (sys.argv[0],)
#    sys.exit()

username = 'adaptiveplayer'
client_id = os.environ['SPOTIPY_CLIENT_ID']
client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
redirect = os.environ['SPOTIPY_REDIRECT_URI']


token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect)

if token:
    	sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
   	for playlist in playlists['items']:
		if playlist['name'] == 'Baochan':
			print (playlist['tracks']['total'])
			results = sp.user_playlist(username,playlist['id'],
				fields="tracks,next")
			tracks = results['tracks']
			playlist_id = str(playlist['id'])
			print "THIS IS PLAYLIST ID %s" %playlist_id
			show_tracks(tracks)
				
#	headers = {
#		'Accept':'application/json',
#		'Authorization': 'Bearer %s' %token}
	
#	user_id = 'donovan.chan-us'
#	url = 'http://api.spotify.com/v1/users/%s' %user_id
	
	#urlpost = 'https://api.spotify.com/v1/users/donovan.chan-us/playlists/1MX4494KtmaKr92dMXVXfT/tracks?uris=spotify%3Atrack%3A2YlZnw2ikdb837oKMKjBkW' 
	
#	urlpost1 = 'https://api.spotify.com/v1/users/%s/playlists/%s' %(user_id,playlist_id) 
#	urlpost2 = '/tracks?uris=spotify%3Atrack%3A2YlZnw2ikdb837oKMKjBkW'
#	urlpost3 = urlpost1 +urlpost2

#	print urlpost3
	
		
#	r= requests.get(url,headers=headers)
#	p = requests.post(urlpost3, headers=headers)
#	print r.json()
#	print p.json()

	

else:
    print "Can't get token for", username


