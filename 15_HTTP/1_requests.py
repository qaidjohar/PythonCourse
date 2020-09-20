import requests
import time


response = requests.get('https://www.mesf.gg/home')
print(response.text)
    # print('Status Code: ',response.status_code)
    # print('Headers Code: ',response.headers)
    # print(type(response.text))
    # print(type(response.json()))
    # d = response.json()
    # # print(d['id'])
    # print(d['joke'])
    # time.sleep(2)