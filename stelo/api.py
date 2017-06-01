# coding=utf-8
import os
import re
import json
import requests
from requests.auth import HTTPBasicAuth

class Api(object):

	def __init__(self, token):
		self.token = token

	def headers(self):
		return {
			"Content-Type": "application/json",
			"Accept": "application/json"
		}

	def main_request(self, url, method, data={}):
		try:
			response = requests.request(method, url,auth=HTTPBasicAuth(self.token, ''),data=json.dumps(data),headers=self.headers())
			return json.loads(response.content.decode('utf-8'))
		except Exception as error:
			raise

	def get(self, url, data={}):
		return self.main_request(url, 'GET', data=data)

	def post(self, url, data={}):
		return self.main_request(url, 'POST', data=data)

	def put(self, url, data={}):
		return self.main_request(url, 'PUT', data=data)

	def delete(self, url):
		return self.main_request(url, 'DELETE')

	def get_url(self, paths):
		'''
		Sandbox 	https://apic1.hml.stelo.com.br
		Produção 	https://api.stelo.com.br
		'''
		url = 'https://api.stelo.com.br'
		for path in paths:
			url = re.sub(r'/?$', re.sub(r'^/?', '/', str(path)), url)
		print (url)
		return url

__main_api__ = None

def main_api():

    global __main_api__
    if __main_api__ is None:
        __main_api__ = Api(token='TOKEN HERE')
    return __main_api__




