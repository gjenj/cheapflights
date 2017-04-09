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
    
    link = skypickerlink(flightsearch)
    results = []
    
    resultendtime = time.time()
    
    result = flightresult(searchuuid = flightsearch.searchuuid, resultuuid = resultuuid, flyfrom = flightsearch.flyfrom,
                          flyto = flightsearch.flyto, datefrom = flightsearch.datefrom, dateto = flightsearch.dateto,
                          siteurl = link, site = 'Kiwi', price = '$500', resultbegintime = resultbegintime,
                          resultendtime = resultendtime)

    results.append(result)

    return results

def skypickerlink(flightsearch):
    skypicker = 'https://api.skypicker.com/flights?'
    linkdict = collections.OrderedDict()

    linkdict = {
        'flyFrom={}&': flightsearch.flyfrom,
        'to={}&': flightsearch.flyto,
        'dateFrom={}&': transformdatetime(flightsearch.datefrom, 1),
        'dateTo={}&': transformdatetime(flightsearch.dateto, 1),
        'longitudeFrom={}&': flightsearch.longitudefrom,
        'latitudeFrom={}&': flightsearch.latitudefrom,
        'radiusFrom={}&': flightsearch.radiusfrom,
        'longitudeTo={}&': flightsearch.longitudeto,
        'latitudeTo={}&': flightsearch.latitudeto,
        'radiusTo={}&': flightsearch.radiusto,
        'daysInDestinationFrom={}&': flightsearch.daysindestfrom,
        'daysInDestinationTo={}&': flightsearch.daysindestto,
        'returnFrom={}&': flightsearch.returnfrom,
        'returnTo={}&': flightsearch.returnto,
        'typeFlight={}&': '',
        'oneforcity={}&': '',
        'one_per_date={}&': '',
        'passengers={}&': '',
        'adults={}&': flightsearch.adults,
        'children={}&': flightsearch.children + flightsearch.youth,
        'infants={}&': flightsearch.infantseat + flightsearch.infantlap,
        'flyDays={}&': '',
        'onlyWorkingDays={}&': '',
        'onlyWeekends={}&': '',
        'directFlights={}&': '',
        'curr={}&': flightsearch.curr,
        'price_from={}&': flightsearch.pricefrom,
        'price_to={}&': flightsearch.priceto,
        'dtimefrom={}&': flightsearch.dtimefrom,
        'dtimeto={}&': flightsearch.dtimefrom,
        'atimefrom={}&': flightsearch.atimefrom,
        'atimeto={}&': flightsearch.atimeto,
        'returndtimefrom={}&': flightsearch.returndtimefrom,
        'returndtimeto={}&': flightsearch.returndtimeto,
        'returnatimefrom={}&': flightsearch.returnatimefrom,
        'returnatimeto={}&': flightsearch.returnatimeto,
        'stopoverfrom={}&': flightsearch.stopoverfrom,
        'stopoverto={}&': flightsearch.stopoverto,
        'limit={}&': '100',
        'sort={}&': 'price'
        }

    link = skypicker

    for key, value in linkdict.items():
        if value != '':
            link = link + key.format(value)
    
    return link

def transformdatetime(dateortime, type):
    if type == 1:
        newdate = datetime.datetime.strptime(dateortime, '%Y-%m-%d').date()
        return str(newdate.day).zfill(2) + '%2F' + str(newdate.month).zfill(2) + '%2F' + str(newdate.year)

# Below is an example of a valid URL #
'''
https://api.skypicker.com/flights?
flyFrom=CZ&
to=porto&
dateFrom=08%2F08%2F2017&
dateTo=08%2F09%2F2017&
longitudeFrom=14.0000&
latitudeFrom=50.2000&
radiusFrom=200&
longitudeTo=14.0000&
latitudeTo=50.2000&
radiusTo=200&
daysInDestinationFrom=2&
daysInDestinationTo=14&
returnFrom=08%2F08%2F2017&
returnTo=08%2F09%2F2017&
typeFlight=oneway&
oneforcity=0&
one_per_date=0&
passengers=1&
adults=1&
children=0&
infants=0&
flyDays=%5B0%2C1%2C2%2C3%2C4%2C5%2C6%5D&
onlyWorkingDays=0&
onlyWeekends=0&
directFlights=0&
partner=picky&
partner_market=us&
v=2&xml=0&
curr=EUR&
locale=en&
price_from=1&
price_to=10000&
dtimefrom=00%3A00&
dtimeto=00%3A00&
atimefrom=00%3A00&
atimeto=00%3A00&
returndtimefrom=00%3A00&
returndtimeto=00%3A00&
returnatimefrom=00%3A00&
returnatimeto=00%3A00&
stopoverfrom=00%3A00&
stopoverto=00%3A00&
booking_token=hashed%20data&
offset=0&
limit=30&
sort=price&
asc=1
'''
