import urllib.parse
import urllib.request
import json

req = urllib.request.Request('https://api.nasa.gov/planetary/apod?api_key=5oi0NGdFzVgIvA23FdQS8YXx5OSInUPSOuhx88RC')
with urllib.request.urlopen(req):
    the_page = response.read()
