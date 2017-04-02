import datetime
from flightsearch import flightsearch
from getkayak import getkayak
from getskypicker import getskypicker

def cheapflights():
    flyfrom = input("Enter departure city or airport code, e.g. Toronto or YYZ:\n")
    datefrom = input("Enter departure date and time, e.g. 2017-03-31 12:00:\n")
    flyto = input("Enter arrival city or airport code, e.g. London or LHR:\n")
    dateto = input("Enter arrival date and time, e.g. 2017-03-31 20:00:\n")
    
    flightsearch1 = flightsearch(flyfrom, datefrom, flyto, dateto)

    flights = aggregatedflights(flightsearch1)

    print(flights)
    
def aggregatedflights(flightsearch):
    kayak = getkayak(flightsearch)
    skypicker = getskypicker(flightsearch)

    aggregated = kayak

    return aggregated
    
