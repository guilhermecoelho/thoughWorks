#-------------------------------------------------------------------------------
# Name:        Menu
# Purpose:     generate the menus
#
# Author:      guilherme
#
# Created:     06/12/2014
# Copyright:   (c) guilherme 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#build menus
def buildMenu(MenuOptions, header):
    isOk = False

    while (isOk == False):
        print '\n'+header+':\n'
        for i, v in MenuOptions.iteritems():
                print i, v

        result = str(raw_input("Choose an option:"))

        try:
            isOk = MenuOptions.has_key(int(result))
        except:
            isOk = MenuOptions.has_key(result)

        if isOk == False:
            print '\nIncorrect option, try again'
        else:
            return str(result)
