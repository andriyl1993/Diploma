# -*- coding: utf-8 -*-

from libs import Text
from levenshteyn import distance as lev_dist


print "#" * 50
text = Text('Марія.txt', True)
words = text.get_word_dict()

word = u"точний"

word = u'connect'
word2 = u'conehead'

print lev_dist(word, word2)

# for w in words:
# 	print "/" * 20
# 	print word
# 	print w
# 	print lev_dist(word, w)
