# -*- coding: utf-8 -*-
import httplib
import json
import re

def search (town):
    conn = httplib.HTTPConnection("api.openweathermap.org")
    url2 = "/data/2.5/weather?q="+town+",br&units=metric"
    conn.request("GET",url2)
    res = conn.getresponse()
    #read the response and formating for json
    data = res.read()
    data =  json.loads(data)
    conn.close

    try:
        if not res.status == 200:
            return "Conhecimento Inexistente para vc"
        else:
            temp_min = str(data["main"]["temp_min"]).encode('utf-8')
            temp_max = str(data["main"]["temp_max"]).encode('utf-8')
            temp = str(data["main"]["temp"]).encode('utf-8')
            message  =  data["name"]+" "+temp+"C agora, com min "+ temp_min+"C e max ".encode('utf-8')+temp_max+"C."
            return message
    except IndexError:
        return "Conhecimento Inexistente para vc"


def get_weather(msg):
    query = re.findall(r'\w+', msg) #pegando cada palavra
    query = '+'.join( query ) #juntando-as com espaço
    return search(query)