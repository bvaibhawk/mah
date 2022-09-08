import math

import pandas as pd
import numpy as np
from pandasql import sqldf


def write_excel(filename, sheet_name, dataframe):
    with pd.ExcelWriter(filename, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        workBook = writer.book
        try:
            workBook.remove(workBook[sheet_name])
            writer.save()
        except:
            print("Worksheet does not exist")
            writer.save()
    with pd.ExcelWriter(filename, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        dataframe.to_excel(writer, sheet_name=sheet_name, index=False)
        writer.save()


def central_mapping():
    clarity_color_mapping = pd.read_excel('input_files/input_price_module_discounts.xlsm', sheet_name='Central',
                                          usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9])

    clarity_cut_dict = {'COLOR': [], 'CLARITY': [], 'KEY': []}

    for i in range(2, 12):
        for j in range(1, len(clarity_color_mapping.columns)):
            clarity_cut_dict['COLOR'].append(clarity_color_mapping.iloc[i, 0])
            clarity_cut_dict['CLARITY'].append(clarity_color_mapping.iloc[1, j])
            clarity_cut_dict['KEY'].append(clarity_color_mapping.iloc[i, j])
    output_df = pd.DataFrame.from_dict(clarity_cut_dict)
    write_excel('output_files/output_extra_discounts.xlsx', 'CENTRAL', output_df)


def diameter_premium():
    data = pd.read_excel('input_files/input_price_module_discounts.xlsm', sheet_name='Diameter Premiums',
                         usecols=[16, 17, 18, 19, 20])
    data_grt_one = pd.read_excel('input_files/input_price_module_discounts.xlsm', sheet_name='Diameter Premiums',
                                 usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    central_map = pd.read_excel('output_files/output_extra_discounts.xlsx', sheet_name='CENTRAL')
    diameter_dict = {'SHAPE': [], 'CUT': [], 'POLY': [], 'SYM': [], 'FLUO': [],
                     'SIZE': [], 'DIAMETER_MIN': [], 'DIAMETER_MAX': [], 'KEY_COLOR_CLARITY': [], 'DISCOUNT': []}

    for i in range(6, 12):
        for j in range(1, len(data.columns)):
            for k in ['NONE', 'FAINT']:
                diameter_dict['SHAPE'].append('RO')
                diameter_dict['CUT'].append('EX')
                diameter_dict['POLY'].append('EX')
                diameter_dict['SYM'].append('EX')
                diameter_dict['FLUO'].append(k)
                diameter_dict['SIZE'].append(data.iloc[4, j])
                diameter = str(data.iloc[5, j])
                diameter = diameter.replace('m', '')
                if diameter[0] == '>' or diameter[0] == '+':
                    diameter_dict['DIAMETER_MAX'].append(100000.0)
                    diameter_dict['DIAMETER_MIN'].append(float(diameter[1:]))
                elif diameter[0] == '<' or diameter[0] == '-':
                    diameter_dict['DIAMETER_MAX'].append(float(diameter[1:]))
                    diameter_dict['DIAMETER_MIN'].append(0)
                color = str(data.iloc[i, 0]).split('/')[0]
                clarity = str(data.iloc[i, 0]).split('/')[1]
                key_col_clar = 0
                key_color_clarity = sqldf("select KEY from central_map "
                                          "where COLOR = '" + color + "' and CLARITY = '" + clarity + "'")
                if len(key_color_clarity) != 0:
                    key_col_clar = key_color_clarity['KEY'][0]
                diameter_dict['KEY_COLOR_CLARITY'].append(key_col_clar)
                diameter_dict['DISCOUNT'].append(data.iloc[i, j])
                # print(data.iloc[i, j], data.iloc[i, 0], data.iloc[5, j], data.iloc[4, j])

    size_grt_than_one = data_grt_one.iloc[3, 0]
    for i in range(3, len(data_grt_one)):
        for j in range(5, len(data_grt_one.columns)):
            if not pd.isnull(data_grt_one.iloc[i, j]):
                for k in ['NONE', 'FAINT']:
                    diameter_dict['SHAPE'].append('RO')
                    for cut_loc in range(i, -1, -1):
                        if not pd.isnull(data_grt_one.iloc[cut_loc, 1]):
                            diameter_dict['CUT'].append(data_grt_one.iloc[cut_loc, 1])
                            break
                    diameter_dict['POLY'].append('')
                    diameter_dict['SYM'].append('')
                    diameter_dict['FLUO'].append(k)
                    diameter_dict['SIZE'].append(size_grt_than_one)
                    diameter = str(data_grt_one.iloc[i, 4])
                    diameter = diameter.replace('m', '').strip()
                    if diameter[0] == '>' or diameter[0] == '+':
                        diameter_dict['DIAMETER_MAX'].append(100000.0)
                        diameter_dict['DIAMETER_MIN'].append(float(diameter[1:]))
                    elif diameter[0] == '<' or diameter[0] == '-':
                        diameter_dict['DIAMETER_MAX'].append(float(diameter[1:]))
                        diameter_dict['DIAMETER_MIN'].append(0)
                    diameter_dict['KEY_COLOR_CLARITY'].append(data_grt_one.iloc[2, j])
                    diameter_dict['DISCOUNT'].append(data_grt_one.iloc[i, j])
    output_df = pd.DataFrame.from_dict(diameter_dict)
    write_excel('output_files/output_extra_discounts.xlsx', 'Diameter Premiums', output_df)


# central_mapping()
diameter_premium()
