#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import subprocess
import pychromecast
import time
import os
from bottle import route, run
from bottle import get, post, request
from flask import Flask, render_template
# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyDo7rPjc6eOCNUQ0Yzg3MM9vVhwnT2grsc"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

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


def makeGoogleHomeSpeech(youtubeURL):
    cmd = "youtube-dl -x -g --audio-format mp3 " + youtubeURL
    soundURL = subprocess.check_output(cmd.split()).decode()
    casts = pychromecast.get_chromecasts()
    if len(casts) == 0:
        print("Counld't find google home device.Try again.")
        sys.exit()
    googlehome = casts[0]
    mc = googlehome.media_controller
    mc.play_media(soundURL, "audio/mp3")

@route("/",method = "GET")
def doLogic():
    keyword = request.query.get("keyword")
    result = youtube_search([keyword])
    makeGoogleHomeSpeech(result[0])

run(host="localhost",port=8080,debug=True)

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
    
