class flightsearch():

    def __init__(self, flyfrom, datefrom, flyto='', dateto='', returnfrom='',returnto='',
                 adults=1, youth=0, children=0, infantseat=0, infantlap=0, fclass=4,
                 curr='CAD', dtimefrom='', dtimeto='', atimefrom='', atimeto='',
                 returndtimefrom='', returndtimeto='', returnatimefrom='', returnatimeto='',
                 longitudefrom='', latitudefrom='',radiusfrom='',longitudeto='',latitudeto='',radiusto='',
                 daysindestfrom='', daysindestto='', stopoverfrom='', stopoverto='', pricefrom='',
                 priceto=''):
        self.flyfrom = flyfrom
        self.datefrom = datefrom
        self.flyto = flyto
        self.dateto = dateto
        self.returnfrom = returnfrom
        self.returnto = returnto
        self.adults = adults
        self.youth = youth
        self.children = children
        self.infantseat = infantseat
        self.infantlap = infantlap
        self.fclass = fclass
        self.curr = curr
        self.dtimefrom = dtimefrom
        self.dtimeto = dtimeto
        self.atimefrom = atimefrom
        self.atimeto = atimeto
        self.returndtimefrom = returndtimefrom
        self.returndtimeto = returndtimeto
        self.returnatimefrom = returnatimefrom
        self.returnatimeto = returnatimeto
        self.longitudefrom = longitudefrom
        self.latitudefrom = latitudefrom
        self.radiusfrom = radiusfrom
        self.longitudeto = longitudeto
        self.latitudeto = latitudeto
        self.radiusto = radiusto
        self.daysindestfrom = daysindestfrom
        self.daysindestto = daysindestto
        self.stopoverfrom = stopoverfrom
        self.stopoverto = stopoverto
        self.pricefrom = pricefrom
        self.priceto = priceto

    def __del__(self):
        class_name = self.__class__.__name__
