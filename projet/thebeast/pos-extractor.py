#-*- coding: utf-8 -*-
import re
search = re.search
tab=[]
with open('./html.html','r') as inp:
	for line in inp:
		print 'ouistiti'
		tab.append(line)
		#L'ensemble des lignes de inp sont stockées dans le tableau.
with open('./out','w') as out:
	for position,line in enumerate(tab):
		print 'ouistiti'
		if search('aligne="none"',line):
			print str(tab[positiion+1])
			
		
