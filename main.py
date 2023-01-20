client_id = "<SPOTIFY_CLIENT_ID>"
client_secret = "<SPOTIFY_CLIENT_SECRET>"
import requests
import json
import spotipy
searchURL = "https://api.spotify.com/v1/search"
from pprint import pprint
scopes = 'playlist-modify-public'
youtube_key = "<YTKEY>"
playlist_id = "<PLAYLIST_ID>"
import googleapiclient
from googleapiclient.discovery import build
import time


def getYouTubePlaylist():

    # Get Video titles in the playlist
    youtube = build('youtube', 'v3', developerKey=youtube_key)
    playlist_id = "<PLAYLIST_ID>"
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
        #print(playlistItems)

    res = []

    for x in range(len(playlistItems)):
        res.append(playlistItems[x]['snippet']['title'])
    #print(res)
    return res

def searchTitleGetURL(title, sp):




    uriLst = []
    checkUri = []
    #print("here")
    # Search for songs and get URI's


    #print("here2")
    try:
        check = sp.playlist_items(playlist_id=playlist_id)['items']
    except spotipy.SpotifyOauthError:

        check = sp.playlist_items(playlist_id=playlist_id)['items']


    for y in range(len(check)):
        #print("here24")
        checkUri.append(check[y]['track']['uri'])
    for x in range(len(title)):
        #print("here344")
        title[x] = title[x].replace("(Official Video)", "")
        title[x] = title[x].replace("(Video)", "")
        title[x] = title[x].replace("(Audio)", "")
        title[x] = title[x].replace("(Official Music Video)", "")
        title[x] = title[x].replace("(Official Audio)", "")
        title[x] = title[x].replace("[Official Audio]", "")
        title[x] = title[x].replace("[Official Music Video]", "")
        title[x] = title[x].replace("[Official Visualizer]", "")
        title[x] = title[x].replace("(Official Visualizer)", "")
        title[x] = title[x].replace("[Official Video]", "")
        title[x] = title[x].replace("(video)", "")


        searchResults = sp.search(q=title[x], type="track", market="US", limit=1)

        if searchResults['tracks']['items'][0]['uri'] not in checkUri:
            uriLst.append(searchResults['tracks']['items'][0]['uri'])
        else:
            pass


    try:
        sp.playlist_add_items(playlist_id=playlist_id, items=uriLst, position=None)
        #print("here22")
    except spotipy.exceptions.SpotifyException:
        print("NO SONGS OR NEW SONGS FOUND")


if __name__ == '__main__':
    sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id=client_id,
                                                           client_secret=client_secret,
                                                           redirect_uri="https://github.com/EliyaFarhat",
                                                           scope=scopes))
    while True:
        try:
            searchTitleGetURL(getYouTubePlaylist(), sp)
        except spotipy.SpotifyOauthError as e:
            sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id=client_id,
                                                           client_secret=client_secret,
                                                           redirect_uri="https://github.com/EliyaFarhat",
                                                           scope=scopes))
        time.sleep(5)




