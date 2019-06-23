#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 16:15:09 2019

@author: beccarobins
"""

# Import necessary packages
from geopy.geocoders import Nominatim
import pandas as pd
import os

# Import dataset from GitHub
ispgr = pd.read_csv('https://raw.githubusercontent.com/beccarobins/ispgr/master/ISPGR_dataset.csv', 
                    usecols = ["Year", "City", "Country"])

# Create geolocator client
geolocator = Nominatim(user_agent="geocoder", timeout=5)

# Create empty lists
latitudes = []
longitudes = []

# Iterate over DataFrame rows to get lat and lon for all conferences
for i,j in ispgr.iterrows():
    location = str(j.City + ", " + j.Country)
    location = geolocator.geocode(location)
    latitudes.append(location.latitude)
    longitudes.append(location.longitude)

# Add lat and lon to DataFrame
ispgr["latitude"] = latitudes
ispgr["longitude"] = longitudes

# Save new data to current working directory
path = os.getcwd()+"/ispgr_data.csv"
export_file = ispgr.to_csv(path, index = False)