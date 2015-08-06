#-*- coding: utf-8 -*-

""" This class is intended to extract phrases according to the given parameters.
 TODO: Implement differents parameters for the phrase extraction from sentences.
Actual parameters are He,  the usual NER from Stanford CoreNLP and the unigramm model without stopwords """

#Loading the Stanford NLP wrapper Lib
from stanford_corenlp_pywrapper import CoreNLP
loc= "/people/panou/Stage/projet/stanford-corenlp-full-2015-04-20/*"


proc = CoreNLP("parse",corenlp_jars=[loc])
