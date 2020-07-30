#! /usr/bin/python

import ephem, datetime, time, re

m = ephem.Mercury

# Load a timescale so that we can translate between different systems for expressing time
t1 = datetime.datetime.now()
time.sleep(5)
t2 = datetime.datetime.now()

# Setting values of RA for times 1 and 2
ra1 = m(t1).ra
ra2 = m(t2).ra

# sanity check for times 1 and 2 terrestrial time for when mercury is not in retrograde
# ra1 = m('2020-1-1').ra
# ra2 = m('2020-1-2').ra


# Split arrays to pull only the numeric values
arr1 = re.sub(r':', '', str(ra1)).split()
arr2 = re.sub(r':', '', str(ra2)).split()

ftr = [3600,60,1]

# Get Angle outputs in seconds
time1_seconds = sum([a*b for a,b in zip(ftr, map(float,arr1))])
time2_seconds = sum([a*b for a,b in zip(ftr, map(float,arr2))])


# interpret output of differences in RAs
if float(time2_seconds - time1_seconds) < 0.000000:
    print("The right ascension of Mercury is negative: Mercury is in retrograde")
elif float(time2_seconds - time1_seconds) > 0.000000:
    print("The right ascension of Mercury is positive: Mercury is not in retrograde")
else:
    print("The stars are not aligned.  I cannot tell if Mercury is in retrograde at the present time.  Please come back later.")
