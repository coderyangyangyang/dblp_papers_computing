import json
import networkx as nx
import string
import matplotlib.pyplot as plt
import test2

#DG=nx.DiGraph()
def json_to_gml(filepath):
    #f=open('info.dat','r')
    f=open(filepath,'r')
    for line in f:
        jsonline=json.loads(line)
        #authours_list=()
        #references_list=()
        #title=""
        #venue=""
        #year=0
        if("authors" in jsonline):
            authours_list=jsonline["authors"]
            print(authours_list)
        if('references' in jsonline):
            if(jsonline['references']!=[]):
                print(jsonline['references'])
                references_list=jsonline["references"]
                print(type(references_list))
                for re_id in jsonline['references']:
                    print(re_id)
        if("title" in jsonline):
            j_title=jsonline["title"]
            print(type(j_title))
        if("venue" in jsonline):
            if(jsonline["venue"]!=[]):
                j_venue=jsonline["venue"]
                print(j_venue)
        if("year" in jsonline):
            if(jsonline["year"]!=[]):
                j_year=int(jsonline["year"])
                print(type(j_year))
        if("id" in jsonline):
            id=jsonline["id"]
            print(type(id))
      #      DG.add_node(id,authours=authours_list,references=references_list,title=j_title,venue=j_venue,year=j_year)
      #  if(references_list!=()):
       #     for end_edg in references_list:
     #           DG.add_edge(id,end_edg)
    #nx.write_gml(DG,"test_graph.gml")

#def main():
    #DG=nx.DiGraph()

#main()
def set_test():
    a=set([1,1,2,2,3])
    print(a)
def string_test():
    s="abcde."
    b=(s[-1]==".")
    s1=s[:-1]
    print(b)
    print(s[-1])
    print(s1)

def get_best_paper_test():
    f=open('SenSys.json','rb')
    paper_json=json.load(f)
    if("value" in paper_json):
        for year_papers in paper_json["value"]:
            str_year=str(list(year_papers.keys())[0])
            if("papers_info" in year_papers[str_year]):
                #print("papersssssssssssssss")
                for paper in year_papers[str_year]["papers_info"]:
                    j_title=paper["title"]
                    if("isBest" in paper):
                        #print("isBest in")
                        if(paper["isBest"]==True):
                            print(str_year,"  bestpaper_title: ",j_title)

    #if("papers_info" in paper_json):
    #    print(paper_json["papers_info"])
    #else:
    #    print("NO")
def Digraph_test():
    DG=nx.DiGraph()
    DG.add_nodes_from([1,2,3,4,5,6])
    DG.add_edges_from([(0,1),(0,2),(1,3),(1,2),(1,3),(2,4),(3,5),(1,5),(6,1)])
    #print(DG.in_degree(0))
    #print(DG.in_degree(2))
    #print(DG.out_degree(1))
    for n in DG:
        print(n)
        #print(type(n))
    #nx.draw(DG,)
    #DG.remove_node(1)
    nx.draw(DG, with_labels=True, font_weight='bold')
    plt.show()

def write_test():
    alist=["aaa","bbb","ccc","ddd"]
    f=open("write_test.txt","w")
    for a in alist:
        f.write(a)
def string_split_test():
    a="abc, 123, xyz, lmn"
    b=a.split(", ")
    print(type(b))
    print(str(b))
def argument_test(a):
    a+=1
def string_split_test():
    a="426938	26167	1964-08-24	10.1103/PhysRevLett.13.275	localized vibrations of phosphorus and aluminum impurities in gasb,w. hayes\n"
    a=a.strip("\n")
    a_list=a.split(maxsplit = 1)
    print(a_list)
def main():
    #json_to_gml("info.dat")
    #print(type(1))
    #get_best_paper_test()
    #Digraph_test()
    #write_test()
    #string_split_test()
    #b=0
    #argument_test(b)
    #print(b)
    #graph_attributes_test()
    #print_a()
    string_split_test()
def graph_attributes_test():
    DG=nx.read_gml("test_graph1.gml")
    for node in DG:
        if "year" in DG.nodes[node]:
            print(type(DG.nodes[node]["year"]))
            if int(DG.nodes[node]["year"])>=1996:
                DG.nodes[node]["Rconference"]=True
    nx.write_gml(DG,"test_graph2.gml")
if __name__=="__main__":
    main()