#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import networkx as nx
import string
import matplotlib.pyplot as plt
#DG=nx.DiGraph()
def json_to_gml(DG,filepath):
    #f=open('info.dat','r')
    f=open(filepath,'r')
    references_count=0
    a=set([])
    
    for line in f:
        has_reference=False
        jsonline=json.loads(line)
        if("authors" in jsonline):
            authours_list=jsonline["authors"]
            print(authours_list)
        if('references' in jsonline):
            if(jsonline['references']!=[]):
                has_reference=True
                print(jsonline['references'])
                references_list=jsonline["references"]
                print(type(references_list))
                for re_id in jsonline['references']:
                    print(re_id)
        if("title" in jsonline):
            j_title=jsonline["title"]
            if(j_title[-1]=="."):
                j_title=j_title[:-1]
                print(type(j_title))
        if("venue" in jsonline):
            j_venue=jsonline["venue"]
            print(j_venue)
        if("year" in jsonline):
             j_year=int(jsonline["year"])
             print(type(j_year))
        if("id" in jsonline):
            id=jsonline["id"]
            print(type(id))
            DG.add_node(id,authours=authours_list,title=j_title,venue=j_venue,year=j_year)
            references_count+=1
            a.add(id)
        if(has_reference):
            for end_edg in references_list:
                DG.add_edge(id,end_edg)
                references_count+=1
                a.add(end_edg)
    print(references_count)
    print(len(a))
    lenth=len(a)
    return lenth
    #nx.write_gml(DG,"test_graph.gml")
def write_to_gml(Graph,filename):
    nx.write_gml(Graph,filename)

def main():
    DG=nx.DiGraph()
    a=json_to_gml(DG,"info.dat")
    b=json_to_gml(DG,"info2.dat")
    all_lenth=a+b
    print(all_lenth)
    write_to_gml(DG,"test_graph1.gml")
    nx.draw(DG)
    plt.show()

if __name__=="__main__":
    main()