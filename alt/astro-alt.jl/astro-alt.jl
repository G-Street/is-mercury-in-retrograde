#!/usr/bin/env bash
    #=
    exec julia --project="~/is-mercury-in-retrograde/alt/astro-alt.jl/" "${BASH_SOURCE[0]}" "$@" -e 'include(popfirst!(ARGS))' \
    "${BASH_SOURCE[0]}" "$@"
    =#

# using AstroLib, JPLEphemeris, Dates, CALCEPH
using Dates, CALCEPH

# Load the DE430 SPK kernel
# spk = SPK("de430.bsp")

# create an ephemeris context
eph = Ephem("inpop13c_TDB_m100_p100_tt.dat")
# eph = Ephem("de430.bsp")

# prefetch ephemeris files data to main memory for faster access
prefetch(eph)

# define planets earth and mercury
# earth, mercury = AstroLib.planets["earth"], AstroLib.planets["mercury"]

t1 = Dates.datetime2julian.(Dates.now())
t2 = Dates.datetime2julian.(Dates.now()+Dates.Minute(5))
# t1 = Dates.datetime2unix.(Dates.now())
# t2 = Dates.datetime2unix.(Dates.now()+Dates.Minute(5))

# pos = position(spk, "earth barycenter", jd)
# println(pos)

# # retrieve constants from ephemeris as a dictionary
# con = constants(eph)
# # list the constants
# println(keys(con))

# retrieve the position, velocity and acceleration of Earth (geocenter) relative
# to the Earth-Moon system barycenter in kilometers, kilometers per second and
# kilometers per second square at JD= 2451624.5 TDB timescale
# for best accuracy the first time argument should be the integer part and the
# delta the fractional part
# when using NAIF identification numbers, useNaifId has to be added to
# the units argument.
# Identification scheme for bodies:
# 1 : Mercury Barycenter
# 3 : Earth
# stuff = compute(eph, t1, t2, naifId.id[:mercury_barycenter], naifId.id[:earth])
stuff = compute(eph, t1, t2, naifId.id[:mercury_barycenter], naifId.id[:earth], useNaifId+unitKM+unitSec, 0)

println(stuff)




# 2-tuple (ha, dec)
#
#     ha: the local apparent hour angle, in degrees. The hour angle is the time that right ascension of 0 hours crosses the local meridian. It is unambiguously defined.
#
#     dec: the local apparent declination, in degrees.
#
# The output coordinates are always floating points and have the same type (scalar or array) as the input coordinates.
#
# Example
#
# Arcturus is observed at an apparent altitude of 59d,05m,10s and an azimuth (measured east of north) of 133d,18m,29s while at the latitude of +43.07833 degrees. What are the local hour angle and declination of this object?

# ha, dec = AstroLib.altaz2hadec(ten(59,05,10), ten(133,18,29), 43.07833)
# AstroLib.adstring(30.4, -1.23)

# println(JPLEphemeris.position(spk, "earth barycenter", "mercury", t1))
# (position(spk, "earth", jd))


# astrometric1 = earth.at(ttime1).observe(mercury)
# astrometric2 = earth.at(ttime2).observe(mercury)
#
# """
#  set values from astrometric arrays
#     ra = right ascension
#     dec = decline
#     ditance = distance
# """
# ra1, dec1, distance1 = astrometric1.radec()
# ra2, dec2, distance2 = astrometric2.radec()
#
# # Split arrays to pull only the numeric values
# arr1 = re.sub(r'[a-zA-Z]+', '', str(ra1)).split()
# arr2 = re.sub(r'[a-zA-Z]+', '', str(ra2)).split()
#
# ftr = [3600,60,1]
#
# # Get Angle outputs in seconds
# time1_seconds = sum([a*b for a,b in zip(ftr, map(float,arr1))])
# time2_seconds = sum([a*b for a,b in zip(ftr, map(float,arr2))])
#
# # get difference in RAs between times
# RA_diff = float(time2_seconds - time1_seconds)
#
# # interpret output of differences in RAs
# if RA_diff < 0.000000:
#     MercRet = "The right ascension of Mercury is negative: Mercury is in retrograde"
# elif RA_diff > 0.000000:
#     MercRet = "The right ascension of Mercury is positive: Mercury is not in retrograde"
# else:
#     MercRet = "The stars are not aligned. I cannot tell if Mercury is in retrograde at the present time. Please come back later."
#
# return MercRet
