import pandas as pd

from discount_integration.discount_sql import get_diameter_premium
from utils.cut_comment_util import get_cut


def calcDiscount(cert, shape, szgr, color, clarity, cut, polish, symmetry, fluo, rap, ktos, sizeprec, tableclean,
                 eyeclean, ha, cutcomments, diameter, internalgraining, surfacegraining, flawless,
                 tableintensity, crownintensity, topef, topcavity, topchip, crownef, crowncavity, crownchip,
                 girdleef, girdlecavity, girdlechip, pavilionef, pavilioncavity, pavilionchip, depth, green,
                 grey, brown, milky, tableopen, crownopen, girdleopen, pavilionopen, topnatural, crownnatural,
                 girdlenatural, pavilionnatural, chip, cavity, upgrade1, upgrade2, downgrade1, downgrade2, days,
                 min_diam, max_diam, tabl, height, ratio, cr_angle, cr_height, pv_angle,
                 pv_depth,
                 girdle_percentage, girdle_from, girdle_to, girdle_condition, star_length,
                 lower_half,
                 identedtopnatural, graining, rap_value, ktos_attribute
                 ):
    # test_df = pd.DataFrame({'SZ GR':[szgr], 'CERTCT':[certct], 'COLOR':[color_dict[color]], 'CLARITY':[clarity_dict[clarity]], 'CUT':[cut],
    #                       'POLISH':[polish], 'SYMMETRY':[symmetry], 'FLUO':[fluo], 'rap':[rap], 'PUR RAP DIS':[pur_rap_dis]})
    # if (cutcomments == 'EX1'):
    #     if (cut == 'EX' and polish == 'EX' and symmetry == 'EX'):
    #         cutcomments = '3EX-EX1'
    #     elif (cut == 'EX' and (polish != 'EX' or symmetry != 'EX')):
    #         cutcomments = 'EX-EX1'
    # elif (cutcomments == 'EX2'):
    #     if (cut == 'EX' and polish == 'EX' and symmetry == 'EX'):
    #         cutcomments = '3EX-EX2'
    #     elif (cut == 'EX' and (polish != 'EX' or symmetry != 'EX')):
    #         cutcomments = 'EX-EX2'
    # elif (cutcomments == 'VG1'):
    #     if (cut == 'VG' and (polish != 'VG' or symmetry != 'VG')):
    #         cutcomments = 'VG-VG1'
    # elif (cutcomments == 'VG2'):
    #     if (cut == 'VG' and (polish != 'VG' or symmetry != 'VG')):
    #         cutcomments = 'VG-VG2'
    base = 0.0
    gdd = 0.0
    ktosd = 0.0
    diameterd = 0.0
    colshaded = 0.0
    milkyd = 0.0
    cutcommentsd = 0.0
    grainingd = 0.0
    had = 0.0
    eyecleand = 0.0
    tablecleand = 0.0
    blackd = 0.0
    sideblackd = 0.0
    sizepremd = 0.0
    opend = 0.0
    naturald = 0.0
    identednaturald = 0.0
    efd = 0.0
    cavityd = 0.0
    chipd = 0.0
    depthd = 0.0
    color1 = 'X'
    capped = 0
    MNcolorD = 0.0
    result = 0.00
    daysd = 0.0
    very_strong_fluod = 0.0
    fancy_fluod = 0.0
    sym_pold = 0.0
    ff = 0
    xx = 0
    identedcrownnatural = '0'
    identedgirdlenatural = '0'
    identedpavilionnatural = '0'
    if (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2'):
        if ((color == 'D') or (color == 'E') or (color == 'F')):
            xx = 1
        if ((color == 'G') or (color == 'H') or (color == 'I')):
            xx = 2
        if ((color == 'J') or (color == 'K') or (color == 'L') or (color == 'M')):
            xx = 3
    if ((clarity == 'VS1') or (clarity == 'VS2')):
        if ((color == 'D') or (color == 'E') or (color == 'F')):
            xx = 4
        if ((color == 'G') or (color == 'H') or (color == 'I')):
            xx = 5
        if ((color == 'J') or (color == 'K') or (color == 'L') or (color == 'M')):
            xx = 6
    if ((clarity == 'SI1') or (clarity == 'SI2') or (clarity == 'I1')):
        if ((color == 'D') or (color == 'E') or (color == 'F')):
            xx = 7
        if ((color == 'G') or (color == 'H') or (color == 'I')):
            xx = 8
        if ((color == 'J') or (color == 'K') or (color == 'L') or (color == 'M') or (color == 'N')):
            xx = 9

    if shape == 'RO' and color == 'N':
        mn_data = pd.read_csv('discountsncolors.csv')
        for i in range(len(mn_data)):
            if mn_data['size_min'][i] <= sizeprec <= mn_data['size_max'][i]:
                color = 'M'
                if cut == 'EX':
                    MNcolorD += mn_data['EX'][i]
                else:
                    MNcolorD += mn_data['EX-'][i]
                result += MNcolorD
                break

    if (shape == 'RO' and sizeprec >= 1.0):
        color1 = color
        # if color == 'N': TBD
        #     MNcolorD = -7
        #     color = 'M'
        df = pd.read_csv('1ct_5ctup.csv')
        for i in range(len(df)):
            # and polish == df['POL'][i] and symmetry == df['SYM'][i]
            if shape == df['Shape'][i] and color == df['COLOR'][i] and clarity == df['CLARITY'][i] and cut == df['CUT'][
                i] and fluo == df['FLUO'][i] and szgr == df['Size'][i]:
                if (cut == 'EX' and polish == 'EX' and symmetry == 'EX'):
                    if (polish == df['POL'][i] and symmetry == df['SYM'][i]):
                        result = df['Discount'][i]
                        ff = 1
                        break
                else:
                    if (cut == df['CUT'][i] and df['POL'][i] == 'EX' and df['SYM'][i] == 'EX'):
                        result = result
                    elif (cut == df['CUT'][i]):
                        result = float(df['Discount'][i])
                        ff = 1
                        break
        # if(color1=='N'):
        #     result=result-0.07
        temp = result
        base = temp * 100
        result = result * 100
        if (cut == 'EX' or cut == 'VG') and (
                polish == 'GD' or symmetry == 'GD') and ff == 1 and sizeprec >= 1.0 and sizeprec <= 2.99:
            for i in range(len(df)):
                if shape == df['Shape'][i] and color == df['COLOR'][i] and clarity == df['CLARITY'][i] and df['CUT'][
                    i] == 'GD' and fluo == df['FLUO'][i] and szgr == df['Size'][i]:
                    tempo = float(df['Discount'][i]) * 100
                    gdd = max(-1 * (round(abs(result - tempo) / 2)), -7)
                    result = result + max(-1 * (round(abs(result - tempo) / 2)), -7)

                    break

        if ff == 1 or sizeprec >= 1.0:

            # result = result * 100
            temp = result
            ktos_data = pd.read_csv('k2s.csv')
            if shape == 'RO' and 1.0 <= sizeprec < 3.0:
                if ktos == 1 and (ktos_attribute == 'Feather' or ktos_attribute == 'Pinpoint'):
                    ktosd = ktos_data[str(xx)][0]
                    result += ktosd
                elif ktos >= 5:
                    ktosd = ktos_data[str(xx)][1]
                    result += ktosd

                # # if sizeprec >= 1.00 and sizeprec <= 1.499 and cut == 'EX':
                # #     if color == 'D':
                # #         ktosd=3
                # #         result = result + 3
                # #     else:
                # #         ktosd=2
                # #         result = result + 2
                # # if sizeprec >= 1.50 and sizeprec <= 1.999 and cut == 'EX':
                # #     if color == 'D':
                # #         ktosd=2
                # #         result = result + 2
                # #     else:
                # #         ktosd=1
                # #         result = float(result) +  float(1)
                # # if sizeprec >= 2.00 and sizeprec <= 2.999 and cut == 'EX':
                # #     if color == 'D':
                # #         ktosd=2
                # #         result = result + 2
                # #     else:
                # #         ktosd=1
                # #         result = result + 1
                #
                # if xx == 1:
                #     if ktos == 1:
                #         ktosd = 1
                #         result = result + 1.0
                #     elif ktos >= 5:
                #         ktosd = -1
                #         result = -1.0 + result
                # elif xx == 2:
                #     if ktos == 1:
                #         ktosd = 1
                #         result = result + 1.0
                #     elif ktos >= 5:
                #         ktosd = -1
                #         result = -1.0 + result
                # elif xx == 3:
                #     if ktos == 1:
                #         ktosd = 1
                #         result = result + 1.0
                #     elif ktos >= 5:
                #         ktosd = -1
                #         result = -1.0 + result
                # elif xx == 4:
                #     if ktos == 1:
                #         ktosd = 1.5
                #         result = result + 1.5
                #     elif ktos >= 5:
                #         ktosd = -1
                #         result = -1.0 + result
                # elif xx == 5:
                #     if ktos == 1:
                #         ktosd = 1.5
                #         result = result + 1.5
                #     if ktos >= 5:
                #         ktosd = -1
                #         result = -1.0 + result
                # elif xx == 6:
                #     if ktos == 1:
                #         ktosd = 1
                #         result = result + 1.0
                #     if ktos >= 5:
                #         ktosd = 0.0
                #         result = 0.0 + result
                # elif xx == 1:
                #     if ktos == 1:
                #         ktosd = 3
                #         result = result + 3.0
                #     if ktos >= 5:
                #         ktosd = 0
                #         result = 0.0 + result
                #
                #         # colour
                # # if color == 'N': #todo: ask shraddha M or N
                # #     if szgr == '1.01-1.09' or szgr == '2.01-2.09' or szgr == '1.50-1.69':
                # #         if cut == 'EX':
                # #             MNcolord=-7
                # #             result = -7 + result
                #
                # # if szgr=='1.01-1.09' or szgr=='1.50-1.69' or szgr=='2.01-2.09':
                # #     if cut=='VG':
    elif (shape != 'RO'):
        df2 = pd.read_csv('fancy_base.csv')
        result = 0.00

        for i in range(len(df2)):
            if clarity == 'IF':
                if shape == df2['Shape'][i] and color == df2['Clarity'][i] and szgr == df2['Size'][i]:
                    result = float(df2['IF'][i])
                    base = float(df2['IF'][i])
                    ff = 2
                    break
            elif clarity == 'VVS1':
                if shape == df2['Shape'][i] and color == df2['Clarity'][i] and szgr == df2['Size'][i]:
                    result = float(df2['VVS1'][i])
                    base = float(df2['VVS1'][i])
                    ff = 2
                    break
            elif clarity == 'VVS2':
                if shape == df2['Shape'][i] and color == df2['Clarity'][i] and szgr == df2['Size'][i]:
                    result = float(df2['VVS2'][i])
                    base = float(df2['VVS2'][i])
                    ff = 2
                    break
            elif clarity == 'VS1':
                if shape == df2['Shape'][i] and color == df2['Clarity'][i] and szgr == df2['Size'][i]:
                    result = float(df2['VS1'][i])
                    base = float(result)
                    ff = 2
                    break
            elif clarity == 'VS2':
                if shape == df2['Shape'][i] and color == df2['Clarity'][i] and szgr == df2['Size'][i]:
                    result = float(df2['VS2'][i])
                    base = float(result)
                    ff = 2
                    break
            elif clarity == 'SI1':
                if shape == df2['Shape'][i] and color == df2['Clarity'][i] and szgr == df2['Size'][i]:
                    result = float(df2['SI1'][i])
                    base = float(result)
                    ff = 2
                    break
            elif clarity == 'SI2':
                if shape == df2['Shape'][i] and color == df2['Clarity'][i] and szgr == df2['Size'][i]:
                    result = float(df2['SI2'][i])
                    base = float(result)
                    ff = 2
                    break
            temp = result
    if sizeprec < 1.0 and shape == 'RO':
        df = pd.read_csv('Dossbase.csv')
        for i in range(len(df)):
            if df['Clarity'][i] == clarity and szgr == df['Size'][i] and df['Fluo'][i] == fluo:
                if cut == 'EX' and polish == 'EX' and symmetry == 'EX':
                    if df['Cut'][i] == 'EX' and df['Polish'][i] == 'EX' and df['Symmetry'][i] == 'EX':
                        if color == 'D':
                            result = result + float(df['D'][i])
                            base = result
                            ff = 1
                        elif color == 'E':
                            result = result + float(df['E'][i])
                            base = result
                            ff = 1
                        elif color == 'F':
                            result = result + float(df['F'][i])
                            base = result
                            ff = 1
                        elif color == 'G':
                            result = result + float(df['G'][i])
                            base = result
                            ff = 1
                        elif color == 'H':
                            result = result + float(df['H'][i])
                            base = result
                            ff = 1
                        elif color == 'I':
                            result = result + float(df['I'][i])
                            base = result
                            ff = 1
                        elif color == 'J':
                            result = result + float(df['J'][i])
                            base = result
                            ff = 1
                        elif color == 'L':
                            result = result + float(df['L'][i])
                            base = result
                            ff = 1
                        elif color == 'M' or color == 'N':
                            result = result + float(df['M'][i])
                            base = result
                            # if color == 'N': TBD
                            #     MNcolorD = -7
                            #     result = result - 7
                            color = 'M'

                            ff = 1
                        elif color == 'K':
                            result = result + float(df['K'][i])
                            base = result
                            ff = 1
                        break
                else:
                    # if(cut==df['CUT'][i] and df['POL'][i] == 'EX' and df['SYM'][i] == 'EX'):
                    #     continue
                    if (cut == df['Cut'][i] and df['Polish'][i] == 'DD' and df['Symmetry'][i] == 'DD'):
                        if color == 'D':
                            result = result + df['D'][i]
                            base = result
                            ff = 1
                        elif color == 'E':
                            result = result + df['E'][i]
                            base = result
                            ff = 1
                        elif color == 'F':
                            result = result + df['F'][i]
                            base = result
                            ff = 1
                        elif color == 'G':
                            result = result + df['G'][i]
                            base = result
                            ff = 1
                        elif color == 'H':
                            result = result + df['H'][i]
                            base = result
                            ff = 1
                        elif color == 'I':
                            result = result + df['I'][i]
                            base = result
                            ff = 1
                        elif color == 'J':
                            result = result + df['J'][i]
                            base = result
                            ff = 1
                        elif color == 'L':
                            result = result + df['L'][i]
                            base = result
                            ff = 1
                        elif color == 'M':
                            result = result + df['M'][i]
                            base = result
                            ff = 1
                        elif color == 'K':
                            result = result + df['K'][i]
                            base = result
                            ff = 1
                        break
        temp = result
        tempos = 0
        if (cut == 'EX' or cut == 'VG') and (
                polish == 'GD' or symmetry == 'GD') and ff == 1 and sizeprec >= 0.3 and sizeprec <= 2.99:
            for i in range(len(df)):
                if (df['Clarity'][i] == clarity and szgr == df['Size'][i] and df['Fluo'][i] == fluo and df['Cut'][
                    i] == 'GD' and df['Polish'][i] == 'DD' and df['Symmetry'][i] == 'DD'):
                    if color == 'D':
                        tempos = df['D'][i]
                        ff = 1
                    elif color == 'E':
                        tempos = df['E'][i]
                        ff = 1
                    elif color == 'F':
                        tempos = df['F'][i]
                        ff = 1
                    elif color == 'G':
                        tempos = df['G'][i]
                        ff = 1
                    elif color == 'H':
                        tempos = df['H'][i]
                        ff = 1
                    elif color == 'I':
                        result = result + df['I'][i]
                        ff = 1
                    elif color == 'J':
                        tempos = df['J'][i]
                        ff = 1
                    elif color == 'L':
                        tempos = df['L'][i]
                        ff = 1
                    elif color == 'M':
                        tempos = df['M'][i]
                        ff = 1
                    elif color == 'K':
                        tempos = df['K'][i]
                        ff = 1
            gdd = max(-1 * (round(abs(result - tempos) / 2)), -5)
            result = result + max(-1 * (round(abs(result - tempos) / 2)), -5)

            # DIAMETER
    # if (shape == 'RO'):
    #     if sizeprec >= 1.0 and sizeprec <= 1.49:
    #         if cut == 'VG':
    #             if (xx == 1):
    #                 if diameter <= 6.2:
    #                     result = result - 0.5
    #                     diameterd=-0.5
    #                 elif diameter >= 6.3:
    #                     result = result + 1.5
    #                     diameterd=1.5
    #             elif (xx == 2):
    #                 if diameter <= 6.2:
    #                     result = result - 0.5
    #                     diameterd=-0.5
    #                 elif diameter >= 6.3:
    #                     result = result + 1.5
    #                     diameterd=1.5
    #             elif (xx == 3 or xx == 4):
    #                 if diameter <= 6.2:
    #                     result = result - 0.5
    #                     diameterd=-0.5
    #                 elif diameter >= 6.3:
    #                     diameterd=1.5
    #                     result = result + 1.5
    #             elif (xx == 5):
    #                 if diameter <= 6.2:
    #                     diameterd=-0.1
    #                     result = result - 0.1
    #                 elif diameter >= 6.3:
    #                     diameterd=1.5
    #                     result = result + 1.5
    #             elif (xx == 6):
    #                 if diameter <= 6.2:
    #                     diameterd=-0.5
    #                     result = result - 0.5
    #                 elif diameter >= 6.3:
    #                     diameterd=1.5
    #                     result = result + 1.5
    #             elif (xx == 7):
    #                 if diameter <= 6.2:
    #                     diameterd=0
    #                     result = result - 0.0
    #                 elif diameter >= 6.3:
    #                     diameterd=0
    #                     result = result + 1.0
    #             elif (xx == 8):
    #                 if diameter <= 6.2:
    #                     diameterd=0
    #                     result = result - 0.0
    #                 elif diameter >= 6.3:
    #                     diameterd=1
    #                     result = result + 1.0
    #     if cut == 'EX' and polish == 'EX' and symmetry == 'EX' and (fluo == 'None' or fluo == 'Faint'):
    #         if sizeprec >= 0.35 and sizeprec <= 0.399 and diameter > 4.5:
    #             if color == 'D':
    #                 if clarity == 'IF':
    #                     diameterd=9
    #                     result = result + 9
    #                 elif clarity == 'VVS1':
    #                     result = result + 14
    #                     diameterd=14
    #                 elif clarity == 'VVS2':
    #                     diameterd=21
    #                     result = result + 21
    #             if color == 'E':
    #                 if clarity == 'IF':
    #                     diameterd=7
    #                     result = result + 7
    #                 elif clarity == 'VVS1':
    #                     diameterd=8
    #                     result = result + 8
    #                 elif clarity == 'VVS2':
    #                     diameterd=2
    #                     result = result + 2
    #             if color == 'F':
    #                 if clarity == 'IF':
    #                     diameterd=7
    #                     result = result + 7
    #                 elif clarity == 'VVS1':
    #                     diameterd=7
    #                     result = result + 7
    #                 elif clarity == 'VVS2':
    #                     diameterd=2
    #                     result = result + 2
    #         if sizeprec >= 0.60 and sizeprec <= 0.649 and diameter > 5.4:
    #             if color == 'D':
    #                 if clarity == 'IF':
    #                     diameterd=6
    #                     result = result + 6
    #                 elif clarity == 'VVS1':
    #                     result = result + 9
    #                     diameterd=9
    #                 elif clarity == 'VVS2':
    #                     result = result + 9
    #                     diameterd=9
    #             if color == 'E':
    #                 if clarity == 'IF':
    #                     diameterd=7
    #                     result = result + 7
    #                 elif clarity == 'VVS1':
    #                     diameterd=5
    #                     result = result + 5
    #                 elif clarity == 'VVS2':
    #                     diameterd=1
    #                     result = result + 1
    #             if color == 'F':
    #                 if clarity == 'IF':
    #                     diameterd=6
    #                     result = result + 6
    #                 elif clarity == 'VVS1':
    #                     result = result + 6
    #                     diameterd=6
    #                 elif clarity == 'VVS2':
    #                     diameterd=1
    #                     result = result + 1
    #         if sizeprec >= 0.80 and sizeprec <= 0.849 and diameter > 6.0:
    #             if color == 'D':
    #                 if clarity == 'IF':
    #                     diameterd=16
    #                     result = result + 16
    #                 elif clarity == 'VVS1':
    #                     diameterd=10
    #                     result = result + 10
    #                 elif clarity == 'VVS2':
    #                     diameterd=11
    #                     result = result + 11
    #             if color == 'E':
    #                 if clarity == 'IF':
    #                     diameterd=5
    #                     result = result + 5
    #                 elif clarity == 'VVS1':
    #                     diameterd=4
    #                     result = result + 4
    #                 elif clarity == 'VVS2':
    #                     diameterd=13
    #                     result = result + 13
    #             if color == 'F':
    #                 if clarity == 'IF':
    #                     result = result + 9
    #                     diameterd=9
    #                 elif clarity == 'VVS1':
    #                     result = result + 9
    #                     diameterd=9
    #                 elif clarity == 'VVS2':
    #                     result = result + 13
    #                     diameterd=13
    #         if sizeprec >= 0.95 and sizeprec <= 0.999 and diameter > 6.3:
    #             if color == 'D':
    #                 if clarity == 'IF':
    #                     diameterd=5
    #                     result = result + 5
    #                 elif clarity == 'VVS1':
    #                     diameterd=6
    #                     result = result + 6
    #                 elif clarity == 'VVS2':
    #                     diameterd=7
    #                     result = result + 7
    #             if color == 'E':
    #                 if clarity == 'IF':
    #                     diameterd=6
    #                     result = result + 6
    #                 elif clarity == 'VVS1':
    #                     diameterd=5
    #                     result = result + 5
    #                 elif clarity == 'VVS2':
    #                     diameterd=5
    #                     result = result + 5
    #             if color == 'F':
    #                 if clarity == 'IF':
    #                     result = result + 6
    #                     diameterd=6
    #                 elif clarity == 'VVS1':
    #                     result = result + 6
    #                     diameterd=6
    #                 elif clarity == 'VVS2':
    #                     result = result + 5
    #                     diameterd=5
    diameterd = get_diameter_premium(shape, cut, polish, symmetry, fluo, szgr, min_diam, max_diam, color, clarity)
    result += diameterd

    # bgm- Note- need to ask whether it is one exculsive table or multiple table combined- currently considered one exclusive table
    if ((sizeprec >= 1.0) and ((cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
            symmetry == 'EX' or symmetry == 'VG')) and (
            fluo == 'None' or fluo == 'Medium' or fluo == 'Faint') and shape == 'RO'):
        bgm_ro = pd.read_csv('BGM_3VG.csv')
        for i in range(len(bgm_ro)):
            if bgm_ro['BGM Type'][i] == colshaded:
                colshaded += bgm_ro[str(xx)][i]
                result += colshaded
                break
            elif bgm_ro['BGM Type'][i] == milkyd:
                milkyd += bgm_ro[str(xx)][i]
                result += milkyd
                break
        # df3 = pd.read_csv('bgmvg.csv')
        # # BROWN
        # for i in range(len(df3)):
        #     # next line giving eror
        #     if ((shape == 'RO') and (xx == df3['Section'][i]) and (brown == df3['bgm'][i]) and (
        #             df3['Shape'][i] == 'RO')):
        #         result = result + df3['Discount'][i]
        #         colshaded = df3['Discount'][i]
        #         break
        #     elif ((shape != 'RO') and (xx == df3['Section'][i]) and (brown == df3['bgm'][i]) and (
        #             df3['Shape'][i] == 'FANCY')):
        #         result = result + df3['Discount'][i]
        #         colshaded = df3['Discount'][i]
        #         break
        #
        # # GREY
        # for i in range(len(df3)):
        #     # next line giving eror
        #     if ((shape == 'RO') and (xx == df3['Section'][i]) and (grey == df3['bgm'][i]) and (
        #             df3['Shape'][i] == 'RO')):
        #         result = result + df3['Discount'][i]
        #         colshaded = df3['Discount'][i]
        #         break
        #     elif ((shape != 'RO') and (xx == df3['Section'][i]) and (grey == df3['bgm'][i]) and (
        #             df3['Shape'][i] == 'FANCY')):
        #         result = result + df3['Discount'][i]
        #         colshaded = df3['Discount'][i]
        #         break
        #         # GREEN
        # for i in range(len(df3)):
        #     # next line giving eror
        #     if ((shape == 'RO') and (xx == df3['Section'][i]) and (green == df3['bgm'][i]) and (
        #             df3['Shape'][i] == 'RO')):
        #         result = result + float(df3['Discount'][i])
        #         colshaded = df3['Discount'][i]
        #         break
        #     elif ((shape != 'RO') and (xx == df3['Section'][i]) and (green == df3['bgm'][i]) and (
        #             df3['Shape'][i] == 'FANCY')):
        #         result = result + float(df3['Discount'][i])
        #         colshaded = df3['Discount'][i]
        #         break
        #         # MILKY
        # for i in range(len(df3)):
        #     # next line giving eror
        #     if ((shape == 'RO') and (xx == df3['Section'][i]) and (milky == df3['bgm'][i]) and (
        #             df3['Shape'][i] == 'RO')):
        #         result = result + float(df3['Discount'][i])
        #         milkyd = float(df3['Discount'][i])
        #         break
        #     elif ((shape != 'RO') and (xx == df3['Section'][i]) and (milky == df3['bgm'][i]) and (
        #             df3['Shape'][i] == 'FANCY')):
        #         result = result + float(df3['Discount'][i])
        #         milkyd = float(df3['Discount'][i])
        #         break
        #         # #OFFCOLOR
        #         # for i in range(len(df3)):
        #         #     #next line giving eror
        #         #     if ((shape == 'RO') and (xx == df3['Section'][i]) and (offcolor == df3['bgm'][i]) and (df3['Shape'][i]=='RO') ):
        #         #         result=result+ df3['Discount'][i]
        #         #         break
        #         #     elif ((shape!='RO') and (xx == df3['Section'][i]) and ( offcolor == df3['bgm'][i]) and (df3['Shape'][i]=='FANCY')):
        #         #         result=result+ df3['Discount'][i]
        #         break
    elif shape == 'RO' and sizeprec >= 1.0:
        df3 = pd.read_csv('BGM_RO.csv')
        for i in range(len(df3)):
            if df3['BGM Type'][i] == colshaded:
                colshaded += df3[str(xx)][i]
                result += colshaded
                break
            elif df3['BGM Type'][i] == milkyd:
                milkyd += df3[str(xx)][i]
                result += milkyd
                break
        #     if (sizeprec >= 1.0 and (shape == 'RO') and (xx == df3['Section'][i]) and (brown == df3['bgm'][i])):
        #         result = result + df3['Discount'][i]
        #         colshaded = df3['Discount'][i]
        #         break
        # for i in range(len(df3)):
        #     if (sizeprec >= 1.0 and (shape == 'RO') and (xx == df3['Section'][i]) and (green == df3['bgm'][i])):
        #         result = result + df3['Discount'][i]
        #         colshaded = df3['Discount'][i]
        #         break
        # for i in range(len(df3)):
        #     if (sizeprec >= 1.0 and (shape == 'RO') and (xx == df3['Section'][i]) and (grey == df3['bgm'][i])):
        #         result = result + df3['Discount'][i]
        #         colshaded = df3['Discount'][i]
        #         break
        # for i in range(len(df3)):
        #     if (sizeprec >= 1.0 and (shape == 'RO') and (xx == df3['Section'][i]) and (milky == df3['bgm'][i])):
        #         result = result + df3['Discount'][i]
        #         milkyd = df3['Discount'][i]
        #         break
        # for i in range(len(df3)):
        #     if ((shape == 'RO') and (xx == df3['Section'][i]) and (offcolor == df3['bgm'][i])):
        #         result=result+ df3['Discount'][i]
        #         break
    # add dossiers as well-irrelevant I guess now
    elif shape != 'RO' and sizeprec >= 1.0:
        df3 = pd.read_csv('BGM_Fancy.csv')
        for i in range(len(df3)):
            if df3['BGM Type'][i] == colshaded:
                colshaded += df3[str(xx)][i]
                result += colshaded
                break
            elif df3['BGM Type'][i] == milkyd:
                milkyd += df3[str(xx)][i]
                result += milkyd
                break
        # milky- written as per pricing module file
        # if (clarity == 'VS1' or clarity == 'VS2'):
        #     if milky == 'M1':
        #         result = result - 7
        #         milkyd = -7
        #     if milky == 'M2-' or milky == 'M2' or milky == 'M3':
        #         result = result - 13
        #         milkyd = -13
        #     # if milky=='M1+':
        #     #     result=result-4
        #     #     milky=-4
        # if (clarity == 'SI1' or clarity == 'SI2'):
        #     if milky == 'M1':
        #         result = result - 11
        #         milkyd = -11
        #     if milky == 'M2-' or milky == 'M2' or milky == 'M3':
        #         result = result - 16
        #         milkyd = -16
        # if (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2'):
        #     if (color == 'D' or color == 'E' or color == 'F'):
        #         if (green == 'B1' or brown == 'B1' or grey == 'B1'):
        #             colshaded = -3
        #             result = result + colshaded
        #         elif (green == 'B2' or brown == 'B2' or grey == 'B2'):
        #             colshaded = -8
        #             result = result + colshaded
        #         elif (green == 'B3' or brown == 'B3' or grey == 'B3'):
        #             colshaded = -13
        #             result = result + colshaded
        #         elif (green == 'G1' or brown == 'G1' or grey == 'G1'):
        #             colshaded = -3
        #             result = result + colshaded
        #         elif (green == 'G2' or brown == 'G2' or grey == 'G2'):
        #             colshaded = -8
        #             result = result + colshaded
        #         elif (green == 'G3' or brown == 'G3' or grey == 'G3'):
        #             colshaded = -13
        #             result = result + colshaded
        #         elif (green == 'MT1' or brown == 'MT1' or grey == 'MT1'):
        #             colshaded = -3
        #             result = result + colshaded
        #         elif (green == 'MT2' or brown == 'MT2' or grey == 'MT2'):
        #             colshaded = -8
        #             result = result + colshaded
        #         elif (green == 'MT3' or brown == 'MT3' or grey == 'MT3'):
        #             colshaded = -13
        #             result = result + colshaded
        #     elif (color == 'G' or color == 'H' or color == 'I'):
        #         if (green == 'B1' or brown == 'B1' or grey == 'B1'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'B2' or brown == 'B2' or grey == 'B2'):
        #             colshaded = -9
        #             result = result + colshaded
        #         elif (green == 'B3' or brown == 'B3' or grey == 'B3'):
        #             colshaded = -14
        #             result = result + colshaded
        #         elif (green == 'G1' or brown == 'G1' or grey == 'G1'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'G2' or brown == 'G2' or grey == 'G2'):
        #             colshaded = -9
        #             result = result + colshaded
        #         elif (green == 'G3' or brown == 'G3' or grey == 'G3'):
        #             colshaded = -14
        #             result = result + colshaded
        #         elif (green == 'MT1' or brown == 'MT1' or grey == 'MT1'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'MT2' or brown == 'MT2' or grey == 'MT2'):
        #             colshaded = -9
        #             result = result + colshaded
        #         elif (green == 'MT3' or brown == 'MT3' or grey == 'MT3'):
        #             colshaded = -14
        #             result = result + colshaded
        #     elif (color == 'J' or color == 'K' or color == 'L' or color == 'M'):
        #         if (green == 'B1' or brown == 'B1' or grey == 'B1'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'B2' or brown == 'B2' or grey == 'B2'):
        #             colshaded = -9
        #             result = result + colshaded
        #         elif (green == 'B3' or brown == 'B3' or grey == 'B3'):
        #             colshaded = -14
        #             result = result + colshaded
        #         elif (green == 'G1' or brown == 'G1' or grey == 'G1'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'G2' or brown == 'G2' or grey == 'G2'):
        #             colshaded = -9
        #             result = result + colshaded
        #         elif (green == 'G3' or brown == 'G3' or grey == 'G3'):
        #             colshaded = -14
        #             result = result + colshaded
        #         elif (green == 'MT1' or brown == 'MT1' or grey == 'MT1'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'MT2' or brown == 'MT2' or grey == 'MT2'):
        #             colshaded = -9
        #             result = result + colshaded
        #         elif (green == 'MT3' or brown == 'MT3' or grey == 'MT3'):
        #             colshaded = -14
        #             result = result + colshaded
        #
        # elif (clarity == 'VS1' or clarity == 'VS2'):
        #     if (color == 'D' or color == 'E' or color == 'F'):
        #         if (green == 'B1' or brown == 'B1' or grey == 'B1'):
        #             colshaded = -4
        #             result = result + colshaded
        #         elif (green == 'B2' or brown == 'B2' or grey == 'B2'):
        #             colshaded = -8
        #             result = result + colshaded
        #         elif (green == 'B3' or brown == 'B3' or grey == 'B3'):
        #             colshaded = -13
        #             result = result + colshaded
        #         elif (green == 'G1' or brown == 'G1' or grey == 'G1'):
        #             colshaded = -4
        #             result = result + colshaded
        #         elif (green == 'G2' or brown == 'G2' or grey == 'G2'):
        #             colshaded = -8
        #             result = result + colshaded
        #         elif (green == 'G3' or brown == 'G3' or grey == 'G3'):
        #             colshaded = -13
        #             result = result + colshaded
        #         elif (green == 'MT1' or brown == 'MT1' or grey == 'MT1'):
        #             colshaded = -4
        #             result = result + colshaded
        #         elif (green == 'MT2' or brown == 'MT2' or grey == 'MT2'):
        #             colshaded = -8
        #             result = result + colshaded
        #         elif (green == 'MT3' or brown == 'MT3' or grey == 'MT3'):
        #             colshaded = -13
        #             result = result + colshaded
        #     elif (color == 'G' or color == 'H' or color == 'I'):
        #         if (green == 'B1' or brown == 'B1' or grey == 'B1'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'B2' or brown == 'B2' or grey == 'B2'):
        #             colshaded = -8
        #             result = result + colshaded
        #         elif (green == 'B3' or brown == 'B3' or grey == 'B3'):
        #             colshaded = -13
        #             result = result + colshaded
        #         elif (green == 'G1' or brown == 'G1' or grey == 'G1'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'G2' or brown == 'G2' or grey == 'G2'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'G3' or brown == 'G3' or grey == 'G3'):
        #             colshaded = -13
        #             result = result + colshaded
        #         elif (green == 'MT1' or brown == 'MT1' or grey == 'MT1'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'MT2' or brown == 'MT2' or grey == 'MT2'):
        #             colshaded = -8
        #             result = result + colshaded
        #         elif (green == 'MT3' or brown == 'MT3' or grey == 'MT3'):
        #             colshaded = -13
        #             result = result + colshaded
        #     elif (color == 'J' or color == 'K' or color == 'L' or color == 'M'):
        #         if (green == 'B1' or brown == 'B1' or grey == 'B1'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'B2' or brown == 'B2' or grey == 'B2'):
        #             colshaded = -8
        #             result = result + colshaded
        #         elif (green == 'B3' or brown == 'B3' or grey == 'B3'):
        #             colshaded = -13
        #             result = result + colshaded
        #         elif (green == 'G1' or brown == 'G1' or grey == 'G1'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'G2' or brown == 'G2' or grey == 'G2'):
        #             colshaded = -8
        #             result = result + colshaded
        #         elif (green == 'G3' or brown == 'G3' or grey == 'G3'):
        #             colshaded = -13
        #             result = result + colshaded
        #         elif (green == 'MT1' or brown == 'MT1' or grey == 'MT1'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'MT2' or brown == 'MT2' or grey == 'MT2'):
        #             colshaded = -8
        #             result = result + colshaded
        #         elif (green == 'MT3' or brown == 'MT3' or grey == 'MT3'):
        #             colshaded = -13
        #             result = result + colshaded
        # elif (clarity == 'SI1' or clarity == 'SI2'):
        #     if (color == 'D' or color == 'E' or color == 'F'):
        #         if (green == 'B1' or brown == 'B1' or grey == 'B1'):
        #             colshaded = -3
        #             result = result + colshaded
        #         elif (green == 'B2' or brown == 'B2' or grey == 'B2'):
        #             colshaded = -7
        #             result = result + colshaded
        #         elif (green == 'B3' or brown == 'B3' or grey == 'B3'):
        #             colshaded = -12
        #             result = result + colshaded
        #         elif (green == 'G1' or brown == 'G1' or grey == 'G1'):
        #             colshaded = -3
        #             result = result + colshaded
        #         elif (green == 'G2' or brown == 'G2' or grey == 'G2'):
        #             colshaded = -7
        #             result = result + colshaded
        #         elif (green == 'G3' or brown == 'G3' or grey == 'G3'):
        #             colshaded = -12
        #             result = result + colshaded
        #         elif (green == 'MT1' or brown == 'MT1' or grey == 'MT1'):
        #             colshaded = -3
        #             result = result + colshaded
        #         elif (green == 'MT2' or brown == 'MT2' or grey == 'MT2'):
        #             colshaded = -7
        #             result = result + colshaded
        #         elif (green == 'MT3' or brown == 'MT3' or grey == 'MT3'):
        #             colshaded = -12
        #             result = result + colshaded
        #     elif (color == 'G' or color == 'H' or color == 'I'):
        #         if (green == 'B1' or brown == 'B1' or grey == 'B1'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'B2' or brown == 'B2' or grey == 'B2'):
        #             colshaded = -8
        #             result = result + colshaded
        #         elif (green == 'B3' or brown == 'B3' or grey == 'B3'):
        #             colshaded = -13
        #             result = result + colshaded
        #         elif (green == 'G1' or brown == 'G1' or grey == 'G1'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'G2' or brown == 'G2' or grey == 'G2'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'G3' or brown == 'G3' or grey == 'G3'):
        #             colshaded = -13
        #             result = result + colshaded
        #         elif (green == 'MT1' or brown == 'MT1' or grey == 'MT1'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'MT2' or brown == 'MT2' or grey == 'MT2'):
        #             colshaded = -8
        #             result = result + colshaded
        #         elif (green == 'MT3' or brown == 'MT3' or grey == 'MT3'):
        #             colshaded = -13
        #             result = result + colshaded
        #     elif (color == 'J' or color == 'K' or color == 'L' or color == 'M'):
        #         if (green == 'B1' or brown == 'B1' or grey == 'B1'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'B2' or brown == 'B2' or grey == 'B2'):
        #             colshaded = -9
        #             result = result + colshaded
        #         elif (green == 'B3' or brown == 'B3' or grey == 'B3'):
        #             colshaded = -14
        #             result = result + colshaded
        #         elif (green == 'G1' or brown == 'G1' or grey == 'G1'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'G2' or brown == 'G2' or grey == 'G2'):
        #             colshaded = -9
        #             result = result + colshaded
        #         elif (green == 'G3' or brown == 'G3' or grey == 'G3'):
        #             colshaded = -14
        #             result = result + colshaded
        #         elif (green == 'MT1' or brown == 'MT1' or grey == 'MT1'):
        #             colshaded = -5
        #             result = result + colshaded
        #         elif (green == 'MT2' or brown == 'MT2' or grey == 'MT2'):
        #             colshaded = -9
        #             result = result + colshaded
        #         elif (green == 'MT3' or brown == 'MT3' or grey == 'MT3'):
        #             colshaded = -14
        #             result = result + colshaded

    elif shape == 'RO' and sizeprec < 1.0:
        df3 = pd.read_csv('BGM_dossier.csv')
        for i in range(len(df3)):
            if df3['BGM Type'][i] == colshaded:
                colshaded += df3[str(xx)][i]
                result += colshaded
                break
            elif df3['BGM Type'][i] == milkyd:
                milkyd += df3[str(xx)][i]
                result += milkyd
                break

    # Cut
    if shape == 'RO' and sizeprec >= 1:
        if (fluo == 'Medium') and (cutcomments == 'VG2' or cutcomments == 'GD2'):
            result = result
        else:
            cut_comments_data = pd.read_csv('cut_comments.csv')
            cps_val = get_cut(cut, polish, symmetry)  # cps stands for cut, poly, sym combo
            for i in range(len(cut_comments_data)):
                if cps_val == cut_comments_data['Cut'][i] and cutcomments == cut_comments_data['Cut Comment'][i]:
                    cutcommentsd = cut_comments_data[str(xx)][i]
                    result += cutcommentsd
    elif sizeprec >= 1:
        cut_comments_data = pd.read_csv('cut_comments.csv')
        cps_val = 'Fancy Shape'  # cps stands for cut, poly, sym combo
        for i in range(len(cut_comments_data)):
            if cps_val == cut_comments_data['Cut'][i] and cutcomments == cut_comments_data['Cut Comment'][i]:
                cutcommentsd = cut_comments_data[str(xx)][i]
                result += cutcommentsd

    # if ((fluo == 'Medium') and (cutcomments == 'VG->VG2' or cutcomments == 'G->GD2')) or shape != 'RO':
    #     result = result
    # else:
    #     if cutcomments == '3EX->EX2':
    #         if (xx == 1):
    #             result = result - 2.0
    #             cutcommentsd = -2
    #         elif (xx == 2):
    #             result = result - 2.0
    #             cutcommentsd = -2
    #         elif (xx == 3):
    #             result = result - 1.0
    #             cutcommentsd = -1
    #         elif (xx == 4):
    #             result = result - 2.0
    #             cutcommentsd = -2
    #         elif (xx == 5):
    #             result = result - 2.0
    #             cutcommentsd = -2
    #         elif (xx == 6):
    #             result = result - 1.0
    #             cutcommentsd = -1
    #         elif (xx == 7):
    #             result = result - 1.0
    #             cutcommentsd = -1
    #         elif (xx == 8):
    #             result = result - 1.0
    #             cutcommentsd = -1
    #         elif (xx == 9):
    #             result = result - 0.5
    #             cutcommentsd = -0.5
    #
    #     if cutcomments == 'EX->EX2':
    #         if (xx == 1):
    #             result = result - 2.0
    #             cutcommentsd = -2
    #         elif (xx == 2):
    #             result = result - 2.0
    #             cutcommentsd = -2
    #         elif (xx == 3):
    #             result = result - 1.0
    #             cutcommentsd = -1
    #         elif (xx == 4):
    #             result = result - 2.0
    #             cutcommentsd = -2
    #         elif (xx == 5):
    #             result = result - 2.0
    #             cutcommentsd = -2
    #         elif (xx == 6):
    #             result = result - 1.0
    #             cutcommentsd = -1
    #         elif (xx == 7):
    #             result = result - 1.5
    #             cutcommentsd = -1.5
    #         elif (xx == 8):
    #             result = result - 1.5
    #             cutcommentsd = -1.5
    #         elif (xx == 9):
    #             result = result - 0.5
    #             cutcommentsd = -0.5
    #     if cutcomments == 'VG->VG1':
    #         if (xx == 1):
    #             result = result + 2.0
    #             cutcommentsd = 2
    #         elif (xx == 2):
    #             result = result + 2.0
    #             cutcommentsd = 2
    #         elif (xx == 3):
    #             result = result + 2.0
    #             cutcommentsd = 2
    #         elif (xx == 4):
    #             result = result + 2.0
    #             cutcommentsd = 2
    #         elif (xx == 5):
    #             result = result + 2.0
    #             cutcommentsd = 2
    #         elif (xx == 6):
    #             result = result + 1.5
    #             cutcommentsd = 1.5
    #         elif (xx == 7):
    #             result = result + 1.5
    #             cutcommentsd = 1.5
    #         elif (xx == 8):
    #             result = result + 1.0
    #             cutcommentsd = 1
    #         elif (xx == 9):
    #             result = result + 1.0
    #             cutcommentsd = 1

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
        # if (surfacegraining == '0' or internalgraining == '0' or surfacegraining == 'NN' or internalgraining == 'NN'):
        #             df21 = pd.read_csv('graining.csv')
        #             result1 = 0
        #             result2 = 0
        #             for i in range(len(df21)):
        #                 if surfacegraining == df21['Graining'][i]:
        #                     if xx == 1:
        #                         result1 = result1 + df21['1'][i]
        #                     if xx == 2:
        #                         result1 = result1 + df21['2'][i]
        #                     if xx == 3:
        #                         result1 = result1 + df21['3'][i]
        #                     if xx == 4:
        #                         result1 = result1 + df21['4'][i]
        #                     if xx == 5:
        #                         result = result + df21['5'][i]
        #                     if xx == 6:
        #                         result = result + df21['6'][i]
        #                     if xx == 7:
        #                         result = result + df21['7'][i]
        #                     if xx == 8:
        #                         result = result + df21['8'][i]
        #                     if xx == 9:
        #                         result = result + df21['9'][i]
        #                     break
        #             for i in range(len(df21)):
        #                 if internalgraining == df21['Graining'][i]:
        #                     if xx == 1:
        #                         result = result + df21['1'][i]
        #                     if xx == 2:
        #                         result = result + df21['2'][i]
        #                     if xx == 3:
        #                         result = result + df21['3'][i]
        #                     if xx == 4:
        #                         result = result + df21['4'][i]
        #                     if xx == 5:
        #                         result = result + df21['5'][i]
        #                     if xx == 6:
        #                         result = result + df21['6'][i]
        #                     if xx == 7:
        #                         result = result + df21['7'][i]
        #                     if xx == 8:
        #                         result = result + df21['8'][i]
        #                     if xx == 9:
        #                         result = result + df21['9'][i]
        #                     break
        #         else:
        df21 = pd.read_csv('graining.csv')
        result1 = 0
        result2 = 0
        for i in range(len(df21)):
            if graining == df21['Graining'][i]:
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
        # for i in range(len(df21)):
        #     if internalgraining == df21['Graining'][i]:
        #         if xx == 1:
        #             result2 = result2 + df21['1'][i]
        #         if xx == 2:
        #             result2 = result2 + df21['2'][i]
        #         if xx == 3:
        #             result2 = result2 + df21['3'][i]
        #         if xx == 4:
        #             result2 = result2 + df21['4'][i]
        #         if xx == 5:
        #             result2 = result2 + df21['5'][i]
        #         if xx == 6:
        #             result2 = result2 + df21['6'][i]
        #         if xx == 7:
        #             result2 = result2 + df21['7'][i]
        #         if xx == 8:
        #             result2 = result2 + df21['8'][i]
        #         if xx == 9:
        #             result2 = result2 + df21['9'][i]
        #         break
        # if (result1 <= result2):
        #
        #     result = result + result1
        #     grainingd = result1
        # else:
        result = result + result1
        grainingd = result1

    # extras
    extra_data = pd.read_csv('extras.csv')
    if ha != '':
        for i in range(len(extra_data)):
            if extra_data['Field'][i] == 'H&A' and shape == 'RO' and extra_data['Shape'][i] == 'RO':
                had += extra_data[str(xx)][i]
                result += had
                break
            elif extra_data['Field'][i] == 'H&A' and shape != 'RO' and extra_data['Shape'][i] == 'Fancy':
                had += extra_data[str(xx)][i]
                result += had
                break

    if tableclean != '':
        for i in range(len(extra_data)):
            if extra_data['Field'][i] == 'Table Clean' and shape == 'RO' and extra_data['Shape'][i] == 'RO':
                tablecleand += extra_data[str(xx)][i]
                result += tablecleand
                break
            elif extra_data['Field'][i] == 'Table Clean' and shape != 'RO' and extra_data['Shape'][i] == 'Fancy':
                tablecleand += extra_data[str(xx)][i]
                result += tablecleand
                break

    if eyeclean != '':
        for i in range(len(extra_data)):
            if extra_data['Field'][i] == 'Eye Clean' and shape == 'RO' and extra_data['Shape'][i] == 'RO':
                eyecleand += extra_data[str(xx)][i]
                result += eyecleand
                break
            elif extra_data['Field'][i] == 'Eye Clean' and shape != 'RO' and extra_data['Shape'][i] == 'Fancy':
                eyecleand += extra_data[str(xx)][i]
                result += eyecleand
                break

    # if ha == 'Y':
    #     if shape == 'RO':
    #         if xx == 1:
    #             result = result + 1
    #             had = 1
    #         if xx == 2:
    #             result = result + 1
    #             had = 1
    #         if xx == 3:
    #             result = result + 0.5
    #             had = 0.5
    #         if xx == 4:
    #             result = result + 1
    #             had = 1
    #         if xx == 5:
    #             result = result + 1
    #             had = 1
    #         if xx == 6:
    #             result = result + 0.5
    #             had = 0.5
    #         if xx == 7:
    #             result = result + 1
    #             had = 1
    #         if xx == 8:
    #             result = result + 1
    #             had = 1
    #         if xx == 9:
    #             result = result + 0
    #             had = 0
    # if eyeclean == 'Y':
    #     if shape == 'RO':
    #         if xx == 7:
    #             result = result + 1.5
    #             eyecleand = 1.5
    #         if xx == 8:
    #             result = result + 1.5
    #             eyecleand = 1.5
    #         if xx == 9:
    #             result = result + 1
    #             eyecleand = 1
    #     else:
    #         if xx == 7:
    #             result = result + 1.5
    #             eyecleand = 1.5
    #         if xx == 8:
    #             result = result + 1.5
    #             eyecleand = 1.5
    #         if xx == 9 or xx == 5 or xx == 6:
    #             eyecleand = 0.5
    #             result = result + 0.5
    # if tableclean == 'Y':
    #     if shape == 'RO':
    #         if xx == 4 or xx == 5 or xx == 6:
    #             tablecleand = 0.5
    #             result = result + 0.5
    #         if xx == 8 or xx == 7:
    #             tablecleand = 2.0
    #             result = result + 2.0
    #         if xx == 9:
    #             tablecleand = 1
    #             result = result + 1
    #     else:
    #         if xx == 4 or xx == 5:
    #             tablecleand = 1
    #             result = result + 1.0
    #         if xx == 8 or xx == 7:
    #             tablecleand = 2
    #             result = result + 2.0
    #         if xx == 9:
    #             tablecleand = 1
    #             result = result + 1

    # #extras- NOT properly written- change line 445
    # df4=pd.read_csv('extras.csv')
    # for i in range(len(df4)):
    #     if(shape=='RO'):
    #         if(df4['extras'][i]=='H&A' and df4['shape'][i]=='RO' ):
    #             if(df4['value'][i]==ha):
    # if xx==1:
    #     result=result+ df4['1'][i]
    # if xx==2:
    #     result=result+ df4['2'][i]
    # if xx==3:
    #     result=result+ df4['3'][i]
    # if xx==4:
    #     result=result+ df4['4'][i]
    # if xx==5:
    #     result=result+ df4['5'][i]
    # if xx==6:
    #     result=result+ df4['6'][i]
    # if xx==7:
    #     result=result+ df4['7'][i]
    # if xx==8:
    #     result=result+ df4['8'][i]
    # if xx==9:
    #                     result=result+ df4['9'][i]
    #         if(df4['extras'][i]=='Eye Clean' and df4['shape'][i]=='RO' ):
    #             if(df4['value'][i]==eyeclean):
    #                 if xx==1:
    #                     result=result+ df4['1'][i]
    #                 elif xx==2:
    #                     result=result+ df4['2'][i]
    #                 elif xx==3:
    #                     result=result+ df4['3'][i]
    #                 elif xx==4:
    #                     result=result+ df4['4'][i]
    #                 elif xx==5:
    #                     result=result+ df4['5'][i]
    #                 elif xx==6:
    #                     result=result+ df4['6'][i]
    #                 elif xx==7:
    #                     result=result+ df4['7'][i]
    #                 elif xx==8:
    #                     result=result+ df4['8'][i]
    #                 elif xx==9:
    #                     result=result+ df4['9'][i]
    #         if(df4['extras'][i]=='Table Clean' and df4['shape'][i]=='RO' ):
    #             if(df4['value'][i]==tableclean):
    #                 if xx==1:
    #                     result=result+ df4['1'][i]
    #                 elif xx==2:
    #                     result=result+ df4['2'][i]
    #                 elif xx==3:
    #                     result=result+ df4['3'][i]
    #                 elif xx==4:
    #                     result=result+ df4['4'][i]
    #                 elif xx==5:
    #                     result=result+ df4['5'][i]
    #                 elif xx==6:
    #                     result=result+ df4['6'][i]
    #                 elif xx==7:
    #                     result=result+ df4['7'][i]
    #                 elif xx==8:
    #                     result=result+ df4['8'][i]
    #                 elif xx==9:
    #                     result=result+ df4['9'][i]

    #     if(shape!='RO'):
    #         if(df4['extras'][i]=='H&A' and df4['shape'][i]=='Fancy'):
    #             if(df4['value'][i]==ha):
    #                 if xx==1:
    #                     result=result+ df4['1'][i]
    #                 if xx==2:
    #                     result=result+ df4['2'][i]
    #                 if xx==3:
    #                     result=result+ df4['3'][i]
    #                 if xx==4:
    #                     result=result+ df4['4'][i]
    #                 if xx==5:
    #                     result=result+ df4['5'][i]
    #                 if xx==6:
    #                     result=result+ df4['6'][i]
    #                 if xx==7:
    #                     result=result+ df4['7'][i]
    #                 if xx==8:
    #                     result=result+ df4['8'][i]
    #                 if xx==9:
    #                     result=result+ df4['9'][i]
    #         if(df4['extras'][i]=='Eye Clean' and df4['shape'][i]=='FANCY' ):
    #             if(df4['value'][i]==eyeclean):
    #                 if xx==1:
    #                     result=result+ df4['1'][i]
    #                 if xx==2:
    #                     result=result+ df4['2'][i]
    #                 if xx==3:
    #                     result=result+ df4['3'][i]
    #                 if xx==4:
    #                     result=result+ df4['4'][i]
    #                 if xx==5:
    #                     result=result+ df4['5'][i]
    #                 if xx==6:
    #                     result=result+ df4['6'][i]
    #                 if xx==7:
    #                     result=result+ df4['7'][i]
    #                 if xx==8:
    #                     result=result+ df4['8'][i]
    #                 if xx==9:
    #                     result=result+ df4['9'][i]
    #         if(df4['extras'][i]=='Table Clean' and df4['shape'][i]=='FANCY' ):
    #             if(df4['value'][i]==tableclean):
    #                 if xx==1:
    #                     result=result+ df4['1'][i]
    #                 if xx==2:
    #                     result=result+ df4['2'][i]
    #                 if xx==3:
    #                     result=result+ df4['3'][i]
    #                 if xx==4:
    #                     result=result+ df4['4'][i]
    #                 if xx==5:
    #                     result=result+ df4['5'][i]
    #                 if xx==6:
    #                     result=result+ df4['6'][i]
    #                 if xx==7:
    #                     result=result+ df4['7'][i]
    #                 if xx==8:
    #                     result=result+ df4['8'][i]
    #                 if xx==9:
    #                     result=result+ df4['9'][i]

    # Inclusion Grading
    # df5=pd.read_csv('inc_grad.csv')
    # for i in range(len(df5)):
    #     #table
    #     if(df5['Location'][i]=='Table'):
    #         if(df5['Shape'][i]==shape and (clarity==df5['CL1'][i] or clarity==df5['CL2'][i]) and df5['Inclusion'][i]==tableinc):
    #             if xx==1:
    #                 result=result+ df5['1'][i]
    #             if xx==2:
    #                 result=result+ df5['2'][i]
    #             if xx==3:
    #                 result=result+ df5['3'][i]
    #             if xx==4:
    #                 result=result+ df5['4'][i]
    #             if xx==5:
    #                 result=result+ df5['5'][i]
    #             if xx==6:
    #                 result=result+ df5['6'][i]
    #             if xx==7:
    #                 result=result+ df5['7'][i]
    #             if xx==8:
    #                 result=result+ df5['8'][i]
    #             if xx==9:
    #                 result=result+ df5['9'][i]
    #             break
    # for i in range(len(df5)):
    #     #crown
    #     if(df5['Location'][i]=='Crown'):
    #         if(df5['Shape'][i]==shape and (clarity==df5['CL1'][i] or clarity==df5['CL2'][i]) and df5['Inclusion'][i]==crowninc):
    #             if xx==1:
    #                 result=result+ df5['1'][i]
    #             if xx==2:
    #                 result=result+ df5['2'][i]
    #             if xx==3:
    #                 result=result+ df5['3'][i]
    #             if xx==4:
    #                 result=result+ df5['4'][i]
    #             if xx==5:
    #                 result=result+ df5['5'][i]
    #             if xx==6:
    #                 result=result+ df5['6'][i]
    #             if xx==7:
    #                 result=result+ df5['7'][i]
    #             if xx==8:
    #                 result=result+ df5['8'][i]
    #             if xx==9:
    #                 result=result+ df5['9'][i]
    #             break
    # for i in range(len(df5)):
    #     #girdle
    #     if(df5['Location'][i]=='Girdle'):
    #         if(df5['Shape'][i]==shape and (clarity==df5['CL1'][i] or clarity==df5['CL2'][i]) and df5['Inclusion'][i]==girdle_inc):
    #             if xx==1:
    #                 result=result+ df5['1'][i]
    #             if xx==2:
    #                 result=result+ df5['2'][i]
    #             if xx==3:
    #                 result=result+ df5['3'][i]
    #             if xx==4:
    #                 result=result+ df5['4'][i]
    #             if xx==5:
    #                 result=result+ df5['5'][i]
    #             if xx==6:
    #                 result=result+ df5['6'][i]
    #             if xx==7:
    #                 result=result+ df5['7'][i]
    #             if xx==8:
    #                 result=result+ df5['8'][i]
    #             if xx==9:
    #                 result=result+ df5['9'][i]
    #             break
    # for i in range(len(df5)):
    #     #pavilion
    #     if(df5['Location'][i]=='Pavilion'):
    #         if(df5['Shape'][i]==shape and (clarity==df5['CL1'][i] or clarity==df5['CL2'][i]) and df5['Inclusion'][i]==pavilioninc):
    #             if xx==1:
    #                 result=result+ df5['1'][i]
    #             if xx==2:
    #                 result=result+ df5['2'][i]
    #             if xx==3:
    #                 result=result+ df5['3'][i]
    #             if xx==4:
    #                 result=result+ df5['4'][i]
    #             if xx==5:
    #                 result=result+ df5['5'][i]
    #             if xx==6:
    #                 result=result+ df5['6'][i]
    #             if xx==7:
    #                 result=result+ df5['7'][i]
    #             if xx==8:
    #                 result=result+ df5['8'][i]
    #             if xx==9:
    #                 result=result+ df5['9'][i]
    #             break

    # BLACK
    #  (sizeprec<=df6['sizemax'][i]) & (cut==df6['cut'][i]) & (df6['Intensity']==tableintensity)
    if sizeprec < 1.0:
        dossier_black = pd.read_csv('black.csv')
        for i in range(len(dossier_black)):
            if dossier_black['Intensity'][i] == tableintensity and dossier_black['Shape'][i] == 'Dossiers':
                blackd += dossier_black[str(xx)][i]
                result += blackd
                break
            if dossier_black['Intensity'][i] == tableintensity and dossier_black['Shape'][i] == 'Dossiers':
                sideblackd += dossier_black[str(xx)][i]
                result += sideblackd
                break
    else:
        df6 = pd.read_csv('black.csv')
        for i in range(len(df6)):
            # table
            if df6['Location'][i] == 'Table':
                if df6['Shape'][i] == shape and shape == 'RO':
                    if ((sizeprec >= df6['sizemin'][i]) and (cut == df6['cut'][i]) and (
                            sizeprec <= df6['sizemax'][i]) and (
                            tableintensity == df6['Intensity'][i])):
                        if fluo != 'None' and fluo != 'Faint':
                            blackd += df6[str(xx)][i]
                            result += blackd
                            break
                        else:
                            blackd += (df6[str(xx)][i] / 2)
                            result += blackd
                            break
                if df6['Shape'][i] == 'Fancy' and shape != 'RO':
                    if (sizeprec >= df6['sizemin'][i] and sizeprec <= df6['sizemax'][i] and df6['sym'][
                        i] == symmetry and df6['polish'][i] == polish and df6['Intensity'][i] == tableintensity):
                        blackd += df6[str(xx)][i]
                        result += blackd
                        break
            # table
        for i in range(len(df6)):
            # table
            if (df6['Location'][i] == 'Crown'):
                if df6['Shape'][i] == shape and shape == 'RO':
                    if ((sizeprec >= df6['sizemin'][i]) and (cut == df6['cut'][i]) and (
                            sizeprec <= df6['sizemax'][i]) and (
                            tableintensity == df6['Intensity'][i])):
                        if fluo != 'None' and fluo != 'Faint':
                            sideblackd += df6[str(xx)][i]
                            result += sideblackd
                            break
                        else:
                            sideblackd += (df6[str(xx)][i] / 2)
                            result += sideblackd
                            break
                if df6['Shape'][i] == 'Fancy' and shape != 'RO':
                    if (sizeprec >= df6['sizemin'][i] and sizeprec <= df6['sizemax'][i] and df6['sym'][
                        i] == symmetry and df6['polish'][i] == polish and df6['Intensity'][i] == tableintensity):
                        sideblackd += df6[str(xx)][i]
                        result += sideblackd
                        break

        # dossblack = 0.0 TBD
        # if (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2'):
        #     if (color == 'D' or color == 'E' or color == 'F'):
        #         if (tableintensity == 'BT1+'):
        #             dossblack = -1
        #         elif (tableintensity == 'BT1'):
        #             dossblack = -2
        #         elif (tableintensity == 'BT2'):
        #             dossblack = -3
        #         elif (tableintensity == 'BT1'):
        #             dossblack = -4
        #     else:
        #         if (tableintensity == 'BT1+'):
        #             dossblack = -1
        #         elif (tableintensity == 'BT1'):
        #             dossblack = -2
        #         elif (tableintensity == 'BT2'):
        #             dossblack = -3
        #         elif (tableintensity == 'BT1'):
        #             dossblack = -4
        # elif (clarity == 'VS1' or clarity == 'VS2'):
        #     if (color == 'D' or color == 'E' or color == 'F'):
        #         if (tableintensity == 'BT1+'):
        #             dossblack = 0
        #         elif (tableintensity == 'BT1'):
        #             dossblack = -2
        #         elif (tableintensity == 'BT2'):
        #             dossblack = -3
        #         elif (tableintensity == 'BT1'):
        #             dossblack = -4
        #     else:
        #         if (tableintensity == 'BT1+'):
        #             dossblack = 0
        #         elif (tableintensity == 'BT1'):
        #             dossblack = -2
        #         elif (tableintensity == 'BT2'):
        #             dossblack = -3
        #         elif (tableintensity == 'BT1'):
        #             dossblack = -4
        # elif (clarity == 'SI1' or clarity == 'SI2'):
        #     if (color == 'D' or color == 'E' or color == 'F'):
        #         if (tableintensity == 'BT1+'):
        #             dossblack = 0
        #         elif (tableintensity == 'BT1'):
        #             dossblack = -1
        #         elif (tableintensity == 'BT2'):
        #             dossblack = -2
        #         elif (tableintensity == 'BT1'):
        #             dossblack = -4
        #     else:
        #         if (tableintensity == 'BT1+'):
        #             dossblack = 0
        #         elif (tableintensity == 'BT1'):
        #             dossblack = -1
        #         elif (tableintensity == 'BT2'):
        #             dossblack = -2
        #         elif (tableintensity == 'BT1'):
        #             dossblack = -4
        # sidedossblack = 0.0
        # if (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2'):
        #     if (color == 'D' or color == 'E' or color == 'F'):
        #         if (crownintensity == 'BC1+'):
        #             sidedossblack = 0
        #         elif (crownintensity == 'BC1'):
        #             sidedossblack = -1
        #         elif (crownintensity == 'BC2'):
        #             sidedossblack = -3
        #         elif (crownintensity == 'BC1'):
        #             sidedossblack = -4
        #     else:
        #         if (crownintensity == 'BC1+'):
        #             sidedossblack = 0
        #         elif (crownintensity == 'BC1'):
        #             sidedossblack = -1
        #         elif (crownintensity == 'BC2'):
        #             sidedossblack = -2
        #         elif (crownintensity == 'BC1'):
        #             sidedossblack = -3
        # elif (clarity == 'VS1' or clarity == 'VS2'):
        #     if (color == 'D' or color == 'E' or color == 'F'):
        #         if (crownintensity == 'BC1+'):
        #             sidedossblack = 0
        #         elif (crownintensity == 'BC1'):
        #             sidedossblack = -1
        #         elif (crownintensity == 'BC2'):
        #             sidedossblack = -3
        #         elif (crownintensity == 'BC1'):
        #             sidedossblack = -4
        #     else:
        #         if (crownintensity == 'BC1+'):
        #             sidedossblack = 0
        #         elif (crownintensity == 'BC1'):
        #             sideossblack = 0
        #         elif (crownintensity == 'BC2'):
        #             sidedossblack = -2
        #         elif (crownintensity == 'BC1'):
        #             sidedossblack = -3
        # elif (clarity == 'SI1' or clarity == 'SI2'):
        #     if (color == 'D' or color == 'E' or color == 'F'):
        #         if (crownintensity == 'BC1+'):
        #             sidedossblack = 0
        #         elif (crownintensity == 'BC1'):
        #             sidedossblack = 0
        #         elif (crownintensity == 'BC2'):
        #             sidedossblack = -1
        #         elif (crownintensity == 'BC1'):
        #             sidedossblack = -3
        #     else:
        #         if (crownintensity == 'BC1+'):
        #             sidedossblack = 0
        #         elif (crownintensity == 'BC1'):
        #             sidedossblack = 0
        #         elif (crownintensity == 'BC2'):
        #             sidedossblack = -1
        #         elif (crownintensity == 'BC1'):
        #             sidedossblack = -3
        # if (dossblack <= sidedossblack):
        #     result = result + dossblack
        #     blackd = dossblack
        # else:
        #     result = result + sidedossblack
        #     sideblackd = sidedossblack

    # df6 = pd.read_csv('black.csv') TBD
    # for i in range(len(df6)):
    #     # table
    #     if (df6['Location'][i] == 'Table'):
    #         if (df6['Shape'][i] == shape and shape == 'RO'):
    #             if ((sizeprec >= df6['sizemin'][i]) and (cut == df6['cut'][i]) and (sizeprec <= df6['sizemax'][i]) and (
    #                     tableintensity == df6['Intensity'][i])):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #
    #                     if xx == 1:
    #                         blackd = df6['1'][i]
    #                         result = result + df6['1'][i]
    #                     if xx == 2:
    #                         blackd = df6['2'][i]
    #                         result = result + df6['2'][i]
    #                     if xx == 3:
    #                         blackd = df6['3'][i]
    #                         result = result + df6['3'][i]
    #                     if xx == 4:
    #                         blackd = df6['4'][i]
    #                         result = result + df6['4'][i]
    #                     if xx == 5:
    #                         blackd = df6['5'][i]
    #                         result = result + df6['5'][i]
    #                     if xx == 6:
    #                         blackd = df6['6'][i]
    #                         result = result + df6['6'][i]
    #                     if xx == 7:
    #                         blackd = df6['7'][i]
    #                         result = result + df6['7'][i]
    #                     if xx == 8:
    #                         blackd = df6['8'][i]
    #                         result = result + df6['8'][i]
    #                     if xx == 9:
    #                         blackd = df6['9'][i]
    #                         result = result + df6['9'][i]
    #                     break
    #                 else:
    #                     if xx == 1:
    #                         result = result + df6['1'][i] / 2
    #                         blackd = df6['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df6['2'][i] / 2
    #                         blackd = df6['2'][i] / 2
    #                     if xx == 3:
    #                         blackd = df6['3'][i] / 2
    #                         result = result + df6['3'][i] / 2
    #                     if xx == 4:
    #                         blackd = df6['4'][i] / 2
    #                         result = result + df6['4'][i] / 2
    #                     if xx == 5:
    #                         blackd = df6['5'][i] / 2
    #                         result = result + df6['5'][i] / 2
    #                     if xx == 6:
    #                         blackd = df6['6'][i] / 2
    #                         result = result + df6['6'][i] / 2
    #                     if xx == 7:
    #                         blackd = df6['7'][i] / 2
    #                         result = result + df6['7'][i] / 2
    #                     if xx == 8:
    #                         blackd = df6['8'][i] / 2
    #                         result = result + df6['8'][i] / 2
    #                     if xx == 9:
    #                         blackd = df6['9'][i] / 2
    #                         result = result + df6['9'][i] / 2
    #                     break
    #         if (df6['Shape'][i] == 'Fancy' and shape != 'RO'):
    #             if (sizeprec >= df6['sizemin'][i] and sizeprec <= df6['sizemax'][i] and df6['symmetry'][
    #                 i] == symmetry and df6['polish'][i] == polish and df6['Intensity'][i] == tableintensity):
    #                 if xx == 1:
    #                     blackd = df6['1'][i]
    #                     result = result + df6['1'][i]
    #                 if xx == 2:
    #                     blackd = df6['2'][i]
    #                     result = result + df6['2'][i]
    #                 if xx == 3:
    #                     blackd = df6['3'][i]
    #                     result = result + df6['3'][i]
    #                 if xx == 4:
    #                     blackd = df6['4'][i]
    #                     result = result + df6['4'][i]
    #                 if xx == 5:
    #                     blackd = df6['5'][i]
    #                     result = result + df6['5'][i]
    #                 if xx == 6:
    #                     blackd = df6['6'][i]
    #                     result = result + df6['6'][i]
    #                 if xx == 7:
    #                     blackd = df6['7'][i]
    #                     result = result + df6['7'][i]
    #                 if xx == 8:
    #                     blackd = df6['8'][i]
    #                     result = result + df6['8'][i]
    #                 if xx == 9:
    #                     blackd = df6['9'][i]
    #                     result = result + df6['9'][i]
    #                 break
    #     # table
    # for i in range(len(df6)):
    #     if (df6['Location'][i] == 'Crown'):
    #         if (df6['Shape'][i] == shape and shape == 'RO'):
    #             if (sizeprec >= df6['sizemin'][i] and sizeprec <= df6['sizemax'][i] and cut == df6['cut'][i] and
    #                     df6['Intensity'][i] == crownintensity):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #
    #                     if xx == 1:
    #                         result = result + df6['1'][i]
    #                         sideblackd = df6['1'][i]
    #                     if xx == 2:
    #                         result = result + df6['2'][i]
    #                         sideblackd = df6['2'][i]
    #                     if xx == 3:
    #                         result = result + df6['3'][i]
    #                         sideblackd = df6['3'][i]
    #                     if xx == 4:
    #                         sideblackd = df6['4'][i]
    #                         result = result + df6['4'][i]
    #                     if xx == 5:
    #                         sideblackd = df6['5'][i]
    #                         result = result + df6['5'][i]
    #                     if xx == 6:
    #                         sideblackd = df6['6'][i]
    #                         result = result + df6['6'][i]
    #                     if xx == 7:
    #                         sideblackd = df6['7'][i]
    #                         result = result + df6['7'][i]
    #                     if xx == 8:
    #                         sideblackd = df6['8'][i]
    #                         result = result + df6['8'][i]
    #                     if xx == 9:
    #                         sideblackd = df6['9'][i]
    #                         result = result + df6['9'][i]
    #                     break
    #                 else:
    #                     if xx == 1:
    #                         sideblackd = df6['1'][i] / 2
    #                         result = result + df6['1'][i] / 2
    #                     if xx == 2:
    #                         sideblackd = df6['2'][i] / 2
    #                         result = result + df6['2'][i] / 2
    #                     if xx == 3:
    #                         sideblackd = df6['3'][i] / 2
    #                         result = result + df6['3'][i] / 2
    #                     if xx == 4:
    #                         sideblackd = df6['4'][i] / 2
    #                         result = result + df6['4'][i] / 2
    #                     if xx == 5:
    #                         sideblackd = df6['5'][i] / 2
    #                         result = result + df6['5'][i] / 2
    #                     if xx == 6:
    #                         sideblackd = df6['6'][i] / 2
    #                         result = result + df6['6'][i] / 2
    #                     if xx == 7:
    #                         sideblackd = df6['7'][i] / 2
    #                         result = result + df6['7'][i] / 2
    #                     if xx == 8:
    #                         sideblackd = df6['8'][i] / 2
    #                         result = result + df6['8'][i] / 2
    #                     if xx == 9:
    #                         sideblackd = df6['9'][i] / 2
    #                         result = result + df6['9'][i] / 2
    #                     break
    #         if (df6['Shape'][i] == 'Fancy' and shape != 'RO'):
    #             if (sizeprec >= df6['sizemin'][i] and sizeprec <= df6['sizemax'][i] and df6['symmetry'][
    #                 i] == symmetry and df6['polish'][i] == polish and df6['Intensity'][i] == crownintensity):
    #                 if xx == 1:
    #                     sideblackd = df6['1'][i]
    #                     result = result + df6['1'][i]
    #                 if xx == 2:
    #                     sideblackd = df6['2'][i]
    #                     result = result + df6['2'][i]
    #                 if xx == 3:
    #                     sideblackd = df6['3'][i]
    #                     result = result + df6['3'][i]
    #                 if xx == 4:
    #                     sideblackd = df6['4'][i]
    #                     result = result + df6['4'][i]
    #                 if xx == 5:
    #                     sideblackd = df6['5'][i]
    #                     result = result + df6['5'][i]
    #                 if xx == 6:
    #                     sideblackd = df6['6'][i]
    #                     result = result + df6['6'][i]
    #                 if xx == 7:
    #                     sideblackd = df6['7'][i]
    #                     result = result + df6['7'][i]
    #                 if xx == 8:
    #                     sideblackd = df6['8'][i]
    #                     result = result + df6['8'][i]
    #                 if xx == 9:
    #                     sideblackd = df6['9'][i]
    #                     result = result + df6['9'][i]
    #                 break

    # for i in range(len(df6)):
    #     if (df6['Location'][i] == 'Girdle'):
    #         if (df6['Shape'][i] == shape and shape == 'RO'):
    #             if (sizeprec >= df6['sizemin'][i] and sizeprec <= df6['sizemax'][i] and cut == df6['cut'][i] and
    #                     df6['Intensity'][i] == girdleintensity):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':

    #                     if xx == 1:
    #                         result = result + df6['1'][i]
    #                     if xx == 2:
    #                         result = result + df6['2'][i]
    #                     if xx == 3:
    #                         result = result + df6['3'][i]
    #                     if xx == 4:
    #                         result = result + df6['4'][i]
    #                     if xx == 5:
    #                         result = result + df6['5'][i]
    #                     if xx == 6:
    #                         result = result + df6['6'][i]
    #                     if xx == 7:
    #                         result = result + df6['7'][i]
    #                     if xx == 8:
    #                         result = result + df6['8'][i]
    #                     if xx == 9:
    #                         result = result + df6['9'][i]
    #                     break
    #                 else:
    #                     if xx == 1:
    #                         result = result + df6['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df6['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df6['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df6['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df6['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df6['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df6['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df6['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df6['9'][i] / 2
    #                     break
    #         if (df6['Shape'][i] == 'Fancy' and shape != 'RO'):
    #             if (sizeprec >= df6['sizemin'][i] and sizeprec <= df6['sizemax'][i] and df6['symmetry'][
    #                 i] == symmetry and df6['polish'][i] == polish and df6['Intensity'][i] == girdleintensity):
    #                 if xx == 1:
    #                     result = result + df6['1'][i]
    #                 if xx == 2:
    #                     result = result + df6['2'][i]
    #                 if xx == 3:
    #                     result = result + df6['3'][i]
    #                 if xx == 4:
    #                     result = result + df6['4'][i]
    #                 if xx == 5:
    #                     result = result + df6['5'][i]
    #                 if xx == 6:
    #                     result = result + df6['6'][i]
    #                 if xx == 7:
    #                     result = result + df6['7'][i]
    #                 if xx == 8:
    #                     result = result + df6['8'][i]
    #                 if xx == 9:
    #                     result = result + df6['9'][i]
    #                 break
    # for i in range(len(df6)):
    #     if (df6['Location'][i] == 'Pavilion'):
    #         if (df6['Shape'][i] == shape and shape == 'RO'):
    #             if (sizeprec >= df6['sizemin'][i] and sizeprec <= df6['sizemax'][i] and cut == df6['cut'][i] and
    #                     df6['Intensity'][i] == pavilionintensity):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':

    #                     if xx == 1:
    #                         result = result + df6['1'][i]
    #                     if xx == 2:
    #                         result = result + df6['2'][i]
    #                     if xx == 3:
    #                         result = result + df6['3'][i]
    #                     if xx == 4:
    #                         result = result + df6['4'][i]
    #                     if xx == 5:
    #                         result = result + df6['5'][i]
    #                     if xx == 6:
    #                         result = result + df6['6'][i]
    #                     if xx == 7:
    #                         result = result + df6['7'][i]
    #                     if xx == 8:
    #                         result = result + df6['8'][i]
    #                     if xx == 9:
    #                         result = result + df6['9'][i]
    #                     break
    #                 else:
    #                     if xx == 1:
    #                         result = result + df6['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df6['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df6['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df6['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df6['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df6['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df6['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df6['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df6['9'][i] / 2
    #                     break
    #         if (df6['Shape'][i] == 'Fancy' and shape != 'RO'):
    #             if (sizeprec >= df6['sizemin'][i] and sizeprec <= df6['sizemax'][i] and df6['symmetry'][
    #                 i] == symmetry and df6['polish'][i] == polish and df6['Intensity'][i] == pavilionintensity):
    #                 if xx == 1:
    #                     result = result + df6['1'][i]
    #                 if xx == 2:
    #                     result = result + df6['2'][i]
    #                 if xx == 3:
    #                     result = result + df6['3'][i]
    #                 if xx == 4:
    #                     result = result + df6['4'][i]
    #                 if xx == 5:
    #                     result = result + df6['5'][i]
    #                 if xx == 6:
    #                     result = result + df6['6'][i]
    #                 if xx == 7:
    #                     result = result + df6['7'][i]
    #                 if xx == 8:
    #                     result = result + df6['8'][i]
    #                 if xx == 9:
    #                     result = result + df6['9'][i]
    #                 break

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
                        if (sizeprec >= df7['From'][i] and sizeprec <= df7['To'][i]):
                            if (sizeprec >= 1.20 and sizeprec <= 2.99 and (
                                    (fluo == 'Strong' or fluo == 'Very Strong'))):
                                result = result + df7['IF VVS F'][i] / 2
                                sizepremd = df7['IF VVS F'][i] / 2
                            else:
                                result = result + df7['IF VVS F'][i]
                                sizepremd = df7['IF VVS F'][i]

                else:
                    df7 = pd.read_csv('roexsm.csv')
                    for i in range(len(df7)):
                        if sizeprec >= df7['From'][i] and sizeprec <= df7['To'][i]:
                            if xx == 1:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and (
                                        (fluo == 'Strong' or fluo == 'Very Strong'))):
                                    result = result + df7['1'][i] / 2
                                    sizepremd = df7['1'][i] / 2
                                else:
                                    result = result + df7['1'][i]
                                    sizepremd = df7['1'][i]
                            elif xx == 2:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and (
                                        (fluo == 'Strong' or fluo == 'Very Strong'))):
                                    result = result + df7['2'][i] / 2
                                    sizepremd = df7['2'][i] / 2
                                else:
                                    result = result + df7['2'][i]
                                    sizepremd = df7['2'][i]
                            elif xx == 3:
                                if (
                                        1.20 <= sizeprec <= 2.99 and (
                                        (fluo == 'Strong' or fluo == 'Very Strong'))):
                                    result = result + df7['3'][i] / 2
                                    sizepremd = df7['3'][i] / 2
                                else:
                                    result = result + df7['3'][i]
                                    sizepremd = df7['3'][i]
                            elif xx == 4:
                                if (
                                        1.20 <= sizeprec <= 2.99 and (
                                        (fluo == 'Strong' or fluo == 'Very Strong'))):
                                    result = result + df7['4'][i] / 2
                                    sizepremd = df7['4'][i] / 2
                                else:
                                    result = result + df7['4'][i]
                                    sizepremd = df7['4'][i]
                            elif xx == 5:
                                if (
                                        1.20 <= sizeprec <= 2.99 and (
                                        (fluo == 'Strong' or fluo == 'Very Strong'))):
                                    result = result + df7['5'][i] / 2
                                    sizepremd = df7['5'][i] / 2
                                else:
                                    result = result + df7['5'][i]
                                    sizepremd = df7['5'][i]
                            elif xx == 6:
                                if (
                                        1.20 <= sizeprec <= 2.99 and (
                                        (fluo == 'Strong' or fluo == 'Very Strong'))):
                                    result = result + df7['6'][i] / 2
                                    sizepremd = df7['6'][i] / 2
                                else:
                                    result = result + df7['6'][i]
                                    sizepremd = df7['6'][i]
                            elif xx == 7:
                                if (
                                        1.20 <= sizeprec <= 2.99 and (
                                        (fluo == 'Strong' or fluo == 'Very Strong'))):
                                    result = result + df7['7'][i] / 2
                                    sizepremd = df7['7'][i] / 2
                                else:
                                    result = result + df7['7'][i]
                                    sizepremd = df7['7'][i]
                            elif xx == 8:
                                if (
                                        1.20 <= sizeprec <= 2.99 and (
                                        fluo == 'Strong' or fluo == 'Very Strong')):
                                    result = result + df7['8'][i] / 2
                                    sizepremd = df7['8'][i] / 2
                                else:
                                    result = result + df7['8'][i]
                                    sizepremd = df7['8'][i]
                            elif xx == 9:
                                if (
                                        1.20 <= sizeprec <= 2.99 and (
                                        fluo == 'Strong' or fluo == 'Very Strong')):
                                    result = result + df7['9'][i] / 2
                                    sizepremd = df7['9'][i] / 2
                                else:
                                    result = result + df7['9'][i]
                                    sizepremd = df7['9'][i]
                            break
            else:
                if color == 'F' and (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2'):
                    df7 = pd.read_csv('rovgsmF.csv')
                    for i in range(len(df7)):
                        if sizeprec >= df7['From'][i] and sizeprec <= df7['To'][i]:
                            if sizeprec >= 1.20 and sizeprec <= 2.99 and (fluo == 'Strong' or fluo == 'Very Strong'):
                                result = result + df7['IF VVS F'][i] / 2
                                sizepremd = df7['IF VVS F'][i] / 2
                            else:
                                sizepremd = df7['IF VVS F'][i]
                                result = result + df7['IF VVS F'][i]

                else:
                    df7 = pd.read_csv('rovgsm.csv')
                    for i in range(len(df7)):

                        if df7['From'][i] <= sizeprec <= df7['To'][i]:
                            if xx == 1:
                                if (
                                        1.20 <= sizeprec <= 2.99 and (
                                        fluo == 'Strong' or fluo == 'Very Strong')):
                                    result = result + df7['1'][i] / 2
                                    sizepremd = df7['1'][i] / 2
                                else:
                                    result = result + df7['1'][i]
                                    sizepremd = df7['1'][i]
                            elif xx == 2:
                                if (
                                        1.20 <= sizeprec <= 2.99 and (
                                        fluo == 'Strong' or fluo == 'Very Strong')):
                                    result = result + df7['2'][i] / 2
                                    sizepremd = df7['2'][i] / 2
                                else:
                                    result = result + df7['2'][i]
                                    sizepremd = df7['2'][i]
                            elif xx == 3:
                                if (
                                        1.20 <= sizeprec <= 2.99 and (
                                        fluo == 'Strong' or fluo == 'Very Strong')):
                                    result = result + df7['3'][i] / 2
                                    sizepremd = df7['3'][i] / 2
                                else:
                                    result = result + df7['3'][i]
                                    sizepremd = df7['3'][i]
                            elif xx == 4:
                                if (
                                        1.20 <= sizeprec <= 2.99 and (
                                        fluo == 'Strong' or fluo == 'Very Strong')):
                                    result = result + df7['4'][i] / 2
                                    sizepremd = df7['4'][i] / 2
                                else:
                                    result = result + df7['4'][i]
                                    sizepremd = df7['4'][i]
                            elif xx == 5:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and (
                                        fluo == 'Strong' or fluo == 'Very Strong')):
                                    result = result + df7['5'][i] / 2
                                    sizepremd = df7['5'][i] / 2
                                else:
                                    result = result + df7['5'][i]
                                    sizepremd = df7['5'][i]
                            elif xx == 6:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and (
                                        fluo == 'Strong' or fluo == 'Very Strong')):
                                    result = result + df7['6'][i] / 2
                                    sizepremd = df7['6'][i] / 2
                                else:
                                    result = result + df7['6'][i]
                                    sizepremd = df7['6'][i]
                            elif xx == 7:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and (
                                        fluo == 'Strong' or fluo == 'Very Strong')):
                                    result = result + df7['7'][i] / 2
                                    sizepremd = df7['7'][i] / 2
                                else:
                                    result = result + df7['7'][i]
                                    sizepremd = df7['7'][i]
                            elif xx == 8:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and (
                                        fluo == 'Strong' or fluo == 'Very Strong')):
                                    result = result + df7['8'][i] / 2
                                    sizepremd = df7['8'][i] / 2
                                else:
                                    result = result + df7['8'][i]
                                    sizepremd = df7['8'][i]
                            elif xx == 9:
                                if (
                                        sizeprec >= 1.20 and sizeprec <= 2.99 and (
                                        fluo == 'Strong' or fluo == 'Very Strong')):
                                    result = result + df7['9'][i] / 2
                                    sizepremd = df7['9'][i] / 2
                                else:
                                    result = result + df7['9'][i]
                                    sizepremd = df7['9'][i]
                            break
        elif sizeprec >= 3.00 and sizeprec <= 6.99:
            if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
                    symmetry == 'EX' or symmetry == 'VG'):
                if (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2') and color == 'F':
                    roexbgf_size_prem = pd.read_csv('roexbgF.csv')
                    for i in range(len(roexbgf_size_prem)):
                        if roexbgf_size_prem['From'][i] <= sizeprec <= roexbgf_size_prem['To'][i]:
                            sizepremd = roexbgf_size_prem['IF VVS F'][i]
                            result += sizepremd
                            break
                else:
                    df7 = pd.read_csv('roexbg.csv')
                    for i in range(len(df7)):
                        if df7['From'][i] <= sizeprec <= df7['To'][i]:
                            sizepremd = df7[str(xx)][i]
                            result += sizepremd
                            break
            # if (sizeprec >= 3.50 and sizeprec <= 3.749): TBD
            #     if (cut == 'EX' and polish == 'EX' and symmetry == 'EX'):
            #         if (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2') and color == 'F':
            #             result = result + 3.0
            #             sizepremd = 3
            #         else:
            #             result = result + 3.0
            #             sizepremd = 3
            #     else:
            #         if (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2') and color == 'F':
            #             result = result + 1.0
            #             sizepremd = 1
            #         else:
            #             sizepremd = 1
            #             result = result + 1.0
            # elif (sizeprec >= 3.75 and sizeprec <= 3.999):
            #     if (cut == 'EX' and polish == 'EX' and symmetry == 'EX'):
            #         result = result + 4.0
            #         sizepremd = 4
            #     else:
            #         sizepremd = 2
            #         result = result + 2.0
            # elif (sizeprec >= 4.50 and sizeprec <= 4.99):
            #     if (cut == 'EX' and polish == 'EX' and symmetry == 'EX'):
            #         result = result + 3.0
            #         sizepremd = 3
            #     else:
            #         sizepremd = 1
            #         result = result + 1.0
            # elif (sizeprec >= 6.50 and sizeprec <= 6.99):
            #     if (cut == 'EX' and polish == 'EX' and symmetry == 'EX'):
            #         result = result + 3.0
            #         sizepremd = 3
            #     else:
            #         sizepremd = 2
            #         result = result + 2.0
            # else:
            #     if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
            #             symmetry == 'EX' or symmetry == 'VG'):
            #         if (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2') and color == 'F':
            #             if (sizeprec >= 3.00 and sizeprec <= 3.00):
            #                 result = result - 2.0
            #                 sizepremd = -2
            #             elif (sizeprec >= 4.00 and sizeprec <= 4.00):
            #                 result = result - 2.0
            #                 sizepremd = -2
            #             elif (sizeprec >= 5.00 and sizeprec <= 5.00):
            #                 result = result - 1.0
            #                 sizepremd = -1
            #         else:
            #             df7 = pd.read_csv('roexbg.csv')
            #             for i in range(len(df7)):
            #                 if sizeprec >= df7['From'][i] and sizeprec <= df7['To'][i]:
            #                     if xx == 1:
            #                         sizepremd = df7['1'][i]
            #                         result = result + df7['1'][i]
            #                     if xx == 2:
            #                         sizepremd = df7['2'][i]
            #                         result = result + df7['2'][i]
            #                     if xx == 3:
            #                         sizepremd = df7['3'][i]
            #                         result = result + df7['3'][i]
            #                     if xx == 4:
            #                         sizepremd = df7['4'][i]
            #                         result = result + df7['4'][i]
            #                     if xx == 5:
            #                         sizepremd = df7['5'][i]
            #                         result = result + df7['5'][i]
            #                     if xx == 6:
            #                         sizepremd = df7['6'][i]
            #                         result = result + df7['6'][i]
            #                     if xx == 7:
            #                         sizepremd = df7['7'][i]
            #                         result = result + df7['7'][i]
            #                     if xx == 8:
            #                         sizepremd = df7['8'][i]
            #                         result = result + df7['8'][i]
            #                     if xx == 9:
            #                         sizepremd = df7['9'][i]
            #                         result = result + df7['9'][i]
            #                     break
        else:
            size_prem_doss = pd.read_csv('roexdossiers.csv')
            if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
                    symmetry == 'EX' or symmetry == 'VG') and (
                    fluo == 'Medium' or fluo == 'None' or fluo == 'Faint') and (
                    clarity == 'I1' or clarity == 'IF' or clarity == 'SI1' or clarity == 'SI2'):
                for i in range(len(size_prem_doss)):
                    size_range = str(size_prem_doss['Size Range'][i])
                    size_low = float(size_range.split('-')[0])
                    size_high = float(size_range.split('-')[1])
                    if size_low <= sizeprec <= size_high:
                        sizepremd = float(size_prem_doss['FL-SI2'][i])
                        result += sizepremd
                        break
    else:
        fancy_size_prem = pd.read_csv('fancy.csv')
        for i in range(len(fancy_size_prem)):
            size_low = fancy_size_prem['From'][i]
            size_high = fancy_size_prem['To'][i]
            if size_low <= sizeprec <= size_high:
                sizepremd = float(fancy_size_prem[str(xx)][i])
                result += sizepremd
                break

        # elif sizeprec >= 0.59 and sizeprec <= 0.599: TBD
        #     if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
        #             symmetry == 'EX' or symmetry == 'VG') and (fluo == 'Medium' or fluo == 'None' or fluo == 'Faint'):
        #         result = result + 1
        #         sizepremd = 1
        # elif sizeprec >= 0.78 and sizeprec <= 0.789:
        #     if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
        #             symmetry == 'EX' or symmetry == 'VG'):
        #         sizepremd = 1
        #         result = result + 1
        # elif sizeprec >= 0.79 and sizeprec <= 0.799:
        #     if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
        #             symmetry == 'EX' or symmetry == 'VG'):
        #         result = result + 2
        #         sizepremd = 2
        # elif sizeprec >= 0.87 and sizeprec <= 0.879:
        #     if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
        #             symmetry == 'EX' or symmetry == 'VG'):
        #         result = result + 1
        #         sizepremd = 1
        # elif sizeprec >= 0.88 and sizeprec <= 0.889:
        #     if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
        #             symmetry == 'EX' or symmetry == 'VG'):
        #         result = result + 2
        #         sizepremd = 2
        # elif sizeprec >= 0.89 and sizeprec <= 0.899:
        #     if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
        #             symmetry == 'EX' or symmetry == 'VG'):
        #         result = result + 3
        #         sizepremd = 3
        # elif sizeprec >= 0.98 and sizeprec <= 0.989:
        #     if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
        #             symmetry == 'EX' or symmetry == 'VG'):
        #         result = result + 1
        #         sizepremd = 1
        # elif sizeprec >= 0.99 and sizeprec <= 0.999:
        #     if (cut == 'EX' or cut == 'VG') and (polish == 'EX' or polish == 'VG') and (
        #             symmetry == 'EX' or symmetry == 'VG'):
        #         result = result + 2
        #         sizepremd = 2
        # Finishing

    # open
    # df9=pd.read_csv('Finishing.csv') TBD
    # for i in range(len(df9)):
    #     #table
    #     if(df6['Location'][i]=='Table'):
    #         if(df6['Shape'][i]==shape and shape=='RO'):
    #             if((sizeprec>=df6['sizemin'][i]) & (cut==df6['cut'][i]) & (sizeprec<=df6['sizemax'][i]) & (tableintensity==df6['Intensity'][i])):
    #                 if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+ df6['1'][i]
    #                     if xx==2:
    #                         result=result+ df6['2'][i]
    #                     if xx==3:
    #                         result=result+ df6['3'][i]
    #                     if xx==4:
    #                         result=result+ df6['4'][i]
    #                     if xx==5:
    #                         result=result+ df6['5'][i]
    #                     if xx==6:
    #                         result=result+ df6['6'][i]
    #                     if xx==7:
    #                         result=result+ df6['7'][i]
    #                     if xx==8:
    #                         result=result+ df6['8'][i]
    #                     if xx==9:
    #                         result=result+ df6['9'][i]
    #                     break
    #                 else:
    #                     if xx==1:
    #                         result=result+ df6['1'][i]/2
    #                     if xx==2:
    #                         result=result+ df6['2'][i]/2
    #                     if xx==3:
    #                         result=result+ df6['3'][i]/2
    #                     if xx==4:
    #                         result=result+ df6['4'][i]/2
    #                     if xx==5:
    #                         result=result+ df6['5'][i]/2
    #                     if xx==6:
    #                         result=result+ df6['6'][i]/2
    #                     if xx==7:
    #                         result=result+ df6['7'][i]/2
    #                     if xx==8:
    #                         result=result+ df6['8'][i]/2
    #                     if xx==9:
    #                         result=result+ df6['9'][i]/2
    #                     break
    #         if(df6['Shape'][i]=='Fancy' and shape!='RO'):
    #             if(sizeprec>=df6['sizemin'][i] and sizeprec<=df6['sizemax'][i] and df6['symmetry'][i]==symmetry and df6['polish'][i]==polish and df6['Intensity'][i]==tableintensity):
    #                 if xx==1:
    #                     result=result+ df6['1'][i]
    #                 if xx==2:
    #                     result=result+ df6['2'][i]
    #                 if xx==3:
    #                     result=result+ df6['3'][i]
    #                 if xx==4:
    #                     result=result+ df6['4'][i]
    #                 if xx==5:
    #                     result=result+ df6['5'][i]
    #                 if xx==6:
    #                     result=result+ df6['6'][i]
    #                 if xx==7:
    #                     result=result+ df6['7'][i]
    #                 if xx==8:
    #                     result=result+ df6['8'][i]
    #                 if xx==9:
    #                     result=result+ df6['9'][i]
    #                 break
    #     #table
    # for i in range(len(df6)):
    #     if(df6['Place'][i]=='Crown'):
    #         if(df6['Shape'][i]==shape and shape=='RO'):
    #             if(sizeprec>=df6['sizemin'][i] and sizeprec<=df6['sizemax'][i] and cut==df6['cut'][i] and df6['Intensity'][i]==crownintensity):
    #                 if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+ df6['1'][i]
    #                     if xx==2:
    #                         result=result+ df6['2'][i]
    #                     if xx==3:
    #                         result=result+ df6['3'][i]
    #                     if xx==4:
    #                         result=result+ df6['4'][i]
    #                     if xx==5:
    #                         result=result+ df6['5'][i]
    #                     if xx==6:
    #                         result=result+ df6['6'][i]
    #                     if xx==7:
    #                         result=result+ df6['7'][i]
    #                     if xx==8:
    #                         result=result+ df6['8'][i]
    #                     if xx==9:
    #                         result=result+ df6['9'][i]
    #                     break
    #                 else:
    #                     if xx==1:
    #                         result=result+ df6['1'][i]/2
    #                     if xx==2:
    #                         result=result+ df6['2'][i]/2
    #                     if xx==3:
    #                         result=result+ df6['3'][i]/2
    #                     if xx==4:
    #                         result=result+ df6['4'][i]/2
    #                     if xx==5:
    #                         result=result+ df6['5'][i]/2
    #                     if xx==6:
    #                         result=result+ df6['6'][i]/2
    #                     if xx==7:
    #                         result=result+ df6['7'][i]/2
    #                     if xx==8:
    #                         result=result+ df6['8'][i]/2
    #                     if xx==9:
    #                         result=result+ df6['9'][i]/2
    #                     break
    #         if(df6['Shape'][i]=='Fancy' and shape!='RO'):
    #             if(sizeprec>=df6['sizemin'][i] and sizeprec<=df6['sizemax'][i] and df6['symmetry'][i]==symmetry and df6['polish'][i]==polish and df6['Intensity'][i]==crownintensity):
    #                 if xx==1:
    #                     result=result+ df6['1'][i]
    #                 if xx==2:
    #                     result=result+ df6['2'][i]
    #                 if xx==3:
    #                     result=result+ df6['3'][i]
    #                 if xx==4:
    #                     result=result+ df6['4'][i]
    #                 if xx==5:
    #                     result=result+ df6['5'][i]
    #                 if xx==6:
    #                     result=result+ df6['6'][i]
    #                 if xx==7:
    #                     result=result+ df6['7'][i]
    #                 if xx==8:
    #                     result=result+ df6['8'][i]
    #                 if xx==9:
    #                     result=result+ df6['9'][i]
    #                 break
    # for i in range(len(df6)):
    #     if(df6['Location'][i]=='Girdle'):
    #         if(df6['Shape'][i]==shape and shape=='RO'):
    #             if(sizeprec>=df6['sizemin'][i] and sizeprec<=df6['sizemax'][i] and cut==df6['cut'][i] and df6['Intensity'][i]==girdleintensity):
    # if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #     if xx==1:
    #         result=result+ df6['1'][i]
    #     if xx==2:
    #         result=result+ df6['2'][i]
    #     if xx==3:
    #         result=result+ df6['3'][i]
    #     if xx==4:
    #         result=result+ df6['4'][i]
    #     if xx==5:
    #         result=result+ df6['5'][i]
    #     if xx==6:
    #         result=result+ df6['6'][i]
    #     if xx==7:
    #         result=result+ df6['7'][i]
    #     if xx==8:
    #         result=result+ df6['8'][i]
    #     if xx==9:
    #         result=result+ df6['9'][i]
    #     break
    # else:
    #     if xx==1:
    #         result=result+ df6['1'][i]/2
    #     if xx==2:
    #         result=result+ df6['2'][i]/2
    #     if xx==3:
    #         result=result+ df6['3'][i]/2
    #     if xx==4:
    #         result=result+ df6['4'][i]/2
    #     if xx==5:
    #         result=result+ df6['5'][i]/2
    #     if xx==6:
    #         result=result+ df6['6'][i]/2
    #     if xx==7:
    #         result=result+ df6['7'][i]/2
    #     if xx==8:
    #         result=result+ df6['8'][i]/2
    #     if xx==9:
    #         result=result+ df6['9'][i]/2
    #     break
    # if(shape=='RO'):
    #     df9=pd.read_csv("Finishing.csv")
    #     for i in range(len(df9)):
    #         #HO
    #         if(halfopen==df9['Place'][i] and df9['value'][i]=='HO' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+ df9['1'][i]
    #                     if xx==2:
    #                         result=result+ df9['2'][i]
    #                     if xx==3:
    #                         result=result+ df9['3'][i]
    #                     if xx==4:
    #                         result=result+ df9['4'][i]
    #                     if xx==5:
    #                         result=result+ df9['5'][i]
    #                     if xx==6:
    #                         result=result+ df9['6'][i]
    #                     if xx==7:
    #                         result=result+ df9['7'][i]
    #                     if xx==8:
    #                         result=result+ df9['8'][i]
    #                     if xx==9:
    #                         result=result+ df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+ df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+ df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+ df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+ df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+ df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+ df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+ df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+ df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+ df9['9'][i]/2
    #         if(smallopen==df9['Place'][i] and df9['value'][i]=='Small' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+ df9['1'][i]
    #                     if xx==2:
    #                         result=result+ df9['2'][i]
    #                     if xx==3:
    #                         result=result+ df9['3'][i]
    #                     if xx==4:
    #                         result=result+ df9['4'][i]
    #                     if xx==5:
    #                         result=result+ df9['5'][i]
    #                     if xx==6:
    #                         result=result+ df9['6'][i]
    #                     if xx==7:
    #                         result=result+ df9['7'][i]
    #                     if xx==8:
    #                         result=result+ df9['8'][i]
    #                     if xx==9:
    #                         result=result+ df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+ df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+ df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+ df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+ df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+ df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+ df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+ df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+ df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+ df9['9'][i]/2
    #         if(bigopen==df9['Place'][i] and df9['value'][i]=='Big' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+ df9['1'][i]
    #                     if xx==2:
    #                         result=result+ df9['2'][i]
    #                     if xx==3:
    #                         result=result+ df9['3'][i]
    #                     if xx==4:
    #                         result=result+ df9['4'][i]
    #                     if xx==5:
    #                         result=result+ df9['5'][i]
    #                     if xx==6:
    #                         result=result+ df9['6'][i]
    #                     if xx==7:
    #                         result=result+ df9['7'][i]
    #                     if xx==8:
    #                         result=result+ df9['8'][i]
    #                     if xx==9:
    #                         result=result+ df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+ df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+ df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+ df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+ df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+ df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+ df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+ df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+ df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+ df9['9'][i]/2
    #         if(mediumopen==df9['Place'][i] and df9['value'][i]=='Medium' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+ df9['1'][i]
    #                     if xx==2:
    #                         result=result+ df9['2'][i]
    #                     if xx==3:
    #                         result=result+ df9['3'][i]
    #                     if xx==4:
    #                         result=result+ df9['4'][i]
    #                     if xx==5:
    #                         result=result+ df9['5'][i]
    #                     if xx==6:
    #                         result=result+ df9['6'][i]
    #                     if xx==7:
    #                         result=result+ df9['7'][i]
    #                     if xx==8:
    #                         result=result+ df9['8'][i]
    #                     if xx==9:
    #                         result=result+ df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+ df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+ df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+ df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+ df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+ df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+ df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+ df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+ df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+ df9['9'][i]/2
    #     for i in range(len(df9)):
    #         #HO
    #         if(identednatural==df9['Place'][i] and df9['value'][i]=='Indented Natural' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+ df9['1'][i]
    #                     if xx==2:
    #                         result=result+ df9['2'][i]
    #                     if xx==3:
    #                         result=result+ df9['3'][i]
    #                     if xx==4:
    #                         result=result+ df9['4'][i]
    #                     if xx==5:
    #                         result=result+ df9['5'][i]
    #                     if xx==6:
    #                         result=result+ df9['6'][i]
    #                     if xx==7:
    #                         result=result+ df9['7'][i]
    #                     if xx==8:
    #                         result=result+ df9['8'][i]
    #                     if xx==9:
    #                         result=result+ df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+ df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+ df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+ df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+ df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+ df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+ df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+ df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+ df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+ df9['9'][i]/2
    #         if(naturalnatural==df9['Place'][i] and df9['value'][i]=='Natural' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+ df9['1'][i]
    #                     if xx==2:
    #                         result=result+ df9['2'][i]
    #                     if xx==3:
    #                         result=result+ df9['3'][i]
    #                     if xx==4:
    #                         result=result+ df9['4'][i]
    #                     if xx==5:
    #                         result=result+ df9['5'][i]
    #                     if xx==6:
    #                         result=result+ df9['6'][i]
    #                     if xx==7:
    #                         result=result+ df9['7'][i]
    #                     if xx==8:
    #                         result=result+ df9['8'][i]
    #                     if xx==9:
    #                         result=result+ df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+ df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+ df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+ df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+ df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+ df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+ df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+ df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+ df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+ df9['9'][i]/2
    #         if(bignatural==df9['Place'][i] and df9['value'][i]=='Big Natural' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+ df9['1'][i]
    #                     if xx==2:
    #                         result=result+ df9['2'][i]
    #                     if xx==3:
    #                         result=result+ df9['3'][i]
    #                     if xx==4:
    #                         result=result+ df9['4'][i]
    #                     if xx==5:
    #                         result=result+ df9['5'][i]
    #                     if xx==6:
    #                         result=result+ df9['6'][i]
    #                     if xx==7:
    #                         result=result+ df9['7'][i]
    #                     if xx==8:
    #                         result=result+ df9['8'][i]
    #                     if xx==9:
    #                         result=result+ df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+ df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+ df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+ df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+ df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+ df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+ df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+ df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+ df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+ df9['9'][i]/2

    #     for i in range(len(df9)):
    #         #HO
    #         if(extrafacet==df9['Place'][i] and df9['value'][i]=='Extra Facet') and cut==df9['Cut'][i]:
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+ df9['1'][i]
    #                     if xx==2:
    #                         result=result+ df9['2'][i]
    #                     if xx==3:
    #                         result=result+ df9['3'][i]
    #                     if xx==4:
    #                         result=result+ df9['4'][i]
    #                     if xx==5:
    #                         result=result+ df9['5'][i]
    #                     if xx==6:
    #                         result=result+ df9['6'][i]
    #                     if xx==7:
    #                         result=result+ df9['7'][i]
    #                     if xx==8:
    #                         result=result+ df9['8'][i]
    #                     if xx==9:
    #                         result=result+ df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+ df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+ df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+ df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+ df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+ df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+ df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+ df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+ df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+ df9['9'][i]/2
    #         if(cavity==df9['Place'][i] and df9['value'][i]=='Cavity' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+ df9['1'][i]
    #                     if xx==2:
    #                         result=result+ df9['2'][i]
    #                     if xx==3:
    #                         result=result+ df9['3'][i]
    #                     if xx==4:
    #                         result=result+ df9['4'][i]
    #                     if xx==5:
    #                         result=result+ df9['5'][i]
    #                     if xx==6:
    #                         result=result+ df9['6'][i]
    #                     if xx==7:
    #                         result=result+ df9['7'][i]
    #                     if xx==8:
    #                         result=result+ df9['8'][i]
    #                     if xx==9:
    #                         result=result+ df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+ df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+ df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+ df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+ df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+ df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+ df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+ df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+ df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+ df9['9'][i]/2
    #         if(chip==df9['Place'][i] and df9['value'][i]=='Chip' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                     if xx==1:
    #                         result=result+ df9['1'][i]
    #                     if xx==2:
    #                         result=result+ df9['2'][i]
    #                     if xx==3:
    #                         result=result+ df9['3'][i]
    #                     if xx==4:
    #                         result=result+ df9['4'][i]
    #                     if xx==5:
    #                         result=result+ df9['5'][i]
    #                     if xx==6:
    #                         result=result+ df9['6'][i]
    #                     if xx==7:
    #                         result=result+ df9['7'][i]
    #                     if xx==8:
    #                         result=result+ df9['8'][i]
    #                     if xx==9:
    #                         result=result+ df9['9'][i]
    #             else:
    #                     if xx==1:
    #                         result=result+ df9['1'][i]/2
    #                     if xx==2:
    #                         result=result+ df9['2'][i]/2
    #                     if xx==3:
    #                         result=result+ df9['3'][i]/2
    #                     if xx==4:
    #                         result=result+ df9['4'][i]/2
    #                     if xx==5:
    #                         result=result+ df9['5'][i]/2
    #                     if xx==6:
    #                         result=result+ df9['6'][i]/2
    #                     if xx==7:
    #                         result=result+ df9['7'][i]/2
    #                     if xx==8:
    #                         result=result+ df9['8'][i]/2
    #                     if xx==9:
    #                         result=result+ df9['9'][i]/2
    # elif(shape!='RO'):
    #     df9=pd.read_csv("FinishingFancy.csv")
    #     for i in range(len(df9)):
    #         #HO
    #         if(halfopen==df9['Place'][i] and df9['value'][i]=='HO' and cut==df9['Cut'][i] and polish==df9['Polish'][i] and symmetry==df9['Symmetry'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                 if xx==1:
    #                     result=result+ df9['1'][i]
    #                 if xx==2:
    #                     result=result+ df9['2'][i]
    #                 if xx==3:
    #                     result=result+ df9['3'][i]
    #                 if xx==4:
    #                     result=result+ df9['4'][i]
    #                 if xx==5:
    #                     result=result+ df9['5'][i]
    #                 if xx==6:
    #                     result=result+ df9['6'][i]
    #                 if xx==7:
    #                     result=result+ df9['7'][i]
    #                 if xx==8:
    #                     result=result+ df9['8'][i]
    #                 if xx==9:
    #                     result=result+ df9['9'][i]
    #             else:
    #                 if xx==1:
    #                     result=result+ df9['1'][i]/2
    #                 if xx==2:
    #                     result=result+ df9['2'][i]/2
    #                 if xx==3:
    #                     result=result+ df9['3'][i]/2
    #                 if xx==4:
    #                     result=result+ df9['4'][i]/2
    #                 if xx==5:
    #                     result=result+ df9['5'][i]/2
    #                 if xx==6:
    #                     result=result+ df9['6'][i]/2
    #                 if xx==7:
    #                     result=result+ df9['7'][i]/2
    #                 if xx==8:
    #                     result=result+ df9['8'][i]/2
    #                 if xx==9:
    #                     result=result+ df9['9'][i]/2
    #         if(smallopen==df9['Place'][i] and df9['value'][i]=='Small' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                 if xx==1:
    #                     result=result+ df9['1'][i]
    #                 if xx==2:
    #                     result=result+ df9['2'][i]
    #                 if xx==3:
    #                     result=result+ df9['3'][i]
    #                 if xx==4:
    #                     result=result+ df9['4'][i]
    #                 if xx==5:
    #                     result=result+ df9['5'][i]
    #                 if xx==6:
    #                     result=result+ df9['6'][i]
    #                 if xx==7:
    #                     result=result+ df9['7'][i]
    #                 if xx==8:
    #                     result=result+ df9['8'][i]
    #                 if xx==9:
    #                     result=result+ df9['9'][i]
    #             else:
    #                 if xx==1:
    #                     result=result+ df9['1'][i]/2
    #                 if xx==2:
    #                     result=result+ df9['2'][i]/2
    #                 if xx==3:
    #                     result=result+ df9['3'][i]/2
    #                 if xx==4:
    #                     result=result+ df9['4'][i]/2
    #                 if xx==5:
    #                     result=result+ df9['5'][i]/2
    #                 if xx==6:
    #                     result=result+ df9['6'][i]/2
    #                 if xx==7:
    #                     result=result+ df9['7'][i]/2
    #                 if xx==8:
    #                     result=result+ df9['8'][i]/2
    #                 if xx==9:
    #                     result=result+ df9['9'][i]/2
    #         if(bigopen==df9['Place'][i] and df9['value'][i]=='Big' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                 if xx==1:
    #                     result=result+ df9['1'][i]
    #                 if xx==2:
    #                     result=result+ df9['2'][i]
    #                 if xx==3:
    #                     result=result+ df9['3'][i]
    #                 if xx==4:
    #                     result=result+ df9['4'][i]
    #                 if xx==5:
    #                     result=result+ df9['5'][i]
    #                 if xx==6:
    #                     result=result+ df9['6'][i]
    #                 if xx==7:
    #                     result=result+ df9['7'][i]
    #                 if xx==8:
    #                     result=result+ df9['8'][i]
    #                 if xx==9:
    #                     result=result+ df9['9'][i]
    #             else:
    #                 if xx==1:
    #                     result=result+ df9['1'][i]/2
    #                 if xx==2:
    #                     result=result+ df9['2'][i]/2
    #                 if xx==3:
    #                     result=result+ df9['3'][i]/2
    #                 if xx==4:
    #                     result=result+ df9['4'][i]/2
    #                 if xx==5:
    #                     result=result+ df9['5'][i]/2
    #                 if xx==6:
    #                     result=result+ df9['6'][i]/2
    #                 if xx==7:
    #                     result=result+ df9['7'][i]/2
    #                 if xx==8:
    #                     result=result+ df9['8'][i]/2
    #                 if xx==9:
    #                     result=result+ df9['9'][i]/2
    #         if(mediumopen==df9['Place'][i] and df9['value'][i]=='Medium' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                 if xx==1:
    #                     result=result+ df9['1'][i]
    #                 if xx==2:
    #                     result=result+ df9['2'][i]
    #                 if xx==3:
    #                     result=result+ df9['3'][i]
    #                 if xx==4:
    #                     result=result+ df9['4'][i]
    #                 if xx==5:
    #                     result=result+ df9['5'][i]
    #                 if xx==6:
    #                     result=result+ df9['6'][i]
    #                 if xx==7:
    #                     result=result+ df9['7'][i]
    #                 if xx==8:
    #                     result=result+ df9['8'][i]
    #                 if xx==9:
    #                     result=result+ df9['9'][i]
    #             else:
    #                 if xx==1:
    #                     result=result+ df9['1'][i]/2
    #                 if xx==2:
    #                     result=result+ df9['2'][i]/2
    #                 if xx==3:
    #                     result=result+ df9['3'][i]/2
    #                 if xx==4:
    #                     result=result+ df9['4'][i]/2
    #                 if xx==5:
    #                     result=result+ df9['5'][i]/2
    #                 if xx==6:
    #                     result=result+ df9['6'][i]/2
    #                 if xx==7:
    #                     result=result+ df9['7'][i]/2
    #                 if xx==8:
    #                     result=result+ df9['8'][i]/2
    #                 if xx==9:
    #                     result=result+ df9['9'][i]/2
    #     for i in range(len(df9)):
    #         #HO
    #         if(identednatural==df9['Place'][i] and df9['value'][i]=='Indented Natural' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                 if xx==1:
    #                     result=result+ df9['1'][i]
    #                 if xx==2:
    #                     result=result+ df9['2'][i]
    #                 if xx==3:
    #                     result=result+ df9['3'][i]
    #                 if xx==4:
    #                     result=result+ df9['4'][i]
    #                 if xx==5:
    #                     result=result+ df9['5'][i]
    #                 if xx==6:
    #                     result=result+ df9['6'][i]
    #                 if xx==7:
    #                     result=result+ df9['7'][i]
    #                 if xx==8:
    #                     result=result+ df9['8'][i]
    #                 if xx==9:
    #                     result=result+ df9['9'][i]
    #             else:
    #                 if xx==1:
    #                     result=result+ df9['1'][i]/2
    #                 if xx==2:
    #                     result=result+ df9['2'][i]/2
    #                 if xx==3:
    #                     result=result+ df9['3'][i]/2
    #                 if xx==4:
    #                     result=result+ df9['4'][i]/2
    #                 if xx==5:
    #                     result=result+ df9['5'][i]/2
    #                 if xx==6:
    #                     result=result+ df9['6'][i]/2
    #                 if xx==7:
    #                     result=result+ df9['7'][i]/2
    #                 if xx==8:
    #                     result=result+ df9['8'][i]/2
    #                 if xx==9:
    #                     result=result+ df9['9'][i]/2
    #         if(naturalnatural==df9['Place'][i] and df9['value'][i]=='Natural' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                 if xx==1:
    #                     result=result+ df9['1'][i]
    #                 if xx==2:
    #                     result=result+ df9['2'][i]
    #                 if xx==3:
    #                     result=result+ df9['3'][i]
    #                 if xx==4:
    #                     result=result+ df9['4'][i]
    #                 if xx==5:
    #                     result=result+ df9['5'][i]
    #                 if xx==6:
    #                     result=result+ df9['6'][i]
    #                 if xx==7:
    #                     result=result+ df9['7'][i]
    #                 if xx==8:
    #                     result=result+ df9['8'][i]
    #                 if xx==9:
    #                     result=result+ df9['9'][i]
    #             else:
    #                 if xx==1:
    #                     result=result+ df9['1'][i]/2
    #                 if xx==2:
    #                     result=result+ df9['2'][i]/2
    #                 if xx==3:
    #                     result=result+ df9['3'][i]/2
    #                 if xx==4:
    #                     result=result+ df9['4'][i]/2
    #                 if xx==5:
    #                     result=result+ df9['5'][i]/2
    #                 if xx==6:
    #                     result=result+ df9['6'][i]/2
    #                 if xx==7:
    #                     result=result+ df9['7'][i]/2
    #                 if xx==8:
    #                     result=result+ df9['8'][i]/2
    #                 if xx==9:
    #                     result=result+ df9['9'][i]/2
    #         if(bignatural==df9['Place'][i] and df9['value'][i]=='Big Natural' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                 if xx==1:
    #                     result=result+ df9['1'][i]
    #                 if xx==2:
    #                     result=result+ df9['2'][i]
    #                 if xx==3:
    #                     result=result+ df9['3'][i]
    #                 if xx==4:
    #                     result=result+ df9['4'][i]
    #                 if xx==5:
    #                     result=result+ df9['5'][i]
    #                 if xx==6:
    #                     result=result+ df9['6'][i]
    #                 if xx==7:
    #                     result=result+ df9['7'][i]
    #                 if xx==8:
    #                     result=result+ df9['8'][i]
    #                 if xx==9:
    #                     result=result+ df9['9'][i]
    #             else:
    #                 if xx==1:
    #                     result=result+ df9['1'][i]/2
    #                 if xx==2:
    #                     result=result+ df9['2'][i]/2
    #                 if xx==3:
    #                     result=result+ df9['3'][i]/2
    #                 if xx==4:
    #                     result=result+ df9['4'][i]/2
    #                 if xx==5:
    #                     result=result+ df9['5'][i]/2
    #                 if xx==6:
    #                     result=result+ df9['6'][i]/2
    #                 if xx==7:
    #                     result=result+ df9['7'][i]/2
    #                 if xx==8:
    #                     result=result+ df9['8'][i]/2
    #                 if xx==9:
    #                     result=result+ df9['9'][i]/2

    #     for i in range(len(df9)):
    #         #HO
    #         if(extrafacet==df9['Place'][i] and df9['value'][i]=='Extra Facet') and cut==df9['Cut'][i]:
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                 if xx==1:
    #                     result=result+ df9['1'][i]
    #                 if xx==2:
    #                     result=result+ df9['2'][i]
    #                 if xx==3:
    #                     result=result+ df9['3'][i]
    #                 if xx==4:
    #                     result=result+ df9['4'][i]
    #                 if xx==5:
    #                     result=result+ df9['5'][i]
    #                 if xx==6:
    #                     result=result+ df9['6'][i]
    #                 if xx==7:
    #                     result=result+ df9['7'][i]
    #                 if xx==8:
    #                     result=result+ df9['8'][i]
    #                 if xx==9:
    #                     result=result+ df9['9'][i]
    #             else:
    #                 if xx==1:
    #                     result=result+ df9['1'][i]/2
    #                 if xx==2:
    #                     result=result+ df9['2'][i]/2
    #                 if xx==3:
    #                     result=result+ df9['3'][i]/2
    #                 if xx==4:
    #                     result=result+ df9['4'][i]/2
    #                 if xx==5:
    #                     result=result+ df9['5'][i]/2
    #                 if xx==6:
    #                     result=result+ df9['6'][i]/2
    #                 if xx==7:
    #                     result=result+ df9['7'][i]/2
    #                 if xx==8:
    #                     result=result+ df9['8'][i]/2
    #                 if xx==9:
    #                     result=result+ df9['9'][i]/2
    #         if(cavity==df9['Place'][i] and df9['value'][i]=='Cavity' and cut==df9['Cut'][i]):
    #             if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #                 if xx==1:
    #                     result=result+ df9['1'][i]
    #                 if xx==2:
    #                     result=result+ df9['2'][i]
    #                 if xx==3:
    #                     result=result+ df9['3'][i]
    #                 if xx==4:
    #                     result=result+ df9['4'][i]
    #                 if xx==5:
    #                     result=result+ df9['5'][i]
    #                 if xx==6:
    #                     result=result+ df9['6'][i]
    #                 if xx==7:
    #                     result=result+ df9['7'][i]
    #                 if xx==8:
    #                     result=result+ df9['8'][i]
    #                 if xx==9:
    #                     result=result+ df9['9'][i]
    #             else:
    #                 if xx==1:
    #                     result=result+ df9['1'][i]/2
    #                 if xx==2:
    #                     result=result+ df9['2'][i]/2
    #                 if xx==3:
    #                     result=result+ df9['3'][i]/2
    #                 if xx==4:
    #                     result=result+ df9['4'][i]/2
    #                 if xx==5:
    #                     result=result+ df9['5'][i]/2
    #                 if xx==6:
    #                     result=result+ df9['6'][i]/2
    #                 if xx==7:
    #                     result=result+ df9['7'][i]/2
    #                 if xx==8:
    #                     result=result+ df9['8'][i]/2
    #                 if xx==9:
    #                     result=result+ df9['9'][i]/2
    #         if(chip==df9['Place'][i] and df9['value'][i]=='Chip' and cut==df9['Cut'][i]):
    # if fluo!='None' and fluo!='Medium' and fluo!='Faint':

    #     if xx==1:
    #         result=result+ df9['1'][i]
    #     if xx==2:
    #         result=result+ df9['2'][i]
    #     if xx==3:
    #         result=result+ df9['3'][i]
    #     if xx==4:
    #         result=result+ df9['4'][i]
    #     if xx==5:
    #         result=result+ df9['5'][i]
    #     if xx==6:
    #         result=result+ df9['6'][i]
    #     if xx==7:
    #         result=result+ df9['7'][i]
    #     if xx==8:
    #         result=result+ df9['8'][i]
    #     if xx==9:
    #         result=result+ df9['9'][i]
    # else:
    #     if xx==1:
    #         result=result+ df9['1'][i]/2
    #     if xx==2:
    #         result=result+ df9['2'][i]/2
    #     if xx==3:
    #         result=result+ df9['3'][i]/2
    #     if xx==4:
    #         result=result+ df9['4'][i]/2
    #     if xx==5:
    #         result=result+ df9['5'][i]/2
    #     if xx==6:
    #         result=result+ df9['6'][i]/2
    #     if xx==7:
    #         result=result+ df9['7'][i]/2
    #     if xx==8:
    #         result=result+ df9['8'][i]/2
    #     if xx==9:
    #         result=result+ df9['9'][i]/2
    # open in dossiers?

    #finishing
    finishing_data = pd.read_csv('finishing.csv')
    for i in range(len(finishing_data)):
        if shape == 'RO' and sizeprec >= 1:
            if cut == finishing_data['Cut'][i] and tableopen == finishing_data['Property'][i] and finishing_data['Shape'][i] == 'RO':
                if fluo in ['None', 'Faint']:
                    opend += (finishing_data[str(xx)][i] / 2)
                    result += opend
                else:
                    opend += finishing_data[str(xx)][i]
                    result += opend
            elif cut == finishing_data['Cut'][i] and topnatural == finishing_data['Property'][i] \
                    and finishing_data['Shape'][i] == 'RO':
                if fluo in ['None', 'Faint']:
                    naturald += (finishing_data[str(xx)][i] / 2)
                    result += naturald
                else:
                    naturald += finishing_data[str(xx)][i]
                    result += naturald
            elif cut == finishing_data['Cut'][i] and identedtopnatural == finishing_data['Property'][i] and finishing_data['Shape'][i] == 'RO':
                if fluo in ['None', 'Faint']:
                    identednaturald += (finishing_data[str(xx)][i] / 2)
                    result += identednaturald
                else:
                    identednaturald += finishing_data[str(xx)][i]
                    result += identednaturald
            elif cut == finishing_data['Cut'][i] and topcavity == finishing_data['Property'][i] and finishing_data['Shape'][i] == 'RO':
                if fluo in ['None', 'Faint']:
                    cavityd += (finishing_data[str(xx)][i] / 2)
                    result += cavityd
                else:
                    cavityd += finishing_data[str(xx)][i]
                    result += cavityd
            elif cut == finishing_data['Cut'][i] and topchip == finishing_data['Property'][i] and finishing_data['Shape'][i] == 'RO':
                if fluo in ['None', 'Faint']:
                    chipd += (finishing_data[str(xx)][i] / 2)
                    result += chipd
                else:
                    chipd += finishing_data[str(xx)][i]
                    result += chipd
            elif cut == finishing_data['Cut'][i] and crownef == finishing_data['Property'][i] and finishing_data['Shape'][i] == 'RO':
                if fluo in ['None', 'Faint']:
                    efd += (finishing_data[str(xx)][i] / 2)
                    result += efd
                else:
                    efd += finishing_data[str(xx)][i]
                    result += efd
        elif shape == 'RO' and sizeprec < 1:
            if cut == finishing_data['Cut'][i] and tableopen == finishing_data['Property'][i] and \
                    finishing_data['Shape'][i] == 'Dossiers':
                if fluo in ['None', 'Faint']:
                    opend += (finishing_data[str(xx)][i] / 2)
                    result += opend
                else:
                    opend += finishing_data[str(xx)][i]
                    result += opend
            elif cut == finishing_data['Cut'][i] and topnatural == finishing_data['Property'][i] \
                    and finishing_data['Shape'][i] == 'Dossiers':
                if fluo in ['None', 'Faint']:
                    naturald += (finishing_data[str(xx)][i] / 2)
                    result += naturald
                else:
                    naturald += finishing_data[str(xx)][i]
                    result += naturald
            elif cut == finishing_data['Cut'][i] and identedtopnatural == finishing_data['Property'][i] and \
                    finishing_data['Shape'][i] == 'Dossiers':
                if fluo in ['None', 'Faint']:
                    identednaturald += (finishing_data[str(xx)][i] / 2)
                    result += identednaturald
                else:
                    identednaturald += finishing_data[str(xx)][i]
                    result += identednaturald
            elif cut == finishing_data['Cut'][i] and topcavity == finishing_data['Property'][i] and \
                    finishing_data['Shape'][i] == 'Dossiers':
                if fluo in ['None', 'Faint']:
                    cavityd += (finishing_data[str(xx)][i] / 2)
                    result += cavityd
                else:
                    cavityd += finishing_data[str(xx)][i]
                    result += cavityd
            elif cut == finishing_data['Cut'][i] and topchip == finishing_data['Property'][i] and \
                    finishing_data['Shape'][i] == 'Dossiers':
                if fluo in ['None', 'Faint']:
                    chipd += (finishing_data[str(xx)][i] / 2)
                    result += chipd
                else:
                    chipd += finishing_data[str(xx)][i]
                    result += chipd
            elif cut == finishing_data['Cut'][i] and crownef == finishing_data['Property'][i] and \
                    finishing_data['Shape'][i] == 'Dossiers':
                if fluo in ['None', 'Faint']:
                    efd += (finishing_data[str(xx)][i] / 2)
                    result += efd
                else:
                    efd += finishing_data[str(xx)][i]
                    result += efd
        elif shape != 'RO':
            if polish == finishing_data['Polish'][i] and tableopen == finishing_data['Property'][i] and \
                    finishing_data['Shape'][i] == 'Fancy' and symmetry == finishing_data['Sym'][i]:
                if fluo in ['None', 'Faint']:
                    opend += (finishing_data[str(xx)][i] / 2)
                    result += opend
                else:
                    opend += finishing_data[str(xx)][i]
                    result += opend
            elif polish == finishing_data['Polish'][i] and tableopen == finishing_data['Property'][i] and \
                    finishing_data['Shape'][i] == 'Fancy' and symmetry == finishing_data['Sym'][i]:
                if fluo in ['None', 'Faint']:
                    naturald += (finishing_data[str(xx)][i] / 2)
                    result += naturald
                else:
                    naturald += finishing_data[str(xx)][i]
                    result += naturald
            elif polish == finishing_data['Polish'][i] and tableopen == finishing_data['Property'][i] and \
                    finishing_data['Shape'][i] == 'Fancy' and symmetry == finishing_data['Sym'][i]:
                if fluo in ['None', 'Faint']:
                    identednaturald += (finishing_data[str(xx)][i] / 2)
                    result += identednaturald
                else:
                    identednaturald += finishing_data[str(xx)][i]
                    result += identednaturald
            elif polish == finishing_data['Polish'][i] and tableopen == finishing_data['Property'][i] and \
                    finishing_data['Shape'][i] == 'Fancy' and symmetry == finishing_data['Sym'][i]:
                if fluo in ['None', 'Faint']:
                    cavityd += (finishing_data[str(xx)][i] / 2)
                    result += cavityd
                else:
                    cavityd += finishing_data[str(xx)][i]
                    result += cavityd
            elif polish == finishing_data['Polish'][i] and tableopen == finishing_data['Property'][i] and \
                    finishing_data['Shape'][i] == 'Fancy' and symmetry == finishing_data['Sym'][i]:
                if fluo in ['None', 'Faint']:
                    chipd += (finishing_data[str(xx)][i] / 2)
                    result += chipd
                else:
                    chipd += finishing_data[str(xx)][i]
                    result += chipd
            elif polish == finishing_data['Polish'][i] and tableopen == finishing_data['Property'][i] and \
                    finishing_data['Shape'][i] == 'Fancy' and symmetry == finishing_data['Sym'][i]:
                if fluo in ['None', 'Faint']:
                    efd += (finishing_data[str(xx)][i] / 2)
                    result += efd
                else:
                    efd += finishing_data[str(xx)][i]
                    result += efd

    # if sizeprec < 1.0:
    #     if (topnatural == 'N1' or crownnatural == 'N1' or girdlenatural == 'N1' or pavilionnatural == 'N1'):
    #         if (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2'):
    #             naturald = -1
    #             result = result - 1
    #         elif (clarity == 'VS1' or clarity == 'VS2'):
    #             naturald = -1
    #             result = result - 1
    #         else:
    #             naturald = 0
    #             result = result + 0
    #     elif (topnatural == 'N2' or crownnatural == 'N2' or girdlenatural == 'N2' or pavilionnatural == 'N2'):
    #         if (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2'):
    #             naturald = -2
    #             result = result - 2
    #         elif (clarity == 'VS1' or clarity == 'VS2'):
    #             naturald = -1
    #             result = result - 1
    #         else:
    #             naturald = -1
    #             result = result - 1
    #     elif (topnatural == 'N3' or crownnatural == 'N3' or girdlenatural == 'N3' or pavilionnatural == 'N3'):
    #         if (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2'):
    #             naturald = -3
    #             result = result - 3
    #         elif (clarity == 'VS1' or clarity == 'VS2'):
    #             naturald = -2
    #             result = result - 2
    #         else:
    #             naturald = -1
    #             result = result - 1
    #     if (
    #             identedtopnatural == 'INT' or identedcrownnatural == 'INT' or identedgirdlenatural == 'INT' or identedpavilionnatural == 'INT'):
    #         if (clarity == 'IF'):
    #             identednaturald = -3
    #             result = result - 3
    #         elif (clarity == 'VVS1' or clarity == 'VVS2'):
    #             identednaturald = -3
    #             result = result - 3
    #         elif (clarity == 'VS1' or clarity == 'VS2'):
    #             identednaturald = -2
    #             result = result - 2
    #         else:
    #             identednaturald = -1
    #             result = result - 1
    #     elif (
    #             identedtopnatural == 'ING' or identedcrownnatural == 'ING' or identedgirdlenatural == 'ING' or identedpavilionnatural == 'ING'):
    #         if (clarity == 'IF'):
    #             identednaturald = -1
    #             result = result - 1
    #         elif (clarity == 'VVS1' or clarity == 'VVS2'):
    #             identednaturald = -1
    #             result = result - 1
    #         elif (clarity == 'VS1' or clarity == 'VS2'):
    #             identednaturald = 0
    #             result = result - 0
    #         else:
    #             identednaturald = 0
    #             result = result - 0
    #     elif (
    #             identedtopnatural == 'INC' or identedcrownnatural == 'INC' or identedgirdlenatural == 'INC' or identedpavilionnatural == 'INC'):
    #         if (clarity == 'IF'):
    #             identednaturald = -2
    #             result = result - 2
    #         elif (clarity == 'VVS1' or clarity == 'VVS2'):
    #             identednaturald = -1
    #             result = result - 1
    #         elif (clarity == 'VS1' or clarity == 'VS2'):
    #             identednaturald = 0
    #             result = result - 0
    #         else:
    #             identednaturald = 0
    #             result = result - 0
    #     elif (
    #             identedtopnatural == 'INP' or identedcrownnatural == 'INP' or identedgirdlenatural == 'INP' or identedpavilionnatural == 'INP'):
    #         if (clarity == 'IF'):
    #             identednaturald = -1
    #             result = result - 1
    #         elif (clarity == 'VVS1' or clarity == 'VVS2'):
    #             identednaturald = -1
    #             result = result - 1
    #         elif (clarity == 'VS1' or clarity == 'VS2'):
    #             identednaturald = -1
    #             result = result - 1
    #         else:
    #             identednaturald = 0
    #             result = result - 0
    # if sizeprec >= 1.0:
    #     df31 = pd.read_csv('FinishingRoOpen.csv')
    #     if (shape == 'RO'):
    #         for i in range(len(df31)):
    #             if (tableopen == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         opend = df31['1'][i]
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         opend = df31['2'][i]
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         opend = df31['3'][i]
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         opend = df31['4'][i]
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         opend = df31['5'][i]
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         opend = df31['6'][i]
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         opend = df31['7'][i]
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         opend = df31['8'][i]
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         opend = df31['9'][i]
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         opend = (df31['1'][i] / 2)
    #                         result = result + (df31['1'][i] / 2)
    #                     if xx == 2:
    #                         opend = (df31['2'][i] / 2)
    #                         result = result + (df31['2'][i] / 2)
    #                     if xx == 3:
    #                         opend = (df31['3'][i] / 2)
    #                         result = result + (df31['3'][i] / 2)
    #                     if xx == 4:
    #                         opend = df31['4'][i] / 2
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         opend = df31['5'][i] / 2
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         opend = df31['6'][i] / 2
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         opend = df31['7'][i] / 2
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         opend = df31['8'][i] / 2
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         opend = df31['9'][i] / 2
    #                         result = result + df31['9'][i] / 2
    #             if (girdleopen == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         opend = result + df31['1'][i]
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         opend = df31['2'][i]
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         opend = df31['3'][i]
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         opend = df31['4'][i]
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         opend = df31['5'][i]
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         opend = df31['6'][i]
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         opend = df31['7'][i]
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         opend = df31['8'][i]
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         opend = df31['9'][i]
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         opend = df31['1'][i] / 2
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         opend = df31['2'][i] / 2
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         opend = df31['3'][i] / 2
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         opend = df31['4'][i] / 2
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         opend = df31['5'][i] / 2
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         opend = df31['6'][i] / 2
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         opend = df31['7'][i] / 2
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         opend = df31['8'][i] / 2
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         opend = df31['9'][i] / 2
    #                         result = result + df31['9'][i] / 2
    #             if (crownopen == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         opend = df31['1'][i]
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         opend = df31['2'][i]
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         opend = df31['3'][i]
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         opend = df31['4'][i]
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         opend = df31['5'][i]
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         opend = df31['6'][i]
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         opend = df31['7'][i]
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         opend = df31['8'][i]
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         opend = df31['9'][i]
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         opend = df31['1'][i] / 2
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         opend = df31['2'][i] / 2
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         opend = df31['3'][i] / 2
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         opend = df31['4'][i] / 2
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         opend = df31['5'][i] / 2
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         opend = df31['6'][i] / 2
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         opend = df31['7'][i] / 2
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         opend = df31['8'][i] / 2
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         opend = df31['9'][i] / 2
    #                         result = result + df31['9'][i] / 2
    #             if (pavilionopen == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         opend = df31['1'][i]
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         opend = df31['2'][i]
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         opend = df31['3'][i]
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         opend = df31['4'][i]
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         opend = df31['5'][i]
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         opend = df31['6'][i]
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         opend = df31['7'][i]
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         opend = df31['8'][i]
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         opend = df31['9'][i]
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         opend = df31['1'][i] / 2
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         opend = df31['2'][i] / 2
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         opend = df31['3'][i] / 2
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         opend = df31['4'][i] / 2
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         opend = df31['5'][i] / 2
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         opend = df31['6'][i] / 2
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         opend = df31['7'][i] / 2
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         opend = df31['8'][i] / 2
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         opend = df31['9'][i] / 2
    #                         result = result + df31['9'][i] / 2
    #         tempnat = result
    #         for i in range(len(df31)):
    #             if (topnatural == df31['open'][i] and cut == df31['Cut'][i]):
    #
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (crownnatural == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (girdlenatural == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (pavilionnatural == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #         naturald = result - tempnat
    #         temppp = result
    #         for i in range(len(df31)):
    #             if (identedtopnatural == df31['open'][i] and cut == df31['Cut'][i]):
    #
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (identedcrownnatural == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (identedgirdlenatural == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (identedpavilionnatural == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #         identednaturald = result - temppp
    #         temppp = result
    #         for i in range(len(df31)):
    #             if (topef == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (crownef == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (girdleef == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (pavilionef == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #         efd = result - temppp
    #         temppp = result
    #         for i in range(len(df31)):
    #             if (topcavity == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (crowncavity == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (girdlecavity == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (pavilioncavity == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #         cavityd = result - temppp
    #         temppp = result
    #         for i in range(len(df31)):
    #             if (topchip == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (crownchip == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (girdlechip == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (pavilionchip == df31['open'][i] and cut == df31['Cut'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #         chipd = result - temppp
    #     else:
    #         temppp = result
    #         for i in range(len(df31)):
    #
    #             if (tableopen == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (girdleopen == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (crownopen == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (pavilionopen == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][
    #                 i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #         opend = result - temppp
    #         temppp = result
    #         for i in range(len(df31)):
    #             if (topnatural == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (crownnatural == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][
    #                 i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (girdlenatural == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][
    #                 i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (pavilionnatural == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][
    #                 i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #         naturald = result - temppp
    #         temppp = result
    #         for i in range(len(df31)):
    #             if (topef == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (crownef == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (girdleef == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (pavilionef == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #         efd = result - temppp
    #         temppp = result
    #         for i in range(len(df31)):
    #             if (topcavity == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (crowncavity == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (girdlecavity == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][
    #                 i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (pavilioncavity == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][
    #                 i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #         cavityd = result - temppp
    #         temppp = result
    #         for i in range(len(df31)):
    #             if (topchip == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (crownchip == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (girdlechip == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #             if (pavilionchip == df31['open'][i] and polish == df31['Polish'][i] and symmetry == df31['Symmetry'][
    #                 i]):
    #                 if fluo != 'None' and fluo != 'Medium' and fluo != 'Faint':
    #                     if xx == 1:
    #                         result = result + df31['1'][i]
    #                     if xx == 2:
    #                         result = result + df31['2'][i]
    #                     if xx == 3:
    #                         result = result + df31['3'][i]
    #                     if xx == 4:
    #                         result = result + df31['4'][i]
    #                     if xx == 5:
    #                         result = result + df31['5'][i]
    #                     if xx == 6:
    #                         result = result + df31['6'][i]
    #                     if xx == 7:
    #                         result = result + df31['7'][i]
    #                     if xx == 8:
    #                         result = result + df31['8'][i]
    #                     if xx == 9:
    #                         result = result + df31['9'][i]
    #                 else:
    #                     if xx == 1:
    #                         result = result + df31['1'][i] / 2
    #                     if xx == 2:
    #                         result = result + df31['2'][i] / 2
    #                     if xx == 3:
    #                         result = result + df31['3'][i] / 2
    #                     if xx == 4:
    #                         result = result + df31['4'][i] / 2
    #                     if xx == 5:
    #                         result = result + df31['5'][i] / 2
    #                     if xx == 6:
    #                         result = result + df31['6'][i] / 2
    #                     if xx == 7:
    #                         result = result + df31['7'][i] / 2
    #                     if xx == 8:
    #                         result = result + df31['8'][i] / 2
    #                     if xx == 9:
    #                         result = result + df31['9'][i] / 2
    #         chipd = result - temppp

            # Internal Grading I dont think this is present in the stockfile
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
        if (shape != 'RO' and 'Fancy' == df30['Shape'][i] and downgrade1 == df30['what'][i]):
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
        if (shape != 'RO' and 'Fancy' == df30['Shape'][i] and downgrade2 == df30['what'][i]):
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

    # Depth discount
    depth_data = pd.read_excel('miscellenious_discounts/output_files/output_extra_discounts.xlsx',
                               sheet_name='Depth')
    if 0.30 <= sizeprec <= 0.99:
        if cut == 'EX' and depth >= 63 and (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2') and (
                color == 'D' or color == 'E' or color == 'F'):
            depthd = depth_data['Depth'][0]
            result = result + depthd
        if cut == 'VG' and depth >= 64.8 and (clarity == 'IF' or clarity == 'VVS1' or clarity == 'VVS2') and (
                color != 'J' or color != 'K' or color != 'L' or color != 'I'):
            depthd = depth_data['Depth'][1]
            result = result + depthd
    # Depth discount

    # Days
    day_csv = pd.read_csv('days_discount.csv')
    for i in range(len(day_csv)):
        if day_csv['Days Min'][i] <= days <= day_csv['Days Max'][i]:
            daysd += day_csv['Discount'][i]
            result += daysd
            break
    # if (sizeprec < 1.0):
    #     if (days >= 60 and days <= 89):
    #         result = result - 1.0
    #         daysd = -1
    #     if (days >= 90 and days <= 119):
    #         result = result - 2.0
    #         daysd = -2
    #     if (days >= 120 and days <= 179):
    #         result = result - 3.0
    #         daysd = -3
    #     if (days >= 180 and days <= 299):
    #         result = result - 5.0
    #         daysd = -5
    #     if (days >= 300 and days <= 499):
    #         result = result - 7.0
    #         daysd = -7
    #     if (days >= 500):
    #         result = result - 10.0

    # daysd = -10

    # very strong fluo
    vst_fluo_data = pd.read_csv('very_strong_fluo.csv')
    for i in range(len(vst_fluo_data)):
        vst_size = vst_fluo_data['Size_min'][i] <= sizeprec <= vst_fluo_data['Size_max'][i]
        if shape == vst_fluo_data['Shape'][i] and vst_size and vst_fluo_data['Fluo'][i] == fluo:
            very_strong_fluod += float(vst_fluo_data['Discount'][i])
            result += very_strong_fluod
            break

    # Parameteres fancy
    ## Fluo discount
    if shape != 'RO':
        fluo_data = pd.read_csv('fluo_disc.csv')
        for i in range(len(fluo_data)):
            if fluo_data['Color'][i] == color and fluo_data['Fluo'][i] == fluo:
                try:
                    fancy_fluod += float(fluo_data[clarity][i])
                    result += fancy_fluod
                    break
                except BaseException as e:
                    pass
    ## symm/polish
    if shape != 'RO' and symmetry == 'GD' and polish == 'GD':
        sym_pol = pd.read_csv('second_df.csv')
        for i in range(len(sym_pol)):
            if sym_pol['Lower'][i] <= sizeprec <= sym_pol['Upper'][i]:
                sym_pold += sym_pol['Discount'][i]
                result += sym_pold
                break
    elif shape != 'RO' and (symmetry == 'VG' or symmetry == 'EX') and (polish == 'VG' or polish == 'EX'):
        sym_pol = pd.read_csv('third_df.csv')
        for i in range(len(sym_pol)):
            size_range = sym_pol['Weight'][i]
            size_mn = float(size_range.split('-')[0])
            size_mx = float(size_range.split('-')[1])
            if size_mn <= sizeprec <= size_mx and sym_pol['Clarity'][i] == color:
                try:
                    sym_pold += sym_pol[clarity][i]
                    result += sym_pold
                    break
                except BaseException as e:
                    pass
    if ff == 0:
        rap = 0;
    if color1 == 'N':
        result = result - 7
    if temp >= -40:
        if temp - result > 20:
            result = temp - 20
            capped = 20
    else:
        if temp - result > 15:
            result = temp - 15
            capped = 15


    # polish_sym
    if shape == 'RO':
        pass


    ans = []
    ans.append(result)
    ans.append(base)
    ans.append(gdd)
    ans.append(diameterd)
    ans.append(colshaded)
    ans.append(milkyd)
    ans.append(cutcommentsd)
    ans.append(grainingd)
    ans.append(had)
    ans.append(eyecleand)
    ans.append(tablecleand)
    ans.append(blackd)
    ans.append(sideblackd)
    ans.append(sizepremd)
    ans.append(opend)
    ans.append(naturald)
    ans.append(identednaturald)
    ans.append(efd)
    ans.append(cavityd)
    ans.append(chipd)
    ans.append(MNcolorD)
    ans.append(depthd)
    ans.append(ktosd)
    ans.append(daysd)
    ans.append(very_strong_fluod)
    ans.append(fancy_fluod)
    ans.append(sym_pold)
    ans.append(capped)

    return ans

# def get_cut_comments(cert, shape, cut, tabl, height, ratio, cr_angle,td,pv_angle, pv_depth, girdle_percentage,star_length, lower_half):
#     if cert=='GIA' and shape=='RO':
#         if(cut=='EX' and tabl>=56 and tabl<=59 and cr_angle>=34 and cr_angle<=35.5 and pv_angle>=40.6 and pv_angle<=41.2 and girdle_percentage>=2.5 and girdle_percentage<=3.5 and ratio>=0 and ratio<=0.5 and star_length>=50 and star_length<=55 and lower_half>=75 and lower_half<=80 and td>=59.5 and td<=62.7):
#             cutcc='EX->EX1'
#         elif(cut=='EX' and tabl>=56 and tabl<=61 and cr_angle>=33 and cr_angle<=36 and pv_angle>=40.6 and pv_angle<=41.2 and girdle_percentage>=2.0 and girdle_percentage<=4 and ratio>=0 and ratio<=0.9 and star_length>=50 and star_length<=55 and lower_half>=75 and lower_half<=80 and td>=59.0 and td<=63.2):
#             cutcc='EX->EX2'    
#         elif(cut=='VG' and tabl>=55 and tabl<=60 and cr_angle>=32.5 and cr_angle<=37.5 and pv_angle>=40.4 and pv_angle<=41.6 and girdle_percentage>=2.5 and girdle_percentage<=4.7 and ratio>=0 and ratio<=0.9 and star_length>=45 and star_length<=55 and lower_half>=70 and lower_half<=80 and td>=58.5 and td<=64):
#             cutcc='VG->VG1'     
#         elif(cut=='VG' and tabl>=54 and tabl<=62 and cr_angle>=32 and cr_angle<=38 and pv_angle>=40.2 and pv_angle<=42.2 and girdle_percentage>=2 and girdle_percentage<=5.5 and ratio>=0 and ratio<=1.2 and star_length>=45 and star_length<=55 and lower_half>=70 and lower_half<=80 and td>=58 and td<=64.7):
#             cutcc='VG->VG2'    
#         elif(cut=='GD' and tabl>=53 and tabl<=62 and cr_angle>=31 and cr_angle<=38.7 and pv_angle>=39.8 and pv_angle<=42.6 and girdle_percentage>=2 and girdle_percentage<=6.5 and ratio>=0 and ratio<=1.6 and star_length>=45 and star_length<=55 and lower_half>=70 and lower_half<=80 and td>=57.5 and td<=66.2):
#             cutcc='G->GD1'
#     return cutcc
