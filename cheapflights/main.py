## Adding ./getresults to the Python path so that the modules in folder can be imported
import sys
sys.path.insert(0, './getresults')

import datetime
from flightsearch import flightsearch, flightresult
import os
import uuid
import time
from pprint import pprint

def main():
    flyfrom = 'YYZ' #input("Enter departure city or airport code, e.g. Toronto or YYZ:\n")
    datefrom = '2017-04-26' #input("Enter departure date and time, e.g. 2017-03-31 12:00:\n")
    flyto = 'LHR' #input("Enter arrival city or airport code, e.g. London or LHR:\n")
    dateto = '2017-05-26' #input("Enter arrival date and time, e.g. 2017-03-31 20:00:\n")

    searchuuid = uuid.uuid4()
    searchbegintime = time.time()
    
    search = flightsearch(searchuuid = searchuuid, searchbegintime = searchbegintime, flyfrom = flyfrom,
                          datefrom = datefrom, flyto = flyto, dateto = dateto)
    results = aggregatedflights(search)

    search.searchendtime = time.time()

    for key, value in results.items():
        for item in value:
            pprint(vars(item))

## This function aggegates the various results obtained from the modules in the ./getresults folder
def aggregatedflights(flightsearch):
    getresultsdir = './getresults'
    resultdict = {}

    for filename in os.listdir(getresultsdir):
        if filename.startswith("get") and filename.endswith(".py"):
            modulename = filename.split('.')[0]
            mod = __import__(modulename)
            resultdict[modulename] = mod.getresult(flightsearch)
        else:
            continue

    return sortbyprice(resultdict)

def sortbyprice(flightresult):
    ## Coming soon
    return flightresult
    
if __name__ == '__main__':
    main()
