# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model
import requests
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# from flask import render_template
# from flask import request

# -- Initialization section --
app = Flask(__name__)

# API

# export SPOTIPY_CLIENT_ID="2aec1864fdb0443da8ea4f23b250f72b"
# export SPOTIPY_CLIENT_SECRET=30a30c6402bb45d3af9b719026218e5a


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
  
    return render_template("index.html")

@app.route('/tracks', methods=["GET", "POST"])
def tracks(): 
    if request.method == "POST":
        user_artist = request.form["artist"]
        user_top_tracks = model.get_top_tracks(user_artist)
        return render_template("tracks.html",
                                user_artist=user_artist,
                                user_top_tracks=user_top_tracks)
    else:
        return "Error"



