# -*- coding: utf-8 -*-

'''
Created on 13 févr. 2014

@author: p702207
'''


from datetime import datetime
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
    
if __name__== '__main__' :
    print "toto"
    case_study()
    