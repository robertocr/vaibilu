# -*- coding: utf-8 -*-
import re
from utils import *
from threading import Thread
from sendgrid_service import send_email

# retorna arquivo de torrent com mais seeds, além da legenda
def get_torrent(message):
# 	query = strip_accents( unicode(message) ).lower() #limpando possiveis acentos, botando em lowercase

# 	hashtags = list(extract_hash_tags( message ))
# 	for hashtag in hashtags:
# 		query = query.replace(hashtag, ""); #matando a hashtag, sei la
# 		query = re.findall(r'\w+', query) #pegando cada palavra
# 		query = '%20'.join( query ) #juntando-as com %20
    query = re.findall(r'\w+', message) #pegando cada palavra
    query = '%20'.join( query ) #juntando-as com %20
    return melhor_torrent(query)

def  melhor_torrent(nome_busca, qtd = None):
    from tpb import TPB
    from tpb import CATEGORIES, ORDERS

    t = TPB('https://thepiratebay.se') # configurando o site do TPB
    # Buscando todos os tipos de Video
    if not qtd:
        search = t.search(nome_busca, category=CATEGORIES.VIDEO.ALL).order(ORDERS.SEEDERS.DES).page(0)
    else:
        search = t.search(nome_busca, category=CATEGORIES.VIDEO.ALL).order(ORDERS.SEEDERS.DES)

    torrents = []
    for torrent in search:
        torrents.append(torrent)

    try:
        if not qtd:
            return torrents[0].magnet_link
        else:
            return torrents[0:qtd]
    except IndexError:
        return None


class get_torrent_thread(Thread):

    def __init__(self, busca, service,email, subject, *args, **kwargs):
        Thread.__init__(self)
        self.busca = busca
        self.service = service
        self.email = email
        self.subject = subject
        self.args = args
        self.kwargs = kwargs

    def run(self):
        response  = get_torrent(self.busca)

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

