#-------------------------------------------------------------------------------
# Name:        Main
# Purpose:     application
#
# Author:      guilherme
#
# Created:     07/12/2014
# Copyright:   (c) guilherme 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
import operator

import dictionary
import city
import menu
import routes
import populate

finish = False
returnMenu = 0

c = city.City()
r = routes.Route()
cityList = {}
routeList = {}

#AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7


#-----------------------------------------#
#For test only, population automatic the vaules
#cityList = {1 :'A', 2 :'B', 3 :'C', 4 :'D', 5 : 'E'}
#routeList = populate.populateRoutes()
#-----------------------------------------#


#run aplication while user dont choose the option 'exit'
while (finish == False):
    returnMenu = menu.buildMenu(dictionary.MenuOptions, 'Menu')

    #insert city
    if returnMenu == '1':
        key = len(cityList)
        c = city.newCity()
        cityList.update({key+1 :c})

    #insert routes
    elif returnMenu == '2':
        cityOrigen = menu.buildMenu(cityList, 'Origen city')
        cityDestiny = menu.buildMenu(cityList, 'Destiny city')

        key = len(routeList)
        r = routes.newRoute(cityOrigen,cityDestiny, cityList)
        routeList.update({key+1  :r})

    #distance betweens cities
    elif returnMenu == '3':
        cityRoutes = {}
        finishCity = False

        while(finishCity == False):

            key = len(cityRoutes)

            if key >= 2:
                cont = str(raw_input("Choose another city? press 'y' for yes or 'n' for no"))
                if cont == 'y':
                    city = menu.buildMenu(cityList, 'Select a city')
                    cityRoutes.update({key+1 : cityList.get(int(city))})
                elif cont == 'n':
                    finishCity = True
                    print 'route distance: '+str(routes.distanceRoutes(cityRoutes, routeList))
                else:
                    print "\nIncorrect option, try again"
            else:
                city = menu.buildMenu(cityList, 'Select a city')
                cityRoutes.update({key+1 : cityList.get(int(city))})

    #number of routes between cities
    elif returnMenu == '4':
        r = routes.Route()
        routeFinal = {}
        cityOrigen = menu.buildMenu(cityList, 'Select origen city')
        cityDestiny = menu.buildMenu(cityList, 'Select destiny city')

        r = routes.numberOfRoutes(routeList, cityList.get(int(cityOrigen)), cityList.get(int(cityDestiny)))

        option = menu.buildMenu(dictionary.MenuRoutesStop, 'Select number of stops')

        if option == '1':
            routeFinal.update({k:v for k,v in r.iteritems() if len(v.routes) <= 4})
        elif option == '2':
            routeFinal.update({k:v for k,v in r.iteritems() if len(v.routes) == 5})
        elif option == '3':
            routeFinal.update({k:v for k,v in r.iteritems() if len(v.routes) <= 30})

        print "Number of routes from "+str(cityList.get(int(cityOrigen)))+" to "+str(cityList.get(int(cityDestiny)))+" with "+dictionary.MenuRoutesStop.get(int(option))+" stops: "+str(len(routeFinal))

    #shortest route between cities
    elif returnMenu == '5':
        r = routes.Route()
        routeFinal = {}
        cityOrigen = menu.buildMenu(cityList, 'Select origen city')
        cityDestiny = menu.buildMenu(cityList, 'Select destiny city')

        r = routes.numberOfRoutes(routeList, cityList.get(int(cityOrigen)), cityList.get(int(cityDestiny)))

        short = routes.shortestLenghtRoute(r)

        print "The shortest lenght route from "+str(cityList.get(int(cityOrigen)))+" to "+str(cityList.get(int(cityDestiny)))+" is: "+str(short)

    #finish program
    elif returnMenu == 'e':
        finish = True
    else:
        print '\nincorrect option, try again\n'







