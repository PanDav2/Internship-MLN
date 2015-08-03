#-*- coding: utf-8 -*-

from stanford_corenlp_pywrapper import CoreNLP

loc= "/people/panou/Stage/projet/stanford-corenlp-full-2015-04-20/*"

proc = CoreNLP("pos", corenlp_jars=[loc])

proc.parse_doc("Which software has been developed by organizations founded in California, USA?")
