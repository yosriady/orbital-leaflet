import sys
import requests

GEOCODE_API_URL = 'http://api.tiles.mapbox.com/v3/%s/geocode/%s.json'
GEOCODE_API_KEY = 'examples.map-zr0njcqy'

def geocode(query):
    url = GEOCODE_API_URL % (GEOCODE_API_KEY, query)
    response = requests.get(url)
    dict = response.json()
    return dict

if __name__ == "__main__":
    for arg in sys.argv:
        print geocode(arg)
