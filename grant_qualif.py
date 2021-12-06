#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 00:40:41 2021

@author: gaoussoukebe
"""

import pandas as pd
import random
import glob

dem_list = []
for filepath in glob.iglob('./Batch*.csv'):
    dem_list.append(pd.read_csv(filepath))
dem_info = pd.concat(dem_list)
already_surveyed = dem_info["WorkerId"].tolist()
workers = pd.read_csv("workers.csv")

workers.loc[workers["Worker ID"].isin(already_surveyed), "UPDATE-already_surveyed"] = "1"
workers.fillna('', inplace=True)

workers.to_csv("updated_workers.csv", index=False)