# -*-coding: utf-8 -*-

def sim(F,G):
    res=np.zeros((len(G),len(G)))
    for pos1,val1 in enumerate(F):
        for pos2,val2 in enumerate(F):
            if pos1!=pos2:
                if metrics.cosine_similarity(val1,val2)>0:
                    res[pos1][pos2]=alpha* metrics.cosine_similarity(val1,val2)+(1-alpha)*LCS_sent(G[pos1],G[pos2])
