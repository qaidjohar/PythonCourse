import requests
import time

while True:
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    # print('Status Code: ',response.status_code)
    # print('Headers Code: ',response.headers)
    # print(type(response.text))
    # print(type(response.json()))
    d = response.json()
    # print(d['id'])
    print(d['joke'])
    time.sleep(2)