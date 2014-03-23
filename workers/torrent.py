# -*- coding: utf-8 -*-
import re
from utils import *

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