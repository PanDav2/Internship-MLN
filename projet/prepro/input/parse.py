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
i=0
with open ("./requetes.txt", "r") as inp:
    with open("./res.txt",'w') as out:
        for elmt in inp:
            print "ligne "+ str(i)
            out.write(str(parse(str(elmt)).where)+'\n')
            i+=1

