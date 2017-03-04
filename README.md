# Project 1 for Udacity's Full Stack Nanodegree

### Project Overview
You will write server-side code to store a list of your favorite movies, including box art imagery and a movie trailer URL. You will then use your code to generate a static web page allowing visitors to browse their movies and watch the trailers.

### Project solution
This solution uses [bottle.py](https://bottlepy.org) as the server side framework.

To add / remove media.Movie class instances, modify the `server.py` file.

No installation is required as bottle 0.12.13 is included in the project files.

Example run commands
* `python -m bottle --debug --reload server` (defaults to `localhost:8080`)
* `python -m bottle -b $IP:$PORT --debug --reload server` (for [c9.io](https://c9.io/))
