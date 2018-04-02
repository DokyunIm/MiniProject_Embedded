import requests
import json
import xml.etree.ElementTree as ET
import math
import os
import sys

global key
key_file = open('./key.secret', 'r')
key = json.loads(key_file.read())

#getIP : get Device IP (but, it may be not accurate)
#return : IP Address
def getIP():
  response_data = requests.get('http://ip.jsontest.com/')
  device_ip = json.loads(response_data.text)
  #print("device IP : "+device_ip['ip'])
  return device_ip['ip'];

#getGeolocation : get address using ip address
#                 and get longitude and latitude using address
#return : longitude, latitude
def getGeolocation(device_ip):
  global key
  url = 'http://whois.kisa.or.kr/openapi/whois.jsp?query='+device_ip+'&key='+key['whois_key']+'&answer=json'
  response_data = requests.get(url)
  __addr_json = json.loads(response_data.text)
  __addr = str(__addr_json['whois']['korean']['user']['netinfo']['addr'])
  #print(__addr)
  
  url ="https://openapi.naver.com/v1/map/geocode?encoding=utf-8&coordType=latlng&query="+__addr
  headers = {
    'X-Naver-Client-Id': key['client_id'],
    'X-Naver-Client-Secret': key['client_secret']
  }
  response_data = requests.get(url, headers=headers)
  __geolocation = json.loads(response_data.text)
  longitude = __geolocation['result']['items'][0]['point']['x']
  latitude = __geolocation['result']['items'][0]['point']['y']
  geolocation = {
    'longitude': longitude,
    'latitude': latitude
  }
  
  #print(geolocation)
  return geolocation

#getAddress : get detail address(dong/myun) using longitude, latitude
#return : address(dong/myun)
def getAddress(longitude, latitude):
  global key
  url ="https://openapi.naver.com/v1/map/reversegeocode?encoding=utf-8&coordType=latlng&query="+longitude+","+latitude+""
  headers = {
    'X-Naver-Client-Id': key['client_id'],
    'X-Naver-Client-Secret': key['client_secret']
  }
  response_data = requests.get(url, headers=headers)
  __address = json.loads(response_data.text)
  address = __address['result']['items'][0]['addrdetail']['dongmyun']
  #print("detail address : "+address)
  return address

#getTM : get TM location using address(dong/myun)
#return : TM location
def getTM(address):
  global key
  url = "http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/getTMStdrCrdnt?umdName="+address+"&pageNo=1&numOfRows=10&ServiceKey="+key['openapi_key']
  response_data = requests.get(url)
  __data = ET.fromstring(response_data.text)
  tmx = (__data.find('body').find("items").find("item").find("tmX")).text
  tmy = (__data.find('body').find("items").find("item").find("tmY")).text
  tmdata = {
    'tmx': str(tmx),
    'tmy': str(tmy),
  }
  #print(tmdata)
  return tmdata

#getStation : get Measuring station name using TM location
#return : station name
def getStation(tm):
  global key
  url ="http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/getNearbyMsrstnList?tmX="+tm['tmx']+"&tmY="+tm['tmy']+"&pageNo=1&numOfRows=10&ServiceKey="+key['openapi_key']
  response_data = requests.get(url)
  __data = ET.fromstring(response_data.text)
  station_name = (__data.find('body').find('items').find('item').find('stationName')).text
  #print("near station name : "+station_name)
  return station_name

#getAirData : get Air data using Open API(www.data.go.kr)
#return : air data(json)
def getAirData(station):
  global key
  url ="http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName="+station+"&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey="+key['openapi_key']+"&ver=1.3"
  response_data = requests.get(url)
  __data = ET.fromstring(response_data.text)
  
  khai_value = (__data.find('body').find('items').find('item').find('khaiValue')).text #0-50:좋음 51-100:보통 101-250:나쁨 251-:매우나쁨
  khai_grade = (__data.find('body').find('items').find('item').find('khaiGrade')).text #1:좋음 2:보통 3:나쁨 4:매우나쁨
  
  air_data = {
    'khai_value': str(khai_value),
    'khai_grade': str(khai_grade)
  }
  #print(air_data)
  return air_data
  
#getAir : main procedure
#return : air data
def getAir():
  global key
  key_file = open('./key.secret', 'r')
  key = json.loads(key_file.read())
  
  geolocation = getGeolocation(str(getIP()))
  address = getAddress(str(geolocation['longitude']), str(geolocation['latitude']))
  tmdata = getTM(address)
  station = getStation(tmdata)
  air_data = getAirData(station)
  return air_data

""" # debugging code
geolocation = getGeolocation(str(getIP()))
address = getAddress(str(geolocation['longitude']), str(geolocation['latitude']))
tmdata = getTM(address)
station = getStation(tmdata)
air_data = getAirData(station)
"""
