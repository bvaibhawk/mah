import pandas as pd


def calcDiscount(shape, szgr, color, clarity, cut, polish, symmetry, fluo, rap, ktos, sizeprec, tableclean,
                 eyeclean, ha, cutcomments, diameter, internalgraining, surfacegraining, flawless,
                 tableintensity, crownintensity, topef, topcavity, topchip, crownef, crowncavity, crownchip,
                 girdleef, girdlecavity, girdlechip, pavilionef, pavilioncavity, pavilionchip, depth, green,
                 grey, brown, milky, tableopen, crownopen, girdleopen, pavilionopen, topnatural, crownnatural,
                 girdlenatural, pavilionnatural, chip, cavity, upgrade1, upgrade2, downgrade1, downgrade2, days,
                 min_diam, max_diam, tabl, height, ratio, col_shade, cr_angle, cr_height, pv_angle,
                 pv_depth,
                 girdle_percentage, girdle_from, girdle_to, girdle_condition, star_length,
                 lower_half,
                 open, natural, intended_natural, extra_facet, graining, rap_value
                 ):
    # test_df = pd.DataFrame({'SZ GR':[szgr], 'CERTCT':[certct], 'COLOR':[color_dict[color]], 'CLARITY':[clarity_dict[clarity]], 'CUT':[cut],
    #                       'POLISH':[polish], 'SYMMETRY':[symmetry], 'FLUO':[fluo], 'rap':[rap], 'PUR RAP DIS':[pur_rap_dis]})
    df = pd.read_csv('Toamin.csv')
    result = 0.00
    ff = 0
    xx = 0
    if (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2'):
        if color == 'D' or color == 'E' or color == 'F':
            xx = 1
        if color == 'G' or color == 'H' or color == 'I':
            xx = 2
        if color == 'J' or color == 'K' or color == 'L' or color == 'M':
            xx = 3
    if (clarity == 'VS1' or clarity == 'VS2'):
        if color == 'D' or color == 'E' or color == 'F':
            xx = 4
        if color == 'G' or color == 'H' or color == 'I':
            xx = 5
        if color == 'J' or color == 'K' or color == 'L' or color == 'M':
            xx = 6
    if (clarity == 'SI1' or clarity == 'SI2' or clarity == 'I1'):
        if color == 'D' or color == 'E' or color == 'F':
            xx = 7
        if color == 'G' or color == 'H' or color == 'I':
            xx = 8
        if color == 'J' or color == 'K' or color == 'L' or color == 'M':
            xx = 9
    for i in range(len(df)):
        # and polish == df['POL'][i] and symmetry == df['SYM'][i]
        if shape == df['Shape'][i] and color == df['COLOR'][i] and clarity == df['CLARITY'][i] and cut == df['CUT'][
            i] and fluo == df['FLUO'][i] and szgr == df['Size'][i]:
            if (cut == 'EX' and polish == 'EX' and symmetry == 'EX'):
                if (polish == df['POL'][i] and symmetry == df['SYM'][i]):
                    result = df['Discount'][i]
                    ff = 1
            else:
                if (cut == df['CUT'][i] and df['POL'][i] == 'EX' and df['SYM'][i] == 'EX'):
                    result = result
                elif (cut == df['CUT'][i]):
                    result = df['Discount'][i]
                    ff = 1

    temp = result

    if ff == 1:

        result = result * 100
        temp = result

        if shape == 'RO':
            if sizeprec >= 1.00 and sizeprec <= 1.499 and cut == 'EX':
                if color == 'D':
                    result = result + 3
                else:
                    result = result + 2
            if sizeprec >= 1.50 and sizeprec <= 1.999 and cut == 'EX':
                if color == 'D':
                    result = result + 2
                else:
                    result = result + 1
            if sizeprec >= 2.00 and sizeprec <= 2.999 and cut == 'EX':
                if color == 'D':
                    result = result + 2
                else:
                    result = result + 1

            if xx == 1:
                if ktos == 1:
                    result = result + 1.0
                elif ktos >= 5:
                    result = -1.0 + result
            elif xx == 2:
                if ktos == 1:
                    result = result + 1.0
                elif ktos >= 5:
                    result = -1.0 + result
            elif xx == 3:
                if ktos == 1:
                    result = result + 1.0
                elif ktos >= 5:
                    result = -1.0 + result
            elif xx == 4:
                if ktos == 1:
                    result = result + 1.5
                elif ktos >= 5:
                    result = -1.0 + result
            elif xx == 5:
                if ktos == 1:
                    result = result + 1.5
                if ktos >= 5:
                    result = -1.0 + result
            elif xx == 6:
                if ktos == 1:
                    result = result + 1.0
                if ktos >= 5:
                    result = 0.0 + result
            elif xx == 1:
                if ktos == 1:
                    result = result + 3.0
                if ktos >= 5:
                    result = 0.0 + result

                    # colour
            if color == 'M':
                if szgr == '1.01-1.09' or szgr == '2.01-2.09' or szgr == '1.50-1.69':
                    if cut == 'EX':
                        result = -7 + result

            # if szgr=='1.01-1.09' or szgr=='1.50-1.69' or szgr=='2.01-2.09':
            #     if cut=='VG':
    else:
        df2 = pd.read_csv('toaminfancy.csv')
        result = 0.00

        for i in range(len(df2)):
            if clarity == 'IF':
                if shape == df2['Shape'][i] and color == df2['EX'][i] and szgr == df2['Size'][i]:
                    result = df2['IF'][i]
                    ff = 2
                    break
            elif clarity == 'VVS1':
                if shape == df2['Shape'][i] and color == df2['EX'][i] and szgr == df2['Size'][i]:
                    result = df2['VVS1'][i]
                    ff = 2
                    break
            elif clarity == 'VVS2':
                if shape == df2['Shape'][i] and color == df2['EX'][i] and szgr == df2['Size'][i]:
                    result = df2['VVS2'][i]
                    ff = 2
                    break
            elif clarity == 'VS1':
                if shape == df2['Shape'][i] and color == df2['EX'][i] and szgr == df2['Size'][i]:
                    result = df2['VS1'][i]
                    ff = 2
                    break
            elif clarity == 'VS2':
                if shape == df2['Shape'][i] and color == df2['EX'][i] and szgr == df2['Size'][i]:
                    result = df2['VS2'][i]
                    ff = 2
                    break
            elif clarity == 'SI1':
                if shape == df2['Shape'][i] and color == df2['EX'][i] and szgr == df2['Size'][i]:
                    result = df2['SI1'][i]
                    ff = 2
                    break
            elif clarity == 'SI2':
                if shape == df2['Shape'][i] and color == df2['EX'][i] and szgr == df2['Size'][i]:
                    result = df2['SI2'][i]
                    ff = 2
                    break
            temp = result
        if ff == 0:
            df = pd.read_csv('Dossbase.csv')
            for i in range(len(df)):
                if (df['Clarity'][i] == clarity and szgr == df['Size'][i] and df['Fluo'][i] == fluo):
                    if cut == 'EX' and polish == 'EX' and symmetry == 'EX':
                        if df['Cut'][i] == 'EX' and df['Polish'][i] == 'EX' and df['Symmetry'][i] == 'EX':
                            if color == 'D':
                                result = result + df['D'][i]
                                ff = 1
                            elif color == 'E':
                                result = result + df['E'][i]
                                ff = 1
                            elif color == 'F':
                                result = result + df['F'][i]
                                ff = 1
                            elif color == 'G':
                                result = result + df['G'][i]
                                ff = 1
                            elif color == 'H':
                                result = result + df['H'][i]
                                ff = 1
                            elif color == 'I':
                                result = result + df['I'][i]
                                ff = 1
                            elif color == 'J':
                                result = result + df['J'][i]
                                ff = 1
                            elif color == 'L':
                                result = result + df['L'][i]
                                ff = 1
                            elif color == 'M' or color == 'N':
                                result = result + df['M'][i]
                                color = 'M'
                                result = result - 7
                                ff = 1
                            elif color == 'K':
                                result = result + df['K'][i]
                                ff = 1
                            break
                    else:
                        # if(cut==df['CUT'][i] and df['POL'][i] == 'EX' and df['SYM'][i] == 'EX'):
                        #     continue
                        if (cut == df['Cut'][i] and df['Polish'][i] == 'DD' and df['Symmetry'][i] == 'DD'):
                            if color == 'D':
                                result = result + df['D'][i]
                                ff = 1
                            elif color == 'E':
                                result = result + df['E'][i]
                                ff = 1
                            elif color == 'F':
                                result = result + df['F'][i]
                                ff = 1
                            elif color == 'G':
                                result = result + df['G'][i]
                                ff = 1
                            elif color == 'H':
                                result = result + df['H'][i]
                                ff = 1
                            elif color == 'I':
                                result = result + df['I'][i]
                                ff = 1
                            elif color == 'J':
                                result = result + df['J'][i]
                                ff = 1
                            elif color == 'L':
                                result = result + df['L'][i]
                                ff = 1
                            elif color == 'M':
                                result = result + df['M'][i]
                                ff = 1
                            elif color == 'K':
                                result = result + df['K'][i]
                                ff = 1
                            break
            temp = result

            # DIAMETER
    if (shape == 'RO'):
        if sizeprec >= 1.0 and sizeprec <= 1.49:
            if cut == 'VG':
                if (xx == 1):
                    if diameter <= 6.2:
                        result = result - 0.5
                    elif diameter >= 6.3:
                        result = result + 1.5
                elif (xx == 2):
                    if diameter <= 6.2:
                        result = result - 0.5
                    elif diameter >= 6.3:
                        result = result + 1.5
                elif (xx == 3 or xx == 4):
                    if diameter <= 6.2:
                        result = result - 0.5
                    elif diameter >= 6.3:
                        result = result + 1.5
                elif (xx == 5):
                    if diameter <= 6.2:
                        result = result - 0.1
                    elif diameter >= 6.3:
                        result = result + 1.5
                elif (xx == 6):
                    if diameter <= 6.2:
                        result = result - 0.5
                    elif diameter >= 6.3:
                        result = result + 1.5
                elif (xx == 7):
                    if diameter <= 6.2:
                        result = result - 0.0
                    elif diameter >= 6.3:
                        result = result + 1.0
                elif (xx == 8):
                    if diameter <= 6.2:
                        result = result - 0.0
                    elif diameter >= 6.3:
                        result = result + 1.0
        if cut == 'EX' and polish == 'EX' and symmetry == 'EX' and (fluo == 'None' or fluo == 'Faint'):
            if sizeprec >= 0.35 and sizeprec <= 0.399 and diameter > 4.5:
                if color == 'D':
                    if clarity == 'IF':
                        result = result + 9
                    elif clarity == 'VVS1':
                        result = result + 14
                    elif clarity == 'VVS2':
                        result = result + 21
                if color == 'E':
                    if clarity == 'IF':
                        result = result + 7
                    elif clarity == 'VVS1':
                        result = result + 8
                    elif clarity == 'VVS2':
                        result = result + 2
                if color == 'F':
                    if clarity == 'IF':
                        result = result + 7
                    elif clarity == 'VVS1':
                        result = result + 7
                    elif clarity == 'VVS2':
                        result = result + 2
            if sizeprec >= 0.60 and sizeprec <= 0.649 and diameter > 5.4:
                if color == 'D':
                    if clarity == 'IF':
                        result = result + 6
                    elif clarity == 'VVS1':
                        result = result + 9
                    elif clarity == 'VVS2':
                        result = result + 9
                if color == 'E':
                    if clarity == 'IF':
                        result = result + 7
                    elif clarity == 'VVS1':
                        result = result + 5
                    elif clarity == 'VVS2':
                        result = result + 1
                if color == 'F':
                    if clarity == 'IF':
                        result = result + 6
                    elif clarity == 'VVS1':
                        result = result + 6
                    elif clarity == 'VVS2':
                        result = result + 1
            if sizeprec >= 0.80 and sizeprec <= 0.849 and diameter > 6.0:
                if color == 'D':
                    if clarity == 'IF':
                        result = result + 16
                    elif clarity == 'VVS1':
                        result = result + 10
                    elif clarity == 'VVS2':
                        result = result + 11
                if color == 'E':
                    if clarity == 'IF':
                        result = result + 5
                    elif clarity == 'VVS1':
                        result = result + 4
                    elif clarity == 'VVS2':
                        result = result + 13
                if color == 'F':
                    if clarity == 'IF':
                        result = result + 9
                    elif clarity == 'VVS1':
                        result = result + 9
                    elif clarity == 'VVS2':
                        result = result + 13
            if sizeprec >= 0.95 and sizeprec <= 0.999 and diameter > 6.3:
                if color == 'D':
                    if clarity == 'IF':
                        result = result + 5
                    elif clarity == 'VVS1':
                        result = result + 6
                    elif clarity == 'VVS2':
                        result = result + 7
                if color == 'E':
                    if clarity == 'IF':
                        result = result + 6
                    elif clarity == 'VVS1':
                        result = result + 5
                    elif clarity == 'VVS2':
                        result = result + 5
                if color == 'F':
                    if clarity == 'IF':
                        result = result + 6
                    elif clarity == 'VVS1':
                        result = result + 6
                    elif clarity == 'VVS2':
                        result = result + 5

                        # bgm- Note- need to ask whether it is one exculsive table or multiple table combined- currently considered one exclusive table
    if (((cut == 'EX' or cut == 'VG') & (polish == 'EX' or polish == 'VG') & (symmetry == 'EX' or symmetry == 'VG')) & (
            fluo == 'None' or fluo == 'Medium')):
        df3 = pd.read_csv('bgmvg.csv')
        # BROWN
        for i in range(len(df3)):
            # next line giving eror
            if ((shape == 'RO') & (xx == df3['Section'][i]) & (brown == df3['bgm'][i]) & (df3['Shape'][i] == 'RO')):
                result = result + df3['Discount'][i]
                break
            elif ((shape != 'RO') & (xx == df3['Section'][i]) & (brown == df3['bgm'][i]) & (
                    df3['Shape'][i] == 'FANCY')):
                result = result + df3['Discount'][i]
                break

        # GREY
        for i in range(len(df3)):
            # next line giving eror
            if ((shape == 'RO') & (xx == df3['Section'][i]) & (grey == df3['bgm'][i]) & (df3['Shape'][i] == 'RO')):
                result = result + df3['Discount'][i]
                break
            elif ((shape != 'RO') & (xx == df3['Section'][i]) & (grey == df3['bgm'][i]) & (df3['Shape'][i] == 'FANCY')):
                result = result + df3['Discount'][i]
                break
                # GREEN
        for i in range(len(df3)):
            # next line giving eror
            if ((shape == 'RO') & (xx == df3['Section'][i]) & (green == df3['bgm'][i]) & (df3['Shape'][i] == 'RO')):
                result = result + float(df3['Discount'][i])
                break
            elif ((shape != 'RO') & (xx == df3['Section'][i]) & (green == df3['bgm'][i]) & (
                    df3['Shape'][i] == 'FANCY')):
                result = result + float(df3['Discount'][i])
                break
                # MILKY
        for i in range(len(df3)):
            # next line giving eror
            if ((shape == 'RO') & (xx == df3['Section'][i]) & (milky == df3['bgm'][i]) & (df3['Shape'][i] == 'RO')):
                result = result + float(df3['Discount'][i])
                break
            elif ((shape != 'RO') & (xx == df3['Section'][i]) & (milky == df3['bgm'][i]) & (
                    df3['Shape'][i] == 'FANCY')):
                result = result + float(df3['Discount'][i])
                break
                # #OFFCOLOR
                # for i in range(len(df3)):
                #     #next line giving eror
                #     if ((shape == 'RO') & (xx == df3['Section'][i]) & (offcolor == df3['bgm'][i]) & (df3['Shape'][i]=='RO') ):
                #         result=result+df3['Discount'][i]
                #         break
                #     elif ((shape!='RO') & (xx == df3['Section'][i]) & ( offcolor == df3['bgm'][i]) & (df3['Shape'][i]=='FANCY')):
                #         result=result+df3['Discount'][i]
                break
    else:
        df3 = pd.read_csv('bgmroelse.csv')
        for i in range(len(df3)):
            if ((shape == 'RO') & (xx == df3['Section'][i]) & (brown == df3['bgm'][i])):
                result = result + df3['Discount'][i]
                break
        for i in range(len(df3)):
            if ((shape == 'RO') & (xx == df3['Section'][i]) & (green == df3['bgm'][i])):
                result = result + df3['Discount'][i]
                break
        for i in range(len(df3)):
            if ((shape == 'RO') & (xx == df3['Section'][i]) & (grey == df3['bgm'][i])):
                result = result + df3['Discount'][i]
                break
        for i in range(len(df3)):
            if ((shape == 'RO') & (xx == df3['Section'][i]) & (milky == df3['bgm'][i])):
                result = result + df3['Discount'][i]
                break
                # for i in range(len(df3)):
        #     if ((shape == 'RO') & (xx == df3['Section'][i]) & (offcolor == df3['bgm'][i])):
        #         result=result+df3['Discount'][i]
        #         break
    # add dossiers as well-irrelevant I guess now

    # Cut
    if ((fluo == 'MED') and (cutcomments == 'VG->VG2' or cutcomments == 'G->GD2')) or shape != 'RO':
        result = result
    else:
        if cutcomments == '3EX->EX2':
            if (xx == 1):
                result = result - 2.0
            elif (xx == 2):
                result = result - 2.0
            elif (xx == 3):
                result = result - 1.0
            elif (xx == 4):
                result = result - 2.0
            elif (xx == 5):
                result = result - 2.0
            elif (xx == 6):
                result = result - 1.0
            elif (xx == 7):
                result = result - 1.0
            elif (xx == 8):
                result = result - 1.0
            elif (xx == 9):
                result = result - 0.5

        if cutcomments == 'EX->EX2':
            if (xx == 1):
                result = result - 2.0
            elif (xx == 2):
                result = result - 2.0
            elif (xx == 3):
                result = result - 1.0
            elif (xx == 4):
                result = result - 2.0
            elif (xx == 5):
                result = result - 2.0
            elif (xx == 6):
                result = result - 1.0
            elif (xx == 7):
                result = result - 1.5
            elif (xx == 8):
                result = result - 1.5
            elif (xx == 9):
                result = result - 0.5
        if cutcomments == 'VG->VG1':
            if (xx == 1):
                result = result + 2.0
            elif (xx == 2):
                result = result + 2.0
            elif (xx == 3):
                result = result + 2.0
            elif (xx == 4):
                result = result + 2.0
            elif (xx == 5):
                result = result + 2.0
            elif (xx == 6):
                result = result + 1.5
            elif (xx == 7):
                result = result + 1.5
            elif (xx == 8):
                result = result + 1.0
            elif (xx == 9):
                result = result + 1.0

    # Graining- add vg+ condition and the extra comment-done
    # if internalgraining=='IGR2':
    #     if xx==1 or xx==2:
    #         result=result-1.5
    #     elif xx==3 or xx==4 or xx==5:
    #         result=result-1.0
    #     elif xx==6:
    #         result=result-0.5
    # elif internalgraining =='Internal->GR3':
    #     if xx==1 or xx==2:
    #         result=result-3.0
    #     elif xx==3 or xx==4 or xx==5:
    #         result=result-3.0
    #     elif xx==6:
    #         result=result-1.0
    # elif graining=='Surface->SGR2':
    #     if xx ==1 or xx==2:
    #         result=result-1.5
    #     elif xx==3 or xx==5 or xx==6:
    #         result=result-1
    if (fluo == 'Faint' or fluo == 'Medium' or fluo == 'None') and ((shape == 'RO' and (
            cut == 'VG' or cut == 'EX') and (polish == 'VG' or polish == 'EX') and (
                                                                             symmetry == 'VG' or symmetry == 'EX')) or (
                                                                            shape != 'RO' and (
                                                                            polish == 'VG' or polish == 'EX') and (
                                                                                    symmetry == 'VG' or symmetry == 'EX'))):
        if (surfacegraining == '0' or internalgraining == '0' or surfacegraining == 'NN' or internalgraining == 'NN'):
            df21 = pd.read_csv('graining.csv')
            for i in range(len(df21)):
                if surfacegraining == df21['Graining'][i]:
                    if xx == 1:
                        result = result + df21['1'][i]
                    if xx == 2:
                        result = result + df21['2'][i]
                    if xx == 3:
                        result = result + df21['3'][i]
                    if xx == 4:
                        result = result + df21['4'][i]
                    if xx == 5:
                        result = result + df21['5'][i]
                    if xx == 6:
                        result = result + df21['6'][i]
                    if xx == 7:
                        result = result + df21['7'][i]
                    if xx == 8:
                        result = result + df21['8'][i]
                    if xx == 9:
                        result = result + df21['9'][i]
                    break
            for i in range(len(df21)):
                if internalgraining == df21['Graining'][i]:
                    if xx == 1:
                        result = result + df21['1'][i]
                    if xx == 2:
                        result = result + df21['2'][i]
                    if xx == 3:
                        result = result + df21['3'][i]
                    if xx == 4:
                        result = result + df21['4'][i]
                    if xx == 5:
                        result = result + df21['5'][i]
                    if xx == 6:
                        result = result + df21['6'][i]
                    if xx == 7:
                        result = result + df21['7'][i]
                    if xx == 8:
                        result = result + df21['8'][i]
                    if xx == 9:
                        result = result + df21['9'][i]
                    break
        else:
            df21 = pd.read_csv('graining.csv')
            result1 = 0
            result2 = 0
            for i in range(len(df21)):
                if surfacegraining == df21['Graining'][i]:
                    if xx == 1:
                        result1 = result1 + df21['1'][i]
                    if xx == 2:
                        result1 = result1 + df21['2'][i]
                    if xx == 3:
                        result1 = result1 + df21['3'][i]
                    if xx == 4:
                        result1 = result1 + df21['4'][i]
                    if xx == 5:
                        result1 = result1 + df21['5'][i]
                    if xx == 6:
                        result1 = result1 + df21['6'][i]
                    if xx == 7:
                        result1 = result1 + df21['7'][i]
                    if xx == 8:
                        result1 = result1 + df21['8'][i]
                    if xx == 9:
                        result1 = result1 + df21['9'][i]
                    break
            for i in range(len(df21)):
                if internalgraining == df21['Graining'][i]:
                    if xx == 1:
                        result2 = result2 + df21['1'][i]
                    if xx == 2:
                        result2 = result2 + df21['2'][i]
                    if xx == 3:
                        result2 = result2 + df21['3'][i]
                    if xx == 4:
                        result2 = result2 + df21['4'][i]
                    if xx == 5:
                        result2 = result2 + df21['5'][i]
                    if xx == 6:
                        result2 = result2 + df21['6'][i]
                    if xx == 7:
                        result2 = result2 + df21['7'][i]
                    if xx == 8:
                        result2 = result2 + df21['8'][i]
                    if xx == 9:
                        result2 = result2 + df21['9'][i]
                    break
            if (result1 >= result2):
                result = result + result1
            else:
                result = result + result2

    if ha == 'Yes':
        if shape == 'RO':
            if xx == 1:
                result = result + 1
            if xx == 2:
                result = result + 1
            if xx == 3:
                result = result + 0.5
            if xx == 4:
                result = result + 1
            if xx == 5:
                result = result + 1
            if xx == 6:
                result = result + 0.5
            if xx == 7:
                result = result + 1
            if xx == 8:
                result = result + 1
            if xx == 9:
                result = result + 0
    if eyeclean == 'Yes':
        if shape == 'RO':
            if xx == 7:
                result = result + 1.5
            if xx == 8:
                result = result + 1.5
            if xx == 9:
                result = result + 1
        else:
            if xx == 7:
                result = result + 1.5
            if xx == 8:
                result = result + 1.5
            if xx == 9 or xx == 5 or xx == 6:
                result = result + 0.5
    if tableclean == 'Yes':
        if shape == 'RO':
            if xx == 4 or xx == 5 or xx == 6:
                result = result + 0.5
            if xx == 8 or xx == 7:
                result = result + 2.0
            if xx == 9:
                result = result + 1
        else:
            if xx == 4 or xx == 5:
                result = result + 1.0
            if xx == 8 or xx == 7:
                result = result + 2.0
            if xx == 9:
                result = result + 1

                # #extras- NOT properly written- change line 445
    # df4=pd.read_csv('extras.csv')
    # for i in range(len(df4)):
    #     if(shape=='RO'):
    #         if(df4['extras'][i]=='H&A' and df4['shape'][i]=='RO' ):
    #             if(df4['value'][i]==ha):
    # if xx==1:
    #     result=result+df4['1'][i]
    # if xx==2:
    #     result=result+df4['2'][i]
    # if xx==3:
    #     result=result+df4['3'][i]
    # if xx==4:
    #     result=result+df4['4'][i]
    # if xx==5:
    #     result=result+df4['5'][i]
    # if xx==6:
    #     result=result+df4['6'][i]
    # if xx==7:
    #     result=result+df4['7'][i]
    # if xx==8:
    #     result=result+df4['8'][i]
    # if xx==9:
    #                     result=result+df4['9'][i]
    #         if(df4['extras'][i]=='Eye Clean' and df4['shape'][i]=='RO' ):
    #             if(df4['value'][i]==eyeclean):
    #                 if xx==1:
    #                     result=result+df4['1'][i]
    #                 elif xx==2:
    #                     result=result+df4['2'][i]
    #                 elif xx==3:
    #                     result=result+df4['3'][i]
    #                 elif xx==4:
    #                     result=result+df4['4'][i]
    #                 elif xx==5:
    #                     result=result+df4['5'][i]
    #                 elif xx==6:
    #                     result=result+df4['6'][i]
    #                 elif xx==7:
    #                     result=result+df4['7'][i]
    #                 elif xx==8:
    #                     result=result+df4['8'][i]
    #                 elif xx==9:
    #                     result=result+df4['9'][i]
    #         if(df4['extras'][i]=='Table Clean' and df4['shape'][i]=='RO' ):
    #             if(df4['value'][i]==tableclean):
    #                 if xx==1:
    #                     result=result+df4['1'][i]
    #                 elif xx==2:
    #                     result=result+df4['2'][i]
    #                 elif xx==3:
    #                     result=result+df4['3'][i]
    #                 elif xx==4:
    #                     result=result+df4['4'][i]
    #                 elif xx==5:
    #                     result=result+df4['5'][i]
    #                 elif xx==6:
    #                     result=result+df4['6'][i]
    #                 elif xx==7:
    #                     result=result+df4['7'][i]
    #                 elif xx==8:
    #                     result=result+df4['8'][i]
    #                 elif xx==9:
    #                     result=result+df4['9'][i]

    #     if(shape!='RO'):
    #         if(df4['extras'][i]=='H&A' and df4['shape'][i]=='Fancy'):
    #             if(df4['value'][i]==ha):
    #                 if xx==1:
    #                     result=result+df4['1'][i]
    #                 if xx==2:
    #                     result=result+df4['2'][i]
    #                 if xx==3:
    #                     result=result+df4['3'][i]
    #                 if xx==4:
    #                     result=result+df4['4'][i]
    #                 if xx==5:
    #                     result=result+df4['5'][i]
    #                 if xx==6:
    #                     result=result+df4['6'][i]
    #                 if xx==7:
    #                     result=result+df4['7'][i]
    #                 if xx==8:
    #                     result=result+df4['8'][i]
    #                 if xx==9:
    #                     result=result+df4['9'][i]
    #         if(df4['extras'][i]=='Eye Clean' and df4['shape'][i]=='FANCY' ):
    #             if(df4['value'][i]==eyeclean):
    #                 if xx==1:
    #                     result=result+df4['1'][i]
    #                 if xx==2:
    #                     result=result+df4['2'][i]
    #                 if xx==3:
    #                     result=result+df4['3'][i]
    #                 if xx==4:
    #                     result=result+df4['4'][i]
    #                 if xx==5:
    #                     result=result+df4['5'][i]
    #                 if xx==6:
    #                     result=result+df4['6'][i]
    #                 if xx==7:
    #                     result=result+df4['7'][i]
    #                 if xx==8:
    #                     result=result+df4['8'][i]
    #                 if xx==9:
    #                     result=result+df4['9'][i]
    #         if(df4['extras'][i]=='Table Clean' and df4['shape'][i]=='FANCY' ):
    #             if(df4['value'][i]==tableclean):
    #                 if xx==1:
    #                     result=result+df4['1'][i]
    #                 if xx==2:
    #                     result=result+df4['2'][i]
    #                 if xx==3:
    #                     result=result+df4['3'][i]
    #                 if xx==4:
    #                     result=result+df4['4'][i]
    #                 if xx==5:
    #                     result=result+df4['5'][i]
    #                 if xx==6:
    #                     result=result+df4['6'][i]
    #                 if xx==7:
    #                     result=result+df4['7'][i]
    #                 if xx==8:
    #                     result=result+df4['8'][i]
    #                 if xx==9:
    #                     result=result+df4['9'][i]

    # Inclusion Grading
    # df5=pd.read_csv('inc_grad.csv')
    # for i in range(len(df5)):
    #     #table
    #     if(df5['Location'][i]=='Table'):
    #         if(df5['Shape'][i]==shape and (clarity==df5['CL1'][i] or clarity==df5['CL2'][i]) and df5['Inclusion'][i]==tableinc):
    #             if xx==1:
    #                 result=result+df5['1'][i]
    #             if xx==2:
    #                 result=result+df5['2'][i]
    #             if xx==3:
    #                 result=result+df5['3'][i]
    #             if xx==4:
    #                 result=result+df5['4'][i]
    #             if xx==5:
    #                 result=result+df5['5'][i]
    #             if xx==6:
    #                 result=result+df5['6'][i]
    #             if xx==7:
    #                 result=result+df5['7'][i]
    #             if xx==8:
    #                 result=result+df5['8'][i]
    #             if xx==9:
    #                 result=result+df5['9'][i]
    #             break
    # for i in range(len(df5)):
    #     #crown
    #     if(df5['Location'][i]=='Crown'):
    #         if(df5['Shape'][i]==shape and (clarity==df5['CL1'][i] or clarity==df5['CL2'][i]) and df5['Inclusion'][i]==crowninc):
    #             if xx==1:
    #                 result=result+df5['1'][i]
    #             if xx==2:
    #                 result=result+df5['2'][i]
    #             if xx==3:
    #                 result=result+df5['3'][i]
    #             if xx==4:
    #                 result=result+df5['4'][i]
    #             if xx==5:
    #                 result=result+df5['5'][i]
    #             if xx==6:
    #                 result=result+df5['6'][i]
    #             if xx==7:
    #                 result=result+df5['7'][i]
    #             if xx==8:
    #                 result=result+df5['8'][i]
    #             if xx==9:
    #                 result=result+df5['9'][i]
    #             break
    # for i in range(len(df5)):
    #     #girdle
    #     if(df5['Location'][i]=='Girdle'):
    #         if(df5['Shape'][i]==shape and (clarity==df5['CL1'][i] or clarity==df5['CL2'][i]) and df5['Inclusion'][i]==girdle_inc):
    #             if xx==1:
    #                 result=result+df5['1'][i]
    #             if xx==2:
    #                 result=result+df5['2'][i]
    #             if xx==3:
    #                 result=result+df5['3'][i]
    #             if xx==4:
    #                 result=result+df5['4'][i]
    #             if xx==5:
    #                 result=result+df5['5'][i]
    #             if xx==6:
    #                 result=result+df5['6'][i]
    #             if xx==7:
    #                 result=result+df5['7'][i]
    #             if xx==8:
    #                 result=result+df5['8'][i]
    #             if xx==9:
    #                 result=result+df5['9'][i]
    #             break
    # for i in range(len(df5)):
    #     #pavilion
    #     if(df5['Location'][i]=='Pavilion'):
    #         if(df5['Shape'][i]==shape and (clarity==df5['CL1'][i] or clarity==df5['CL2'][i]) and df5['Inclusion'][i]==pavilioninc):
    #             if xx==1:
    #                 result=result+df5['1'][i]
    #             if xx==2:
    #                 result=result+df5['2'][i]
    #             if xx==3:
    #                 result=result+df5['3'][i]
    #             if xx==4:
    #                 result=result+df5['4'][i]
    #             if xx==5:
    #                 result=result+df5['5'][i]
    #             if xx==6:
    #                 result=result+df5['6'][i]
    #             if xx==7:
    #                 result=result+df5['7'][i]
    #             if xx==8:
    #                 result=result+df5['8'][i]
    #             if xx==9:
    #                 result=result+df5['9'][i]
    #             break

    # BLACK
    #  (sizeprec<=df6['sizemax'][i]) & (cut==df6['cut'][i]) & (df6['Intensity']==tableintensity)
    df6 = pd.read_csv('black.csv')
    for i in range(len(df6)):
        # table
        if (df6['Location'][i] == 'Table'):
            if (df6['Shape'][i] == shape and shape == 'RO'):
                if ((sizeprec >= df6['sizemin'][i]) & (cut == df6['cut'][i]) & (sizeprec <= df6['sizemax'][i]) & (
                        tableintensity == df6['Intensity'][i])):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':

                        if xx == 1:
                            result = result + df6['1'][i]
                        if xx == 2:
                            result = result + df6['2'][i]
                        if xx == 3:
                            result = result + df6['3'][i]
                        if xx == 4:
                            result = result + df6['4'][i]
                        if xx == 5:
                            result = result + df6['5'][i]
                        if xx == 6:
                            result = result + df6['6'][i]
                        if xx == 7:
                            result = result + df6['7'][i]
                        if xx == 8:
                            result = result + df6['8'][i]
                        if xx == 9:
                            result = result + df6['9'][i]
                        break
                    else:
                        if xx == 1:
                            result = result + df6['1'][i] / 2
                        if xx == 2:
                            result = result + df6['2'][i] / 2
                        if xx == 3:
                            result = result + df6['3'][i] / 2
                        if xx == 4:
                            result = result + df6['4'][i] / 2
                        if xx == 5:
                            result = result + df6['5'][i] / 2
                        if xx == 6:
                            result = result + df6['6'][i] / 2
                        if xx == 7:
                            result = result + df6['7'][i] / 2
                        if xx == 8:
                            result = result + df6['8'][i] / 2
                        if xx == 9:
                            result = result + df6['9'][i] / 2
                        break
            if (df6['Shape'][i] == 'Fancy' and shape != 'RO'):
                if (sizeprec >= df6['sizemin'][i] and sizeprec <= df6['sizemax'][i] and df6['symmetry'][
                    i] == symmetry and df6['polish'][i] == polish and df6['Intensity'][i] == tableintensity):
                    if xx == 1:
                        result = result + df6['1'][i]
                    if xx == 2:
                        result = result + df6['2'][i]
                    if xx == 3:
                        result = result + df6['3'][i]
                    if xx == 4:
                        result = result + df6['4'][i]
                    if xx == 5:
                        result = result + df6['5'][i]
                    if xx == 6:
                        result = result + df6['6'][i]
                    if xx == 7:
                        result = result + df6['7'][i]
                    if xx == 8:
                        result = result + df6['8'][i]
                    if xx == 9:
                        result = result + df6['9'][i]
                    break
        # table
    for i in range(len(df6)):
        if (df6['Location'][i] == 'Crown'):
            if (df6['Shape'][i] == shape and shape == 'RO'):
                if (sizeprec >= df6['sizemin'][i] and sizeprec <= df6['sizemax'][i] and cut == df6['cut'][i] and
                        df6['Intensity'][i] == crownintensity):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':

                        if xx == 1:
                            result = result + df6['1'][i]
                        if xx == 2:
                            result = result + df6['2'][i]
                        if xx == 3:
                            result = result + df6['3'][i]
                        if xx == 4:
                            result = result + df6['4'][i]
                        if xx == 5:
                            result = result + df6['5'][i]
                        if xx == 6:
                            result = result + df6['6'][i]
                        if xx == 7:
                            result = result + df6['7'][i]
                        if xx == 8:
                            result = result + df6['8'][i]
                        if xx == 9:
                            result = result + df6['9'][i]
                        break
                    else:
                        if xx == 1:
                            result = result + df6['1'][i] / 2
                        if xx == 2:
                            result = result + df6['2'][i] / 2
                        if xx == 3:
                            result = result + df6['3'][i] / 2
                        if xx == 4:
                            result = result + df6['4'][i] / 2
                        if xx == 5:
                            result = result + df6['5'][i] / 2
                        if xx == 6:
                            result = result + df6['6'][i] / 2
                        if xx == 7:
                            result = result + df6['7'][i] / 2
                        if xx == 8:
                            result = result + df6['8'][i] / 2
                        if xx == 9:
                            result = result + df6['9'][i] / 2
                        break
            if (df6['Shape'][i] == 'Fancy' and shape != 'RO'):
                if (sizeprec >= df6['sizemin'][i] and sizeprec <= df6['sizemax'][i] and df6['symmetry'][
                    i] == symmetry and df6['polish'][i] == polish and df6['Intensity'][i] == crownintensity):
                    if xx == 1:
                        result = result + df6['1'][i]
                    if xx == 2:
                        result = result + df6['2'][i]
                    if xx == 3:
                        result = result + df6['3'][i]
                    if xx == 4:
                        result = result + df6['4'][i]
                    if xx == 5:
                        result = result + df6['5'][i]
                    if xx == 6:
                        result = result + df6['6'][i]
                    if xx == 7:
                        result = result + df6['7'][i]
                    if xx == 8:
                        result = result + df6['8'][i]
                    if xx == 9:
                        result = result + df6['9'][i]
                    break
    for i in range(len(df6)):
        if (df6['Location'][i] == 'Girdle'):
            if (df6['Shape'][i] == shape and shape == 'RO'):
                if (sizeprec >= df6['sizemin'][i] and sizeprec <= df6['sizemax'][i] and cut == df6['cut'][i] and
                        df6['Intensity'][i] == girdleintensity):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':

                        if xx == 1:
                            result = result + df6['1'][i]
                        if xx == 2:
                            result = result + df6['2'][i]
                        if xx == 3:
                            result = result + df6['3'][i]
                        if xx == 4:
                            result = result + df6['4'][i]
                        if xx == 5:
                            result = result + df6['5'][i]
                        if xx == 6:
                            result = result + df6['6'][i]
                        if xx == 7:
                            result = result + df6['7'][i]
                        if xx == 8:
                            result = result + df6['8'][i]
                        if xx == 9:
                            result = result + df6['9'][i]
                        break
                    else:
                        if xx == 1:
                            result = result + df6['1'][i] / 2
                        if xx == 2:
                            result = result + df6['2'][i] / 2
                        if xx == 3:
                            result = result + df6['3'][i] / 2
                        if xx == 4:
                            result = result + df6['4'][i] / 2
                        if xx == 5:
                            result = result + df6['5'][i] / 2
                        if xx == 6:
                            result = result + df6['6'][i] / 2
                        if xx == 7:
                            result = result + df6['7'][i] / 2
                        if xx == 8:
                            result = result + df6['8'][i] / 2
                        if xx == 9:
                            result = result + df6['9'][i] / 2
                        break
            if (df6['Shape'][i] == 'Fancy' and shape != 'RO'):
                if (sizeprec >= df6['sizemin'][i] and sizeprec <= df6['sizemax'][i] and df6['symmetry'][
                    i] == symmetry and df6['polish'][i] == polish and df6['Intensity'][i] == girdleintensity):
                    if xx == 1:
                        result = result + df6['1'][i]
                    if xx == 2:
                        result = result + df6['2'][i]
                    if xx == 3:
                        result = result + df6['3'][i]
                    if xx == 4:
                        result = result + df6['4'][i]
                    if xx == 5:
                        result = result + df6['5'][i]
                    if xx == 6:
                        result = result + df6['6'][i]
                    if xx == 7:
                        result = result + df6['7'][i]
                    if xx == 8:
                        result = result + df6['8'][i]
                    if xx == 9:
                        result = result + df6['9'][i]
                    break
    for i in range(len(df6)):
        if (df6['Location'][i] == 'Pavilion'):
            if (df6['Shape'][i] == shape and shape == 'RO'):
                if (sizeprec >= df6['sizemin'][i] and sizeprec <= df6['sizemax'][i] and cut == df6['cut'][i] and
                        df6['Intensity'][i] == pavilionintensity):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':

                        if xx == 1:
                            result = result + df6['1'][i]
                        if xx == 2:
                            result = result + df6['2'][i]
                        if xx == 3:
                            result = result + df6['3'][i]
                        if xx == 4:
                            result = result + df6['4'][i]
                        if xx == 5:
                            result = result + df6['5'][i]
                        if xx == 6:
                            result = result + df6['6'][i]
                        if xx == 7:
                            result = result + df6['7'][i]
                        if xx == 8:
                            result = result + df6['8'][i]
                        if xx == 9:
                            result = result + df6['9'][i]
                        break
                    else:
                        if xx == 1:
                            result = result + df6['1'][i] / 2
                        if xx == 2:
                            result = result + df6['2'][i] / 2
                        if xx == 3:
                            result = result + df6['3'][i] / 2
                        if xx == 4:
                            result = result + df6['4'][i] / 2
                        if xx == 5:
                            result = result + df6['5'][i] / 2
                        if xx == 6:
                            result = result + df6['6'][i] / 2
                        if xx == 7:
                            result = result + df6['7'][i] / 2
                        if xx == 8:
                            result = result + df6['8'][i] / 2
                        if xx == 9:
                            result = result + df6['9'][i] / 2
                        break
            if (df6['Shape'][i] == 'Fancy' and shape != 'RO'):
                if (sizeprec >= df6['sizemin'][i] and sizeprec <= df6['sizemax'][i] and df6['symmetry'][
                    i] == symmetry and df6['polish'][i] == polish and df6['Intensity'][i] == pavilionintensity):
                    if xx == 1:
                        result = result + df6['1'][i]
                    if xx == 2:
                        result = result + df6['2'][i]
                    if xx == 3:
                        result = result + df6['3'][i]
                    if xx == 4:
                        result = result + df6['4'][i]
                    if xx == 5:
                        result = result + df6['5'][i]
                    if xx == 6:
                        result = result + df6['6'][i]
                    if xx == 7:
                        result = result + df6['7'][i]
                    if xx == 8:
                        result = result + df6['8'][i]
                    if xx == 9:
                        result = result + df6['9'][i]
                    break

                    # sizeprem
    # if ro or fancy
    # if 1-3 or 3-7
    # if if vvs f or not
    if shape == 'RO':
        if sizeprec >= 1.00 and sizeprec <= 2.99:
            if cut == 'EX' and polish == 'EX' and symmetry == 'EX':
                if color == 'F' and (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2'):
                    df7 = pd.read_csv('roexsmF.csv')
                    for i in range(len(df7)):
                        if (sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                            result = result + df7['IF VVS F'][i] / 2
                        else:
                            result = result + df7['IF VVS F'][i]

                else:
                    df7 = pd.read_csv('roexsm.csv')
                    for i in range(len(df7)):
                        if sizeprec >= df7['From'][i] and sizeprec <= df7['To'][i]:
                            if xx == 1:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                                    result = result + df7['1'][i] / 2
                                else:
                                    result = result + df7['1'][i]
                            elif xx == 2:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                                    result = result + df7['2'][i] / 2
                                else:
                                    result = result + df7['2'][i]
                            elif xx == 3:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                                    result = result + df7['3'][i] / 2
                                else:
                                    result = result + df7['3'][i]
                            elif xx == 4:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                                    result = result + df7['4'][i] / 2
                                else:
                                    result = result + df7['4'][i]
                            elif xx == 5:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                                    result = result + df7['5'][i] / 2
                                else:
                                    result = result + df7['5'][i]
                            elif xx == 6:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                                    result = result + df7['6'][i] / 2
                                else:
                                    result = result + df7['6'][i]
                            elif xx == 7:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                                    result = result + df7['7'][i] / 2
                                else:
                                    result = result + df7['7'][i]
                            elif xx == 8:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                                    result = result + df7['8'][i] / 2
                                else:
                                    result = result + df7['8'][i]
                            elif xx == 9:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                                    result = result + df7['9'][i] / 2
                                else:
                                    result = result + df7['9'][i]
                            break
            else:
                if color == 'F' and (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2'):
                    df7 = pd.read_csv('rovgsmF.csv')
                    for i in range(len(df7)):
                        if (sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                            result = result + df7['IF VVS F'][i] / 2
                        else:
                            result = result + df7['IF VVS F'][i]

                else:
                    df7 = pd.read_csv('rovgsm.csv')
                    for i in range(len(df7)):
                        if sizeprec >= df7['From'][i] and sizeprec <= df7['To'][i]:
                            if xx == 1:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                                    result = result + df7['1'][i] / 2
                                else:
                                    result = result + df7['1'][i]
                            elif xx == 2:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                                    result = result + df7['2'][i] / 2
                                else:
                                    result = result + df7['2'][i]
                            elif xx == 3:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                                    result = result + df7['3'][i] / 2
                                else:
                                    result = result + df7['3'][i]
                            elif xx == 4:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                                    result = result + df7['4'][i] / 2
                                else:
                                    result = result + df7['4'][i]
                            elif xx == 5:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                                    result = result + df7['5'][i] / 2
                                else:
                                    result = result + df7['5'][i]
                            elif xx == 6:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                                    result = result + df7['6'][i] / 2
                                else:
                                    result = result + df7['6'][i]
                            elif xx == 7:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                                    result = result + df7['7'][i] / 2
                                else:
                                    result = result + df7['7'][i]
                            elif xx == 8:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                                    result = result + df7['8'][i] / 2
                                else:
                                    result = result + df7['8'][i]
                            elif xx == 9:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and fluo == 'Strong' or fluo == 'Very Strong'):
                                    result = result + df7['9'][i] / 2
                                else:
                                    result = result + df7['9'][i]
                            break
        elif sizeprec >= 3.00 and sizeprec <= 6.99:
            if (sizeprec >= 3.50 and sizeprec <= 3.749):
                if (cut == 'EX' and polish == 'EX' and symmetry == 'EX'):
                    if (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2') and color == 'F':
                        result = result + 3.0
                    else:
                        result = result + 3.0
                else:
                    if (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2') and color == 'F':
                        result = result + 1.0
                    else:
                        result = result + 1.0
            elif (sizeprec >= 3.75 and sizeprec <= 3.999):
                if (cut == 'EX' and polish == 'EX' and symmetry == 'EX'):
                    result = result + 4.0
                else:
                    result = result + 2.0
            elif (sizeprec >= 4.50 and sizeprec <= 4.99):
                if (cut == 'EX' and polish == 'EX' and symmetry == 'EX'):
                    result = result + 3.0
                else:
                    result = result + 1.0
            elif (sizeprec >= 6.50 and sizeprec <= 6.99):
                if (cut == 'EX' and polish == 'EX' and symmetry == 'EX'):
                    result = result + 3.0
                else:
                    result = result + 2.0
            else:
                if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
                        symmetry == 'EX' or symmetry == 'VG'):
                    if (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2') and color == 'F':
                        if (sizeprec >= 3.00 and sizeprec <= 3.00):
                            result = result - 2.0
                        elif (sizeprec >= 4.00 and sizeprec <= 4.00):
                            result = result - 2.0
                        elif (sizeprec >= 5.00 and sizeprec <= 5.00):
                            result = result - 1.0
                    else:
                        df7 = pd.read_csv('roexbg.csv')
                        for i in range(len(df7)):
                            if (sizeprec >= df7['From'][i] and sizeprec <= df7['To'][i]):
                                if xx == 1:
                                    result = result + df7['1'][i]
                                if xx == 2:
                                    result = result + df7['2'][i]
                                if xx == 3:
                                    result = result + df7['3'][i]
                                if xx == 4:
                                    result = result + df7['4'][i]
                                if xx == 5:
                                    result = result + df7['5'][i]
                                if xx == 6:
                                    result = result + df7['6'][i]
                                if xx == 7:
                                    result = result + df7['7'][i]
                                if xx == 8:
                                    result = result + df7['8'][i]
                                if xx == 9:
                                    result = result + df7['9'][i]
                                break
        elif sizeprec >= 0.59 and sizeprec <= 0.599:
            if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
                    symmetry == 'EX' or symmetry == 'VG') and (fluo == 'Medium' or fluo == 'None' or fluo == 'Faint'):
                result = result + 1
        elif sizeprec >= 0.78 and sizeprec <= 0.789:
            if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
                    symmetry == 'EX' or symmetry == 'VG'):
                result = result + 1
        elif sizeprec >= 0.79 and sizeprec <= 0.799:
            if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
                    symmetry == 'EX' or symmetry == 'VG'):
                result = result + 2
        elif sizeprec >= 0.87 and sizeprec <= 0.879:
            if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
                    symmetry == 'EX' or symmetry == 'VG'):
                result = result + 1
        elif sizeprec >= 0.88 and sizeprec <= 0.889:
            if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
                    symmetry == 'EX' or symmetry == 'VG'):
                result = result + 2
        elif sizeprec >= 0.89 and sizeprec <= 0.899:
            if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
                    symmetry == 'EX' or symmetry == 'VG'):
                result = result + 3
        elif sizeprec >= 0.98 and sizeprec <= 0.989:
            if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
                    symmetry == 'EX' or symmetry == 'VG'):
                result = result + 1
        elif sizeprec >= 0.99 and sizeprec <= 0.999:
            if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
                    symmetry == 'EX' or symmetry == 'VG'):
                result = result + 2
                # Finishing

    # open
    # df9=pd.read_csv('Finishing.csv')
    # for i in range(len(df9)):
    #     #table
    #     if(df6['Location'][i]=='Table'):
    #         if(df6['Shape'][i]==shape and shape=='RO'):
    #             if((sizeprec>=df6['sizemin'][i]) & (cut==df6['cut'][i]) & (sizeprec<=df6['sizemax'][i]) & (tableintensity==df6['Intensity'][i])):
    #                 if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+df6['1'][i]
    #                     if xx==2:
    #                         result=result+df6['2'][i]
    #                     if xx==3:
    #                         result=result+df6['3'][i]
    #                     if xx==4:
    #                         result=result+df6['4'][i]
    #                     if xx==5:
    #                         result=result+df6['5'][i]
    #                     if xx==6:
    #                         result=result+df6['6'][i]
    #                     if xx==7:
    #                         result=result+df6['7'][i]
    #                     if xx==8:
    #                         result=result+df6['8'][i]
    #                     if xx==9:
    #                         result=result+df6['9'][i]
    #                     break
    #                 else:
    #                     if xx==1:
    #                         result=result+df6['1'][i]/2
    #                     if xx==2:
    #                         result=result+df6['2'][i]/2
    #                     if xx==3:
    #                         result=result+df6['3'][i]/2
    #                     if xx==4:
    #                         result=result+df6['4'][i]/2
    #                     if xx==5:
    #                         result=result+df6['5'][i]/2
    #                     if xx==6:
    #                         result=result+df6['6'][i]/2
    #                     if xx==7:
    #                         result=result+df6['7'][i]/2
    #                     if xx==8:
    #                         result=result+df6['8'][i]/2
    #                     if xx==9:
    #                         result=result+df6['9'][i]/2
    #                     break
    #         if(df6['Shape'][i]=='Fancy' and shape!='RO'):
    #             if(sizeprec>=df6['sizemin'][i] and sizeprec<=df6['sizemax'][i] and df6['symmetry'][i]==symmetry and df6['polish'][i]==polish and df6['Intensity'][i]==tableintensity):
    #                 if xx==1:
    #                     result=result+df6['1'][i]
    #                 if xx==2:
    #                     result=result+df6['2'][i]
    #                 if xx==3:
    #                     result=result+df6['3'][i]
    #                 if xx==4:
    #                     result=result+df6['4'][i]
    #                 if xx==5:
    #                     result=result+df6['5'][i]
    #                 if xx==6:
    #                     result=result+df6['6'][i]
    #                 if xx==7:
    #                     result=result+df6['7'][i]
    #                 if xx==8:
    #                     result=result+df6['8'][i]
    #                 if xx==9:
    #                     result=result+df6['9'][i]
    #                 break
    #     #table
    # for i in range(len(df6)):
    #     if(df6['Place'][i]=='Crown'):
    #         if(df6['Shape'][i]==shape and shape=='RO'):
    #             if(sizeprec>=df6['sizemin'][i] and sizeprec<=df6['sizemax'][i] and cut==df6['cut'][i] and df6['Intensity'][i]==crownintensity):
    #                 if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+df6['1'][i]
    #                     if xx==2:
    #                         result=result+df6['2'][i]
    #                     if xx==3:
    #                         result=result+df6['3'][i]
    #                     if xx==4:
    #                         result=result+df6['4'][i]
    #                     if xx==5:
    #                         result=result+df6['5'][i]
    #                     if xx==6:
    #                         result=result+df6['6'][i]
    #                     if xx==7:
    #                         result=result+df6['7'][i]
    #                     if xx==8:
    #                         result=result+df6['8'][i]
    #                     if xx==9:
    #                         result=result+df6['9'][i]
    #                     break
    #                 else:
    #                     if xx==1:
    #                         result=result+df6['1'][i]/2
    #                     if xx==2:
    #                         result=result+df6['2'][i]/2
    #                     if xx==3:
    #                         result=result+df6['3'][i]/2
    #                     if xx==4:
    #                         result=result+df6['4'][i]/2
    #                     if xx==5:
    #                         result=result+df6['5'][i]/2
    #                     if xx==6:
    #                         result=result+df6['6'][i]/2
    #                     if xx==7:
    #                         result=result+df6['7'][i]/2
    #                     if xx==8:
    #                         result=result+df6['8'][i]/2
    #                     if xx==9:
    #                         result=result+df6['9'][i]/2
    #                     break
    #         if(df6['Shape'][i]=='Fancy' and shape!='RO'):
    #             if(sizeprec>=df6['sizemin'][i] and sizeprec<=df6['sizemax'][i] and df6['symmetry'][i]==symmetry and df6['polish'][i]==polish and df6['Intensity'][i]==crownintensity):
    #                 if xx==1:
    #                     result=result+df6['1'][i]
    #                 if xx==2:
    #                     result=result+df6['2'][i]
    #                 if xx==3:
    #                     result=result+df6['3'][i]
    #                 if xx==4:
    #                     result=result+df6['4'][i]
    #                 if xx==5:
    #                     result=result+df6['5'][i]
    #                 if xx==6:
    #                     result=result+df6['6'][i]
    #                 if xx==7:
    #                     result=result+df6['7'][i]
    #                 if xx==8:
    #                     result=result+df6['8'][i]
    #                 if xx==9:
    #                     result=result+df6['9'][i]
    #                 break
    # for i in range(len(df6)):
    #     if(df6['Location'][i]=='Girdle'):
    #         if(df6['Shape'][i]==shape and shape=='RO'):
    #             if(sizeprec>=df6['sizemin'][i] and sizeprec<=df6['sizemax'][i] and cut==df6['cut'][i] and df6['Intensity'][i]==girdleintensity):
    # if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #     if xx==1:
    #         result=result+df6['1'][i]
    #     if xx==2:
    #         result=result+df6['2'][i]
    #     if xx==3:
    #         result=result+df6['3'][i]
    #     if xx==4:
    #         result=result+df6['4'][i]
    #     if xx==5:
    #         result=result+df6['5'][i]
    #     if xx==6:
    #         result=result+df6['6'][i]
    #     if xx==7:
    #         result=result+df6['7'][i]
    #     if xx==8:
    #         result=result+df6['8'][i]
    #     if xx==9:
    #         result=result+df6['9'][i]
    #     break
    # else:
    #     if xx==1:
    #         result=result+df6['1'][i]/2
    #     if xx==2:
    #         result=result+df6['2'][i]/2
    #     if xx==3:
    #         result=result+df6['3'][i]/2
    #     if xx==4:
    #         result=result+df6['4'][i]/2
    #     if xx==5:
    #         result=result+df6['5'][i]/2
    #     if xx==6:
    #         result=result+df6['6'][i]/2
    #     if xx==7:
    #         result=result+df6['7'][i]/2
    #     if xx==8:
    #         result=result+df6['8'][i]/2
    #     if xx==9:
    #         result=result+df6['9'][i]/2
    #     break
    # if(shape=='RO'):
    #     df9=pd.read_csv("Finishing.csv")
    #     for i in range(len(df9)):
    #         #HO
    #         if(halfopen==df9['Place'][i] and df9['value'][i]=='HO' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+df9['1'][i]
    #                     if xx==2:
    #                         result=result+df9['2'][i]
    #                     if xx==3:
    #                         result=result+df9['3'][i]
    #                     if xx==4:
    #                         result=result+df9['4'][i]
    #                     if xx==5:
    #                         result=result+df9['5'][i]
    #                     if xx==6:
    #                         result=result+df9['6'][i]
    #                     if xx==7:
    #                         result=result+df9['7'][i]
    #                     if xx==8:
    #                         result=result+df9['8'][i]
    #                     if xx==9:
    #                         result=result+df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+df9['9'][i]/2
    #         if(smallopen==df9['Place'][i] and df9['value'][i]=='Small' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+df9['1'][i]
    #                     if xx==2:
    #                         result=result+df9['2'][i]
    #                     if xx==3:
    #                         result=result+df9['3'][i]
    #                     if xx==4:
    #                         result=result+df9['4'][i]
    #                     if xx==5:
    #                         result=result+df9['5'][i]
    #                     if xx==6:
    #                         result=result+df9['6'][i]
    #                     if xx==7:
    #                         result=result+df9['7'][i]
    #                     if xx==8:
    #                         result=result+df9['8'][i]
    #                     if xx==9:
    #                         result=result+df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+df9['9'][i]/2
    #         if(bigopen==df9['Place'][i] and df9['value'][i]=='Big' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+df9['1'][i]
    #                     if xx==2:
    #                         result=result+df9['2'][i]
    #                     if xx==3:
    #                         result=result+df9['3'][i]
    #                     if xx==4:
    #                         result=result+df9['4'][i]
    #                     if xx==5:
    #                         result=result+df9['5'][i]
    #                     if xx==6:
    #                         result=result+df9['6'][i]
    #                     if xx==7:
    #                         result=result+df9['7'][i]
    #                     if xx==8:
    #                         result=result+df9['8'][i]
    #                     if xx==9:
    #                         result=result+df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+df9['9'][i]/2
    #         if(mediumopen==df9['Place'][i] and df9['value'][i]=='Medium' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+df9['1'][i]
    #                     if xx==2:
    #                         result=result+df9['2'][i]
    #                     if xx==3:
    #                         result=result+df9['3'][i]
    #                     if xx==4:
    #                         result=result+df9['4'][i]
    #                     if xx==5:
    #                         result=result+df9['5'][i]
    #                     if xx==6:
    #                         result=result+df9['6'][i]
    #                     if xx==7:
    #                         result=result+df9['7'][i]
    #                     if xx==8:
    #                         result=result+df9['8'][i]
    #                     if xx==9:
    #                         result=result+df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+df9['9'][i]/2
    #     for i in range(len(df9)):
    #         #HO
    #         if(identednatural==df9['Place'][i] and df9['value'][i]=='Indented Natural' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+df9['1'][i]
    #                     if xx==2:
    #                         result=result+df9['2'][i]
    #                     if xx==3:
    #                         result=result+df9['3'][i]
    #                     if xx==4:
    #                         result=result+df9['4'][i]
    #                     if xx==5:
    #                         result=result+df9['5'][i]
    #                     if xx==6:
    #                         result=result+df9['6'][i]
    #                     if xx==7:
    #                         result=result+df9['7'][i]
    #                     if xx==8:
    #                         result=result+df9['8'][i]
    #                     if xx==9:
    #                         result=result+df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+df9['9'][i]/2
    #         if(naturalnatural==df9['Place'][i] and df9['value'][i]=='Natural' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+df9['1'][i]
    #                     if xx==2:
    #                         result=result+df9['2'][i]
    #                     if xx==3:
    #                         result=result+df9['3'][i]
    #                     if xx==4:
    #                         result=result+df9['4'][i]
    #                     if xx==5:
    #                         result=result+df9['5'][i]
    #                     if xx==6:
    #                         result=result+df9['6'][i]
    #                     if xx==7:
    #                         result=result+df9['7'][i]
    #                     if xx==8:
    #                         result=result+df9['8'][i]
    #                     if xx==9:
    #                         result=result+df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+df9['9'][i]/2
    #         if(bignatural==df9['Place'][i] and df9['value'][i]=='Big Natural' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+df9['1'][i]
    #                     if xx==2:
    #                         result=result+df9['2'][i]
    #                     if xx==3:
    #                         result=result+df9['3'][i]
    #                     if xx==4:
    #                         result=result+df9['4'][i]
    #                     if xx==5:
    #                         result=result+df9['5'][i]
    #                     if xx==6:
    #                         result=result+df9['6'][i]
    #                     if xx==7:
    #                         result=result+df9['7'][i]
    #                     if xx==8:
    #                         result=result+df9['8'][i]
    #                     if xx==9:
    #                         result=result+df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+df9['9'][i]/2

    #     for i in range(len(df9)):
    #         #HO
    #         if(extrafacet==df9['Place'][i] and df9['value'][i]=='Extra Facet') and cut==df9['Cut'][i]:
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+df9['1'][i]
    #                     if xx==2:
    #                         result=result+df9['2'][i]
    #                     if xx==3:
    #                         result=result+df9['3'][i]
    #                     if xx==4:
    #                         result=result+df9['4'][i]
    #                     if xx==5:
    #                         result=result+df9['5'][i]
    #                     if xx==6:
    #                         result=result+df9['6'][i]
    #                     if xx==7:
    #                         result=result+df9['7'][i]
    #                     if xx==8:
    #                         result=result+df9['8'][i]
    #                     if xx==9:
    #                         result=result+df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+df9['9'][i]/2
    #         if(cavity==df9['Place'][i] and df9['value'][i]=='Cavity' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+df9['1'][i]
    #                     if xx==2:
    #                         result=result+df9['2'][i]
    #                     if xx==3:
    #                         result=result+df9['3'][i]
    #                     if xx==4:
    #                         result=result+df9['4'][i]
    #                     if xx==5:
    #                         result=result+df9['5'][i]
    #                     if xx==6:
    #                         result=result+df9['6'][i]
    #                     if xx==7:
    #                         result=result+df9['7'][i]
    #                     if xx==8:
    #                         result=result+df9['8'][i]
    #                     if xx==9:
    #                         result=result+df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+df9['9'][i]/2
    #         if(chip==df9['Place'][i] and df9['value'][i]=='Chip' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+df9['1'][i]
    #                     if xx==2:
    #                         result=result+df9['2'][i]
    #                     if xx==3:
    #                         result=result+df9['3'][i]
    #                     if xx==4:
    #                         result=result+df9['4'][i]
    #                     if xx==5:
    #                         result=result+df9['5'][i]
    #                     if xx==6:
    #                         result=result+df9['6'][i]
    #                     if xx==7:
    #                         result=result+df9['7'][i]
    #                     if xx==8:
    #                         result=result+df9['8'][i]
    #                     if xx==9:
    #                         result=result+df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+df9['9'][i]/2
    # elif(shape!='RO'):
    #     df9=pd.read_csv("FinishingFancy.csv")
    #     for i in range(len(df9)):
    #         #HO
    #         if(halfopen==df9['Place'][i] and df9['value'][i]=='HO' and cut==df9['Cut'][i] and polish==df9['Polish'][i] and symmetry==df9['Symmetry'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                 if xx==1:
    #                     result=result+df9['1'][i]
    #                 if xx==2:
    #                     result=result+df9['2'][i]
    #                 if xx==3:
    #                     result=result+df9['3'][i]
    #                 if xx==4:
    #                     result=result+df9['4'][i]
    #                 if xx==5:
    #                     result=result+df9['5'][i]
    #                 if xx==6:
    #                     result=result+df9['6'][i]
    #                 if xx==7:
    #                     result=result+df9['7'][i]
    #                 if xx==8:
    #                     result=result+df9['8'][i]
    #                 if xx==9:
    #                     result=result+df9['9'][i]
    #             else:
    #                 if xx==1:
    #                     result=result+df9['1'][i]/2
    #                 if xx==2:
    #                     result=result+df9['2'][i]/2
    #                 if xx==3:
    #                     result=result+df9['3'][i]/2
    #                 if xx==4:
    #                     result=result+df9['4'][i]/2
    #                 if xx==5:
    #                     result=result+df9['5'][i]/2
    #                 if xx==6:
    #                     result=result+df9['6'][i]/2
    #                 if xx==7:
    #                     result=result+df9['7'][i]/2
    #                 if xx==8:
    #                     result=result+df9['8'][i]/2
    #                 if xx==9:
    #                     result=result+df9['9'][i]/2
    #         if(smallopen==df9['Place'][i] and df9['value'][i]=='Small' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                 if xx==1:
    #                     result=result+df9['1'][i]
    #                 if xx==2:
    #                     result=result+df9['2'][i]
    #                 if xx==3:
    #                     result=result+df9['3'][i]
    #                 if xx==4:
    #                     result=result+df9['4'][i]
    #                 if xx==5:
    #                     result=result+df9['5'][i]
    #                 if xx==6:
    #                     result=result+df9['6'][i]
    #                 if xx==7:
    #                     result=result+df9['7'][i]
    #                 if xx==8:
    #                     result=result+df9['8'][i]
    #                 if xx==9:
    #                     result=result+df9['9'][i]
    #             else:
    #                 if xx==1:
    #                     result=result+df9['1'][i]/2
    #                 if xx==2:
    #                     result=result+df9['2'][i]/2
    #                 if xx==3:
    #                     result=result+df9['3'][i]/2
    #                 if xx==4:
    #                     result=result+df9['4'][i]/2
    #                 if xx==5:
    #                     result=result+df9['5'][i]/2
    #                 if xx==6:
    #                     result=result+df9['6'][i]/2
    #                 if xx==7:
    #                     result=result+df9['7'][i]/2
    #                 if xx==8:
    #                     result=result+df9['8'][i]/2
    #                 if xx==9:
    #                     result=result+df9['9'][i]/2
    #         if(bigopen==df9['Place'][i] and df9['value'][i]=='Big' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                 if xx==1:
    #                     result=result+df9['1'][i]
    #                 if xx==2:
    #                     result=result+df9['2'][i]
    #                 if xx==3:
    #                     result=result+df9['3'][i]
    #                 if xx==4:
    #                     result=result+df9['4'][i]
    #                 if xx==5:
    #                     result=result+df9['5'][i]
    #                 if xx==6:
    #                     result=result+df9['6'][i]
    #                 if xx==7:
    #                     result=result+df9['7'][i]
    #                 if xx==8:
    #                     result=result+df9['8'][i]
    #                 if xx==9:
    #                     result=result+df9['9'][i]
    #             else:
    #                 if xx==1:
    #                     result=result+df9['1'][i]/2
    #                 if xx==2:
    #                     result=result+df9['2'][i]/2
    #                 if xx==3:
    #                     result=result+df9['3'][i]/2
    #                 if xx==4:
    #                     result=result+df9['4'][i]/2
    #                 if xx==5:
    #                     result=result+df9['5'][i]/2
    #                 if xx==6:
    #                     result=result+df9['6'][i]/2
    #                 if xx==7:
    #                     result=result+df9['7'][i]/2
    #                 if xx==8:
    #                     result=result+df9['8'][i]/2
    #                 if xx==9:
    #                     result=result+df9['9'][i]/2
    #         if(mediumopen==df9['Place'][i] and df9['value'][i]=='Medium' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                 if xx==1:
    #                     result=result+df9['1'][i]
    #                 if xx==2:
    #                     result=result+df9['2'][i]
    #                 if xx==3:
    #                     result=result+df9['3'][i]
    #                 if xx==4:
    #                     result=result+df9['4'][i]
    #                 if xx==5:
    #                     result=result+df9['5'][i]
    #                 if xx==6:
    #                     result=result+df9['6'][i]
    #                 if xx==7:
    #                     result=result+df9['7'][i]
    #                 if xx==8:
    #                     result=result+df9['8'][i]
    #                 if xx==9:
    #                     result=result+df9['9'][i]
    #             else:
    #                 if xx==1:
    #                     result=result+df9['1'][i]/2
    #                 if xx==2:
    #                     result=result+df9['2'][i]/2
    #                 if xx==3:
    #                     result=result+df9['3'][i]/2
    #                 if xx==4:
    #                     result=result+df9['4'][i]/2
    #                 if xx==5:
    #                     result=result+df9['5'][i]/2
    #                 if xx==6:
    #                     result=result+df9['6'][i]/2
    #                 if xx==7:
    #                     result=result+df9['7'][i]/2
    #                 if xx==8:
    #                     result=result+df9['8'][i]/2
    #                 if xx==9:
    #                     result=result+df9['9'][i]/2
    #     for i in range(len(df9)):
    #         #HO
    #         if(identednatural==df9['Place'][i] and df9['value'][i]=='Indented Natural' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                 if xx==1:
    #                     result=result+df9['1'][i]
    #                 if xx==2:
    #                     result=result+df9['2'][i]
    #                 if xx==3:
    #                     result=result+df9['3'][i]
    #                 if xx==4:
    #                     result=result+df9['4'][i]
    #                 if xx==5:
    #                     result=result+df9['5'][i]
    #                 if xx==6:
    #                     result=result+df9['6'][i]
    #                 if xx==7:
    #                     result=result+df9['7'][i]
    #                 if xx==8:
    #                     result=result+df9['8'][i]
    #                 if xx==9:
    #                     result=result+df9['9'][i]
    #             else:
    #                 if xx==1:
    #                     result=result+df9['1'][i]/2
    #                 if xx==2:
    #                     result=result+df9['2'][i]/2
    #                 if xx==3:
    #                     result=result+df9['3'][i]/2
    #                 if xx==4:
    #                     result=result+df9['4'][i]/2
    #                 if xx==5:
    #                     result=result+df9['5'][i]/2
    #                 if xx==6:
    #                     result=result+df9['6'][i]/2
    #                 if xx==7:
    #                     result=result+df9['7'][i]/2
    #                 if xx==8:
    #                     result=result+df9['8'][i]/2
    #                 if xx==9:
    #                     result=result+df9['9'][i]/2
    #         if(naturalnatural==df9['Place'][i] and df9['value'][i]=='Natural' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                 if xx==1:
    #                     result=result+df9['1'][i]
    #                 if xx==2:
    #                     result=result+df9['2'][i]
    #                 if xx==3:
    #                     result=result+df9['3'][i]
    #                 if xx==4:
    #                     result=result+df9['4'][i]
    #                 if xx==5:
    #                     result=result+df9['5'][i]
    #                 if xx==6:
    #                     result=result+df9['6'][i]
    #                 if xx==7:
    #                     result=result+df9['7'][i]
    #                 if xx==8:
    #                     result=result+df9['8'][i]
    #                 if xx==9:
    #                     result=result+df9['9'][i]
    #             else:
    #                 if xx==1:
    #                     result=result+df9['1'][i]/2
    #                 if xx==2:
    #                     result=result+df9['2'][i]/2
    #                 if xx==3:
    #                     result=result+df9['3'][i]/2
    #                 if xx==4:
    #                     result=result+df9['4'][i]/2
    #                 if xx==5:
    #                     result=result+df9['5'][i]/2
    #                 if xx==6:
    #                     result=result+df9['6'][i]/2
    #                 if xx==7:
    #                     result=result+df9['7'][i]/2
    #                 if xx==8:
    #                     result=result+df9['8'][i]/2
    #                 if xx==9:
    #                     result=result+df9['9'][i]/2
    #         if(bignatural==df9['Place'][i] and df9['value'][i]=='Big Natural' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                 if xx==1:
    #                     result=result+df9['1'][i]
    #                 if xx==2:
    #                     result=result+df9['2'][i]
    #                 if xx==3:
    #                     result=result+df9['3'][i]
    #                 if xx==4:
    #                     result=result+df9['4'][i]
    #                 if xx==5:
    #                     result=result+df9['5'][i]
    #                 if xx==6:
    #                     result=result+df9['6'][i]
    #                 if xx==7:
    #                     result=result+df9['7'][i]
    #                 if xx==8:
    #                     result=result+df9['8'][i]
    #                 if xx==9:
    #                     result=result+df9['9'][i]
    #             else:
    #                 if xx==1:
    #                     result=result+df9['1'][i]/2
    #                 if xx==2:
    #                     result=result+df9['2'][i]/2
    #                 if xx==3:
    #                     result=result+df9['3'][i]/2
    #                 if xx==4:
    #                     result=result+df9['4'][i]/2
    #                 if xx==5:
    #                     result=result+df9['5'][i]/2
    #                 if xx==6:
    #                     result=result+df9['6'][i]/2
    #                 if xx==7:
    #                     result=result+df9['7'][i]/2
    #                 if xx==8:
    #                     result=result+df9['8'][i]/2
    #                 if xx==9:
    #                     result=result+df9['9'][i]/2

    #     for i in range(len(df9)):
    #         #HO
    #         if(extrafacet==df9['Place'][i] and df9['value'][i]=='Extra Facet') and cut==df9['Cut'][i]:
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                 if xx==1:
    #                     result=result+df9['1'][i]
    #                 if xx==2:
    #                     result=result+df9['2'][i]
    #                 if xx==3:
    #                     result=result+df9['3'][i]
    #                 if xx==4:
    #                     result=result+df9['4'][i]
    #                 if xx==5:
    #                     result=result+df9['5'][i]
    #                 if xx==6:
    #                     result=result+df9['6'][i]
    #                 if xx==7:
    #                     result=result+df9['7'][i]
    #                 if xx==8:
    #                     result=result+df9['8'][i]
    #                 if xx==9:
    #                     result=result+df9['9'][i]
    #             else:
    #                 if xx==1:
    #                     result=result+df9['1'][i]/2
    #                 if xx==2:
    #                     result=result+df9['2'][i]/2
    #                 if xx==3:
    #                     result=result+df9['3'][i]/2
    #                 if xx==4:
    #                     result=result+df9['4'][i]/2
    #                 if xx==5:
    #                     result=result+df9['5'][i]/2
    #                 if xx==6:
    #                     result=result+df9['6'][i]/2
    #                 if xx==7:
    #                     result=result+df9['7'][i]/2
    #                 if xx==8:
    #                     result=result+df9['8'][i]/2
    #                 if xx==9:
    #                     result=result+df9['9'][i]/2
    #         if(cavity==df9['Place'][i] and df9['value'][i]=='Cavity' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                 if xx==1:
    #                     result=result+df9['1'][i]
    #                 if xx==2:
    #                     result=result+df9['2'][i]
    #                 if xx==3:
    #                     result=result+df9['3'][i]
    #                 if xx==4:
    #                     result=result+df9['4'][i]
    #                 if xx==5:
    #                     result=result+df9['5'][i]
    #                 if xx==6:
    #                     result=result+df9['6'][i]
    #                 if xx==7:
    #                     result=result+df9['7'][i]
    #                 if xx==8:
    #                     result=result+df9['8'][i]
    #                 if xx==9:
    #                     result=result+df9['9'][i]
    #             else:
    #                 if xx==1:
    #                     result=result+df9['1'][i]/2
    #                 if xx==2:
    #                     result=result+df9['2'][i]/2
    #                 if xx==3:
    #                     result=result+df9['3'][i]/2
    #                 if xx==4:
    #                     result=result+df9['4'][i]/2
    #                 if xx==5:
    #                     result=result+df9['5'][i]/2
    #                 if xx==6:
    #                     result=result+df9['6'][i]/2
    #                 if xx==7:
    #                     result=result+df9['7'][i]/2
    #                 if xx==8:
    #                     result=result+df9['8'][i]/2
    #                 if xx==9:
    #                     result=result+df9['9'][i]/2
    #         if(chip==df9['Place'][i] and df9['value'][i]=='Chip' and cut==df9['Cut'][i]):
    # if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #     if xx==1:
    #         result=result+df9['1'][i]
    #     if xx==2:
    #         result=result+df9['2'][i]
    #     if xx==3:
    #         result=result+df9['3'][i]
    #     if xx==4:
    #         result=result+df9['4'][i]
    #     if xx==5:
    #         result=result+df9['5'][i]
    #     if xx==6:
    #         result=result+df9['6'][i]
    #     if xx==7:
    #         result=result+df9['7'][i]
    #     if xx==8:
    #         result=result+df9['8'][i]
    #     if xx==9:
    #         result=result+df9['9'][i]
    # else:
    #     if xx==1:
    #         result=result+df9['1'][i]/2
    #     if xx==2:
    #         result=result+df9['2'][i]/2
    #     if xx==3:
    #         result=result+df9['3'][i]/2
    #     if xx==4:
    #         result=result+df9['4'][i]/2
    #     if xx==5:
    #         result=result+df9['5'][i]/2
    #     if xx==6:
    #         result=result+df9['6'][i]/2
    #     if xx==7:
    #         result=result+df9['7'][i]/2
    #     if xx==8:
    #         result=result+df9['8'][i]/2
    #     if xx==9:
    #         result=result+df9['9'][i]/2
    if sizeprec >= 1.0:
        df31 = pd.read_csv('FinishingRoOpen.csv')
        if (shape == 'RO'):
            for i in range(len(df31)):
                if (tableopen == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + (df31['1'][i] / 2)
                        if xx == 2:
                            result = result + (df31['2'][i] / 2)
                        if xx == 3:
                            result = result + (df31['3'][i] / 2)
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (girdleopen == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (crownopen == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (pavilionopen == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (topnatural == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (crownnatural == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (girdlenatural == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (pavilionnatural == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (topef == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (crownef == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (girdleef == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (pavilionef == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (topcavity == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (crowncavity == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (girdlecavity == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (pavilioncavity == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (topchip == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (crownchip == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (girdlechip == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (pavilionchip == df31['open'][i] and cut == df31['Cut'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
        else:
            for i in range(len(df31)):
                if (tableopen == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (girdleopen == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (crownopen == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (pavilionopen == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][
                    i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (topnatural == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (crownnatural == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][
                    i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (girdlenatural == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][
                    i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (pavilionnatural == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][
                    i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (topef == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (crownef == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (girdleef == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (pavilionef == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (topcavity == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (crowncavity == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (girdlecavity == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][
                    i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (pavilioncavity == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][
                    i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (topchip == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (crownchip == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (girdlechip == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2
                if (pavilionchip == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][
                    i]):
                    if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
                        if xx == 1:
                            result = result + df31['1'][i]
                        if xx == 2:
                            result = result + df31['2'][i]
                        if xx == 3:
                            result = result + df31['3'][i]
                        if xx == 4:
                            result = result + df31['4'][i]
                        if xx == 5:
                            result = result + df31['5'][i]
                        if xx == 6:
                            result = result + df31['6'][i]
                        if xx == 7:
                            result = result + df31['7'][i]
                        if xx == 8:
                            result = result + df31['8'][i]
                        if xx == 9:
                            result = result + df31['9'][i]
                    else:
                        if xx == 1:
                            result = result + df31['1'][i] / 2
                        if xx == 2:
                            result = result + df31['2'][i] / 2
                        if xx == 3:
                            result = result + df31['3'][i] / 2
                        if xx == 4:
                            result = result + df31['4'][i] / 2
                        if xx == 5:
                            result = result + df31['5'][i] / 2
                        if xx == 6:
                            result = result + df31['6'][i] / 2
                        if xx == 7:
                            result = result + df31['7'][i] / 2
                        if xx == 8:
                            result = result + df31['8'][i] / 2
                        if xx == 9:
                            result = result + df31['9'][i] / 2

                            # Internal Grading
    df30 = pd.read_csv('InternalGrading.csv')
    for i in range(len(df30)):
        if (shape == 'RO' and shape == df30['Shape'][i] and upgrade1 == df30['what'][i]):
            if df30['Grade'][i] == 'Upgrade':
                if xx == 1:
                    result = result + 100 * df30['1'][i]

                if xx == 2:
                    result = result + 100 * df30['2'][i]
                if xx == 3:
                    result = result + 100 * df30['3'][i]
                if xx == 4:
                    result = result + 100 * df30['4'][i]
                if xx == 5:
                    result = result + 100 * df30['5'][i]
                if xx == 6:
                    result = result + 100 * df30['6'][i]
                if xx == 7:
                    result = result + 100 * df30['7'][i]
                if xx == 8:
                    result = result + 100 * df30['8'][i]
                if xx == 9:
                    result = result + 100 * df30['9'][i]
        if (shape == 'RO' and shape == df30['Shape'][i] and downgrade1 == df30['what'][i]):
            if df30['Grade'][i] == 'Downgrade':
                if xx == 1:
                    result = result + 100 * df30['1'][i]
                if xx == 2:
                    result = result + 100 * df30['2'][i]
                if xx == 3:
                    result = result + 100 * df30['3'][i]
                if xx == 4:
                    result = result + 100 * df30['4'][i]
                if xx == 5:
                    result = result + 100 * df30['5'][i]
                if xx == 6:
                    result = result + 100 * df30['6'][i]
                if xx == 7:
                    result = result + 100 * df30['7'][i]
                if xx == 8:
                    result = result + 100 * df30['8'][i]
                if xx == 9:
                    result = result + 100 * df30['9'][i]
        if (shape != 'RO' and 'Fancy' == df30['Shape'][i] and upgrade1 == df30['what'][i]):
            if df30['Grade'][i] == 'Upgrade':
                if xx == 1:
                    result = result + 100 * df30['1'][i]
                if xx == 2:
                    result = result + 100 * df30['2'][i]
                if xx == 3:
                    result = result + 100 * df30['3'][i]
                if xx == 4:
                    result = result + 100 * df30['4'][i]
                if xx == 5:
                    result = result + 100 * df30['5'][i]
                if xx == 6:
                    result = result + 100 * df30['6'][i]
                if xx == 7:
                    result = result + 100 * df30['7'][i]
                if xx == 8:
                    result = result + 100 * df30['8'][i]
                if xx == 9:
                    result = result + 100 * df30['9'][i]
        if (shape != 'RO' and 'Famcy' == df30['Shape'][i] and downgrade1 == df30['what'][i]):
            if df30['Grade'][i] == 'Downgrade':
                if xx == 1:
                    result = result + 100 * df30['1'][i]
                if xx == 2:
                    result = result + 100 * df30['2'][i]
                if xx == 3:
                    result = result + 100 * df30['3'][i]
                if xx == 4:
                    result = result + 100 * df30['4'][i]
                if xx == 5:
                    result = result + 100 * df30['5'][i]
                if xx == 6:
                    result = result + 100 * df30['6'][i]
                if xx == 7:
                    result = result + 100 * df30['7'][i]
                if xx == 8:
                    result = result + 100 * df30['8'][i]
                if xx == 9:
                    result = result + 100 * df30['9'][i]
        if (shape == 'RO' and shape == df30['Shape'][i] and upgrade2 == df30['what'][i]):
            if df30['Grade'][i] == 'Upgrade':
                if xx == 1:
                    result = result + 100 * df30['1'][i]
                if xx == 2:
                    result = result + 100 * df30['2'][i]
                if xx == 3:
                    result = result + 100 * df30['3'][i]
                if xx == 4:
                    result = result + 100 * df30['4'][i]
                if xx == 5:
                    result = result + 100 * df30['5'][i]
                if xx == 6:
                    result = result + 100 * df30['6'][i]
                if xx == 7:
                    result = result + 100 * df30['7'][i]
                if xx == 8:
                    result = result + 100 * df30['8'][i]
                if xx == 9:
                    result = result + 100 * df30['9'][i]
        if (shape == 'RO' and shape == df30['Shape'][i] and downgrade2 == df30['what'][i]):
            if df30['Grade'][i] == 'Downgrade':
                if xx == 1:
                    result = result + 100 * df30['1'][i]
                if xx == 2:
                    result = result + 100 * df30['2'][i]
                if xx == 3:
                    result = result + 100 * df30['3'][i]
                if xx == 4:
                    result = result + 100 * df30['4'][i]
                if xx == 5:
                    result = result + 100 * df30['5'][i]
                if xx == 6:
                    result = result + 100 * df30['6'][i]
                if xx == 7:
                    result = result + 100 * df30['7'][i]
                if xx == 8:
                    result = result + 100 * df30['8'][i]
                if xx == 9:
                    result = result + 100 * df30['9'][i]
        if (shape != 'RO' and 'Fancy' == df30['Shape'][i] and upgrade2 == df30['what'][i]):
            if df30['Grade'][i] == 'Upgrade':
                if xx == 1:
                    result = result + 100 * df30['1'][i]
                if xx == 2:
                    result = result + 100 * df30['2'][i]
                if xx == 3:
                    result = result + 100 * df30['3'][i]
                if xx == 4:
                    result = result + 100 * df30['4'][i]
                if xx == 5:
                    result = result + 100 * df30['5'][i]
                if xx == 6:
                    result = result + 100 * df30['6'][i]
                if xx == 7:
                    result = result + 100 * df30['7'][i]
                if xx == 8:
                    result = result + 100 * df30['8'][i]
                if xx == 9:
                    result = result + 100 * df30['9'][i]
        if (shape != 'RO' and 'Famcy' == df30['Shape'][i] and downgrade2 == df30['what'][i]):
            if df30['Grade'][i] == 'Downgrade':
                if xx == 1:
                    result = result + 100 * df30['1'][i]
                if xx == 2:
                    result = result + 100 * df30['2'][i]
                if xx == 3:
                    result = result + 100 * df30['3'][i]
                if xx == 4:
                    result = result + 100 * df30['4'][i]
                if xx == 5:
                    result = result + 100 * df30['5'][i]
                if xx == 6:
                    result = result + 100 * df30['6'][i]
                if xx == 7:
                    result = result + 100 * df30['7'][i]
                if xx == 8:
                    result = result + 100 * df30['8'][i]
                if xx == 9:
                    result = result + 100 * df30['9'][i]
    if (sizeprec >= 0.30 and sizeprec <= 0.99):
        if cut == 'EX' and depth >= 63 and (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2') and (
                color == 'D' or color == 'E' or color == 'F'):
            result = result - 1.0
        if cut == 'VG' and depth >= 64.8 and (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2') and (
                color != 'J' or color != 'K' or color != 'L' or color != 'I'):
            result = result - 1.0
    if ff == 0:
        rap = 0;
    if temp >= -40:
        if temp - result > 20:
            result = temp - 20
    else:
        if temp - result > 15:
            result = temp - 15

    return result


def get_cut_comments(min_diam, max_diam, tabl, height, ratio, col_shade, cr_angle,
                     cr_height, pv_angle, pv_depth, girdle_percentage, girdle_from, girdle_to, girdle_condition,
                     star_length, lower_half, open, natural, intended_natural, extra_facet, graining, rap_value):
    return ''