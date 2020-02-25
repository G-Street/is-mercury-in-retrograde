#! /usr/bin/python

from skyfield.api import load
import datetime, time, re

# get time five seconds ago
t1 = datetime.datetime.now() - datetime.timedelta(seconds=-5)
precise_second_t1 = t1.strftime("%-S.%f")
# get time now
t2 = datetime.datetime.now()
precise_second_t2 = t2.strftime("%-S.%f")

# fetch data from the United States Naval Observatory and the International Earth Rotation Service
planets = load('de421.bsp')
# define planets earth and mercury
earth, mercury = planets['earth'], planets['mercury']

# Load a timescale so that we can translate between different systems for expressing time
ts = load.timescale()

# Set times 1 and 2 as terrestrial time
ttime1 = ts.utc(t1.year, t1.month, t1.day, t1.hour, t1.minute, float(precise_second_t1))
ttime2 = ts.utc(t2.year, t2.month, t2.day, t2.hour, t2.minute, float(precise_second_t2))

# sanity check for times 1 and 2 terrestrial time for when mercury is not in retrograde
# ttime1 = ts.utc(2020, 1, 1, 12, 0, 0)
# ttime2 = ts.utc(2020, 1, 1, 12, 5, 0)

# get atrometric measurements from earth to mercury at times 1 and 2
astrometric1 = earth.at(ttime1).observe(mercury)
astrometric2 = earth.at(ttime2).observe(mercury)

# set values from astrometric arrays
ra1, dec1, distance1 = astrometric1.radec()
ra2, dec2, distance2 = astrometric2.radec()

# Split arrays
arr1 = re.sub(r'[a-zA-Z]+', '', str(ra1)).split()
arr2 = re.sub(r'[a-zA-Z]+', '', str(ra2)).split()

ftr = [3600,60,1]

# Get Angle outputs in seconds
time1_seconds = sum([a*b for a,b in zip(ftr, map(float,arr1))])
time2_seconds = sum([a*b for a,b in zip(ftr, map(float,arr2))])

# print(time2_seconds - time1_seconds)

print('Then:', ra1)
print('Now: ', ra2)
# print('Then:', time1_seconds)
# print('Now: ', time2_seconds)