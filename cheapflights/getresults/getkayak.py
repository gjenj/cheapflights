from flightsearch import flightsearch, flightresult
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import html
import uuid
import time

def getresult(flightsearch):
    PHANTOMJS_PATH = './phantomjs.exe'
    resultuuid = uuid.uuid4()
    resultbegintime = time.time()
    results = []

    link = kayaklink(flightsearch)
    #browser = webdriver.PhantomJS(PHANTOMJS_PATH)
    #browser.get(link)

    #kayak_search = BeautifulSoup(browser.page_source, "html.parser")
    #kayak_tree = html.fromstring(kayak_search.content)
    #result = str(kayak_tree.xpath('//*[@id="priceAnchor264"]/a'))
    #result = soup.find_all('tr', {'class': 'stage-finished'})
    #kayak_search = requests.get(link)
    #if kayak_search.status_code == 200:
        #kayak_tree = html.fromstring(kayak_search.content)
        #result = kayak_search.content #str(kayak_tree.xpath('/html/body/table/tbody/tr[1]/td[2]/text()'))
        #//*[@id=""]/a
        #//*[@id="priceAnchor160"]/a
        #//*[@id="content_div"]/div[6]/div/div/div[1]/div[1]
        #//*[@id="infolink478"]/div[2]/div[2]/div[4]/div[1]/div[2]
        #/html/body/table/tbody/tr[2284]/td[2]/text()
        #/html/body/table/tbody/tr[1692]/td[2]/text()

    resultendtime = time.time()
    result = flightresult(searchuuid = flightsearch.searchuuid, resultuuid = resultuuid, flyfrom = flightsearch.flyfrom,
                          flyto = flightsearch.flyto, datefrom = flightsearch.datefrom, dateto = flightsearch.dateto,
                          site = 'Kayak', siteurl = link, price = '$600', resultbegintime = resultbegintime, resultendtime = resultendtime)

    results.append(result)
    
    return results

def kayaklink(flightsearch):
    kayak = 'https://www.ca.kayak.com/flights/'

    link = kayak + \
        flightsearch.flyfrom + \
        '-' + \
        flightsearch.flyto + \
        '/' + \
        flightsearch.datefrom + \
        '/' + \
        flightsearch.dateto + \
        '/' + \
        str(flightsearch.adults) + \
        'adults' + \
        getclasslink(flightsearch.fclass) + \
        getchildrenlink(flightsearch.youth, flightsearch.children,
                        flightsearch.infantseat, flightsearch.infantlap)

    return link

def getchildrenlink(youth, children, infantseat, infantlap):
    if youth + children + infantseat + infantlap == 0:
        return ''
    else:
        childlink = '/children'

    for i in range (0, youth):
        childlink = childlink + '-17'
    for i in range (0, children):
        childlink = childlink + '-11'
    for i in range (0, infantseat):
        childlink = childlink + '-1S'
    for i in range (0, infantlap):
        childlink = childlink + '-1l'

    return childlink

def getclasslink(fclass):
    if fclass == 1:
        return '/first'
    elif fclass == 2:
        return '/business'
    elif fclass == 3:
        return '/premium'
    else:
        return '/economy'
