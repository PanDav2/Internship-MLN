#-*- coding: utf-8 -*-
import time
import sys
from stanford_corenlp_pywrapper import CoreNLP

toolbar_width = 40
loc= "/people/panou/Stage/projet/stanford-corenlp-full-2015-04-20/*"
#toolbar setup
"""
sys.stdout.write("[%s]"% (" "* toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b"* (toolbar_width+1))# return to start of line, after '['
"""
#for i in xrange(toolbar_width):
proc = CoreNLP("pos", corenlp_jars=[loc])    
"""    sys.stdout.write("-")
    sys.stdout.flush()
    sys.stdout.write("\n")"""


#proc.parse_doc("Which software has been developed by organizations founded in California, USA?")
