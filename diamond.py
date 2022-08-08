import time

import streamlit as st
import dill as pickle
import pandas as pd
import cv2
from datetime import date, datetime

from Discount import calcDiscount

st.set_page_config(page_title="Discount Calculator", page_icon='💎', layout="wide", initial_sidebar_state="collapsed",
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
    #         #                    mime='text/csv', file_name='sampleinput.csv')
    #     else:
    #         st.error("Please input proper values")
    format = '%b %d %Y %H:%M:%S'
    now = datetime.now()
    last_updated = pd.read_csv('lastupdated.csv')
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7, col8, col9 = st.columns(3)
    with col2:
        updated_file = st.file_uploader("Choose a csv file to update rapnet pricing", type='csv')
    with col5:
        if len(last_updated) == 0:
            st.write("Rapnet pricing not updated yet")
        else:
            st.write("Rapnet pricing last updated on  - " + last_updated['update_date'][len(last_updated) - 1])
    if updated_file is not None:
        with col8:
            update_button = st.button('Update rapnet pricing')
        if update_button is not None:
            newRapPrice = pd.read_csv(updated_file)
            newRapPrice.to_csv('rap_price.csv')
            with col5:
                st.write('Price updated')

    uploaded_file = st.file_uploader("Choose a csv file to get discount values", type='csv')
    if uploaded_file is not None:
        diamondData = pd.read_csv(uploaded_file)
        diamondData = diamondData.assign(DISCOUNT='NAN')
        for i in range(len(diamondData)):
            try:
                shape = diamondData['SHAPE'][i]
                szgr = diamondData['SIZE RANGE'][i]
                color = diamondData['COLOUR'][i]
                clarity = diamondData['CLARITY'][i]
                cut = diamondData['CUT'][i]
                polish = diamondData['POLISH'][i]
                symmetry = diamondData['SYMMETRY'][i]
                fluo = diamondData['FLUO'][i]
                rap = diamondData['RAP'][i]
                ktos = diamondData['KTOS'][i]
                sizeprec = diamondData['PRECISE SIZE'][i]
                tableclean = diamondData['TABLE_CLEAN'][i]
                eyeclean = diamondData['EYE_CLEAN'][i]
                ha = diamondData['H&A'][i]
                cutcomments = diamondData['CUT_COMMENTS'][i]
                diameter = diamondData['DIAMETER'][i]
                internalgraining = diamondData['INTERNAL_GRAINING'][i]
                surfacegraining = diamondData['SURFACE_GRAINING'][i]
                pavilionintensity = diamondData['PAVILION_INTENSITY_needless'][i]
                tableintensity = diamondData['TABLE_INTENSITY'][i]
                crownintensity = diamondData['CROWN_INTENSITY'][i]
                girdleintensity = diamondData['GIRDLE_INTENSITY_needless'][i]
                girdle_inc = diamondData['GIRDLE_INCLUSION_needless'][i]
                tableinc = diamondData['TABLE_INCLUSION_needless'][i]
                crowninc = diamondData['CROWN_INCLUSION_needless'][i]
                pavilioninc = diamondData['PAVILION_INCLUSION_needless'][i]
                tableopen = diamondData['TABLE_OPEN'][i]
                tablenatural = diamondData['TABLE_NATURAL'][i]
                tableothers = diamondData['TABLE_OTHERS'][i]
                crownopen = diamondData['CROWN_OPEN'][i]
                crownnatural = diamondData['CROWN_NATURAL'][i]
                crownothers = diamondData['CROWN_OTHERS'][i]
                girdleopen = diamondData['GIRDLE_OPEN'][i]
                girdlenatural = diamondData['GIRDLE_NATURAL'][i]
                girdleothers = diamondData['GIRDLE_OTHERS'][i]
                pavilionopen = diamondData['PAVILION_OPEN'][i]
                pavilionnatural = diamondData['PAVILION_NATURAL'][i]
                green = diamondData['GREEN'][i]
                grey = diamondData['GREY'][i]
                brown = diamondData['BROWN'][i]
                milky = diamondData['MILKY'][i]
                offcolor = diamondData['OFF_COLOR_needless'][i]
                halfopen = diamondData['HALF_OPEN'][i]
                smallopen = diamondData['SMALL_OPEN'][i]
                bigopen = diamondData['BIG_OPEN'][i]
                mediumopen = diamondData['MEDIUM_OPEN'][i]
                identednatural = diamondData['Idented Natural'][i]
                naturalnatural = diamondData['Natural'][i]
                bignatural = diamondData['Big Natural'][i]
                extrafacet = diamondData['EXTRA_FACET'][i]
                chip = diamondData['CHIP'][i]
                cavity = diamondData['CAVITY'][i]
                upgrade1 = diamondData['Upgrade_Color'][i]
                upgrade2 = diamondData['Upgrade_Clarity'][i]
                downgrade1 = diamondData['Downgrade_Color'][i]
                downgrade2 = diamondData['Downgrade_Clarity'][i]
                result = calcDiscount(shape, szgr, color, clarity, cut, polish, symmetry, fluo, rap, ktos, sizeprec,
                                      tableclean, eyeclean, ha, cutcomments, diameter, internalgraining,
                                      surfacegraining, pavilionintensity, tableintensity, crownintensity, girdleintensity,
                                      girdle_inc, tableinc, crowninc, pavilioninc, tableopen, tablenatural, tableothers,
                                      crownopen, crownnatural, girdleothers, girdleopen, girdlenatural, pavilionopen
                                      , pavilionnatural, green, grey, brown, milky, offcolor, halfopen, smallopen,
                                      bigopen, mediumopen, identednatural, naturalnatural, bignatural,
                                      extrafacet, chip, cavity, upgrade1, upgrade2, downgrade1, downgrade2)
                print(result)
                diamondData['DISCOUNT'][i] = result
            except Exception as e:
                print('Something went wrong', e)
        st.write(diamondData)
        st.download_button('Download CSV', diamondData.to_csv(index=False),
                           mime='text/csv', file_name='discountOutput.csv')


page_names = {
    "Newest sheet": page1

}

st.sidebar.markdown("<h1>Discount Calculator</h1>", unsafe_allow_html=True)
selected_page = st.sidebar.selectbox("Select Calculator", page_names.keys())
page_names[selected_page]()

st.markdown(footer, unsafe_allow_html=True)
