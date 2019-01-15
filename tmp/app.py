#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import subprocess
import pychromecast
import time
import os
from flask import Flask, render_template, request, session
from flask_ngrok import run_with_ngrok
import sys
import json

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.

app = Flask(__name__)
#run_with_ngrok(app)

DEVELOPER_KEY = "AIzaSyDo7rPjc6eOCNUQ0Yzg3MM9vVhwnT2grsc"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
CONNECTION_INFO = "192.168.11.3"
app.secret_key = "hogehoge"

def youtube_search(keyword):#suppose that keyword is list type[]
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=keyword,
    part="id,snippet",
    maxResults=25,
  ).execute()

  videos = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
#      videos.append("%s (%s)" % (search_result["snippet"]["title"],
#                                 search_result["id"]["videoId"]))
      videos.append("%s" %(search_result["id"]["videoId"]))

  return videos


def get_info_from_url(youtubeURL):

    cmd = "youtube-dl -x -g --audio-format mp3 --get-duration " + youtubeURL
    soundInfo= subprocess.check_output(cmd.split()).decode().split("\n")
    return soundInfo


class GoogleHomeController:
    def __init__(self, CONNECTION_INFO):
        googlehome = pychromecast.Chromecast(CONNECTION_INFO)
        self.mc = googlehome.media_controller

    def play_googlehome(self, soundURL):
        self.mc.play_media(soundURL,"audio/mp3")

    def pause_googlehome(self):
        self.mc.pause()


    
def calc_sec(str_time):
    time = 0
    count = 0
    for item in reversed(str_time.split(":")):
        time += int(item) * 60 ** count
        count += 1
    return time

class MusicController:
    def __init__(self, CONNECTION_INFO):
        url_list = session.get("url_list")
        l = []
        for i, url in enumerate(url_list, 1):
            keys = ["number", "url", "playFlag"]
            values = [i, url, 0]
            d = dict(zip(keys, values))
            l.append(d)
        self.l = l
        self.googlehome = GoogleHomeController(CONNECTION_INFO)

    def play_music(self,num):
        l = self.l
        soundInfo = get_info_from_url(l[num]["url"])
        duration = calc_sec(soundInfo[1])
        self.googlehome.play_googlehome(soundInfo[0])
        # Flag change to "Now playing"
        l[num]["playFlag"] = 1
        # wait until music end
        time.sleep(duration)
        # Flag change to "Halting"
        l[num]["playFlag"] = 0

    def get_status(self):
        return self.l





"""
CONSTRUCT instance
"""
googlehome = GoogleHomeController(CONNECTION_INFO)

@app.route("/form")
def form():
    return render_template("form.html")
"""
@app.route("/search")
def search():
    if request.method == "POST":
        keyword = str(json.loads(request.data.decode("UTF-8"))\
                 ["queryResult"]["parameters"]["any"])
    else:
        keyword = "chopin"
    url_list =  youtube_search[keyword]
    session["url_list"] = url_list
"""

@app.route("/next", methods=["POST"])
def next_music():
    music_list = session.get("url_list")

@app.route("/play", methods=["POST"])
def play_music():
    if request.method == "POST":
        keyword = str(json.loads(request.data.decode("UTF-8"))\
                 ["queryResult"]["parameters"]["any"])
    else:
        keyword = "chopin"
    url_list =  youtube_search([keyword])
    session["url_list"] = url_list

    m = MusicController(CONNECTION_INFO)
    m.play_music(0)



    return render_template("music.html", title="test", keyword=keyword)
"""
    for item in results:
        soundInfo = get_info_from_url(defaultURL + item)
        make_googlehome_speech(CONNECTION_INFO, soundInfo[0])
        duration = calc_sec(soundInfo[1])
        time.sleep(duration)

   t return render_template("music.html",title="test",keyword=keyword)

"""

#run(host="localhost",port=8080,debug=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    
    app.run(port = port, threaded = True)
"""
if __name__ == "__main__":
  try:
    result = youtube_search(key)
    defaultURL = "https://www.youtube.com/watch?v="
    makeGoogleHomeSpeech(defaultURL + result[0])
    time.sleep(20)
  except HttpError as e:
    print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
"""
    
