#! /usr/bin/python

from skyfield.api import load
import datetime, time, re

# fetch data from the United States Naval Observatory and the International Earth Rotation Service
planets = load('de421.bsp')
# define planets earth and mercury
earth, mercury = planets['earth'], planets['mercury']

# Load a timescale so that we can translate between different systems for expressing time
ts = load.timescale()

# Set times 1 and 2 as terrestrial time
ttime1 = ts.now()
time.sleep(7)
ttime2 = ts.now()

# sanity check for times 1 and 2 terrestrial time for when mercury is not in retrograde
# ttime1 = ts.utc(2020, 1, 1, 12, 1, 0)
# ttime2 = ts.utc(2020, 1, 1, 12, 1, 5)

# get atrometric measurements from earth to mercury at times 1 and 2
astrometric1 = earth.at(ttime1).observe(mercury)
astrometric2 = earth.at(ttime2).observe(mercury)

"""
 set values from astrometric arrays
    ra = right ascension
    dec = decline
    ditance = distance
"""
ra1, dec1, distance1 = astrometric1.radec()
ra2, dec2, distance2 = astrometric2.radec()

# Split arrays to pull only the numeric values
arr1 = re.sub(r'[a-zA-Z]+', '', str(ra1)).split()
arr2 = re.sub(r'[a-zA-Z]+', '', str(ra2)).split()

ftr = [3600,60,1]

# Get Angle outputs in seconds
time1_seconds = sum([a*b for a,b in zip(ftr, map(float,arr1))])
time2_seconds = sum([a*b for a,b in zip(ftr, map(float,arr2))])

# interpret output of differences in RAs
if float(time2_seconds - time1_seconds) < 0:
    print("The right ascension of Mercury is negative: Mercury is in retrograde")
elif float(time2_seconds - time1_seconds) > 0:
    print("The right ascension of Mercury is positive: Mercury is not in retrograde")
else:
    print("The stars are not aligned.  I cannot tell if Mercury is in retrograde at the present time.  Please come back later.")