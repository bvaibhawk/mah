import pandas as pd
import numpy as np
from pandasql import sqldf
import os


def get_section_mapping(color, clarity):  # central mapping
    data_central = pd.read_excel('miscellenious_discounts/output_files/output_extra_discounts.xlsx',
                                 sheet_name='CENTRAL')
    query_output = sqldf("select KEY from data_central where COLOR = '" + color +
                         "' and CLARITY = '" + clarity + "'")
    if len(query_output) != 0:
        return query_output['KEY'][0]
    return 0


def get_diameter_premium(shape, cut, poly, sym, fluo, size, diameter_min, diameter_max, color, clarity):
    data_diameter = pd.read_excel('miscellenious_discounts/output_files/output_extra_discounts.xlsx',
                                  sheet_name='Diameter Premiums')
    key_section = get_section_mapping(color, clarity)
    query_output = sqldf("select DISCOUNT from data_diameter where SHAPE = '" + shape
                         + "' and CUT = '" + cut
                         + "' and POLY = '" + poly
                         + "' and SYM = '" + sym
                         + "' and FLUO = '" + fluo
                         + "' and SIZE = '" + size
                         + "' and DIAMETER_MIN <= " + str(diameter_min)
                         + " and DIAMETER_MAX >= " + str(diameter_max)
                         + " and KEY_COLOR_CLARITY = " + str(key_section))
    if len(query_output) != 0:
        return query_output['DISCOUNT'][0]
    return 0


#print(get_diameter_premium('RO', 'EX', 'EX', 'EX', 'NONE', '0.35-0.399', '4.6', '4.7', 'D', 'IF'))
