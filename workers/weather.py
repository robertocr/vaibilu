# -*- coding: utf-8 -*-
import httplib
import json

class Weather():
  @staticmethod
  def search (town):
    conn = httplib.HTTPConnection("api.openweathermap.org")
    url2 = "/data/2.5/weather?q="+town+",br&units=metric"
    conn.request("GET",url2)
    res = conn.getresponse()
    #read the response and formating for json
    data = res.read()
    data =  json.loads(data)
    conn.close
    temp_min = str(data["main"]["temp_min"]).encode('utf-8')
    temp_max = str(data["main"]["temp_max"]).encode('utf-8')
    temp = str(data["main"]["temp"]).encode('utf-8')
    message  =  data["name"]+" "+temp+"C agora com minima"+ temp_min+"C e maxima ".encode('utf-8')+temp_max+"C."
    return message

  @staticmethod
  def get_weather(msg):
    m = msg.group('/^[(#\w)|(@\w)]*/')
    return TwitterWeather.search(m)





