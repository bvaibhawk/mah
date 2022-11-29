import math
import numpy as np
import time
import streamlit as st
import traceback
import logging
import dill as pickle
import pandas as pd
import cv2
from datetime import date, datetime
# from Discount import calcDiscount, get_cut_comments
from Discount import calcDiscount, round_05
from FetchRap import fetchrap, fetch_size
from days_discount_upload import page4
from price_module_upload import page3
from singlediscount import page2
import warnings
from sys import platform

from very_strong_fl_upload import page5
from price_module_history import page6
from individual_history import page7
from upload_sheet import page8



def match(a: str, b: str):
    return a.casefold() == b.casefold()

data_path = ''
if platform.startswith('linux'):
    data_path = ''
elif platform.startswith('win32'):
    data_path = ''

warnings.filterwarnings("ignore")
st.set_page_config(page_title="Discount Calculator", page_icon='💎', layout="wide",
                   initial_sidebar_state="collapsed",
                   menu_items=None)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
footer = """<style>
a:link , a:visited{
color: #006DCC;
background-color: transparent;
text-decoration: underline;
font-weight: bold;
}
a:link , a:unvisited{
color: #006DCC;
background-color: transparent;
text-decoration: underline;
font-weight: bold;
}
a:hover,  a:active {
color: #2E8BC0;
background-color: transparent;
text-decoration: underline;
font-weight: bold;
}
.footer {
position: fixed;
left: 0;
bottom: 0;
padding-top: 15px;
width: 100%;
background-color: #d4af37;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Powered by <a href = 'https://www.ripik.ai' target='_blank'>Ripik.ai</a></p>
</div>
"""

logo = cv2.imread("logo.png")
logo = cv2.cvtColor(logo, cv2.COLOR_BGR2RGB)
logo = cv2.resize(logo, (300, 100))
st.image(logo)
st.text("\n")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S', filename='discount-tool.log', filemode='w')

class ColumnError(Exception):
    pass

def column_default_validation(diamondData, col, i, defaultValue=None, no_comma=None):
    if col in diamondData.keys():
        if no_comma is None:
            return diamondData[col][i]
        else:
            return diamondData[col][i].replace(',', '')
    if defaultValue is None:
        raise ColumnError(col + ' is missing in the uploaded CSV file. ' \
                                'Please upload the CSV file in correct format')
    return float(defaultValue) if defaultValue == 0 else defaultValue

def page1():
    # with open('diamond.pkl', 'rb') as handle:
    #     model = pickle.load(handle)
    #
    # col1, col2, col3, col4, col5 = st.columns(5)
    # col6, col7, col8, col9, col10 = st.columns(5)
    # col11, col12, col13, col14, col15 = st.columns(5)
    # col16, col17, col18, col19, col20 = st.columns(5)
    # col21, col22, col23, col24, col25 = st.columns(5)
    # col26, col27, col28, col29, col30 = st.columns(5)
    # col31, col32, col33, col34, col35 = st.columns(5)
    # col36, col37, col38, col39, col40 = st.columns(5)
    # col41, col42, col43, col44, col45 = st.columns(5)
    # col46, col47, col48, col49 = st.columns(4)
    #
    # # color_dict = {"D":10,"E":9,"F":8,"G":7,"H":6,"I":5,"J":4,"K":3,"L":2,"M":1}
    # # clarity_dict = {"IF":8,"VVS1":7,"VVS2":6,"VS1":5,"VS2":4,"SI1":3,"SI2":2,"I1":1}
    # # fluo_dict = {"FNT":1,"MED":2,"NON":3,"SIG":4,"VST":5}
    #
    # dictCsv = {}
    # with col1:
    #     shape = st.selectbox("SHAPE*", options=['RO', 'CS', 'EM', 'HT', 'MAO', 'PR', 'PRINCESS', 'OV'])
    #     dictCsv['SHAPE'] = shape
    #
    # with col2:
    #     szgr = st.selectbox("SIZE RANGE*"
    #                         , options=['1.01-1.09', '1.50-1.69', '2.01-2.09', '3.01-3.09', '4.01-4.09', '5.01-5.09'])
    #     dictCsv['SIZE RANGE'] = szgr
    #
    # with col3:
    #     color = st.selectbox("COLOUR*", options=['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'])
    #     dictCsv['COLOUR'] = color
    #
    # with col4:
    #     clarity = st.selectbox("CLARITY*", options=['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'])
    #     dictCsv['CLARITY'] = clarity
    #
    # with col5:
    #     cut = st.selectbox("CUT*", options=['EX', 'GD', 'VG'])
    #     dictCsv['CUT'] = cut
    #
    # with col6:
    #     polish = st.selectbox("POLISH*", options=['EX', 'GD', 'VG'])
    #     dictCsv['POLISH'] = polish
    #
    # with col7:
    #     symmetry = st.selectbox("SYMMETRY*", options=['EX', 'GD', 'VG'])
    #     dictCsv['SYMMETRY'] = symmetry
    #
    # with col8:
    #     fluo = st.selectbox("FLUO*", options=['Faint', 'Medium', 'None', 'Strong', 'Very Strong'])
    #     dictCsv['FLUO'] = fluo
    #
    # with col9:
    #     rap = st.number_input("RAP*")
    #     dictCsv['RAP'] = rap
    #
    # with col10:
    #     ktos = st.number_input("KTOS")
    #     dictCsv['KTOS'] = ktos
    # with col11:
    #     sizeprec = st.number_input("PRECISE SIZE")
    #     dictCsv['PRECISE SIZE'] = sizeprec
    # with col12:
    #     tableclean = st.selectbox("TABLE_CLEAN", options=['Yes', 'No'])
    #     dictCsv['TABLE_CLEAN'] = tableclean
    # with col13:
    #     eyeclean = st.selectbox("EYE_CLEAN", options=['Yes', 'No'])
    #     dictCsv['EYE_CLEAN'] = eyeclean
    # with col14:
    #     ha = st.selectbox("H&A", options=['Yes', 'No'])
    #     dictCsv['H&A'] = ha
    # with col15:
    #     cutcomments = st.selectbox("CUT_COMMENTS",
    #                                options=['0', '3EX->EX1', '3EX->EX2', 'EX->EX1', 'EX->EX2', 'VG->VG1', 'VG->VG2',
    #                                         'G->GD1', 'G->GD2', 'Fancy->Ideal', 'Fancy->Premium', 'Fancy->Very Good'])
    #     dictCsv['CUT_COMMENTS'] = cutcomments
    # with col16:
    #     diameter = st.number_input("DIAMETER")
    #     dictCsv['DIAMETER'] = diameter
    # with col17:
    #     internalgraining = st.selectbox("INTERNAL_GRAINING", options=['0', 'NN', 'IGR1', 'IGR2', 'IGR3'])
    #     dictCsv['INTERNAL_GRAINING'] = internalgraining
    # with col18:
    #     surfacegraining = st.selectbox("SURFACE_GRAINING", options=['0', 'NN', 'SGR1', 'SGR2', 'SGR3'])
    #     dictCsv['SURFACE_GRAINING'] = surfacegraining
    # with col19:
    #     pavilionintensity = st.selectbox("PAVILION_INTENSITY_needless", options=[0, 1, 2, 3, 4])
    #     dictCsv['PAVILION_INTENSITY_needless'] = pavilionintensity
    # with col20:
    #     tableintensity = st.selectbox("TABLE_INTENSITY", options=['NN', 'BT1+', 'BT1', 'BT2', 'BT3'])
    #     dictCsv['TABLE_INTENSITY'] = tableintensity
    # with col21:
    #     crownintensity = st.selectbox("CROWN_INTENSITY", options=['NN', 'BC1+', 'BC1', 'BC2', 'BC3'])
    #     dictCsv['CROWN_INTENSITY'] = crownintensity
    # with col22:
    #     girdleintensity = st.selectbox("GIRDLE_INTENSITY_needless", options=[0, 1, 2, 3, 4])
    #     dictCsv['GIRDLE_INTENSITY_needless'] = girdleintensity
    # with col23:
    #     girdle_inc = st.selectbox("GIRDLE_INCLUSION_needless",
    #                               options=['0', 'PP1', 'PP2', 'F1', 'F2', 'F3', 'F4', 'TW1', 'TW2', 'TW3', 'N1', 'N2',
    #                                        'N3', 'N4', 'C1', 'C2', 'C3', 'CO1', 'CO2', 'CO3', 'CL1', 'CL2', 'CL3',
    #                                        'None'])
    #     dictCsv['GIRDLE_INCLUSION_needless'] = girdle_inc
    # with col24:
    #     tableinc = st.selectbox("TABLE_INCLUSION_needless",
    #                             options=['0', 'PP1', 'PP2', 'F1', 'F2', 'F3', 'F4', 'TW1', 'TW2', 'TW3', 'N1', 'N2',
    #                                      'N3', 'N4', 'C1', 'C2', 'C3', 'CO1', 'CO2', 'CO3', 'CL1', 'CL2', 'CL3',
    #                                      'None'])
    #     dictCsv['TABLE_INCLUSION_needless'] = tableinc
    # with col25:
    #     crowninc = st.selectbox("CROWN_INCLUSION_needless",
    #                             options=['0', 'PP1', 'PP2', 'F1', 'F2', 'F3', 'F4', 'TW1', 'TW2', 'TW3', 'N1', 'N2',
    #                                      'N3', 'N4', 'C1', 'C2', 'C3', 'CO1', 'CO2', 'CO3', 'CL1', 'CL2', 'CL3',
    #                                      'None'])
    #     dictCsv['CROWN_INCLUSION_needless'] = crowninc
    # with col26:
    #     pavilioninc = st.selectbox("PAVILION_INCLUSION_needless",
    #                                options=['0', 'PP1', 'PP2', 'F1', 'F2', 'F3', 'F4', 'TW1', 'TW2', 'TW3', 'N1', 'N2',
    #                                         'N3', 'N4', 'C1', 'C2', 'C3', 'CO1', 'CO2', 'CO3', 'CL1', 'CL2', 'CL3',
    #                                         'None'])
    #     dictCsv['PAVILION_INCLUSION_needless'] = pavilioninc
    # with col27:
    #     tableopen = st.selectbox("TABLE_OPEN", options=['No', 'HO', 'Small', 'Medium', 'Big'])
    #     dictCsv['TABLE_OPEN'] = tableopen
    # with col28:
    #     tablenatural = st.selectbox("TABLE_NATURAL", options=['No', 'Idented', 'Natural', 'Big Natural'])
    #     dictCsv['TABLE_NATURAL'] = tablenatural
    # with col29:
    #     tableothers = st.selectbox("TABLE_OTHERS", options=['No', 'Extra Facet', 'Cavity', 'Chip'])
    #     dictCsv['TABLE_OTHERS'] = tableothers
    # with col30:
    #     crownopen = st.selectbox("CROWN_OPEN", options=['No', 'HO', 'Small', 'Medium', 'Big'])
    #     dictCsv['CROWN_OPEN'] = crownopen
    # with col31:
    #     crownnatural = st.selectbox("CROWN_NATURAL", options=['No', 'Idented', 'Natural', 'Big Natural'])
    #     dictCsv['CROWN_NATURAL'] = crownnatural
    # with col32:
    #     crownothers = st.selectbox("CROWN_OTHERS", options=['No', 'Extra Facet', 'Cavity', 'Chip'])
    #     dictCsv['CROWN_OTHERS'] = crownothers
    # with col33:
    #     girdleopen = st.selectbox("GIRDLE_OPEN", options=['No', 'HO', 'Small', 'Medium', 'Big'])
    #     dictCsv['GIRDLE_OPEN'] = girdleopen
    # with col34:
    #     girdlenatural = st.selectbox("GIRDLE_NATURAL", options=['No', 'Idented', 'Natural', 'Big Natural'])
    #     dictCsv['GIRDLE_NATURAL'] = girdlenatural
    # with col35:
    #     girdleothers = st.selectbox("GIRDLE_OTHERS", options=['No', 'Extra Facet', 'Cavity', 'Chip'])
    #     dictCsv['GIRDLE_OTHERS'] = girdleothers
    # with col33:
    #     pavilionopen = st.selectbox("PAVILION_OPEN", options=['No', 'HO', 'Small', 'Medium', 'Big'])
    #     dictCsv['PAVILION_OPEN'] = pavilionopen
    # with col34:
    #     pavilionnatural = st.selectbox("PAVILION_NATURAL", options=['No', 'Idented', 'Natural', 'Big Natural'])
    #     dictCsv['PAVILION_NATURAL'] = pavilionnatural
    # with col35:
    #     green = st.selectbox("GREEN", options=['No', 'G1', 'G2', 'G3', 'G4'])
    #     dictCsv['GREEN'] = green
    # with col36:
    #     grey = st.selectbox("GREY", options=['No', 'MT1', 'MT2', 'MT3'])
    #     dictCsv['GREY'] = grey
    # with col37:
    #     brown = st.selectbox("BROWN", options=['0', 'B1', 'B2', 'B3'])
    #     dictCsv['BROWN'] = brown
    # with col38:
    #     milky = st.selectbox("MILKY", options=['No', 'M1+', 'M1', 'M2', 'M3'])
    #     dictCsv['MILKY'] = milky
    # with col39:
    #     offcolor = st.selectbox("OFF_COLOR_needless", options=['No', 'OC1', 'OC2'])
    #     dictCsv['OFF_COLOR_needless'] = offcolor
    # with col40:
    #     halfopen = st.selectbox("HALF_OPEN", options=['No', 'Table', 'Crown', 'Girdle', 'Pavilion'])
    #     dictCsv['HALF_OPEN'] = halfopen
    # with col41:
    #     smallopen = st.selectbox("SMALL_OPEN", options=['No', 'Table', 'Crown', 'Girdle', 'Pavilion'])
    #     dictCsv['SMALL_OPEN'] = smallopen
    # with col42:
    #     bigopen = st.selectbox("BIG_OPEN", options=['No', 'Table', 'Crown', 'Girdle', 'Pavilion'])
    #     dictCsv['BIG_OPEN'] = bigopen
    # with col43:
    #     mediumopen = st.selectbox("MEDIUM_OPEN", options=['No', 'Table', 'Crown', 'Girdle', 'Pavilion'])
    #     dictCsv['MEDIUM_OPEN'] = mediumopen
    # with col44:
    #     identednatural = st.selectbox("Idented Natural", options=['No', 'Top', 'Bottom', 'Girdle'])
    #     dictCsv['Idented Natural'] = identednatural
    # with col45:
    #     naturalnatural = st.selectbox("Natural", options=['No', 'Top', 'Bottom', 'Girdle'])
    #     dictCsv['Natural'] = naturalnatural
    # with col46:
    #     bignatural = st.selectbox("Big Natural", options=['No', 'Top', 'Bottom', 'Girdle'])
    #     dictCsv['Big Natural'] = bignatural
    # with col47:
    #     extrafacet = st.selectbox("EXTRA_FACET", options=['No', 'Top', 'Bottom', 'Girdle'])
    #     dictCsv['EXTRA_FACET'] = extrafacet
    # with col48:
    #     chip = st.selectbox("CHIP", options=['No', 'Top', 'Bottom', 'Girdle'])
    #     dictCsv['CHIP'] = chip
    # with col49:
    #     cavity = st.selectbox("CAVITY", options=['No', 'Top', 'Bottom', 'Girdle'])
    #     dictCsv['CAVITY'] = cavity
    #
    # result = calcDiscount(shape, szgr, color, clarity, cut, polish, symmetry, fluo, rap, ktos, sizeprec,
    #                       tableclean, eyeclean, ha, cutcomments, diameter, internalgraining, surfacegraining,
    #                       pavilionintensity, tableintensity, crownintensity, girdleintensity, girdle_inc,
    #                       tableinc, crowninc, pavilioninc, tableopen, tablenatural, tableothers, crownopen,
    #                       crownnatural, girdleothers, girdleopen, girdlenatural, pavilionopen
    #                       , pavilionnatural, green, grey, brown, milky, offcolor, halfopen, smallopen, bigopen,
    #                       mediumopen, identednatural, naturalnatural, bignatural, extrafacet, chip, cavity)
    # st.text("\n")
    # if st.button("Calculate Final Price"):
    #     if int(rap) != 0:
    #         st.markdown(
    #             f"<big><b>Discount(in Percentage wrt RAP):</b> </big><font color='green' size=6>{float(result)}% </font>",
    #             unsafe_allow_html=True)
    #         print(dictCsv)
    #         # st.download_button('Download CSV', pd.DataFrame(dictCsv, index=[0]).to_csv(index=False),
    #         #                    mime='text/csv', file_name='sampleinput2.csv')
    #     else:
    #         st.error("Please input proper values")
    format = '%b %d %Y %H:%M:%S'
    now = datetime.now()
    last_updated_r = pd.read_csv('lastupdated_round.csv')
    last_updated_f = pd.read_csv('lastupdated_fancy.csv')
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7, col8, col9 = st.columns(3)
    col10, col11, col12 = st.columns(3)
    with col2:
        updated_file = st.file_uploader("Choose a csv file to update rapnet pricing", type='csv')
    with col5:
        if len(last_updated_r) == 0:
            st.write("Rapnet pricing not updated yet")
        else:
            st.write(
                "Round Rapnet pricing last updated on  - " + last_updated_r['update_date'][len(last_updated_r) - 1])
            st.write(
                "Fancy Rapnet pricing last updated on  - " + last_updated_f['update_date'][len(last_updated_f) - 1])
    if updated_file is not None:
        with col8:
            update_button = st.button('Update rapnet pricing for round')
        with col11:
            update_button2 = st.button('Update rapnet pricing for fancy')
        if update_button:
            newRapPrice = pd.read_csv(updated_file, encoding='unicode_escape')
            rap_columns = ['SHAPE', 'CLARITY', 'COLOUR', 'SIZE_RANGE_MIN', 'SIZE_RANGE_MAX', 'RAP']
            col_check = (x for x in rap_columns if x not in newRapPrice.keys())
            if len(list(col_check)) == 0:
                newRapPrice.to_csv('rap_price_round.csv')
                last_updated_r.loc[len(last_updated_r['update_date'])] = [now.strftime(format)]
                last_updated_r.to_csv('lastupdated_round.csv', index=False)
                # with col5:
                #     st.write('Price updated')
            else:
                with col5:
                    st.write("Incorrect format for csv file. Must contain 'SHAPE', 'CLARITY', 'COLOUR', "
                             "'SIZE_RANGE_MIN', 'SIZE_RANGE_MAX', 'RAP' columns")
        elif update_button2:
            newRapPrice = pd.read_csv(updated_file, encoding='unicode_escape')
            rap_columns = ['SHAPE', 'CLARITY', 'COLOUR', 'SIZE_RANGE_MIN', 'SIZE_RANGE_MAX', 'RAP']
            col_check = (x for x in rap_columns if x not in newRapPrice.keys())
            if len(list(col_check)) == 0:
                newRapPrice.to_csv('rap_price_fancy.csv')
                last_updated_f.loc[len(last_updated_f['update_date'])] = [now.strftime(format)]
                last_updated_f.to_csv('lastupdated_fancy.csv', index=False)
                # with col5:
                #     st.write('Price updated')
            else:
                with col5:
                    st.write("Incorrect format for csv file. Must contain 'SHAPE', 'CLARITY', 'COLOUR', "
                             "'SIZE_RANGE_MIN', 'SIZE_RANGE_MAX', 'RAP' columns")

    uploaded_file = st.file_uploader("Choose a csv file to get discount values", type='csv')

    result = 0.0
    exception_flag = False
    if uploaded_file is not None:
        start_process = st.button("Start Processing")
        if not start_process:
            return
        diamondData = pd.read_csv(uploaded_file, encoding='unicode_escape')
        diamondData.columns = diamondData.columns.str.strip()
        diamondData = diamondData.astype(str)
        for i in diamondData.keys():
            if diamondData[i].dtype == object:
                diamondData[i] = diamondData[i].str.strip()

        diamondData = diamondData.assign(FINAL_DISCOUNT_AFTER_CAPOFF='')
        diamondData = diamondData.assign(DISCOUNT_BEFORE_CAPOFF='')
        diamondData = diamondData.assign(Capoff='')
        diamondData = diamondData.assign(Differnce_between_Capped_and_Uncapped_Dis='')
        diamondData = diamondData.assign(Discounted_RAP_price_of_stone='')
        diamondData = diamondData.assign(Base_Dis='')
        diamondData = diamondData.assign(Size_Premium='')
        diamondData = diamondData.assign(GD_Dis='')
        diamondData = diamondData.assign(Diameter_Dis_or_MM_Premium='')
        diamondData = diamondData.assign(Colshade_Dis='')
        diamondData = diamondData.assign(Milky_Dis='')

        diamondData = diamondData.assign(ha_Dis='')
        diamondData = diamondData.assign(EyeClean_Dis='')
        diamondData = diamondData.assign(TableClean_Dis='')
        diamondData = diamondData.assign(table_black='')
        diamondData = diamondData.assign(SideBlack_Dis='')

        diamondData = diamondData.assign(Open_Dis='')
        diamondData = diamondData.assign(Natural_Dis='')
        diamondData = diamondData.assign(IdentedNatural_Dis='')

        diamondData = diamondData.assign(Cavity_Dis='')
        diamondData = diamondData.assign(Chip_Dis='')
        diamondData = diamondData.assign(Ncolor_Dis='')
        diamondData = diamondData.assign(Depth_Dis='')
        diamondData = diamondData.assign(Days_Dis='')
        diamondData = diamondData.assign(Ktos_Dis='')
        diamondData = diamondData.assign(cutcomments_Dis='')
        diamondData = diamondData.assign(Graining_Dis='')
        diamondData = diamondData.assign(Extra_Facet_Dis='')
        diamondData = diamondData.assign(Very_Strong_Fluo_Dis='')
        diamondData = diamondData.assign(FR_PR_dis='')
        diamondData = diamondData.assign(Fancy_Fluo_Dis='')
        diamondData = diamondData.assign(Fancy_Poly_Sym_Dis='')
        diamondData = diamondData.assign(FL_Premium='')
        diamondData = diamondData.assign(Round_Polish_Symmetry_Dis='')
        diamondData = diamondData.assign(Capoff_premiums='')
        diamondData = diamondData.assign(Capoff_discounts='')
        diamondData = diamondData.assign(Final_Total_discount='')
        diamondData = diamondData.assign(Discounted_RAP_price_of_stone='')

        records_processed = st.empty()
        progress = st.progress(0)
        for i in range(len(diamondData)):
            try:

                cert = column_default_validation(diamondData, 'CERT', i)
                shape = column_default_validation(diamondData, 'SHAPE', i)  # updated with client stock sheet
                szgr = '0.30-0.34'  # column_default_validation(diamondData, 'SIZE RANGE', i, '0.30-0.34')
                color = column_default_validation(diamondData, 'COLOR', i, 'D')  # updated with client stock sheet
                clarity = column_default_validation(diamondData, 'CLARITY', i,
                                                    'IF')  # updated with client stock sheet
                cut = column_default_validation(diamondData, 'CUT', i, 'EX')
                polish = column_default_validation(diamondData, 'POL', i, 'EX')
                symmetry = column_default_validation(diamondData, 'SY', i, 'EX')
                fluo = column_default_validation(diamondData, 'FLUO', i, 'Faint')
                rap = column_default_validation(diamondData, 'RAP', i, 0)
                ktos = column_default_validation(diamondData, 'KEY_TO_SYMBOL', i, 0)
                sizeprec = float(column_default_validation(diamondData, 'WEIGHT', i, 0))
                tableclean = column_default_validation(diamondData, 'TABLE_CLEAN', i, 'Yes')
                eyeclean = column_default_validation(diamondData, 'EYE_CLEAN', i, 'Yes')
                ha = column_default_validation(diamondData, 'HA', i, 'Yes')
                cutcomments = column_default_validation(diamondData, 'CUT_COMMENTS', i, '0')
                diameter = column_default_validation(diamondData, 'DIAMETER', i, 0)
                internalgraining = column_default_validation(diamondData, 'INTERNAL_GRAINING', i, '0')
                surfacegraining = column_default_validation(diamondData, 'SURFACE_GRAINING', i, '0')
                flawless = column_default_validation(diamondData, 'Flawless', i, 'Yes(select IF color)')
                tableintensity = column_default_validation(diamondData, 'TABLE_BLACK', i, 'NN')
                crownintensity = column_default_validation(diamondData, 'SIDE_BLACK', i, 'NN')
                topef = column_default_validation(diamondData, 'Top_Extra_Facet', i, '0')
                topcavity = column_default_validation(diamondData, 'Top_cavity', i, '0')
                topchip = column_default_validation(diamondData, 'Top_Chip', i, '0')
                crownef = column_default_validation(diamondData, 'Crown_Extra_Facet', i, '0')
                crowncavity = column_default_validation(diamondData, 'Crown_cavity', i, '0')
                crownchip = column_default_validation(diamondData, 'Crown_Chip', i, '0')
                girdleef = column_default_validation(diamondData, 'Girdle_Extra_Facet', i, '0')
                girdlecavity = column_default_validation(diamondData, 'Girdle_cavity', i, '0')
                girdlechip = column_default_validation(diamondData, 'Girdle_Chip', i, '0')
                pavilionef = column_default_validation(diamondData, 'Pavilion_Extra_Facet', i, '0')
                pavilioncavity = column_default_validation(diamondData, 'Pavilion_cavity', i, '0')
                pavilionchip = column_default_validation(diamondData, 'Pavilion_Chip', i, '0')
                depth = column_default_validation(diamondData, 'TD', i, 0, no_comma=1)
                if depth == '-':
                    depth = 0.0
                else:
                    try:
                        depth = float(depth)
                    except:
                        depth = 0.0
                green = column_default_validation(diamondData, 'GREEN', i, 'No')
                grey = column_default_validation(diamondData, 'GREY', i, 'No')
                brown = column_default_validation(diamondData, 'BROWN', i, '0')
                milky = column_default_validation(diamondData, 'MILKY', i, 'No')
                tableopen = column_default_validation(diamondData, 'TABLE_OPEN', i, 'No')
                crownopen = column_default_validation(diamondData, 'CROWN_OPEN', i, 'No')
                girdleopen = column_default_validation(diamondData, 'GIRDLE_OPEN', i, 'No')
                pavilionopen = column_default_validation(diamondData, 'PAVILION_OPEN', i, 'No')
                topnatural = column_default_validation(diamondData, 'Top_Natural', i, 'No')
                crownnatural = column_default_validation(diamondData, 'Crown_Natural', i, 'No')
                girdlenatural = column_default_validation(diamondData, 'Girdle_Natural', i, 'No')
                pavilionnatural = column_default_validation(diamondData, 'Pavilion_Natural', i, 'No')
                try:
                    days = int(float(column_default_validation(diamondData, 'REF_DAYS', i, 0, no_comma=1)))
                except:
                    days = 0
                chip = column_default_validation(diamondData, 'CHIP', i, 'No')
                cavity = column_default_validation(diamondData, 'CAVITY', i, 'No')
                upgrade1 = column_default_validation(diamondData, 'Upgrade_Color', i, '0')
                upgrade2 = column_default_validation(diamondData, 'Upgrade_Clarity', i, '0')
                downgrade1 = column_default_validation(diamondData, 'Downgrade_Color', i, '0')
                downgrade2 = column_default_validation(diamondData, 'Downgrade_Clarity', i, '0')

                # new variables added here 10-08-2022
                min_diam = column_default_validation(diamondData, 'MIN_DIAM', i, no_comma=1)
                max_diam = column_default_validation(diamondData, 'MAX_DIAM', i, no_comma=1)
                if min_diam == '-':
                    min_diam = 0.0
                else:
                    min_diam = float(min_diam)
                if max_diam == '-':
                    max_diam = 0.0
                else:
                    max_diam = float(max_diam)
                tabl = column_default_validation(diamondData, 'TABL', i)
                height = column_default_validation(diamondData, 'HEIGHT', i)
                ratio = column_default_validation(diamondData, 'RATIO', i)
                col_shade = column_default_validation(diamondData, 'COL_SHADE', i)
                cr_angle = column_default_validation(diamondData, 'CR_ANGLE', i)
                cr_height = column_default_validation(diamondData, 'CR_HEIGHT', i)
                pv_angle = column_default_validation(diamondData, 'PV_ANGLE', i)
                pv_depth = column_default_validation(diamondData, 'PV_DEPTH', i)
                girdle_percentage = column_default_validation(diamondData, 'GIRDLE_PERCENTAGE', i)
                girdle_from = column_default_validation(diamondData, 'GIRDLE_FROM', i)
                girdle_to = column_default_validation(diamondData, 'GIRDLE_TO', i)
                girdle_condition = column_default_validation(diamondData, 'GIRDLE_CONDITION', i)
                star_length = column_default_validation(diamondData, 'STAR_LENGTH', i)
                lower_half = column_default_validation(diamondData, 'LOWER_HALF', i)
                open1 = column_default_validation(diamondData, 'OPEN', i)
                natural = column_default_validation(diamondData, 'NATURAL', i)
                intended_natural = column_default_validation(diamondData, 'INTENDED_NATURAL', i)
                extra_facet = column_default_validation(diamondData, 'EXTRA_FACET', i)
                graining = column_default_validation(diamondData, 'GRAINING', i)
                cavity = column_default_validation(diamondData, 'CAVITY', i)
                chip = column_default_validation(diamondData, 'CHIP', i)
                remarks = column_default_validation(diamondData, 'REMARKS', i)
                rap_value = column_default_validation(diamondData, 'RAP_VALUE', i)
                # new variables added here 10-08-2022

                if match(shape, 'ROUND') or match(shape, 'RO') or match(shape, 'BR'):
                    shape = 'RO'
                    diamondData['SHAPE'][i] = shape
                if match(shape, 'CUSHION') or match(shape, 'CS') or match(shape, 'CUSHION MODIFIED') or \
                        match(shape, 'CUSHION BRILLIANT') or match(shape, 'SQAURE CUSHION'):
                    shape = 'CUSHION'
                    diamondData['SHAPE'][i] = shape
                if match(shape, 'EMERALD') or match(shape, 'EM'):
                    shape = 'EMERALD'
                    diamondData['SHAPE'][i] = shape
                if match(shape, 'MARQUISE') or match(shape, 'MQ'):
                    shape = 'MARQUISE'
                    diamondData['SHAPE'][i] = shape
                if match(shape, 'PR') or match(shape, 'PEAR'):
                    shape = 'PEAR'
                    diamondData['SHAPE'][i] = shape
                if match(shape, 'PS') or match(shape, 'PRINCESS'):
                    shape = 'PRINCESS'
                    diamondData['SHAPE'][i] = shape
                if match(shape, 'OV') or match(shape, 'OVAL'):
                    shape = 'OVAL'
                    diamondData['SHAPE'][i] = shape
                if match(shape, 'HEART') or match(shape, 'HT'):
                    shape = 'HEART'
                    diamondData['SHAPE'][i] = shape
                if match(shape, 'RADIANT') or match(shape, 'RD') or match(shape, 'LONG RADIANT'):
                    shape = 'RADIANT'
                    diamondData['SHAPE'][i] = shape
                if match(shape, 'ASSHER') or match(shape, 'SQUARE EMERALD'):
                    shape = 'ASSHER'
                    diamondData['SHAPE'][i] = shape
                if match(shape, 'BUGGET'):
                    shape = 'BUGGET'
                    diamondData['SHAPE'][i] = shape
                try:
                    if match(shape, 'PRN'):
                        if 0.95 <= float(ratio) <= 1.05:
                            shape = 'PRINCESS'
                        else:
                            shape = 'PEAR'
                except:
                    pass

                if match(fluo, 'FNT') or match(fluo, 'FAINT'):
                    fluo = 'Faint'
                    diamondData['FLUO'][i] = fluo
                if match(fluo, 'MED') or match(fluo, 'MEDIUM') or match(fluo, 'STL'):
                    fluo = 'Medium'
                    diamondData['FLUO'][i] = fluo
                if match(fluo, 'NON') or match(fluo, 'NN') or match(fluo, 'NONE'):
                    fluo = 'None'
                    diamondData['FLUO'][i] = fluo
                if match(fluo, 'STG') or match(fluo, 'STR') or match(fluo, 'STRONG'):
                    fluo = 'Strong'
                    diamondData['FLUO'][i] = fluo
                if match(fluo, 'VST') or match(fluo, 'VERY STRONG'):
                    fluo = 'Very Strong'
                    diamondData['FLUO'][i] = fluo

                if match(cut, 'EX') or match(cut, 'EXCELLENT') or match(cut, 'BL'):
                    cut = 'EX'
                if match(cut, 'VG') or match(cut, 'VERY GOOD'):
                    cut = 'VG'
                if match(cut, 'G') or match(cut, 'GD'):
                    cut = 'GD'

                if match(polish, 'EX') or match(polish, 'EXCELLENT'):
                    polish = 'EX'
                if match(polish, 'VG') or match(polish, 'VERY GOOD'):
                    polish = 'VG'
                if match(polish, 'G') or match(polish, 'GD'):
                    polish = 'GD'

                if match(symmetry, 'EX') or match(symmetry, 'EXCELLENT'):
                    symmetry = 'EX'
                if match(symmetry, 'VG') or match(symmetry, 'VERY GOOD'):
                    symmetry = 'VG'
                if match(symmetry, 'G') or match(symmetry, 'GD'):
                    symmetry = 'GD'

                if match(ha, 'Yes') or match(ha, 'Y'):
                    ha = 'Y'
                if match(ha, 'No') or match(ha, 'N'):
                    ha = 'N'

                if match(tableclean, 'Yes') or match(tableclean, 'Y'):
                    tableclean = 'Y'
                if match(tableclean, 'No') or match(tableclean, 'N'):
                    tableclean = 'N'

                if match(eyeclean, 'Yes') or match(eyeclean, 'Y'):
                    eyeclean = 'Y'
                if match(eyeclean, 'No') or match(eyeclean, 'N'):
                    eyeclean = 'N'

                # case matching for other attributes
                color = color.upper()
                clarity = clarity.upper()

                # Function calls to determine ktos, size range, cutcomments and rap_value ##################
                #                 diamondData['CUT_COMMENTS'][i] = get_cut_comments(cert,shape,cut, tabl, height, ratio,
                #                                                                   cr_angle,depth, pv_angle, pv_depth, girdle_percentage,
                #                                                                   star_length, lower_half)

                #                 cutcomments ='NN'
                ktos_attribute = ktos
                ktos = len(ktos.split(',')) if isinstance(ktos, str) else 0
                szgr = fetch_size(shape, sizeprec)
                rap = fetchrap(shape, szgr, color, clarity, sizeprec)
                rap_value = rap * sizeprec
                diamondData['RAP_VALUE'][i] = rap_value
                # Function calls to determine ktos, size range, cutcomments and rap_price ##################
                if (sizeprec >= 1):
                    if (max_diam <= 6.2):
                        diameter = max_diam
                    elif (min_diam >= 6.3):
                        diameter = min_diam
                    else:
                        diameter = 6.25
                else:
                    diameter = min_diam
                diamondData['RAP'][i] = rap
                if graining == 'IGR1' or graining == 'IGR2' or graining == 'IGR3':
                    internalgrainig = graining
                    surfacegraining = '0'
                else:
                    internalgrainig = '0'
                    surfacegraining = graining

                result = calcDiscount(cert, shape, szgr, color, clarity, cut, polish, symmetry, fluo, rap, ktos,
                                      sizeprec,
                                      tableclean,
                                      eyeclean, ha, cutcomments, diameter, internalgraining, surfacegraining,
                                      flawless,
                                      tableintensity, crownintensity, topef, cavity, chip, extra_facet, crowncavity,
                                      crownchip,
                                      girdleef, girdlecavity, girdlechip, pavilionef, pavilioncavity, pavilionchip,
                                      depth, col_shade,
                                      grey, brown, milky, open1, crownopen, girdleopen, pavilionopen, natural,
                                      crownnatural,
                                      girdlenatural, pavilionnatural, chip, cavity, upgrade1, upgrade2, downgrade1,
                                      downgrade2, days,
                                      min_diam, max_diam, tabl, height, ratio, cr_angle, cr_height, pv_angle,
                                      pv_depth,
                                      girdle_percentage, girdle_from, girdle_to, girdle_condition, star_length,
                                      lower_half,
                                      intended_natural, graining, rap_value, ktos_attribute, remarks)

                diamondData['FINAL_DISCOUNT_AFTER_CAPOFF'][i] = result[0]
                if result[1] == 0 or pd.isna(result[1]):
                    diamondData['Base_Dis'][i] = 'NA'
                    result[1] = 0
                else:
                    diamondData['Base_Dis'][i] = result[1]
                diamondData['GD_Dis'][i] = result[2] if result[2] != 0 else ''
                diamondData['Diameter_Dis_or_MM_Premium'][i] = result[3] if result[3] != 0 else ''
                diamondData['Colshade_Dis'][i] = result[4] if result[4] != 0 else ''
                diamondData['Milky_Dis'][i] = result[5] if result[5] != 0 else ''
                diamondData['cutcomments_Dis'][i] = result[6] if result[6] != 0 else ''
                diamondData['Graining_Dis'][i] = result[7] if result[7] != 0 else ''
                diamondData['ha_Dis'][i] = result[8] if result[8] != 0 else ''
                diamondData['EyeClean_Dis'][i] = result[9] if result[9] != 0 else ''
                diamondData['TableClean_Dis'][i] = result[10] if result[10] != 0 else ''
                diamondData['table_black'][i] = result[11] if result[11] != 0 else ''
                diamondData['SideBlack_Dis'][i] = result[12] if result[12] != 0 else ''
                diamondData['Size_Premium'][i] = result[13] if result[13] != 0 else ''
                diamondData['Open_Dis'][i] = result[14] if result[14] != 0 else ''
                diamondData['Natural_Dis'][i] = result[15] if result[15] != 0 else ''
                diamondData['IdentedNatural_Dis'][i] = result[16] if result[16] != 0 else ''
                diamondData['Extra_Facet_Dis'][i] = result[17] if result[17] != 0 else ''
                diamondData['Cavity_Dis'][i] = result[18] if result[18] != 0 else ''
                diamondData['Chip_Dis'][i] = result[19] if result[19] != 0 else ''
                diamondData['Ncolor_Dis'][i] = result[20] if result[20] != 0 else ''
                diamondData['Depth_Dis'][i] = result[21] if result[21] != 0 else ''
                diamondData['Ktos_Dis'][i] = result[22] if result[22] != 0 else ''
                diamondData['Days_Dis'][i] = result[23] if result[23] != 0 else ''
                diamondData['Very_Strong_Fluo_Dis'][i] = result[24] if result[24] != 0 else ''
                diamondData['Fancy_Fluo_Dis'][i] = result[25] if result[25] != 0 else ''
                diamondData['Fancy_Poly_Sym_Dis'][i] = result[26] if result[26] != 0 else ''
                diamondData['FL_Premium'][i] = result[27] if result[27] != 0 else ''
                diamondData['Round_Polish_Symmetry_Dis'][i] = result[28] if result[28] != 0 else ''
                diamondData['Capoff_premiums'][i] = result[29] if result[29] != 0 else ''
                diamondData['Capoff_discounts'][i] = result[30] if result[30] != 0 else ''
                diamondData['Capoff'][i] = result[31] if result[31] != 0 else ''
                diamondData['FR_PR_dis'][i] = result[32] if result[32] != 0 else ''

                final_sum = 0
                for j in range(len(result)):
                    if j not in [0, 31, 7, 8, 9, 10, 6, 4, 5, 11, 12, 14, 15, 16, 17, 18, 19]:
                        final_sum += result[j]
                final_sum = round_05(final_sum)
                diamondData['Final_Total_discount'][i] = final_sum
                diamondData['Differnce_between_Capped_and_Uncapped_Dis'][i] = result[0] - final_sum
                # diamondData['BaseD'][i] = result[1]
                diamondData['Discounted_RAP_price_of_stone'][i] = round(rap_value * ((100 + final_sum) / 100), 2)

            except ColumnError as c:
                logging.error('Something went wrong, ' + str(c))
                st.write(str(c))
                exception_flag = True
                break
            except BaseException as e:
                logging.error('Something went wrong' + str(e))
                logging.error('Something went wrong with record number ' + str(i + 1) + ' ' + str(e))
                logging.error(traceback.format_exc())
            records_processed.text(str(i) + ' out of ' + str(len(diamondData) - 1) + ' records processed')
            progress.progress(float(i) / (len(diamondData)))
        if not exception_flag:
            diamondData = diamondData.drop(
                columns=['FINAL_DISCOUNT_AFTER_CAPOFF', 'GD_Dis', 'Capoff', 'DISCOUNT_BEFORE_CAPOFF',
                         'Differnce_between_Capped_and_Uncapped_Dis'])
            diamondData = diamondData.astype(str)
            cols = diamondData.columns.tolist()
            # cols[-1], cols[-2], cols[-3] = cols[-2], cols[-3], cols[-1]
            cols.remove('Discounted_RAP_price_of_stone')
            cols.append('Discounted_RAP_price_of_stone')
            cols.remove('Final_Total_discount')
            cols.append('Final_Total_discount')
            diamondData = diamondData[cols]
            st.write(diamondData)
            st.download_button('Download CSV', diamondData.to_csv(index=False),
                               mime='text/csv', file_name='discountOutput.csv')

page_names = {
    "Bulk upload": page1,
    'Price Module upload': page3,
    'Days discount upload': page4,
    'Very Strong Fluorescence upload': page5,
    'Price Module History': page6,
    'Individual Discount History': page7,
    'Upload Discount Sheet': page8
}
st.sidebar.markdown("<h1>Discount Calculator</h1>", unsafe_allow_html=True)
selected_page = st.sidebar.selectbox("Select Calculator", page_names.keys())
page_names[selected_page]()
st.markdown(footer, unsafe_allow_html=True)
