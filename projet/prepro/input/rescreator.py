#-*- coding: utf-8 -*-

import re

g=[]
res=[]
error=[16, 30, 37, 65, 78, 84, 98, 99, 114, 121, 131, 135, 136, 139, 140, 143, 149, 150, 152, 162, 168, 169, 170, 173, 175, 182, 186]
j=1
with open ("./res.txt", "r") as inp:
    with open ("./out.txt", "w") as out:
        for i,line in enumerate(inp): 
            temp =re.findall("'[^']+'",line)
            for elmt in temp:
                if elmt not in res:
                    res.append(elmt)
                    out.write(elmt+'\n')


"""
        for elmt in g:
            if j not in error:
                print "ligne " + str(j)
                print elmt
                j=j+1
            else :
                j=j+1
"""
