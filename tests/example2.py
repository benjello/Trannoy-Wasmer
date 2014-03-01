# -*- coding: utf-8 -*-

'''
Created on 13 févr. 2014

@author: p702207
'''


import datetime
from openfisca_core import model
import openfisca_france
openfisca_france.init_country()
from openfisca_core.simulations import ScenarioSimulation

def case_study(year = 2013):
    simulation = ScenarioSimulation()  #on instancie on prends une instance de ScenarioSimulation, on prends un exemple de cette classe là
    simulation.set_config(year = year, 
                    nmen = 4, #nombre de ménages
                    maxrev = 10000, 
                    x_axis = 'sali')#salaire imposable (une seule personne dans le ménage)

    simulation.set_param()#prends les paramètres par défaut de la législation
    df = simulation.get_results_dataframe() #renvoie la dataframe avec tout calculé
    print df.to_string()
    
    
def case_study2(year=2013):
    simulation = ScenarioSimulation()  #on instancie on prends une instance de ScenarioSimulation, on prends un exemple de cette classe là
    simulation.set_config(year = year, 
                    nmen = 8, #nombre de ménages
                    maxrev = 10000, 
                    x_axis = 'sali')#salaire imposable (une seule personne dans le ménage)
    #print simulation.scenario
    
    simulation.scenario.addIndiv(1, datetime.date(1975, 1 ,1), 'conj', 'part')
   

    simulation.set_param()#prends les paramètres par défaut de la législation
    df = simulation.get_results_dataframe(index_by_code=True) #renvoie la dataframe avec tout calculé
    
 
    print df.to_string()
    #print df.transpose()['logt']
    
    a = df.loc['sal'] 
    print a
    
    #print df.loc['logt']
    
    
    #print simulation.output_table.table.to_string()
    
if __name__== '__main__' :
    case_study2()
    
    import pylab, numpy
    x = numpy.linspace(-10,10,100)
    
    y = x **2

    pylab.plot (x,y)

    pylab.show()      

