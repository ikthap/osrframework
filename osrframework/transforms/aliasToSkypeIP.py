# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2015 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################


import sys
import json
from osrframework.transforms.lib.maltego import *
import osrframework.thirdparties.resolvethem_com.processing as resolvethem_com

def aliasToSkypeIP(query=None):
    ''' 
        Method that checks if a given alias appears in Skype.

        :param query:    query to verify.

    '''
    me = MaltegoTransform()

    jsonData = resolvethem_com.checkIPFromAlias(alias=query)

    newEntities = []

    # Checking if something has been found
    if jsonData != {}:
        newEntities.append(jsonData)

    me.addListOfEntities(newEntities)
        
    # Returning the output text...
    me.returnOutput()

if __name__ == "__main__":
    aliasToSkypeIP(query=sys.argv[1])

