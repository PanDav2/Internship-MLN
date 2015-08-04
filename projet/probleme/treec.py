#-*- coding: utf-8 -*-

#Cette classe permet la création d'un arbre par rapport à la sortie retournée par
#Le proc['sentences'][0]['parse'] de Stanford NLP qui est de la forme 
# (Root (TAG elemt))

class Tree():
	def __init__(self,left,right):
		self.l=left
		self.r=right
x = Tree(5,4)
