#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:25:37 2018

@author: buckz
"""
import spotipy
import sys
import spotipy.util as util

username="21xmfxgckg2bisyfqbt6lykyi"
clientId= "5f178b3e6b754af9988ead29952c8fc1"
clientSecret="a53f2c50ce89408fa4c0ecf29d35d9a6"
scope = 'playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private streaming ugc-image-upload user-follow-modify user-follow-read user-library-read user-library-modify user-read-private user-read-birthdate user-read-email user-top-read user-read-playback-state user-modify-playback-state user-read-currently-playing user-read-recently-played'

token = util.prompt_for_user_token(username,scope=scope,client_id=clientId,client_secret=clientSecret,redirect_uri='http://localhost/')
