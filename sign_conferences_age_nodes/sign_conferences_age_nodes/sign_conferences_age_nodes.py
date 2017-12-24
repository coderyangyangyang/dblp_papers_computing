import networkx as nx

def To_sign_conferences_age_bestpaper_nodes(conferences_filename,bestpaper_id_filename,gml_filename,gml_signed_filename):
    conferences_name_list=[]
    bestpaper_id_list=[]
    f_conferences=open(conferences_filename,"r")
    for conferences_name in f_conferences:
        conferences_name_list.append(conferences_name.strip("\n"))
    f_conferences.close()
    f_bestpaper=open(bestpaper_id_filename,"r")
    for bestpaper_id in f_bestpaper:
        bestpaper_id_list.append(bestpaper_id.strip("\n"))
    f_bestpaper.close()
    conference_froz_set=frozenset(conferences_name_list)
    bestpaper_froz_set=frozenset(bestpaper_id_list)
    DG=nx.read_gml(gml_filename)
    for node in DG:
        if "venue" in DG.nodes[node] and "year" in DG.nodes[node]:
            if DG.nodes[node]["venue"] in conference_froz_set and int(DG.nodes[node]["year"])>=1996:
                DG.nodes[node]["Rconference"]=True
        if node in bestpaper_froz_set:
            DG.nodes[node]["bestpaper"]=True
    nx.write_gml(DG,gml_signed_filename)
To_sign_conferences_age_bestpaper_nodes("bestpapers_venue_dblp_v10_uniq.dat","bestpaper_id_dblp_v10.dat","dblp_v10.gml","dblp_v10_signed.gml")

