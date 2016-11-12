# -*- coding: utf-8 -*-

UKR_ALPHABET = "абвгдеиіїжзийклмнопрстуфхцчшщьєюяАБВГДИІЇЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЄЮЯ"

def ukr_letter(letter):
	return letter in UKR_ALPHABET

def work_ukr_chars(word):
	for s in word:
		if not ukr_letter(s):
			return False
	return True

def get_words(word):
	res = []
	start = 0
	for i, s in enumerate(word):
		if not ukr_letter(s):
			if len(word[start:i]):
				res.append(word[start:i])
				start = i + 1
	if i != start and len(word[start:i]):
		res.append(word[start:i])
	return res