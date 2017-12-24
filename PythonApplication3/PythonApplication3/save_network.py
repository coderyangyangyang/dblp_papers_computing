#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import networkx as nx
import string
#import matplotlib.pyplot as plt
def json_to_gml(DG,filepath):
    f=open(filepath,'r')
    
    for line in f:
        has_reference=False
        jsonline=json.loads(line)
        if("authors" in jsonline):
            authours_list=jsonline["authors"]
        if('references' in jsonline):
            if(jsonline['references']!=[]):
                has_reference=True
                references_list=jsonline["references"]
        if("title" in jsonline):
            j_title=jsonline["title"]
            if(j_title[-1]=="."):
                j_title=j_title[:-1]
        if("venue" in jsonline):
            j_venue=jsonline["venue"]
        if("year" in jsonline):
             j_year=int(jsonline["year"])
        if("id" in jsonline):
            id=jsonline["id"]
            DG.add_node(id,authours=authours_list,title=j_title,venue=j_venue,year=j_year)
        if(has_reference):
            for end_edg in references_list:
                DG.add_edge(id,end_edg)
def write_to_gml(Graph,filename):
    nx.write_gml(Graph,filename)

def remove_nodes(DG):
    cut_nodes=[]
    for node in DG:
        if DG.in_degree(node)==0:
            cut_nodes.append(node)
    DG.remove_nodes_from(cut_nodes)
def count_nodes(DG):
    c=0
    for n in DG:
       c+=1
    print(c)
def main():
    DG=nx.DiGraph()
    json_to_gml(DG,"info.dat")
    json_to_gml(DG,"info2.dat")
    remove_nodes(DG)
    count_nodes(DG)
    write_to_gml(DG,"test_graph1.gml")

if __name__=="__main__":
    main()
