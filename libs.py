# -*- coding: utf-8 -*-
from letters import work_ukr_chars, get_words

class Text(object):
	def __init__(self, text=None, is_path=False):
		self.text = ""
		self.words = list()

		if text and not is_path:
			self.text = text
		elif text and is_path:
			f = open(text, 'r')
			self.text = f.read()

	def set_text(self, text):
		self.text = text

	def get_word_dict(self):
		if not self.text:
			raise Exception('No text data')

		words = []
		for row in self.text.split('\n'):
			for word in row.split():
				words += get_words(word)

		return words

