# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 20:07:26 2015

@author: tedscott
"""

def azureml_main(frame1):
    import pandas as pd
    import os.path
    
    ## set a flag to define which environment we're in
    Azure = False
    
    # if in Azure, the sata frame is passed to the function
    # if running in the IDE, load it from a local file
    if(Azure==False):
        pathName="C:/GIT/EdX-DataSci/DAT203_Lab02B"
        fileName = "cadairydata.csv"
        filePath = os.path.join(pathName, fileName)
        frame1 = pd.read_csv(filePath)
        
    # select a subset of columns
    frame1 = frame1[["Year","Month","Cottagecheese.Prod","Icecream.Prod","Milk.Prod"]]
        
    #filter and add a column to show totals for August
    frame1 = frame1[frame1["Month"]=="Aug"]
    frame1["Total.prod"] = frame1["Cottagecheese.Prod"]+frame1["Icecream.Prod"]+frame1["Milk.Prod"]
    
    return frame1