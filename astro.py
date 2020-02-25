#! /usr/bin/python

from skyfield.api import load
import datetime, time, re

t = datetime.datetime.now() - datetime.timedelta(minutes=-1)
precise_second = t.strftime("%-S.%f")

planets = load('de421.bsp')
earth, mercury = planets['earth'], planets['mercury']

ts = load.timescale()
tthen = ts.now()
tnow = ts.now()
# tthen = ts.utc(t.year, t.month, t.day, t.hour, t.minute, float(precise_second))

# tnow = ts.utc(2020, 1, 1, 0, 1, 0)
# tthen = ts.utc(2020, 1, 1, 0, 0, 0)

astrometric_now = earth.at(tnow).observe(mercury)
astrometric_then = earth.at(tthen).observe(mercury)

ra_n, dec_n, distance_n = astrometric_now.radec()
ra_t, dec_t, distance_t = astrometric_then.radec()

arr_t = re.sub(r'[a-zA-Z]+', '', str(ra_t)).split()
arr_n = re.sub(r'[a-zA-Z]+', '', str(ra_n)).split()

ftr = [3600,60,1]

time_now_seconds = sum([a*b for a,b in zip(ftr, map(float,arr_n))])
time_then_seconds = sum([a*b for a,b in zip(ftr, map(float,arr_t))])

# print(time_then_seconds - time_now_seconds)

print('Then:', ra_t)
print('Now: ', ra_n)

# nextTime = datetime.datetime.now() + datetime.timedelta(minutes = -1)
# print("Next request @ " + nextTime.strftime("%Y-%m-%d %H:%M:%S"))