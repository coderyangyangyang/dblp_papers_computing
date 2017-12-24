#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx

def get_id_title(gml_filename,title_filename,id_title_filename):
    title_list=[]
    f_title=open(title_filename,"r")
    for title in f_title:
        title_list.append(title.strip("\n"))
    f_title.close()
    froz_set=frozenset(title_list)
    print(str(froz_set))
    f_id=open(id_title_filename,"w")
    DG=nx.read_gml(gml_filename)
    for node in DG:
        if "title" in DG.nodes[node]:
            if DG.nodes[node]["title"] in froz_set:
                f_id.write(node+"\t"+DG.nodes[node]["title"]+"\n")

get_id_title("test_graph1.gml","all_bestpapers_final.dat","id_title_dblp_v10_test.dat")

