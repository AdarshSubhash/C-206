import plotly.express as pe
import csv
import numpy as np 
def getdata(datapath):
    icecreamsales=[]
    colddrinksales=[]
    with open(datapath) as f:
        reader=csv.DictReader(f)
        for i in reader:
            icecreamsales.append(float(i["Temperature"]))
            colddrinksales.append(float(i["Icecream"]))
    return{"x":icecreamsales,"y":colddrinksales}
def findcorelation(datasource):
    corelation=np.corrcoef(datasource["x"],datasource["y"])            
    print("Corelation between temperature and icecreamsales:",corelation[0,1])
def setup():
    datapath="Ice-cream.csv"
    datasource=getdata(datapath)
    findcorelation(datasource)
setup()        