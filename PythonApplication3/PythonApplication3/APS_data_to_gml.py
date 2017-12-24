import networkx as nx

def APS_to_gml(APS_nodes_filename,APS_edges_filename,APS_gml_filename):
    DG=nx.DiGraph()
    f_nodes=open(APS_nodes_filename,"r")
    for strline in f_nodes:
        strline=strline.strip("\n")
        node_info_list=strline.split(maxsplit = 4)
        DG.add_node(node_info_list[0],age=node_info_list[1],year=node_info_list[2],DOI=node_info_list[3],title=node_info_list[4])
    f_nodes.close()
    f_edges=open(APS_edges_filename,"r")
    for strline in f_edges:
        strline=strline.strip("\n")
        edges_info_list=strline.split()
        DG.add_edge(edges_info_list[0],edges_info_list[1],age=edges_info_list[2])
    f_edges.close()
    nx.write_gml(DG,APS_gml_filename)
APS_to_gml("ID_vs_DOI.dat","APS_citations.dat","APS.gml")
    

        

