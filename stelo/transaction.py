# coding=utf-8
from action import Action
from exception import RequiredParameters


class Transaction(Action):

	def create(self, data):
		url = self.api.get_url([])
		return super(Transaction, self).create(url, data)

	
