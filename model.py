
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
def get_top_tracks(artist): 
    cid = '2aec1864fdb0443da8ea4f23b250f72b'
    secret = '8100126adef24003b819e136fbc13afe'
    client_credentials_manager = SpotifyClientCredentials(
        client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


    data = sp.search(q="artist:" + artist, type="artist")
    uri = data["artists"]["items"][0]["uri"]
    results = sp.artist_top_tracks(uri)
    top_tracks = []


    for track in results['tracks'][:10]:
        top_tracks.append([track['name'], track['album']['images'][0]['url'], track["external_urls"]["spotify"]])
        print(track["external_urls"]["spotify"])
        # print('track    : ' + track['name'])
        # # print('audio    : ' + track['preview_url'])
        # print('cover art: ' + track['album']['images'][0]['url'])
    print(top_tracks)
    return top_tracks