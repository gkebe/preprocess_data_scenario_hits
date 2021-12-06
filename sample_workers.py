#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 14:49:15 2021

@author: gaoussoukebe
"""

import pandas as pd
import random

dem_info = pd.read_csv("demographic_information_filtered.csv")


dem_info = dem_info.iloc[: , :-2].values.tolist()

def samples_info(samples):
    num_blacks = 0
    num_asians = 0
    num_women = 0
    num_native = 0
    num_hispanic = 0
    num_elder = 0
    
    for i in samples:
        if "black" in i[2].lower():
            num_blacks += 1
        if "asian" in i[2].lower():
            num_asians += 1
        if "native" in i[2].lower():
            num_native += 1
        if "female" in i[4].lower():
            num_women += 1
        if "yes" in i[3].lower():
            num_hispanic += 1
        if "65" in i[5].lower():
            num_elder += 1
    return num_blacks, num_asians, num_native, num_hispanic, num_women, num_elder

def criteria(samples_info):
    criterias = [3,3,1,2,10,1]
    return all(samples_info[i] >= criterias[i] for i in range(len(samples_info)))

samples = []
while(not criteria(samples_info(samples))):
    samples = random.sample(dem_info, 20)