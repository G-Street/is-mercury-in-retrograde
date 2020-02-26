from skyfield.api import load
import datetime, time, re

planets = load('de421.bsp')
earth, mercury = planets['earth'], planets['mercury']

ts = load.timescale()

t1 = datetime.datetime.now()
precise_second_t1 = float(t1.strftime("%-S.%f"))

t_now = ts.now()
t_utc_now = datetime.utcnow(t1.year, t1.month, t1.day, t1.hour, t1.minute, precise_second_t1)

astrometric1 = earth.at(t_now).observe(mercury)
astrometric2 = earth.at(t_utc_now).observe(mercury)

ra1, dec1, distance1 = astrometric1.radec()
ra2, dec2, distance2 = astrometric2.radec()

#print('RA for ts.now():\t', ra1)
#print('RA for ts.utc(...):\t', ra2)

#print(ts.utcnow())
