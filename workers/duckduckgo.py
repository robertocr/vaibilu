# -*- coding: utf-8 -*-
import re, json
from utils import *
import requests
from duckduckgosdk import duckduckgo

# retorna arquivo de torrent com mais seeds, além da legenda
def get_abstract(message):
	# query = strip_accents( unicode(message) ).lower() #limpando possiveis acentos, botando em lowercase

	# hashtags = list(extract_hash_tags( message ))
	# for hashtag in hashtags:
	# 	query = query.replace(hashtag, ""); #matando a hashtag, sei la
	# 	for mention in list(extract_mentions( query )):
	# 		query = query.replace(mention, ""); #matando a mention, sei la
	query = re.findall(r'\w+', message) #pegando cada palavra
	query = ' '.join( query ) #juntando-as com espaço

	answer = duckduckgo.get_zci(query)

	if answer == '' :
		return message+" eh "+message+", oras! Busque conhecimento!"
	else:
		return answer




	# query = strip_accents( unicode(message) ).lower() #limpando possiveis acentos, botando em lowercase

	# # query = query.replace(hashtag, ""); #matando a hashtag, sei la
	# query = re.findall(r'\w+', query) #pegando cada palavra
	# query = '+'.join( query ) #juntando-as com %20

	# r = requests.get("http://api.duckduckgo.com/?q=%s&format=json" % query)
	# response = json.loads(r.text)

	# response = response['AbstractText']
	# if response!='':
	# 	return response
	# else:
	# 	return message+" eh "+message+", oras! Busque conhecimento!"




	# response = json.loads(r.text)
	# response = response['AbstractText']


	# return response

	




	# hashtags = list(extract_hash_tags( message ))
	# for hashtag in hashtags:
	# 	query = query.replace(hashtag, ""); #matando a hashtag, sei la
	# 	query = re.findall(r'\w+', query) #pegando cada palavra
	# 	query = '%20'.join( query ) #juntando-as com %20

	# 	# r = requests.get("http://api.duckduckgo.com/?q=%s&format=json&pretty=1" % query)
	# 	r = requests.get("http://api.duckduckgo.com/?q=%s&format=json" % query)
	# 	response = json.loads(r.text)
	# 	response = response['AbstractText']

	# 	# return response
	# 	return 'ae'