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

from __future__ import division

import os
import datetime
import matplotlib.pyplot as plt #pour plotter
import openfisca_france
openfisca_france.init_country()

from openfisca_core.simulations import ScenarioSimulation


# destination_dir = "c:/users/utilisateur/documents/"
# fname_all = "aggregates_inflated_loyers.xlsx"
# fname_all = os.path.join(destination_dir, fname_all)

def test_case(year, save = False):

    country = 'france'
    salaires_nets = 40000
    nmen = 6 #nombre de ménages que je fait varier

    for reforme in [False, True]: #fais tourner un fois pour faux et une fois pour vrai
        simulation = ScenarioSimulation()
        simulation.set_config(year = year,
                              reforme = reforme,
                              nmen = nmen,
                              maxrev = salaires_nets,
                              x_axis = 'sali')

        # Adding a husband/wife on the same tax sheet (foyer)
        simulation.scenario.addIndiv(1, datetime.date(1975, 1, 1), 'conj', 'part')
    #     simulation.scenario.addIndiv(2, datetime(2000,1,1).date(), 'pac', 'enf')
    #     simulation.scenario.addIndiv(3, datetime(2000,1,1).date(), 'pac', 'enf')

        # Loyers set statut d'occupation
        simulation.scenario.menage[0].update({"loyer": 2000}) #fixe les variables au niveau du ménage
        simulation.scenario.menage[0].update({"so": 4}) #

        simulation.set_param() #va chercher des params de la législation
        simulation.P.ir.autre.charge_loyer.active = 1  #simulation.p est un attribu de simulation
        simulation.P.ir.autre.charge_loyer.plaf = 1000
        simulation.P.ir.autre.charge_loyer.plaf_nbp = 0
        print simulation.P #montre ce qui est écrit dans param.xml
        reduc = 0
        print simulation.P.ir.bareme #change le barème de l'impot sur le revenu
        print simulation.P.ir.bareme.nb #nb de tranche du brarème de l'impot
        for i in range(2, simulation.P.ir.bareme.nb):
            simulation.P.ir.bareme.setSeuil(i, simulation.P.ir.bareme.seuils[i] * (1 - reduc)) #a partir de la 2nd tranche réduit les seuils des barèmes

        print simulation.P.ir.bareme #nouvea barème
        print simulation.P.ir.bareme.nb

        if simulation.reforme is True:
            df = simulation.get_results_dataframe(difference = True) # prends la différence(argument de la fonction getresultdataframe
        
        
        
            ts = df

            ts = ts.cumsum()

            ts.plot()
        
        
        
        
        
        else:
            df = simulation.get_results_dataframe()
        print df.to_string()

        # Save example to excel
        if save:
            destination_dir = "c:/users/utilisateur/documents/"
            if reforme:
                fname = destination_dir + "Trannoy_reforme_new_diff.%s" % "xlsx"
                print "Saving " + fname
                df.to_excel(fname, sheet_name = "difference")
            else:
                fname = destination_dir + "Trannoy_reforme_new.%s" % "xlsx"
                print "Saving " + fname
                df.to_excel(fname, sheet_name = "Trannoy")

                return df


if __name__ == '__main__':
#    survey_case(2010)
    test_case(2013)

    #ts = Series(randn(1000), index= sali)
    ts = df(randn(1000), index=date_range('1/1/2000', periods=1000))

    ts = ts.cumsum()

    ts.plot()
