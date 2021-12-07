import requests
import json

def get_temp():    
    payload = {'access_token': '7c0c4fcc8f834ebd56aa0b1124d9157d19075563'}
    access_token=r = requests.get("https://api.particle.io/v1/devices/430024000a47373336323230/analogvalue/", params=payload)


    # some JSON:
    x =  r.text

    # parse x:
    y = json.loads(x)

    # the result is a Python dictionary:
    return y["result"]

