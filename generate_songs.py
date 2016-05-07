import requests, json
import random
import sys,os
import spotipy
import spotipy.util as util
import pprint
import subprocess
import setenv
import danceability_prediction
import data_interface
import time

scope = 'playlist-read-private playlist-modify-public playlist-read-collaborative'

playlist_id = ""
#song_id  = []
artist_id = ""
genre = ""
genre_old = ""
acousticness = 0.0
popularity = 100
energy = 0.0
danceability = 0.0
instrumentalness = 0.0
track_id = []
playlist_tracks ={}
playlist_tracks2 = []
song_limit = 10

username = 'adaptiveplayer'
client_id = os.environ['SPOTIPY_CLIENT_ID']
client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
redirect = os.environ['SPOTIPY_REDIRECT_URI']

token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect)

def show_tracks(tracks,sp):
	for i, item in enumerate(tracks['items']):
		track = item['track']
		trackid = track['id']
		playlist_tracks[trackid]=0
		playlist_tracks2.append(trackid)
	
def get_playlist_tracks(username,playlist_id,sp):
	
	results = sp.user_playlist(username, playlist_id, fields ="tracks,next")
	tracks = results['tracks']
	show_tracks(tracks,sp)
	while tracks['next']:
		tracks = sp.next(tracks)
		show_tracks(tracks,sp)
	return

def get_audio_features(username, playlist_id, sp):

		results = sp.user_playlist(username, playlist_id, fields="tracks,next")
		tracks = results['tracks']
		show_tracks(tracks,sp)
		while tracks['next']:
			tracks =sp.next(tracks)
			show_tracks(tracks,sp)
		return

def add_tracks(username, playlist_id, tracks,sp):
   try:   
	while True:
		try:
			#token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect)
			#sp = spotipy.Spotify(auth= token)
							
			sp.user_playlist_add_tracks(username,playlist_id,tracks)
			song_id = []
			print "SONGS ADDED"
		except:
			continue
		break	
   except KeyboardInterrupt:
	exit
   return

def gett_rec(seed_genres,song_limit,acousticness,popularity,energy,danceability,instrumentalness,sp):
   try:   
	while True:
		try:
			#token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect)
			song_id = []	
			#sp = spotipy.Spotify(auth=token)
	
			rec =sp.recommendations(seed_genres=seed_genres,limit=song_limit,country=None,target_acousticness=acousticness,target_popularity=popularity,target_energy=energy,target_danceability=danceability,target_instrumentalness=instrumentalness)
			for item in rec['tracks']:
				song_id.append(item['id'])
				#print(song_id)
		except:
			continue
		break
   except KeyboardInterrupt:
	exit
   return song_id 
		
def replace_tracks(username,playlist_id,tracks,sp):
   

   	return

## Function to get data from sensors and pass them to prediction.py to get the prediction results   ###
## returns the prediction model's parameters

def get_data():
	
	data_collected = data_interface.get_sensor_readings()
	#print data_collected
	danceprediction,acousticprediction,instrumentprediction,energyprediction,genreprediction = danceability_prediction.realtime_predict(data_collected)
	
	danceability = danceprediction['Prediction']['predictedValue']
	if(danceability>1):
		 danceability = 1
	if(danceability<0):
                 danceability = 0
	acousticness = acousticprediction['Prediction']['predictedValue']
	if(acousticness>1):
		acousticness = 1
	if(acousticness<0):
                acousticness = 0
	instrumentalness = instrumentprediction['Prediction']['predictedValue']
	if(instrumentalness>1):
		instrumentalness = 1
	if(instrumentalness<0):
                instrumentalness = 0
	energy = energyprediction['Prediction']['predictedValue']
	if(energy>100):
		energy = 100
	if(energy<0):
                energy = 0
	genre = genreprediction['Prediction']['predictedLabel']

	print "DANCE:   %s" %danceability
	print "ACOUSTIC:    %s" %acousticness
	print "INSTRUMENT:    %s" %instrumentalness
	print "ENERGY:     %s" %energy
	print "GENRE:    %s" %genre

	return danceability,acousticness,instrumentalness,energy,genre

while True:
 if token:
   try:
	sp = spotipy.Spotify(auth=token)	
	sp.trace = False	
	#########            PLAYLIST CREATION PLUS CHECK FOR DUPLICATE PLAYLIST	#########
	playlist_creation = raw_input("Do you wish to create a playlist? (Y/N)")
	if (playlist_creation == 'Y'):
		playlist_name = raw_input("Enter name of Playlist:   ")
		list_playlist = sp.user_playlists(username)
		if list_playlist['items'] != []:

			for nameof_playlists in list_playlist['items']:
				if(nameof_playlists['name'] == playlist_name):
					print "Playlist name already exists, please enter another:  "
					playlist_name1 = raw_input("Enter name of Playlist:    ")
					while (playlist_name1 == playlist_name):
						print "Playlist name already exists, please enter another:    "
						playlist_name1 = raw_input("Enter name of Playlist:    ")
					playlist = sp.user_playlist_create(username,playlist_name1)
					print "PLAYLIST CREATED"
					playlist_id = playlist['id']
				else:
					playlist = sp.user_playlist_create(username, playlist_name)
					print "PLAYLIST CREATED"
					pprint.pprint(playlist)
					playlist_id = playlist['id']
		else:
	
			playlist = sp.user_playlist_create(username,playlist_name)
			print "PLAYLIST CREATED"
			pprint.pprint(playlist)
			playlist_id = playlist['id']

	else:
		list_playlist = sp.user_playlists(username)
		for playlistid in list_playlist['items']:
			playlist_id = playlistid['id']
			print "Playlist name :  %s                Playlist ID: %s" %(playlistid['name'],playlist_id)
   except:
	continue
   break

 else:
	print ("can't get token")
	#########			END OF PLAYLIST CREATION      			############

	
	
while(1): 
	
	decision = raw_input("DO YOU WANT TO ADD NEW SONGS?(Y/N)"       )

	if(decision == "Y" or decision =="y"):
		
		danceability,acousticness,instrumentalness,energy,genre = get_data()
		song_list = gett_rec(genre,10,acousticness,popularity,energy,danceability,instrumentalness,sp)
		get_playlist_tracks(username, playlist_id,sp)		

		if genre_old == genre:
	
			
			for item in song_list[::-1]:		
			
				if(playlist_tracks.has_key(item)):
				
					song_list.remove(item)
					print song_list
			if song_list: 
					
				add_tracks(username,playlist_id,song_list,sp)
			else:
				song_limit = song_limit+10
				song_list =gett_rec(genre,song_limit,acousticness,popularity,energy,danceability,instrumentalness,sp)

				for item in song_list[::-1]:

	                                if(playlist_tracks.has_key(item)):

        	                                song_list.remove(item)
                	                        print song_list
                        	if song_list:
                                      	
                                	add_tracks(username,playlist_id,song_list,sp)
					
	

		else:
                        song_limit = 10
			
			if playlist_tracks:
				for item in song_list[::-1]:
				
					if(playlist_tracks.has_key(item)):
						song_list.remove(item)
						print song_list

				if song_list:
					sp.user_playlist_remove_all_occurrences_of_tracks(username, playlist_id, playlist_tracks)
					add_tracks(username,playlist_id,song_list,sp)
					genre_old = genre							
				
			else:
				add_tracks(username,playlist_id,song_list,sp)
				genre_old = genre 
		
 
	elif (decision == "N" or decision == "n"):
		time.sleep(30)
	else:
		print "WRONG INPUT, TRY AGAIN"

####   @copyright tofu coporations  ####
####	adaptiveplayer	####
