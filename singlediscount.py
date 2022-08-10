import streamlit as st
import dill as pickle
import pandas as pd
import cv2

from Discount import calcDiscount


def page2():
    with open('diamond.pkl', 'rb') as handle:
        model = pickle.load(handle)

    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)
    col11, col12, col13, col14, col15 = st.columns(5)
    col16, col17, col18, col19, col20 = st.columns(5)
    col21, col22, col23, col24, col25 = st.columns(5)
    col26, col27, col28, col29, col30 = st.columns(5)
    col31, col32, col33, col34, col35 = st.columns(5)
    col36, col37, col38, col39, col40 = st.columns(5)
    col41, col42, col43, col44, col45 = st.columns(5)
    col46, col47, col48, col49, col50 = st.columns(5)
    col51, col52, col53, col54, col55 = st.columns(5)

    # color_dict = {"D":10,"E":9,"F":8,"G":7,"H":6,"I":5,"J":4,"K":3,"L":2,"M":1}
    # clarity_dict = {"IF":8,"VVS1":7,"VVS2":6,"VS1":5,"VS2":4,"SI1":3,"SI2":2,"I1":1}
    # fluo_dict = {"FNT":1,"MED":2,"NON":3,"SIG":4,"VST":5}

    dictCsv = {}
    with col1:
        shape = st.selectbox("SHAPE*", options=['RO', 'CS', 'EM', 'HT', 'MAO', 'PR', 'PRINCESS', 'OV'])
        dictCsv['SHAPE'] = shape

    with col2:
        szgr = st.selectbox("SIZE RANGE*",
                            options=['0.30-0.34', '0.35-0.39', '0.40-0.44', '0.45-0.49', '0.50-0.59', '0.60-0.69',
                                     '0.70-0.74', '0.75-0.79', '0.80-0.89', '0.90-0.94', '0.95-0.99', '1.01-1.09',
                                     '1.50-1.69', '2.01-2.09', '3.01-3.09', '4.01-4.09', '5.01-5.09', '0.50-0.599',
                                     '0.60-0.699', '0.70-0.799', '0.70-0.799', '0.80-0.899', '0.90-0.979', '0.98-0.999',
                                     '1.00-1.099', '1.10-1.199', '1.20-1.299', '1.30-1.399', '1.40-1.499', '1.50-1.599',
                                     '1.60-1.699', '1.70-1.799', '1.80-1.899', '1.90-1.999', '2.00-2.099', '2.10-2.199',
                                     '2.20-2.499', '2.50-2.699', '2.70-2.799', '2.80-2.999', '3.01-3.09', '4.01-4.09',
                                     '5.01-5.09'])
        dictCsv['SIZE RANGE'] = szgr

    with col3:
        color = st.selectbox("COLOUR*", options=['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'])
        dictCsv['COLOR'] = color

    with col4:
        clarity = st.selectbox("CLARITY*", options=['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'])
        dictCsv['CLARITY'] = clarity

    with col5:
        cut = st.selectbox("CUT*", options=['EX', 'GD', 'VG'])
        dictCsv['CUT'] = cut

    with col6:
        polish = st.selectbox("POLISH*", options=['EX', 'GD', 'VG'])
        dictCsv['POL'] = polish

    with col7:
        symmetry = st.selectbox("SYMMETRY*", options=['EX', 'GD', 'VG'])
        dictCsv['SY'] = symmetry

    with col8:
        fluo = st.selectbox("FLUO*", options=['Faint', 'Medium', 'None', 'Strong', 'Very Strong'])
        dictCsv['FLUO'] = fluo

    with col9:
        rap = st.number_input("RAP*")
        dictCsv['RAP'] = rap

    with col10:
        ktos = st.number_input("KTOS")
        dictCsv['KEY_TO_SYMBOL'] = ktos
    with col11:
        sizeprec = st.number_input("PRECISE SIZE")
        dictCsv['WEIGHT'] = sizeprec
    with col12:
        tableclean = st.selectbox("TABLE_CLEAN", options=['Yes', 'No'])
        dictCsv['TABLE_CLEAN'] = tableclean
    with col13:
        eyeclean = st.selectbox("EYE_CLEAN", options=['Yes', 'No'])
        dictCsv['EYE_CLEAN'] = eyeclean
    with col14:
        ha = st.selectbox("H&A", options=['Yes', 'No'])
        dictCsv['HA'] = ha
    with col15:
        cutcomments = st.selectbox("CUT_COMMENTS",
                                   options=['0', '3EX->EX1', '3EX->EX2', 'EX->EX1', 'EX->EX2', 'VG->VG1', 'VG->VG2',
                                            'G->GD1', 'G->GD2', 'Fancy->Ideal', 'Fancy->Premium', 'Fancy->Very Good'])
        dictCsv['CUT_COMMENTS'] = cutcomments
    with col16:
        diameter = st.number_input("DIAMETER")
        dictCsv['DIAMETER'] = diameter
    with col17:
        internalgraining = st.selectbox("INTERNAL_GRAINING", options=['0', 'NN', 'IGR1', 'IGR2', 'IGR3'])
        dictCsv['INTERNAL_GRAINING'] = internalgraining
    with col18:
        surfacegraining = st.selectbox("SURFACE_GRAINING", options=['0', 'NN', 'SGR1', 'SGR2', 'SGR3'])
        dictCsv['SURFACE_GRAINING'] = surfacegraining
    with col19:
        flawless = st.selectbox("Flawless", options=['Yes(select IF color)', 'No'])
        dictCsv['Flawless'] = flawless
    with col20:
        tableintensity = st.selectbox("TABLE_INTENSITY", options=['NN', 'BT1+', 'BT1', 'BT2', 'BT3'])
        dictCsv['TABLE_BLACK'] = tableintensity
    with col21:
        crownintensity = st.selectbox("CROWN_INTENSITY", options=['NN', 'BC1+', 'BC1', 'BC2', 'BC3'])
        dictCsv['SIDE_BLACK'] = crownintensity
    with col22:
        topef = st.selectbox("Top_Extra_Facet", options=['0', 'EFT'])
        dictCsv['Top_Extra_Facet'] = topef
    with col23:
        topcavity = st.selectbox("Top_cavity", options=['0', 'CTT'])
        dictCsv['Top_cavity'] = topcavity
    with col24:
        topchip = st.selectbox("Top_Chip", options=['0', 'CHT'])
        dictCsv['Top_Chip'] = topchip
    with col25:
        crownef = st.selectbox("Crown_Extra_Facet", options=['0', 'EFC'])
        dictCsv['Crown_Extra_Facet'] = crownef
    with col26:
        crowncavity = st.selectbox("Crown_cavity", options=['0', 'CTC'])
        dictCsv['Crown_cavity'] = crowncavity
    with col27:
        crownchip = st.selectbox("Crown_Chip", options=['0', 'CHC'])
        dictCsv['Crown_Chip'] = crownchip
    with col28:
        girdleef = st.selectbox("Girdle_Extra_Facet", options=['0', 'EFG'])
        dictCsv['Girdle_Extra_Facet'] = girdleef
    with col29:
        girdlecavity = st.selectbox("Girdle_cavity", options=['0', 'CTG'])
        dictCsv['Girdle_cavity'] = girdlecavity
    with col30:
        girdlechip = st.selectbox("Girdle_Chip", options=['0', 'CHG'])
        dictCsv['Girdle_Chip'] = girdlechip
    with col31:
        pavilionef = st.selectbox("Pavilion_Extra_Facet", options=['0', 'EFP'])
        dictCsv['Pavilion_Extra_Facet'] = pavilionef
    with col32:
        pavilioncavity = st.selectbox("Pavilion_cavity", options=['0', 'CTP'])
        dictCsv['Pavilion_cavity'] = pavilioncavity
    with col33:
        pavilionchip = st.selectbox("Pavilion_Chip", options=['0', 'CHP'])
        dictCsv['Pavilion_Chip'] = pavilionchip
    with col34:
        depth = st.number_input("Depth")
        dictCsv['TD '] = depth
    # with col26:
    #     pavilioninc = st.selectbox("PAVILION_INCLUSION_needless",options=['0','PP1', 'PP2', 'F1', 'F2','F3','F4','TW1','TW2','TW3','N1','N2','N3','N4','C1','C2','C3','CO1','CO2','CO3','CL1','CL2','CL3','None'])
    # with col27:
    #     tableopen = st.selectbox("TABLE_OPEN", options=['No','EX-Open-HO-Table','EX-Open-Small-Table','EX-Open-Medium-Table','EX-Open-Big-Table','VG-Open-HO-Table','VG-Open-Small-Table','VG-Open-Medium-Table','VG-Open-Big-Table','G-Open-HO-Table','G-Open-Small-Table','G-Open-Medium-Table','G-Open-Big-Table'])
    # with col28:
    #     topnatural = st.selectbox("TOP_NATURAL", options=['No','EX-Natural-Indented Natural-Top','EX-Natural-Natural-Top','EX-Natural-Big Natural-Top','VG-Natural-Indented Natural-Top','VG-Natural-Natural-Top','','','',''])
    # with col29:
    #     topeothers = st.selectbox("TOP_OTHERS", options=['No','Extra Facet','Cavity','Chip'])
    # with col30:
    #     crownopen = st.selectbox("CROWN_OPEN", options=['No','HO','Small','Medium','Big'])
    # with col31:
    #     crownnatural = st.selectbox("CROWN_NATURAL", options=['No','Idented','Natural','Big Natural'])
    # with col32:
    #     girdleothers = st.selectbox("CROWN_OTHERS", options=['No','Extra Facet','Cavity','Chip'])
    # with col33:
    #     girdleopen = st.selectbox("GIRDLE_OPEN", options=['No','HO','Small','Medium','Big'])
    # with col34:
    #     girdlenatural = st.selectbox("GIRDLE_NATURAL", options=['No','Idented','Natural','Big Natural'])
    # with col35:
    #     girdleothers = st.selectbox("GIRDLE_OTHERS", options=['No','Extra Facet','Cavity','Chip'])
    # with col33:
    #     pavilionopen = st.selectbox("PAVILION_OPEN", options=['No','HO','Small','Medium','Big'])
    # with col34:
    #     pavilionnatural = st.selectbox("PAVILION_NATURAL", options=['No','Idented','Natural','Big Natural'])
    with col35:
        green = st.selectbox("GREEN", options=['No', 'G1', 'G2', 'G3', 'G4'])
        dictCsv['GREEN'] = green
    with col36:
        grey = st.selectbox("GREY", options=['No', 'MT1', 'MT2', 'MT3'])
        dictCsv['GREY'] = grey
    with col37:
        brown = st.selectbox("BROWN", options=['0', 'B1', 'B2', 'B3'])
        dictCsv['BROWN'] = brown
    with col38:
        milky = st.selectbox("MILKY", options=['No', 'M1+', 'M1', 'M2', 'M3'])
        dictCsv['MILKY'] = milky
    with col39:
        days = st.number_input("Days")
        dictCsv['REF_DAYS'] = days
    with col40:
        tableopen = st.selectbox("TABLE_OPEN", options=['No', 'OHT', 'OT1', 'OT2', 'OT3'])
        dictCsv['TABLE_OPEN'] = tableopen
    with col41:
        crownopen = st.selectbox("CROWN_OPEN", options=['No', 'OHC', 'OC1', 'OC2', 'OC3'])
        dictCsv['CROWN_OPEN'] = crownopen
    with col42:
        girdleopen = st.selectbox("GIRDLE_OPEN", options=['No', 'OHG', 'OG1', 'OG2', 'OG3'])
        dictCsv['GIRDLE_OPEN'] = girdleopen
    with col43:
        pavilionopen = st.selectbox("PAVILION_OPEN", options=['No', 'OHP', 'OP1', 'OP2', 'OP3'])
        dictCsv['PAVILION_OPEN'] = pavilionopen
    with col44:
        topnatural = st.selectbox("Top_Natural", options=['No', 'INT', 'NC1', 'NC2', 'NC3'])
        dictCsv['Top_Natural'] = topnatural
    with col45:
        crownnatural = st.selectbox("Crown_Natural", options=['No', 'INC'])
        dictCsv['Crown_Natural'] = crownnatural
    with col46:
        girdlenatural = st.selectbox("Girdle_Natural", options=['No', 'ING'])
        dictCsv['Girdle_Natural'] = girdlenatural
    with col47:
        pavilionnatural = st.selectbox("Pavilion_Natural", options=['No', 'INP', 'NP1', 'NP2', 'NP3'])
        dictCsv['Pavilion_Natural'] = pavilionnatural
    with col48:
        chip = st.selectbox("CHIP", options=['No', 'Top', 'Bottom', 'Girdle'])
        dictCsv['CHIP'] = chip
    with col49:
        cavity = st.selectbox("CAVITY", options=['No', 'Top', 'Bottom', 'Girdle'])
        dictCsv['CAVITY'] = cavity
    with col50:
        upgrade1 = st.selectbox("Upgrade_Color",
                                options=['0', '0.5 Color', '1 Color', '1.5 Color', '2 Color', '2.5 Color'])
        dictCsv['Upgrade_Color'] = upgrade1
    with col51:
        upgrade2 = st.selectbox("Upgrade_Clarity",
                                options=['0', '0.5 Clarity', '1 Clarity', '1.5 Clarity', '2 Clarity', '2.5 Clarity'])
        dictCsv['Upgrade_Clarity'] = upgrade2
    with col52:
        downgrade1 = st.selectbox("Downgrade_Color",
                                  options=['0', '0.5 Color', '1 Color', '1.5 Color', '2 Color', '2.5 Color'])
        dictCsv['Downgrade_Color'] = downgrade1
    with col53:
        downgrade2 = st.selectbox("Downgrade_Clarity",
                                  options=['0', '0.5 Clarity', '1 Clarity', '1.5 Clarity', '2 Clarity', '2.5 Clarity'])
        dictCsv['Downgrade_Clarity'] = downgrade2

        # TO DO- WRITE FINISHING, PUT OPTIONS ACCORDINGLY, BGMROELSE

        min_diam = ''
        max_diam = ''
        tabl = ''
        height = ''
        ratio = ''
        col_shade = ''
        cr_angle = ''
        cr_height = ''
        pv_angle = ''
        pv_depth = ''
        girdle_percentage = ''
        girdle_from = ''
        girdle_to = ''
        girdle_condition = ''
        star_length = ''
        lower_half = ''
        open1 = ''
        natural = ''
        intended_natural = ''
        extra_facet = ''
        graining = ''
        cavity = ''
        chip = ''
        rap_value = ''

    result = calcDiscount(shape, szgr, color, clarity, cut, polish, symmetry, fluo, rap, ktos, sizeprec, tableclean,
                          eyeclean, ha, cutcomments, diameter, internalgraining, surfacegraining, flawless,
                          tableintensity, crownintensity, topef, topcavity, topchip, crownef, crowncavity, crownchip,
                          girdleef, girdlecavity, girdlechip, pavilionef, pavilioncavity, pavilionchip, depth, green,
                          grey, brown, milky, tableopen, crownopen, girdleopen, pavilionopen, topnatural, crownnatural,
                          girdlenatural, pavilionnatural, chip, cavity, upgrade1, upgrade2, downgrade1, downgrade2, days,
                          min_diam, max_diam, tabl, height, ratio, col_shade,
                          cr_angle,
                          cr_height, pv_angle, pv_depth, girdle_percentage,
                          girdle_from, girdle_to, girdle_condition,
                          star_length, lower_half, open, natural,
                          intended_natural, extra_facet, graining, rap_value
                          )



    st.text("\n")

    if st.button("Calculate Final Price"):
        if int(rap) != 0:
            st.markdown(
                f"<big><b>Discount(in Percentage wrt RAP):</b> </big><font color='green' size=6>{(result)} </font>",
                unsafe_allow_html=True)
            st.download_button('Download CSV', pd.DataFrame(dictCsv, index=[0]).to_csv(index=False),
                               mime='text/csv', file_name='sampleinput2.csv')
        else:
            st.error("Please input proper values")
