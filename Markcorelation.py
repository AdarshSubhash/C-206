import plotly.express as pe
import csv
import numpy as np 
def getdata(datapath):
    m=[]
    d=[]
    with open(datapath) as f:
        reader=csv.DictReader(f)
        for i in reader:
            m.append(float(i["Marks"]))
            d.append(float(i["Days"]))
    return{"x":m,"y":d}
def findcorelation(datasource):
    corelation=np.corrcoef(datasource["x"],datasource["y"])            
    print("Corelation between Marks and Days:",corelation[0,1])
def setup():
    datapath="Marks.csv"
    datasource=getdata(datapath)
    findcorelation(datasource)
setup()        