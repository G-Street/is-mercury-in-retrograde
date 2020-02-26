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
t1 = datetime.datetime.now() - datetime.timedelta(seconds=5)
precise_second_t1 = float(t1.strftime("%-S.%f"))
t2 = datetime.datetime.now()
precise_second_t2 = float(t2.strftime("%-S.%f"))

# Sanity check for times
#print(t1.year, t1.month, t1.day, t1.hour, t1.minute, precise_second_t1)
#print(t2.year, t2.month, t2.day, t2.hour, t2.minute, precise_second_t2)

# setting times 1 and 2 as terrestrial times
ttime1 = ts.utc(t1.year, t1.month, t1.day, t1.hour, t1.minute, precise_second_t1)
ttime2 = ts.utc(t2.year, t2.month, t2.day, t2.hour, t2.minute, precise_second_t2)

# sanity check for times 1 and 2 terrestrial time for when mercury is not in retrograde
#ttime1 = ts.utc(2020, 4, 1, 12, 0, 0)
#ttime2 = ts.utc(2020, 4, 1, 12, 5, 0)

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

# get difference in RAs between times
RA_diff = float(time2_seconds - time1_seconds)

# interpret output of differences in RAs
if RA_diff < 0.000000:
    MercRet = True
elif RA_diff > 0.000000:
    MercRet = False
else:
    MercRet = None