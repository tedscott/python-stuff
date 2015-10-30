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
    
    # The script MUST contain a function named azureml_main
# which is the entry point for this module.
#
# The entry point function can contain up to two input arguments:
#   Param<dataframe1>: a pandas.DataFrame
#   Param<dataframe2>: a pandas.DataFrame
def azureml_main(frame1):
    import matplotlib
    matplotlib.use('agg')
    import pandas as pd
    import matplotlib.pyplot as plt
    from pandas.tools.plotting import scatter_matrix
    
    ## remove unwanted columns
    frame1.drop(["X","Y","month","day"], axis=1, inplace=True)
    
    ## create a scatter plot matrix
    fig1=plt.figure(1,figsize=(12,9))
    ax=fig1.gca()
    scatter_matrix(frame1, alpha=0.2, figsize=(10,10),diagonal='kde',ax=ax)
    fig1.savefig('scatter.png')


    
    # Return value must be of a sequence of pandas.DataFrame
    return frame1


    