import networkx as nx
import matplotlib.pyplot as plt
def get_bestpapers_id(gml_filename,title_filename,new_id_title_filename):
    DG=nx.read_gml(gml_filename)
    title_label={}
    title_list=[]
    for node in DG:
        if "title" in DG.nodes[node]:
            N_title=DG.nodes[node]["title"]
            title_label[N_title]=node
    f_title=open(title_filename,"r")
    for title_line in f_title:
        title_list.append(title_line)
    f_title.close()
    f_out=open(new_id_title_filename,"w")
    for title_line in title_list:
        if title_line in title_label:
            f_out.write(title_label[title_line]+"\t"+title_line+"\n")
            
get_bestpapers_id("test_graph1.gml",r"E:\Codes\PythonCodes\get_bestpaers\get_bestpaers\all_bestpapers_final000.dat","id_title_dblp_v10.dat")   
