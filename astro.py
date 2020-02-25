#! /usr/bin/python

from skyfield.api import load

planets = load('de421.bsp')
earth, mercury = planets['earth'], planets['mercury']

ts = load.timescale()
t = ts.now()
astrometric = earth.at(t).observe(mercury)
ra, dec, distance = astrometric.radec()

print(ra)
print(dec)
print(distance)
