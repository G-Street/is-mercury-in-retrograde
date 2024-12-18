<h1 align="center">
  Is Mercury in retrograde ??
</h1>

### What am I reading?

This is a description for the back-end of a website which tells you whether or not Mercury is in retrograde.  This project is dedicated to Olivia.  This project has been developed by [jakewilliami](https://github.com/jakewilliami) and [andfield](https://github.com/andfield).

---

### Contents

- [Ephemeris](#ephemeris)
- [What am I reading?](#what-am-i-reading)
- [Contents](#contents)
- [How to set up this project](#how-to-set-up-this-project)
- [What is retrograde motion?](#what-is-retrograde-motion)
- [Calculation and Generation of Ephemerides](#calculation-and-generation-of-ephemerides)
- [Room for improvement](#room-for-improvement)

---

### How to set up this project

Our dependency for [Flask](https://palletsprojects.com/p/flask/) is that you have Python 3.3+.  You need to check this is installed:
```
python[3] --version
```
Now download your virtual environment toolbox:
```
pip[3] install virtualenv
```
`cd` to your project directory and run
```
python[3] -m venv <project-name>
virtualenv <project-name>
source <project-name>/bin/activate
```
Now we need to set up flask and get our dependencies.  Run
```
pip[3] install -r requirements.txt
```
And you are set up.  Run `python[3] app.py` to get the local server running.  Non-local server is currently in progress.  You can run `deactivate` to escape your virtual environment.

### Calculation and Generation of Ephemerides

Within one's personal computer, one can access wonders.

We have found four very excellent and open-source repositories that have helped us to determine this critical question:

1. [A Python library developed by Brandon Rhodes](https://github.com/brandon-rhodes/python-jplephem).  This library provides mathematical tools (used by the *Jet Propulsion Laboratory* to calculate their ephemerides) to predict raw planetary positions in three-dimensional space.
2. [A Python library developed by skyfielders](https://github.com/skyfielders/python-skyfield).  This library sources data from the *United States Naval Observatory and the International Earth Rotation Service*, and used the above repository in its calculations.
3. [A python library also developed by Brandon Rhodes](https://github.com/brandon-rhodes/pyephem).  This library is specifically focussed on the Scientific calculations for Atronomy.
4. [A Julia library](https://github.com/JuliaAstro/JPLEphemeris.jl) provided by [JuliaAstro](https://juliaastro.github.io/).  This is based on the former-mentioned repository, and provides a [Julia](https://julialang.org/) implementation of these mathematical and astronomical tools.

With the help of these excellent resources, we have managed to calculate whether or not Mercury is in retrograde.

---

### Setting Up Julia Alternative

Ensure you have [Julia](https://julialang.org/) downloaded and installed.  We have created a virtual environment in `alt/astro-alt.jl/`.  To use this on your machine, run
```
$ cd is-mercury-in-retrograde/alt/astro-alt.jl/
$ julia
julia> ]
pkg> activate .
(astro-alt.jl) instantiate
```
To run the project, you will need to specify the project directory:
```
$ cd is-mercury-in-retrograde/alt/astro-alt.jl/
$ julia --project=. astro-alt.jl
```
See the [manual](is-mercury-in-retrograde/alt/astro-alt.jl/) for more information on this.

Finally, you need to download the data file:
```
$ cd is-mercury-in-retrograde/alt/astro-alt.jl/
$ wget https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de430.bsp # for the JPLEphemeris package
$ wget ftp://ftp.imcce.fr/pub/ephem/planets/inpop13c/inpop13c_TDB_m100_p100_tt.dat # for the CALCEPH package
```

---

### Room for improvement

There is room for improvement.  Within the script `astro.py` and `astro-alt.py`, we have defined two points in time by defining one, waiting, and defining another.  This is undoubtably not the best way to do this, but this was the only way I found that works.  In the early drafts of the script, we would define a time `t1` which is five seconds before the current time, but this did not work for some reason.  We would always be open for any help on this.

### To Do

 - Create request for user accessing website to give back-end user's timezone for python calculations.
 - Work on pyinstaller standalone executiable for any server.
 - Work on frontend
