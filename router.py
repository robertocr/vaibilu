# -*- coding: utf-8 -*-

from workers.utils import *

def router(message, service):
    response = message

    #tenta descobrir se a pessoa quer torrent ou seilaoque
    hashtags = extract_hash_tags(message)

    query = strip_accents( unicode(message.decode('utf8')) ).lower() #limpando possiveis acentos, botando em lowercase
    for hashtag in list(hashtags):
        query = query.replace(hashtag, "") #matando a hashtag, sei la
        for mention in list(extract_mentions( query )):
            query = query.replace(mention, "") #matando a mention, sei la


    if "torrent" in hashtags:
        try:
            from workers import torrent
            response = torrent.get_torrent(query)
        except:
            response = u"Serviço TPB em manutenção"
    elif "placar" in hashtags:
        response = u"não ocorre nenhum jogo agora, terráqueo."
    elif "hn" in hashtags:
        try:
            from workers import pega_hn
            response  = pega_hn.get_hn(query)
        except:
            response = u"Serviço HN em manutenção"
    elif "weather" in hashtags:
        from workers import weather
        response  = weather.get_weather(query)
    elif "mm" in hashtags:
        from workers.mm import get_mms
        response  = get_mms(query)
    elif "porn" in hashtags:
        from workers.porn import get_porn
        response, extras  = get_porn(query)
    elif "fonte" in hashtags:
        response  = u"http://github.com/robertocr/vaibilu #compartilhe_conhecimento"
    else:
        from workers import duckduckgo
        response = duckduckgo.get_abstract(query)


    if service == "sendgrid":
        response = response+"<br>"
        for extra in extras:
            response += u"<img src='%s'>" % extra

        response += u"<br>-------<br>"+\
                   u"\"Busquem conhecimento\" - ET Bilu<br>" +\
                   u"<img src='http://vaibilu.com/static/bilu_small.jpg'>"
    elif service == "twitter":
        if response:
            response = response[:160]
        else:
            response = u'Busquem conhecimento!'

    return response