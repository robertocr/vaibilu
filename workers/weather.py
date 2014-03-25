# -*- coding: utf-8 -*-
import httplib
import json
import re
from threading import Thread
from sendgrid_service import send_email

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

class get_weather_thread(Thread):

    def __init__(self, busca, service,email, subject, *args, **kwargs):
        Thread.__init__(self)
        self.busca = busca
        self.service = service
        self.email = email
        self.subject = subject
        self.args = args
        self.kwargs = kwargs

    def run(self):
        response  = get_weather(self.busca)

        if self.service == u"sendgrid":
            response = response+"<br>"
            response += u"<br>-------<br>"+\
                        u"\"Busquem conhecimento\" - ET Bilu<br>" +\
                        u"<img src='http://vaibilu.com/static/bilu_small.jpg'>"

            return send_email(response, self.email, self.subject)

        elif self.service == "twitter":
            if response:
                response = response[:160]
            else:
                response = u'Busquem conhecimento!'

