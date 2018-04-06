#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 16:11:24 2018

@author: buckz
"""
import pandas as pd
import numpy as np
import os

gl = pd.read_table('game_logs.csv', sep=',', low_memory=False)
gl.head()