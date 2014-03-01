# -*- coding: utf-8 -*-


# OpenFisca -- A versatile microsimulation software
# By: OpenFisca Team <contact@openfisca.fr>
#
# Copyright (C) 2011, 2012, 2013, 2014 OpenFisca Team
# https://github.com/openfisca
#
# This file is part of OpenFisca.
#
# OpenFisca is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenFisca is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Exemple of a simple simulation

import matplotlib.pyplot as plt
import datetime

import openfisca_france
openfisca_france.init_country()

from openfisca_core.simulations import ScenarioSimulation


def get_alloc(maxrev = 30000, conj = False, nbenf = 0, zone_apl = 1, loyer_mensuel = 500, nmen = 51):

    # Creating a case_study household with one individual whose taxable income (salaire imposable, sali
    # varies from 0 to maxrev = 100000 in nmen = 3 steps
    simulation = ScenarioSimulation()
    simulation.set_config(year = 2013,
                          nmen = nmen,
                          maxrev = maxrev,
                          x_axis = 'sali')


    scenario = simulation.scenario
    if conj:
    # Adding a husband/wife on the same tax sheet (ie foyer, as conj) and of course same family (as part)
        scenario.addIndiv(1, datetime.date(1975, 1, 1), 'conj', 'part')

    for i in range(nbenf):

    # Adding 3 kids on the same tax sheet and family
        scenario.addIndiv(1 + conj + i, datetime.date(2001, 1, 1), 'pac', 'enf')

    # Add caracteristics of menage
    scenario.menage[0]['loyer'] = loyer_mensuel
    scenario.menage[0]['zone_apl'] = zone_apl

    # Set legislative parameters
    simulation.set_param()
   # print scenario
    # Compute the pandas dataframe of the household case_study
    df = simulation.get_results_dataframe()#(index_by_code= True)
    print df
    df2 = df.transpose()[['Salaires imposables', 'Revenu disponible' ,'Prestations logement' ]]
    return df2

   
#def TrannoyWesmer():
   # pass 


if __name__ == '__main__':
    
    df3 = get_alloc(loyer_mensuel = 600, zone_apl = 1, nbenf = 0 )
    
   # print df3
    
    df3['Social contribution'] = df3['Revenu disponible'] - df3['Salaires imposables']
    print df3.to_string()
    
   # df3['sc'] = df3['Social contribution'] - df3['Prestation logement']
   # print df3.to_string()
    
   # df4 = get_alloc(loyer_mensuel = 800, zone_apl = 1, nbenf = 1, conj = True )
  #  print df4.to_string()
    
    
   # df5 = df4 - df3
    
   # print  df4.describe()
    #print df5.to_string() 

    #df5.concat(df3['Salaires imposables'],df4['Prestations logement'])
    #print df5
    #df2.to_excel('/openfiscaxl/simulation1.xls')
    #df4.to_excel('/openfiscaxl/simulation1.xls')
    
    plt.figure(figsize=(10,10))
    

    p = df3.plot(['Social contribution'],['Salaires imposables'] )
    
    print type(p)
    
    #plt.plot(df3['Social contribution'], df3['Salaires imposables'])
    plt.show()
    
    