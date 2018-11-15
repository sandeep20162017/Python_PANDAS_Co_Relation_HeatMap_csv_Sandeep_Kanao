import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def getDF(data_url, columns):#retrieve data from url, create dataframe, return it
    data = pd.read_csv(data_url, names=columns)
    return data
    
def heatMap(df):#Create Correlation df
    corr = df.corr()
    #Plot figsize
    fig, ax = plt.subplots(figsize=(10, 10))
    #Generate Color Map
    colormap = sns.diverging_palette(220, 10, as_cmap=True)
    #Generate Heat Map, allow annotations and place floats in map
    sns.heatmap(corr, cmap=colormap, annot=True, fmt=".2f")
    #Apply xticks
    plt.xticks(range(len(corr.columns)), corr.columns);
    #Apply yticks
    plt.yticks(range(len(corr.columns)), corr.columns)
    #show plot
    plt.show()

#set target
data_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"#set titles                                                          
columns = ['Sex','Length','Diameter','Height','WholeWeight', 
            'ShuckedWeight', 'VisceraWeight', 'ShellWeight', 'Rings']
df = getDF(data_url, columns)
heatMap(df)