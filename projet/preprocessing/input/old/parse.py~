#-*- coding: utf-8 -*-

import re
from fyzz import parse
"""
with open ("./requetes.txt", "w") as out:
    with open("./donnee.xml","r") as inp:
        a=[]
        for line in inp:
            m=re.search("PREFIX(.)*",line)
            if m!=None:
                a.append(str(m.group(0)))
                out.write(m.group(0)+"\n")
                print m.group(0)
"""


g=[16, 30, 37, 65, 78, 84, 98, 99, 114, 121, 131, 135, 136, 139, 140, 143, 149, 150, 152, 162, 168, 169, 170, 173, 175, 182, 186]
i=1
with open ("./requetes.txt", "r") as inp:
    with open("./res.txt",'w') as out:
        for elmt in inp:
            #if re.search("^#",elmt)==None:
            if i not in g :
                #print "ligne "+ str(i)
                out.write(str(parse(str(elmt)).where)+'\n')
            else :
                g.append(i)
            i+=1

with open ("./res.txt", "r+") as file:
    old = file.read()
    file.seek(0)
    file.write(str(g)+'\n'+old)

with open ("./res.txt", "r+") as file:
    print str(file.seek(2))
    
