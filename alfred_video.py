#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 12:34:37 2021

@author: gaoussoukebe
"""

with open("alfred_files.txt", "r") as f:
    alfred_files = f.readlines()
    
video_lines = ["/".join(i.split("/")[5:]) for i in alfred_files]
videos_dict = {}

for line in video_lines:
    split = line.split("/")[0]
    task =line.split("/")[1].split("-")[0]
    if split not in videos_dict:
        videos_dict[split] = {}
    if task not in videos_dict[split]:
        videos_dict[split][task] = []
    videos_dict[split][task].append("https://ai2-vision-alfred-data-explorer.s3-us-west-2.amazonaws.com/" + "/".join(line.split("/")[1:]))