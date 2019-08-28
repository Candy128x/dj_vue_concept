import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/movie/'

r = requests.get(BASE_URL+ENDPOINT)
data = r.json()

for movie in data:
    print('Movie name:', movie['name'])
    print('Movie launch date:', movie['launch_date'])
    print()