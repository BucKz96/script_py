#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 13:50:07 2018

@author: buckz
"""
import urllib.request as urllib
import pprint
import sys
import spotipy
import spotipy.util as util
import json
username = "21xmfxgckg2bisyfqbt6lykyi"
        
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='5f178b3e6b754af9988ead29952c8fc1',
client_secret='a53f2c50ce89408fa4c0ecf29d35d9a6')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = spotify.search(q= 'Au calme', type='playlist')

def read(url):
    json_obj1 = urllib.urlopen(url)
    data1 = json.load(json_obj1)
    return data1

read("http://api.wunderground.com/api/3d830f4b3b8f6d07/conditions/q/FR/Paris.json")

