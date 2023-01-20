client_id = ""
client_secret = ""
import requests
import json
import spotipy
searchURL = "https://api.spotify.com/v1/search"
from pprint import pprint
scopes = 'playlist-modify-public'
youtube_key = ""
playlist_id = ""
import googleapiclient
from googleapiclient.discovery import build
import time
def getYouTubePlaylist():
    # Get Video titles in the playlist
    youtube = build('youtube', 'v3', developerKey=youtube_key)
    playlist_id = ""
    response = youtube.playlistItems().list(part="snippet",
                                            playlistId=playlist_id,
                                            maxResults=50).execute()

    playlistItems = response['items']
    nextPageToken = response.get('nextPageToken')

    while nextPageToken:
        response = youtube.playlistItems().list(part="snippet",
                                                playlistId=playlist_id,
                                                maxResults=50).execute()
        playlistItems.extend(response['items'])
        nextPageToken = response.get('nextPageToken')

    res = []

    for x in range(len(playlistItems)):
        res.append(playlistItems[x]['snippet']['title'])

    return res
def searchTitleGetURL(title):

    sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id=client_id,
                                                           client_secret=client_secret,
                                                           redirect_uri="https://github.com/EliyaFarhat", scope=scopes))
    uriLst = []
    checkUri = []
    # Search for songs and get URI's
    try:
        check = sp.playlist_items(playlist_id=playlist_id)['items']
        for y in range(len(check)):
            checkUri.append(check[y]['track']['uri'])
        for x in range(len(title)):
            if ((title[x])[::-1])[:16] == ")oiduA laciffO(" or ((title[x])[::-1])[:16] == ")oediV laciffO(" :
                title[x] = ((title[x])[::-1])[16::][::-1]
            if title[x] == "bladee - egobaby (Official Video)":
                title[x] = "bladee - egobaby"
            if title[x] == "XXXTENTACION - Everybody Dies In Their Nightmares (Audio)":
                title[x] = "XXXTENTACION - Everybody Dies In Their Nightmares"
            searchResults = sp.search(q=title[x], type="track", market="US", limit=1)

            if searchResults['tracks']['items'][0]['uri'] not in checkUri:
                uriLst.append(searchResults['tracks']['items'][0]['uri'])
            else:
                pass


        try:
            sp.playlist_add_items(playlist_id=playlist_id, items=uriLst, position=None)
        except spotipy.exceptions.SpotifyException:
            print("NO SONGS OR NEW SONGS FOUND")
    except spotipy.SpotifyOauthError as e:
        sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id="",
                                                               client_secret="",
                                                               redirect_uri="https://github.com/EliyaFarhat", scope=scopes))



while True:
    searchTitleGetURL(getYouTubePlaylist())
    time.sleep(1)




