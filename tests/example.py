# -*- coding: utf-8 -*-

'''
Created on 13 févr. 2014

@author: p702207
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import matplotlib.pyplot as plt
from datetime import datetime
from openfisca_core import model
import openfisca_france
openfisca_france.init_country()
from openfisca_core.simulations import ScenarioSimulation

def case_study(year = 2013):
    simulation = ScenarioSimulation()  #on instancie on prends une instance de ScenarioSimulation, on prends un exemple de cette classe là
    simulation.set_config(year = year, 
                    nmen = 500, #nombre de ménages
                    maxrev = 100000, 
                    x_axis = 'sali')#salaire imposable (une seule personne dans le ménage)
    simulation.set_param()#prends les paramètres par défaut de la législation
    df = simulation.get_results_dataframe() #renvoie la dataframe avec tout calculé
    #print df.to_string()
    return df
if __name__== '__main__' :
    print "toto"
    df1 = case_study()
    
    df = df1.transpose()
    plt.figure()
    
    #p = df.plot()
    
    #print type(p)
    
    df.plot(legend=False)
    
    #plt.legend(False)
    plt.plot(  df['Salaires imposables'], df['Revenu disponible'])
    
    plt.show()