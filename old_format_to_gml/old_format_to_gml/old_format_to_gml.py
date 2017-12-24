#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx
import codecs

def read_old_file(DG, old_filename):
    symbol_title="#*"
    len_symbol_title=len(symbol_title)
    #print(len_symbol_title)
    symbol_authors="#@"
    len_symbol_authors=len(symbol_authors)
    symbol_year="#t"
    len_symbol_year=len(symbol_year)
    symbol_venue="#c"
    len_symbol_venue=len(symbol_venue)
    symbol_id="#index"
    len_symbol_id=len(symbol_id)
    symbol_to_id="#%"
    len_symbol_to_id=len(symbol_to_id)
    #f_in=codecs.open(old_filename,"r","utf-8")
    f_in=open(old_filename,"r")
    for line in f_in:
        line=line.strip("\n")
        if(line[:len_symbol_title]==symbol_title):
            l_title=line[len_symbol_title:]
            if(l_title[-1]=="."):
                l_title=l_title[:-1]
        elif(line[:len_symbol_authors]==symbol_authors):
            l_authors_list=line[len_symbol_authors:].split(", ")
        elif(line[:len_symbol_year]==symbol_year):
            l_year=line[len_symbol_year:]
        elif(line[:len_symbol_venue]==symbol_venue):
            l_venue=line[len_symbol_venue:]
        elif(line[:len_symbol_id]==symbol_id):
            l_id=line[len_symbol_id:]
            DG.add_node(l_id,authours=l_authors_list,title=l_title,venue=l_venue,year=l_year)
        elif(line[:len_symbol_to_id]==symbol_to_id):
            l_to_id=line[len_symbol_to_id:]
            DG.add_edge(l_id,l_to_id)
def write_to_gml(Graph,filename):
    nx.write_gml(Graph,filename)
def remove_nodes(DG):
    cut_nodes=[]
    for node in DG:
        if DG.in_degree(node)==0:
            cut_nodes.append(node)
    DG.remove_nodes_from(cut_nodes)
def change_to_gml(old_filename,gml_filename):
    DG=nx.DiGraph()
    read_old_file(DG,old_filename)
    remove_nodes(DG)
    write_to_gml(DG,gml_filename)
def main():
   change_to_gml("/home/wxy/data_set/citation-acm-v8.txt","acm_v8.gml")
   change_to_gml("/home/wxy/data_set/dblp_v8.txt","dblp_v8.gml")

if __name__=="__main__":
    main()