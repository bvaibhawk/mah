import pandas as pd
from pandasql import sqldf


def fetchrap(shape, szgr, color, clarity, sizeprec):
    if shape == 'RO':
        shape = 'BR'
        rapsheet = pd.read_csv('rap_price_round.csv')
    else:
        shape = 'PS'
        rapsheet = pd.read_csv('rap_price_fancy.csv')
    if color == 'N':
        color = 'M'
    pysqldf = lambda q: sqldf(q, globals())
    szlist = list(map(str, szgr.strip().split('-')))
    szmin = 0
    szmax = 0
    if len(szlist) == 2:
        szmin = szlist[0]
        szmax = szlist[1]
    rap = sqldf(
        "select RAP as RAP from rapsheet as r where r.shape = '" + str(shape) + "' and r.colour = '" + str(
            color) + "' and r.clarity = '" + str(clarity) + "'"
                                                            " and r.size_range_min <= " + str(
            sizeprec) + " and r.size_range_max >= " + str(sizeprec) + " limit 1")
    if len(rap) == 0:
        return 0
    else:
        return rap['RAP'][0]


def fetch_size(shape, sizeprec):
    if shape == 'RO':
        size_range_ro = pd.read_csv('size_range_round.csv')
        for i in range(len(size_range_ro['ROUND'])):
            k = size_range_ro['ROUND'][i]
            szlist = list(map(float, k.strip().strip("'").split('-')))
            szmin = szlist[0]
            szmax = szlist[1]
            if szmin <= sizeprec <= szmax:
                return size_range_ro['VAL'][i].strip().strip("'")
    else:
        size_range_fn = pd.read_csv('size_range_fancy.csv')
        for i in size_range_fn['FANCY']:
            szlist = list(map(float, i.strip().strip("'").split('-')))
            szmin = szlist[0]
            szmax = szlist[1]
            if szmin <= sizeprec <= szmax:
                return i.strip().strip("'")
