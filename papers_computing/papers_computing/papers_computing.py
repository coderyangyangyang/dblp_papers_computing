from operator import attrgetter, itemgetter
import networkx as nx
import numpy as np
import scipy as sp

def sort_wirte_nodes_by_year(Digraph):
    f_sort=open("sorted_id_year.dat","w")
    id_year_list=[(node,Digraph.nodes[node]["year"]) for node in Digraph if "year" in Digraph.nodes[node]]
    sorted_id_year_nodes_list=sorted(id_year_list,key=itemgetter(1))
    for node_tuple in sorted_id_year_nodes_list:
        f_sort.write(node_tuple[0]+"\t"+str(node_tuple[1])+"\n")
    odered_id_list=[node[0] for node in sorted_id_year_nodes_list]
    return odered_id_list

def read_odered_age_id(odered_age_id_filename):
    f_odered_id=open(odered_age_id_filename,"r")
    odered_id_list=[strline.split(maxsplit=1)[0] for strline in f_odered_id]
    return odered_id_list

def add_PageRank_attribute_to_nodes(Digraph):
    pagerank_dict=nx.algorithms.link_analysis.pagerank_alg.pagerank_scipy(Digraph,alpha=0.5,tol=1.0e-9)
    for key in pagerank_dict.keys():
        Digraph.nodes[key]["PageRank"]=pagerank_dict[key]

def add_HITS_attribute_to_nodes(Digraph):
    HITS_tuple=nx.algorithms.link_analysis.hits_alg.hits_scipy(Digraph,tol=1.0e-9)
    HITS_authority_dict=HITS_tuple[0]
    for key in HITS_authority_dict.keys():
        Digraph.nodes[key]["HTau"]=HITS_authority_dict[key]

def output_network_info(Digraph,odered_id_list):
    #Digraph=nx.DiGraph()#----------------------
    in_degree_list=[]
    out_degree_list=[]
    pr_list=[]
    HT_list=[]
    num_Rconference=0
    for node in odered_id_list:
        in_degree_list.append(Digraph.in_degree(node))
        out_degree_list.append(Digraph.out_degree(node))
        pr_list.append(Digraph.nodes[node]["PageRank"])
        HT_list.append(Digraph.nodes[node]["HTau"])
        if Digraph.nodes[node]["Rconference"]==1:
            num_Rconference+=1
    num_nodes=Digraph.number_of_nodes()
    num_edges=Digraph.number_of_edges()
    f_in_deg=open("dblp_10_in_degree.dat","w")
    for in_degree in in_degree_list:
        f_in_deg.write(str(in_degree)+"\n")
    f_in_deg.close()
    f_out_deg=open("dblp_v10_out_degree.dat","w")
    for out_degree in out_degree_list:
        f_out_deg.write(str(out_degree)+"\n")
    f_out_deg.close()
    f_pr=open("dblp_v10_pagerank.dat","w")
    for pr in pr_list:
        f_pr.write(str(pr)+"\n")
    f_pr.close()
    f_HT=open("dblp_v10_HTau.dat","w")
    for HT in HT_list:
        f_HT.write(str(HT)+"\n")
    f_HT.close()
    f_num=open("dblp_v10_num_info.dat","w")
    f_num.write("num_Rconference: "+str(num_Rconference)+"\n"+"num_nodes: "+str(num_nodes)+"\n"+"num_edges: "+str(num_edges)+"\n")
    f_num.close()

def rank_score(ordered_age_score_list):
    index_score_list=[(index,score) for index,score in enumerate(ordered_age_score_list)]
    ranked_score_list=sorted(index_score_list,key=itemgetter(1))
    odered_age_rank_list=[0]*len(ranked_score_list)
    for i in range(len(ranked_score_list)):
        odered_age_rank_list[ranked_score_list[i][0]]=i
    return odered_age_rank_list

def rank_bias_by_age(odered_age_rank_list,z,group_size,rank_name):
    size=len(odered_age_rank_list)
    best_size=int(z*size)
    top_age_group_list=[0]*best_size
    for i in range(size):
        if odered_age_rank_list[i]<=best_size:
            group_num=int(i/int(group_size))
            top_age_group_list[group_num]+=1
    f_bias=open(rank_name+"_time_bias.dat","w")
    for i in range(len(top_age_group_list)):
        f_bias.write(str(i)+"\t"+str(top_age_group_list[i])+"\n")

def get_atribute_score_list(Digraph,odered_age_id_list,score_name):
    score_list=[Digraph.nodes[id][score_name] for id in odered_age_id_list]
    return score_list

def main():
    DG=nx.read_gml("dblp_v10_pr_HT.gml")
    N=DG.number_of_nodes()
    #odered_age_id_list=sort_wirte_nodes_by_year(DG)
    odered_age_id_list=read_odered_age_id("sorted_id_year.dat")

    pr_score_list=get_atribute_score_list(DG,odered_age_id_list,"PageRank")
    odered_age_pr_rank_list=rank_score(pr_score_list)
    rank_bias_by_age(odered_age_pr_rank_list,0.01,N/40,"PageRank")

    HT_score_list=get_atribute_score_list(DG,odered_age_id_list,"HTau")
    odered_age_HT_rank_list=rank_score(HT_score_list)
    rank_bias_by_age(odered_age_HT_rank_list,0.01,N/40,"HITS-authority")
    #output_network_info(DG,odered_id_list)

    #add_PageRank_attribute_to_nodes(DG)
    #add_HITS_attribute_to_nodes(DG)

    #nx.write_gml(DG,"dblp_v10_pr_HT.gml")
if __name__=="__main__":
    main()