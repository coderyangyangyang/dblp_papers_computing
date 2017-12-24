import os
import json
def get_all_best_papers(path_name,best_file_name):
    rootdir = path_name
    count=0
    fout=open(best_file_name,'w')
    list = os.listdir(rootdir) 
    for i in range(0,len(list)):
        s_path = os.path.join(rootdir,list[i])
        if os.path.isfile(s_path):
            print(s_path)
            count+=1
            get_best_papers_info(s_path,fout)
    print(count)

def get_best_papers_info(input_filename,fout):
    f=open(input_filename,'rb')
    paper_json=json.load(f)
    if("value" in paper_json):
        for year_papers in paper_json["value"]:
            str_year=str(list(year_papers.keys())[0])
            if("papers_info" in year_papers[str_year]):
                for paper in year_papers[str_year]["papers_info"]:  
                    j_title=paper["title"]
                    j_id=paper["id"]
                    if("isBest" in paper):
                        if(paper["isBest"]==True):
                            #print(str_year,"  bestpaper_title: ",j_title)
                            fout.write(j_id+"\t"+j_title+"\n")
def main():
    get_all_best_papers('E:\ACM_BestPaper_material\Aminer_best_paper',"all_bestpapers.dat")

if(__name__=="__main__"):
    main()