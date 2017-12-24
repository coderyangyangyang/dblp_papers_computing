import networkx as nx

def get_network_info_0(gml_filename):
    DG=nx.read_gml("test_graph1.gml")
    f=open("test_graph_info.dat","w")
    in_degree_list=[]
    out_degree_list=[]
    node_count=0
    for node in DG:
        in_degree_list.append(DG.in_degree(node))
        out_degree_list.append(DG.out_degree(node))
        node_count+=1
    f.write("in_degree_list:\n")
    f.write(str(in_degree_list))
    f.write("\n")
    f.write("out_degree_list:\n")
    f.write(str(out_degree_list))
    f.write("\n")
    f.write("nodes num:\n")
    f.write(str(node_count))

def get_network_info_1(gml_filename):
    DG=nx.read_gml("test_graph1.gml")
    node_count=0
    f_in_degree=open("test_graph_in_degree.dat","w")
    f_out_degree=open('test_garaph_out_degree.dat',"w")
    for node in DG:
        f_in_degree.write(str(DG.in_degree(node))+"\n")
        f_out_degree.write(str(DG.out_degree(node))+"\n")
        node_count+=1
    print(node_count)
get_network_info_1("test_graph1.gml")