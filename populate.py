#-------------------------------------------------------------------------------
# Name:        Populate
# Purpose:      poulate routes automaty for tests
#
# Author:      guilherme coelho
#
# Created:     08/12/2014
# Copyright:   (c) 34506100824 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import city
import routes

#populate routes
def populateRoutes():
    #AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
    cityList = {1 :'A', 2 :'B', 3 :'C', 4 :'D', 5 : 'E'}
    routeList = {}

    c = city.City()
    r = routes.Route()

    r = routes.Route()

    #AB5
    r.cityOrigen = cityList.get(1)
    r.cityDestiny = cityList.get(2)
    r.distance = 5

    routeList.update({1 : r})

    #BC4
    r = routes.Route()
    r.cityOrigen = cityList.get(2)
    r.cityDestiny = cityList.get(3)
    r.distance = 4

    routeList.update({2 : r})

    #CD8
    r = routes.Route()
    r.cityOrigen = cityList.get(3)
    r.cityDestiny = cityList.get(4)
    r.distance = 8

    routeList.update({3 : r})

    #DC8
    r = routes.Route()
    r.cityOrigen = cityList.get(4)
    r.cityDestiny = cityList.get(3)
    r.distance = 8

    routeList.update({4 : r})

    #DE6
    r = routes.Route()
    r.cityOrigen = cityList.get(4)
    r.cityDestiny = cityList.get(5)
    r.distance = 6

    routeList.update({5 : r})

    #AD5
    r = routes.Route()
    r.cityOrigen = cityList.get(1)
    r.cityDestiny = cityList.get(4)
    r.distance = 5

    routeList.update({6 : r})

    #CE2
    r = routes.Route()
    r.cityOrigen = cityList.get(3)
    r.cityDestiny = cityList.get(5)
    r.distance = 2

    routeList.update({7 : r})

    #EB3
    r = routes.Route()
    r.cityOrigen = cityList.get(5)
    r.cityDestiny = cityList.get(2)
    r.distance = 3

    routeList.update({8 : r})

    #AE7
    r = routes.Route()
    r.cityOrigen = cityList.get(1)
    r.cityDestiny = cityList.get(5)
    r.distance = 7

    routeList.update({9 : r})

    return routeList