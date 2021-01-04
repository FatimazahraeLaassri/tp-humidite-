import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

""" la fonction clean_data2 a un seul paramètre data de type list, elle permet de remplacer les valeurs de la listes supérieurs à 200 par la valeur nan de la bibliothèque numpy """
def clean_data2(data):
    for j in range(len(data)):
         if data[j]==200:
                data[j]=np.nan
    return data


""" la fonction save_plot_to_file prend comme paramètres : dataframe, title, start_date, end_date, nom du fichier.
elle crée une figure de 10x10 pouces, dpi100 et constituée de 3 graphes, qui ont l'axe des X en commun. elle permet d'afficher et de grapher les données d'un fichier json. elle définie 3 variables(data1, data2, data3) les listes de données de chaques labels, (label1 , label2 , label3) et time_index.
puis elle crée un objet dataframe nommée humidity_dataframe. Utilise la foncton clean_data sur les trois listes ; data1, data2, data3. extraction et stockage des valeurs de chaque data (par labels) de la dataframe dans tois variables: Values1, values2, values3. Extraction de l'index des valeurs.
Affichage sur les trois graphes, remplissage des zones par couleur,et les limites des remplissages, title de la figure, légendes des 3 graphes, yticks placées au milieu des seuils et xticks plus les labels de chacunes"""

def save_plot_to_file(dataframe, title,start_date, end_date, filename):
    pas = 0
    fig, (ax1, ax2, ax3) = plt.subplots(3,figsize=(10,10),dpi=100,sharex = True)
    data1 = dataframe['datasets'][0]['data']
    data2 = dataframe['datasets'][1]['data']
    data3 = dataframe['datasets'][2]['data']
    label1 = '1: 1m/30cm [kPa]'
    label2 = '2: 1cm/30cm [kPa]'
    label3 = '3: 1m/30cm [kPa]'
    time_index = dataframe['labels'][0]

    humidity_dataframe = pd.DataFrame(
    data={
    label1: data1,
    label2: data2,
    label3: data3,
    },
    index=time_index,
    dtype='float'
    )
    humidity_dataframe[label1]= clean_data2(data1)
    humidity_dataframe[label2]= clean_data2(data2)
    humidity_dataframe[label3]= clean_data2(data3)
    values1 = humidity_dataframe[start_date:end_date][label1].values
    values2 = humidity_dataframe[start_date:end_date][label2].values
    values3 = humidity_dataframe[start_date:end_date][label3].values 
    index = humidity_dataframe[start_date:end_date].index
    ax1.plot(index,values1, color = 'blue', alpha = 0.2)
    ax1.fill_between(x=index, y1=0, y2=15, color='red', alpha=0.2)
    ax1.fill_between(x=index, y1=15, y2=30, color='orange', alpha=0.2)
    ax1.fill_between(x=index, y1=30, y2=60, color='green', alpha=0.2)
    ax1.fill_between(x=index, y1=60, y2=100, color='yellow', alpha=0.2)
    ax1.fill_between(x=index, y1=100, y2=200, color='red', alpha=0.2)
    ax1.set_yticks([15/2,(30+15)/2,(30+60)/2,(60+100)/2,(100+200)/2])
    ax1.set_yticklabels(['saturated','too wet','perfect','plan to water','dry'])
    ax1.set_xlim([0,len(values1)])
    ax1.set_ylim([0,200])
    ax1.legend(ax1.plot(index,values1), ('1: 1m/30cm [kPa]',), loc = 'upper left')
    ax1.set_title(title)
    
    ax2.plot(index,values2, color = 'blue', alpha = 0.2)
    ax2.fill_between(x=index, y1=0, y2=15, color='red', alpha=0.2)
    ax2.fill_between(x=index, y1=15, y2=30, color='orange', alpha=0.2)
    ax2.fill_between(x=index, y1=30, y2=60, color='green', alpha=0.2)
    ax2.fill_between(x=index, y1=60, y2=100, color='yellow', alpha=0.2)
    ax2.fill_between(x=index, y1=100, y2=200, color='red', alpha=0.2)
    ax2.set_yticks([15/2,(30+15)/2,(30+60)/2,(60+100)/2,(100+200)/2])
    ax2.set_yticklabels(['saturated','too wet','perfect','plan to water','dry'])
    ax2.set_xlim([0,len(values2)])
    ax2.set_ylim([0,200])
    ax2.legend(ax2.plot(index,values2), ('2: 1cm/30cm [kPa]',), loc = 'upper left')
    
    ax3.plot(index,values3, color = 'blue', alpha = 0.2)
    ax3.fill_between(x=index, y1=0, y2=15, color='red', alpha=0.2)
    ax3.fill_between(x=index, y1=15, y2=30, color='orange', alpha=0.2)
    ax3.fill_between(x=index, y1=30, y2=60, color='green', alpha=0.2)
    ax3.fill_between(x=index, y1=60, y2=100, color='yellow', alpha=0.2)
    ax3.fill_between(x=index, y1=100, y2=200, color='red', alpha=0.2)
    ax3.set_yticks([15/2,(30+15)/2,(30+60)/2,(60+100)/2,(100+200)/2])
    ax3.set_yticklabels(['saturated','too wet','perfect','plan to water','dry'])
    ax3.set_xticks([(len(values3)/7)/2,2*len(values3)/7-(len(values3)/7)/2,3*len(values3)/7-(len(values3)/7)/2,4*len(values3)/7-(len(values3)/7)/2,5*len(values3)/7-(len(values3)/7)/2,6*len(values3)/7-(len(values3)/7)/2,(7*len(values3)/7)-(len(values3)/7)/2])
    tick = []
    l = []
    l2 = []
    ind = 0
    for i in range(len(index)):
        ind = index[i][0:11]
        l.append(ind)
    l2.append(l[0])
    for j in range(len(l)): 
        if l[j] not in l2:
            l2.append(l[j])
    pas = int(len(l2)/7)
    for k in range(3,len(l2),pas):
        tick.append(l2[k]) 
    ax3.set_xticklabels(tick)
    ax3.set_xlim([0,len(values3)])
    ax3.set_ylim([0,200])
    fig.autofmt_xdate()
    ax3.legend(ax3.plot(index,values3), ('3: 1m/30cm [kPa]',), loc = 'upper left')
    plt.savefig(filename)
  
    

if __name__ == '__main__':
    with open('eco-sensors_irrigation_2020-06-01_2020-08-31.json') as fichier:
        data_dict = json.load(fichier)

    humidity_dataframe = pd.DataFrame(data_dict)
    humidity_dataframe


    save_plot_to_file(humidity_dataframe, 'irrigation June 2020','2020-06-01', '2020-06-31', 'irrigation_graph_2020-06')
    save_plot_to_file(humidity_dataframe, 'irrigation July 2020','2020-07-01', '2020-08-01', 'irrigation_graph_2020-07')
    save_plot_to_file(humidity_dataframe, 'irrigation August 2020','2020-08-01', '2020-09-01', 'irrigation_graph_2020-08')
