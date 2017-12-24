#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx

def get_bestpapers_venue(gml_filename,bestpapers_id_filename,bestpapers_venue_filename):
    f_id=open(bestpapers_id_filename,"r")
    DG=nx.read_gml(gml_filename)
    f_venue=open(bestpapers_venue_filename,"w")
    for bestpaper in f_id:
        #print(bestpaper)
        bestpaper=bestpaper.strip("\n")
        if "venue" in DG.nodes[bestpaper]:
            f_venue.write(DG.nodes[bestpaper]["venue"]+"\n")
get_bestpapers_venue("test_graph1.gml","id.dat","venue_dblp_v10_test.dat")
