#-------------------------------------------------------------------------------
# Name:        Routes
# Purpose:      define classes and functions for Route
#
# Author:      guilherme
#
# Created:     06/12/2014
# Copyright:   (c) guilherme 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Cities:
    def __init(cityOrigen,cityOrigenKey, cityDestiny, cityDestinyKey):
        self.cityOrigen = cityOrigen
        self.cityOrigenKey = cityOrigenKey
        self.cityDestiny = cityDestiny
        self.cityDestinyKey = cityDestinyKey
    pass

class Route(Cities):
    def __init( distance, routes):
        self.distance= distance
        self.routes = routes
    pass

#create a new route
def newRoute(cityOrigen,cityDestiny, cityList):
    r = Route()

    r.cityOrigen = cityList.get(int(cityOrigen))
    r.cityOrigenKey = int(cityList.keys()[cityList.values().index(r.cityOrigen)])

    r.cityDestiny = cityList.get(int(cityDestiny))
    r.cityDestinyKey = int(cityList.keys()[cityList.values().index(r.cityDestiny)])

    r.distance = int(raw_input("Distance: "))

    return r

#return the distance between cities
def distanceRoutes(cityRoutes, routeList):
   sum = 0
   existRoute = False

   for i, v in cityRoutes.iteritems():
        origen = cityRoutes.get(i)

        keyDestiny = i + 1
        destiny = cityRoutes.get(keyDestiny)

        if destiny:
            existRoute = False
            for j, x in routeList.iteritems():
                if origen == x.cityOrigen and  destiny == x.cityDestiny:
                    sum += x.distance
                    existRoute = True
   if existRoute == False:
        return 'NO SUCH ROUTE'
   else:
        return sum

#return the possibles routes between two cities
def numberOfRoutes(routeList, origen, destiny):
    final ={}
    startCity = {}
    finishCity = {}
    key = 0
    convert = ''
    r = Route()

    startCity.update({k:v for k,v in routeList.iteritems() if v.cityOrigen == origen})

    for i, j in startCity.iteritems():
        finishCity.update({k:v for k,v in routeList.iteritems() if v.cityOrigen == j.cityDestiny})
        for k, l in finishCity.iteritems():
            stepOne ={}
            if j.cityDestiny == l.cityOrigen:
                if l.cityDestiny == destiny:
                    r = Route()
                    r.routes = str(j.cityOrigen+''+ l.cityOrigen+''+ l.cityDestiny)
                    r.distance = j.distance + l.distance
                    key += 1
                    final.update({key : r})
                #two stops
                stepOne.update({k:v for k,v in routeList.iteritems() if v.cityOrigen == l.cityDestiny})
                for x, y in stepOne.iteritems():
                    stepTwo = {}
                    if l.cityDestiny == y.cityOrigen:
                        if y.cityDestiny == destiny:
                            r = Route()
                            r.routes = str(j.cityOrigen+''+ l.cityOrigen+''+ y.cityOrigen+''+ y.cityDestiny)
                            r.distance = j.distance + l.distance + y.distance
                            key += 1
                            final.update({key : r})
                        #four stops
                        stepTwo.update({k:v for k,v in routeList.iteritems() if v.cityOrigen == y.cityDestiny})
                        for z, a in stepTwo.iteritems():
                            stepThree ={}
                            if y.cityDestiny == a.cityOrigen:
                                if a.cityDestiny == destiny:
                                    r = Route()
                                    r.routes = str(j.cityOrigen+''+ l.cityOrigen+''+ y.cityOrigen+''+ a.cityOrigen+''+a.cityDestiny)
                                    r.distance = j.distance + l.distance + y.distance + a.distance
                                    key += 1
                                    final.update({key : r})
                                #five stops
                                stepThree.update({k:v for k,v in routeList.iteritems() if v.cityOrigen == a.cityDestiny})
                                for w, b in stepThree.iteritems():
                                    stepFour ={}
                                    if a.cityDestiny == b.cityOrigen:
                                        if b.cityDestiny == destiny:
                                            r = Route()
                                            r.routes = str(j.cityOrigen+''+ l.cityOrigen+''+ y.cityOrigen+''+ a.cityOrigen+''+ b.cityOrigen+''+b.cityDestiny)
                                            r.distance = j.distance + l.distance + y.distance + a.distance + b.distance
                                            key += 1
                                            final.update({key : r})
                                        #six stops
                                        stepFour.update({k:v for k,v in routeList.iteritems() if v.cityOrigen == b.cityDestiny})
                                        for x, c in stepFour.iteritems():
                                            stepFive ={}
                                            if c.cityDestiny == b.cityOrigen:
                                                if b.cityDestiny == destiny:
                                                    r = Route()
                                                    r.routes = str(j.cityOrigen+''+ l.cityOrigen+''+ y.cityOrigen+''+ a.cityOrigen+''+ b.cityOrigen+''+ c.cityOrigen+''+c.cityDestiny)
                                                    r.distance = j.distance + l.distance + y.distance + a.distance + b.distance + c.distance
                                                    key += 1
                                                    final.update({key : r})
                                                #seven stops
                                                stepFive.update({k:v for k,v in routeList.iteritems() if v.cityOrigen == c.cityDestiny})
                                                for u, d in stepFive.iteritems():
                                                    stepSix ={}
                                                    if c.cityDestiny == d.cityOrigen:
                                                        if d.cityDestiny == destiny:
                                                            r = Route()
                                                            r.routes = str(j.cityOrigen+''+ l.cityOrigen+''+ y.cityOrigen+''+ a.cityOrigen+''+ b.cityOrigen+''+ c.cityOrigen+''+d.cityOrigen+''+d.cityDestiny)
                                                            r.distance = j.distance + l.distance + y.distance + a.distance + b.distance + c.distance + d.distance
                                                            key += 1
                                                            final.update({key : r})
                                                     #eight stops
                                                    stepSix.update({k:v for k,v in routeList.iteritems() if v.cityOrigen == d.cityDestiny})
                                                    for we, e in stepSix.iteritems():
                                                        stepSeven ={}
                                                        if d.cityDestiny == e.cityOrigen:
                                                            if e.cityDestiny == destiny:
                                                                r = Route()
                                                                r.routes = str(j.cityOrigen+''+ l.cityOrigen+''+ y.cityOrigen+''+ a.cityOrigen+''+ b.cityOrigen+''+ c.cityOrigen+''+d.cityOrigen+''+e.cityOrigen+''+e.cityDestiny)
                                                                r.distance = j.distance + l.distance + y.distance + a.distance + b.distance + c.distance + d.distance + e.distance
                                                                key += 1
                                                                final.update({key : r})
                                                        #nine stops
                                                        stepSeven.update({k:v for k,v in routeList.iteritems() if v.cityOrigen == e.cityDestiny})
                                                        for wf, f in stepSeven.iteritems():
                                                            stepEight ={}
                                                            if e.cityDestiny == f.cityOrigen:
                                                                if f.cityDestiny == destiny:
                                                                    r = Route()
                                                                    r.routes = str(j.cityOrigen+''+ l.cityOrigen+''+ y.cityOrigen+''+ a.cityOrigen+''+ b.cityOrigen+''+ c.cityOrigen+''+d.cityOrigen+''+e.cityOrigen+''+f.cityOrigen+''+f.cityDestiny)
                                                                    r.distance = j.distance + l.distance + y.distance + a.distance + b.distance + c.distance + d.distance + e.distance + f.distance
                                                                    key += 1
                                                                    final.update({key : r})
                                                            #ten stops
                                                            stepEight.update({k:v for k,v in routeList.iteritems() if v.cityOrigen == f.cityDestiny})
                                                            for wg, g in stepEight.iteritems():
                                                                stepNine ={}
                                                                if f.cityDestiny == g.cityOrigen:
                                                                    if g.cityDestiny == destiny:
                                                                        r = Route()
                                                                        r.routes = str(j.cityOrigen+''+ l.cityOrigen+''+ y.cityOrigen+''+ a.cityOrigen+''+ b.cityOrigen+''+ c.cityOrigen+''+d.cityOrigen+''+e.cityOrigen+''+f.cityOrigen+''+g.cityOrigen+''+g.cityDestiny)
                                                                        r.distance = j.distance + l.distance + y.distance + a.distance + b.distance + c.distance + d.distance + e.distance + f.distance + g.distance
                                                                        key += 1
                                                                        final.update({key : r})

    return final

#return the shortest distance from the routes
def shortestLenghtRoute(routeList):
    listRoutes = list()
    for k, v in routeList.items():
        listRoutes.append(v.distance)
    listRoutes.sort
    return listRoutes[0]