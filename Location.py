# -*- coding: utf-8 -*-
"""
This script was created to be able to get location of current
ip address
@author: mac
"""
import requests

def get_data():
    geo_request_url = 'https://get.geojs.io/v1/ip/geo/' +ip_add() + '.json'
    geo_request = requests.get(geo_request_url)
    geo_data = geo_request.json()
    return geo_data

def ip_add():
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']  # ip_request.json() => {ip: 'XXX.XXX.XX.X'}
    return my_ip
    
def get_city():
    return get_data()['city']

def get_code():
    return get_data()['country_code']

def get_country():
    return get_data()['country']
# {
# "area_code": "0",
# "continent_code": "NA",
# "country": "United States",
# "country_code": "US",
# "country_code3": "USA",
# "ip": "198.975.33.4",
# "latitude": "37.7510",
# "longitude": "-97.8220",
# "organization": "AS15169 Google Inc.",
# "timezone": ""
# }  This is a fake example I grabbed from the GeoJS website