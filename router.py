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
        from workers import torrent
        tor = torrent.get_torrent(query)
        if tor:
            if service == "sendgrid":
                response = "<a href=%s>Baixar o melhor torrent para %s</a>" % (tor,query)
            else:
                response = "%s" % tor
        else:
            response = "Conhecimento Inexistente para vc"
    elif "placar" in hashtags:
        response = u"não ocorre nenhum jogo agora, terráqueo."
    elif "hn" in hashtags:
        from workers import hn
        noticia = hn.get_hn()
        response  = "<a href=%s>%s</a>" % (noticia.link,noticia.title)
    elif "mm" in hashtags:
        from workers.mm import get_mms
        response  = get_mms()
    elif "fonte" in hashtags:
        response  = "github.com/robertocr/vaibilu"
    else:
        from workers import duckduckgo
        response = duckduckgo.get_abstract(query)



    if service == "sendgrid":
        response = response+"<br>"+\
	               "<br>-------<br>"+\
	               "\"Busquem conhecimento\" - ET Bilu<br>" +\
                   "<img src='http://vaibilu.com/static/bilu_small.jpg'>"
    elif service == "twitter":
        response = response[:160]

    return response