from flightsearch import flightsearch, flightresult
import requests
import lxml
import datetime
import collections
import uuid
import time

def getresult(flightsearch):
    resultuuid = uuid.uuid4()
    resultbegintime = time.time()
    results = []

    link = sitelink(flightsearch)

    resultendtime = time.time()
    result = flightresult(searchuuid = flightsearch.uuid, resultuuid = resultuuid, flyfrom = flightsearch.flyfrom
                          flyto = flightsearch.flyto, datefrom = flightsearch.datefrom, dateto = flightsearch.dateto
                          site = 'sitename', siteurl = link, price = '$0.00', resultbegintime = resultbegintime,
                          resultendtime = resultendtime)

    results.append(result)

    return result

def sitelink(flightsearch):
    site = 'https://examplesite.com'
    linkdict = collections.OrderedDict()

    linkdict = {
        ## Set site search variables here. Example:
        # 'flyFrom={}&': flightsearch.flyfrom,
        # 'to={}&': flightsearch.flyto
        }

    link = site

    for key, value in linkdict.items():
        if value != '':
            link = link + key.format(value)
    
    return link
