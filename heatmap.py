import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

#changing directory
os.chdir(r'C:\Users\micha.DESKTOP-U2HVTMF\MyPythonScripts\VSCode Workspace\SEES Data')

plt.rcParams.update({'font.size': 7}) #changing font size

#reading and creating plot
mosquito = pd.read_csv('mosquito 7-24.csv')
mosquito.head()
matrix = np.triu(mosquito.corr())
plot = sns.heatmap(mosquito.corr(), annot = True, mask=matrix, cmap= 'coolwarm')
plt.show()