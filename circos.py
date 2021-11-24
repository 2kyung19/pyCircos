import pycircos
import matplotlib.pyplot as plt
Garc    = pycircos.Garc
Gcircle = pycircos.Gcircle

#Set chromosomes
circle = Gcircle()
with open("circos_1.csv") as f:
    f.readline()
    for line in f:
        line   = line.rstrip().split(",") 
        name   = line[0]
        length = int(line[-1]) 
        if name=='food':
            arc=Garc(arc_id=name,size=length, interspace=3, raxis_range=(800,850), labelposition=60, label_visible=True)
        else:
            arc    = Garc(arc_id=name, size=length, interspace=3, raxis_range=(950,1000), labelposition=60, label_visible=True)
        circle.add_garc(arc) 
circle.set_garcs() 

import collections

arcdata_dict = collections.defaultdict(dict)
with open("circos_2.csv") as f:
    f.readline()
    for line in f:
        line  = line.rstrip().split(",")
        name  = line[0]     
        start = int(line[2])-1 
        width = int(line[3])-(int(line[2])-1) 
        color = line[-1]
        if name not in arcdata_dict:
            arcdata_dict[name]["positions"] = []
            arcdata_dict[name]["widths"]    = [] 
            arcdata_dict[name]["colors"]    = [] 
        arcdata_dict[name]["positions"].append(start) 
        arcdata_dict[name]["widths"].append(width)
        arcdata_dict[name]["colors"].append(color)
    
for key in arcdata_dict:
    if key=='food':
        circle.barplot(key, data=[1]*len(arcdata_dict[key]["positions"]), positions=arcdata_dict[key]["positions"], 
                   width=arcdata_dict[key]["widths"], raxis_range=[800,850], facecolor=arcdata_dict[key]["colors"],spine=True)    
    else:
        circle.barplot(key, data=[1]*len(arcdata_dict[key]["positions"]), positions=arcdata_dict[key]["positions"], 
                   width=arcdata_dict[key]["widths"], raxis_range=[900,950], facecolor=arcdata_dict[key]["colors"],spine=True)    

values_all   = [] 
arcdata_dict = collections.defaultdict(dict)
with open("circos_3.csv") as f:
    f.readline()
    for line in f:
        line  = line.rstrip().split(",")
        name1  = line[0]     
        start1 = int(line[3])-1
        end1   = int(line[4])
        name2  = line[5]     
        start2 = int(line[7])-1
        end2   = int(line[8])
        color = line[-1]
        source = (name1, start1, end1, 900)
        destination = (name2, start2, end2, 800)
        circle.chord_plot(source, destination, facecolor=color)

plt.show()