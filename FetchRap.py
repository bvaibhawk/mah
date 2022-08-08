import pandas as pd
from pandasql import sqldf


def fetchrap(shape, szgr, color, clarity):
    if shape == 'RO':
        shape = 'BR'
    pysqldf = lambda q: sqldf(q, globals())
    rapsheet = pd.read_csv('rap_price.csv')
    szlist = list(map(str, szgr.strip().split('-')))
    szmin = szlist[0]
    szmax = szlist[1]
    rap = sqldf(
        "select RAP from rapsheet as r where r.shape = '" + shape + "' and r.colour = '" + color + "' and r.clarity = '" + clarity + "'"
        " and r.size_range_min <= " + szmin + " and r.size_range_max >= " + szmax + " limit 1")
    if len(rap) == 0:
        return 0
    else:
        return rap['RAP'][0]
