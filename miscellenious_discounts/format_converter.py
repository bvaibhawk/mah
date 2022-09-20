import math
import numbers

import pandas as pd
import numpy as np
from pandasql import sqldf
from openpyxl import load_workbook
from skimage.measure import label, regionprops


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
    clarity_color_mapping = pd.read_excel('miscellenious_discounts/input_files/input_price_module_discounts.xlsm',
                                          sheet_name='Central',
                                          usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9])

    clarity_cut_dict = {'COLOR': [], 'CLARITY': [], 'KEY': []}

    for i in range(2, 12):
        for j in range(1, len(clarity_color_mapping.columns)):
            clarity_cut_dict['COLOR'].append(clarity_color_mapping.iloc[i, 0])
            clarity_cut_dict['CLARITY'].append(clarity_color_mapping.iloc[1, j])
            clarity_cut_dict['KEY'].append(clarity_color_mapping.iloc[i, j])
    output_df = pd.DataFrame.from_dict(clarity_cut_dict)
    write_excel('miscellenious_discounts/output_files/output_extra_discounts.xlsx', 'CENTRAL', output_df)


def diameter_premium():
    data = pd.read_excel('miscellenious_discounts/input_files/input_price_module_discounts.xlsm',
                         sheet_name='Diameter Premiums',
                         usecols=[16, 17, 18, 19, 20])
    data_grt_one = pd.read_excel('miscellenious_discounts/input_files/input_price_module_discounts.xlsm',
                                 sheet_name='Diameter Premiums',
                                 usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    central_map = pd.read_excel('miscellenious_discounts/output_files/output_extra_discounts.xlsx',
                                sheet_name='CENTRAL')
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
    write_excel('miscellenious_discounts/output_files/output_extra_discounts.xlsx', 'Diameter Premiums', output_df)


def size_premium():
    xls = pd.ExcelFile("miscellenious_discounts/input_files/input_price_module_discounts.xlsm")
    df1 = pd.read_excel(xls, "Size Premiums")
    arr = df1.to_numpy()

    def saveDataFrame(nparr: np.array, name: str):

        nparrdf = pd.DataFrame(list(nparr))

        nparrdf.columns = nparrdf.iloc[0]

        if (list(nparrdf.columns).__contains__("Class")):
            nparrdf = nparrdf.drop(["Class"], axis=1)

        nparrdf = nparrdf.drop(nparrdf.index[0])

        for i in range(len(nparrdf.columns.values)):

            if isinstance(nparrdf.columns.values[i], numbers.Number):
                nparrdf.columns.values[i] = int(nparrdf.columns.values[i])
        nparrdf.to_csv(f"{name}.csv", index=False)

    def saveDFSizePremiums(df_size_premiums):
        # converting df to np.array
        arr = df_size_premiums.to_numpy()

        # Extracting Important Locations
        # Round Excelent (3VG+) Big (3 to 7 Carats)
        roexbg = arr[1:25, 14:26]
        roexbgF = arr[28:52, 14:18]

        # Round Excelent Small (1 to 3 Carats)
        roexsm = arr[1:21, 1:12]
        roexsmF = arr[24:44, 1:4]

        # Round VeryGood Small (1 to 3 Carats)
        rovgsm = arr[47:67, 1:12]
        rovgsmF = arr[70:90, 1:4]

        # Fancy Section
        fancy = arr[1:44, 28:39]

        # Round 3VG+ Dossiers
        roexdossiers = arr[2:15, 40:43]

        # Calling The Save File Functions

        saveDataFrame(roexbg, "roexbg")
        saveDataFrame(roexbgF, "roexbgF")

        saveDataFrame(roexsm, "roexsm")
        saveDataFrame(roexsmF, "roexsmF")

        saveDataFrame(rovgsm, "rovgsm")
        saveDataFrame(rovgsmF, "rovgsmF")

        saveDataFrame(fancy, "fancy")

        saveDataFrame(roexdossiers, "roexdossiers")

    # saves all tables in size premium sheet to 8 csv files
    saveDFSizePremiums(df1)


def doss_base():
    sheet_names = ['0.30-0.34', '0.35-0.39', '0.40-0.44', '0.40-0.44', '0.45-0.49', '0.50-0.59', '0.70-0.74',
                   '0.75-0.79', '0.80-0.89', '0.90-0.94', '0.95-0.99']

    final_df = pd.DataFrame()
    for sheet in sheet_names:
        df_list = []

        df = pd.read_excel("miscellenious_discounts/input_files/input_price_module_discounts.xlsm", sheet_name=sheet)

        # extracting required tables in form of dataframes from spreadsheet
        binary_rep = np.array(df.notnull().astype('int'))
        l = label(binary_rep)
        for s in regionprops(l):
            if df.iloc[s.bbox[0]:s.bbox[2], s.bbox[1]:s.bbox[3]].shape[1] >= 2:
                df_list.append(df.iloc[s.bbox[0]:s.bbox[2], s.bbox[1]:s.bbox[3]])

        # iterating through extracted dataframes
        for d in df_list:
            clarity = []
            Cut = []
            Polish = []
            Symmetry = []
            Fluo = []
            Size = []
            size_name = sheet

            if d.iloc[0][1] == "Max-55":
                cut_name = d.iloc[1][1]

            else:
                cut_name = d.iloc[0][1]

            if cut_name.count("X") == 3:
                Cut.append("EX")
                Polish.append("EX")
                Symmetry.append("EX")
            elif cut_name.count("X") == 1:
                Cut.append("EX")
                Polish.append("DD")
                Symmetry.append("DD")
            elif "VG" in cut_name:
                Cut.append("VG")
                Polish.append("DD")
                Symmetry.append("DD")
            elif "GD" in cut_name:
                Cut.append("GD")
                Polish.append("DD")
                Symmetry.append("DD")

            if "NONE" in cut_name:
                Fluo.append("None")
            elif "FAINT" in cut_name:
                Fluo.append("Faint")
            elif "MED" in cut_name:
                Fluo.append("Med")
            elif "VERY STRONG" in cut_name:
                Fluo.append("Very Strong")
            elif "STRONG" in cut_name:
                Fluo.append("Strong")

            Size.append(size_name)

            sd = d.copy()
            sd.reset_index(drop=True, inplace=True)
            if d.iloc[0][1] == "Max-55":
                sd.columns = sd.iloc[2]
                sd = sd.drop([0, 1, 2])
            else:
                sd.columns = sd.loc[1]
                sd = sd.drop([0, 1])
            sd['Cut'] = Cut * len(sd)
            sd['Polish'] = Polish * len(sd)
            sd['Symmetry'] = Symmetry * len(sd)
            sd['Fluo'] = Fluo * len(sd)
            sd['Size'] = Size * len(sd)
            sd.rename(columns={sd.columns[0]: "Clarity"}, inplace=True)
            # print(d)
            final_df = final_df.append(sd, ignore_index=True)

    final_df.reset_index(inplace=True, drop=True)
    final_df.to_csv("Dossbase.csv")


def black_csv():
    xls = pd.ExcelFile("miscellenious_discounts/input_files/input_price_module_discounts.xlsm")
    df_black = pd.read_excel(xls, "Black")

    black = df_black.to_numpy()
    # defining extra cols and their values according to the respective dataframes.
    cols = ["sizemin", "sizemax", "cut", "polish", "sym", "Shape"]
    colvalues_roex1to6 = [1, 5.99, "EX", "", "", "RO"]
    colvalues_rovg1to6 = [1, 5.99, "VG", "", "", "RO"]
    colvalues_rog1to6 = [1, 5.99, "G", "", "", "RO"]
    colvalues_faex1to3 = [0, 2.99, "EX", "EX", "EX", "Fancy"]
    colvalues_favg1to3 = [0, 2.99, "", "VG", "VG", "Fancy"]
    colvalues_faexabove3 = [3, 10, "EX", "EX", "EX", "Fancy"]
    colvalues_favgabove3 = [3, 10, "", "VG", "VG", "Fancy"]
    colvalues_dossiers = [0, 0.99, "", "", "", "Dossiers"]

    colvalues_list = [colvalues_roex1to6, colvalues_rovg1to6, colvalues_rog1to6, colvalues_faex1to3,
                      colvalues_favg1to3, colvalues_faexabove3, colvalues_favgabove3, colvalues_dossiers]

    k = 1
    for i in range(4):
        black[1, k] = "Location"
        black[15, k] = "Location"
        black[29, k] = "Location"
        k = k + 12

    # helper functions
    # fills nan values in the location column

    def fillnaLocations(df):
        df["Location"] = df["Location"].fillna(method='ffill')
        return df

    # converts np array to dataframe

    def toDataFrame(nparr: np.array, index: list):
        nparrdf = pd.DataFrame(list(nparr))
        nparrdf.columns = nparrdf.iloc[0]
        nparrdf = fillnaLocations(nparrdf)
        for i in range(len(nparrdf["Intensity"])):
            if nparrdf.Location[i] == "Table":
                nparrdf["Intensity"][i] = "BT" + str(nparrdf["Intensity"][i])
            elif nparrdf.Location[i] == "Crown":
                nparrdf["Intensity"][i] = "BC" + str(nparrdf["Intensity"][i])
        for i in range(len(nparrdf.columns.values)):
            if isinstance(nparrdf.columns.values[i], numbers.Number):
                nparrdf.columns.values[i] = int(nparrdf.columns.values[i])
        nparrdf = nparrdf.drop(nparrdf.index[0])
        nparrdf = nparrdf.set_index(pd.Index(index))
        return nparrdf

    # adds extra columns in the dataframes as per the requirements

    def fillExtraCols(df: pd.DataFrame, cols: list, colvalues: list):
        for i in range(len(cols)):
            df[f"{cols[i]}"] = colvalues[i]

    def saveBlackCSV(black):
        # checks to see if the sheet is correct or not
        freq = {}
        included = ["Section", "Intensity", "Table", "Crown"]
        for row in black:
            for ele in row:
                if ele not in included:
                    continue
                if ele in freq:
                    freq[ele] += 1
                else:
                    freq[ele] = 1

        if not (list(freq.keys()) == included and np.unique(list(freq.values()))[0] == 8):
            raise Exception("Invalid Format for Black Discount Sheet")

        # defining regions
        roex1to6 = black[1:12, 1:12]
        rovg1to6 = black[15:26, 1:12]
        rog1to6 = black[29:40, 1:12]
        faex1to3 = black[1:12, 13:24]
        favg1to3 = black[15:26, 13:24]
        faexabove3 = black[1:12, 25:36]
        favgabove3 = black[15:26, 25:36]
        dossiers = black[1:12, 37:48]

        # converting to individual dataframes
        roex1to6df = toDataFrame(roex1to6, list(i for i in range(10)))
        rovg1to6df = toDataFrame(rovg1to6, list(i for i in range(10, 20)))
        rog1to6df = toDataFrame(rog1to6, list(i for i in range(20, 30)))
        faex1to3df = toDataFrame(faex1to3, list(i for i in range(30, 40)))
        favg1to3df = toDataFrame(favg1to3, list(i for i in range(40, 50)))
        faexabove3df = toDataFrame(faexabove3, list(i for i in range(50, 60)))
        favgabove3df = toDataFrame(favgabove3, list(i for i in range(60, 70)))
        dossiersdf = toDataFrame(dossiers, list(i for i in range(70, 80)))

        df_list = [roex1to6df, rovg1to6df, rog1to6df, faex1to3df,
                   favg1to3df, faexabove3df, favgabove3df, dossiersdf]

        # filling nan values in the "Location" column
        for df in df_list:
            df = fillnaLocations(df)

        for i in range(len(df_list)):
            fillExtraCols(df_list[i], cols, colvalues_list[i])

        result = pd.concat(df_list)
        path = "black.csv"
        result.to_csv(path, index=False)
        print(f"File Saved Successfully to {path}")

    saveBlackCSV(black)


def depth_csv():
    depth_data = pd.read_excel('miscellenious_discounts/input_files/input_price_module_discounts.xlsm',
                               sheet_name='Depth')
    depth_dict = {'Depth': []}
    depth_dict['Depth'].append(depth_data.iloc[2, 1])
    depth_dict['Depth'].append(depth_data.iloc[3, 1])
    output_df = pd.DataFrame.from_dict(depth_dict)
    write_excel('miscellenious_discounts/output_files/output_extra_discounts.xlsx', 'Depth', output_df)


def cut_csv():
    xls = pd.ExcelFile("miscellenious_discounts/input_files/input_price_module_discounts.xlsm")
    df_cut = pd.read_excel(xls, "Cut")

    def toDataFrame(nparr: np.array):
        nparrdf = pd.DataFrame(list(nparr))
        nparrdf.columns = nparrdf.iloc[0]
        nparrdf = nparrdf.drop(nparrdf.index[0])
        for i in range(len(nparrdf.columns.values)):
            if isinstance(nparrdf.columns.values[i], numbers.Number):
                nparrdf.columns.values[i] = int(nparrdf.columns.values[i])
        return nparrdf

    def saveCutCSV(df_cut: pd.DataFrame):
        cut = df_cut.to_numpy()
        freq = {}
        included = ["Section", "Cut"]
        for row in cut:
            for ele in row:
                if ele not in included:
                    continue
                if ele in freq:
                    freq[ele] += 1
                else:
                    freq[ele] = 1

        if not (list(freq.keys()) == included and np.unique(list(freq.values()))[0] == 1):
            raise Exception("Invalid Format for Cut Discount Sheet")
        cut[1, 2] = "Cut Comment"
        cut_imp = cut[1:13, 1:13]
        cutdf = toDataFrame(cut_imp)
        cutdf["Cut"] = cutdf["Cut"].fillna(method="ffill")
        cutdf.to_csv("cut_comments.csv", index=False)

    saveCutCSV(df_cut)


def cut_1_5_base_csv():
    sheet_names = ['1.01-1.09', '1.50-1.69', '2.01-2.09', '3.01-3.09', '4.01-4.09', '5.01-5.09']
    final_df = pd.DataFrame()

    for sheet in sheet_names:
        df_list = []

        df = pd.read_excel("miscellenious_discounts/input_files/input_price_module_discounts.xlsm", sheet_name=sheet)

        # extracting required tables in form of dataframes from spreadsheet
        binary_rep = np.array(df.notnull().astype('int'))
        l = label(binary_rep)
        for s in regionprops(l):
            if df.iloc[s.bbox[0]:s.bbox[2], s.bbox[1]:s.bbox[3]].shape[1] >= 2:
                df_list.append(df.iloc[s.bbox[0]:s.bbox[2], s.bbox[1]:s.bbox[3]])

        # iterating through extracted dataframes
        for d in df_list:
            clarity = []
            Cut = []
            Polish = []
            Symmetry = []
            Fluo = []
            Size = []
            size_name = sheet.split(" ")[-1]
            flag = 0

            d.reset_index(drop=True, inplace=True)
            # if d.iloc[:,0].isna().sum()>1:
            # print(d)
            #     cut_name = d.iloc[0][0]
            #     d.drop(d.columns[0], axis=1, inplace=True)
            # else:
            cut_name = d.iloc[0][0]
            # print(d)

            if cut_name == 'Very Strong':
                cut_name = 'GD Very Strong'

            # print(cut_name)
            # print(cut_name[0])

            if cut_name[0] == '3':
                val = cut_name.split(" ")[0]
                val2 = " ".join(cut_name.split(" ")[1:])
                Cut.append(val[1:])
                Polish.append(val[1:])
                Symmetry.append(val[1:])
                Fluo.append(val2)
            elif "-" in cut_name:
                val = cut_name.split("-")[0]
                val2 = cut_name.split("-")[1]
                Cut.append(val)
                Polish.append(val)
                Symmetry.append(val)
                Fluo.append(val2)
            else:
                if len(cut_name) < 3:
                    val = cut_name.split(" ")[0]
                    if val == "Good":
                        val = "GD"
                    val2 = cut_name.split(" ")[1]
                    Cut.append(val)
                    Polish.append(val)
                    Symmetry.append(val)
                    Fluo.append(val2)
                else:
                    val = cut_name.split(" ")[0]
                    if val == "Good":
                        val = "GD"
                    val2 = " ".join(cut_name.split(" ")[1:])
                    Cut.append(val)
                    Polish.append(val)
                    Symmetry.append(val)
                    Fluo.append(val2)

            # elif "VG" in cut_name:
            #     Cut.append("VG")
            #     Polish.append("DD")
            #     Symmetry.append("DD")
            # elif "GD" in cut_name:
            #     Cut.append("GD")
            #     Polish.append("DD")
            #     Symmetry.append("DD")

            # if "NON" in cut_name:
            #     Fluo.append("None")
            # elif "FNT" in cut_name:
            #     Fluo.append("Faint")
            # elif "MED" in cut_name:
            #     Fluo.append("Medium")
            # elif "STG" in cut_name:
            #     Fluo.append("Strong")
            # elif "VST" in cut_name:
            #     Fluo.append("Very Strong")

            Size.append(size_name)

            sd = d.copy()
            sd.reset_index(drop=True, inplace=True)

            # print(Cut)

            sd.drop(sd.columns[0], axis=1, inplace=True)
            sd.columns = sd.loc[0]
            sd = sd.drop([0])
            sd.rename(columns={sd.columns[0]: "Clarity"}, inplace=True)

            # if flag==0:
            #     sd.columns = sd.loc[1]
            #     sd = sd.drop([0,1])
            #     sd.rename(columns={sd.columns[0]: "Clarity" }, inplace = True)

            # else:

            #     sd.columns = sd.iloc[2]
            #     sd = sd.drop([1,2])

            #     sd.rename(columns={sd.columns[0]: "Clarity" }, inplace = True)
            sd = pd.melt(sd, id_vars='Clarity', value_vars=['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'])

            sd.rename(columns={'Clarity': 'COLOR', 0: 'CLARITY', 'value': 'Discount'}, inplace=True)

            sd['Shape'] = ['RO'] * len(sd)
            sd['CUT'] = Cut * len(sd)
            sd['POL'] = Polish * len(sd)
            sd['SYM'] = Symmetry * len(sd)
            sd['FLUO'] = Fluo * len(sd)
            sd['Size'] = Size * len(sd)

            sd = sd[['Discount', 'Shape', 'COLOR', 'CLARITY', 'CUT', 'POL', 'SYM', 'FLUO', 'Size']]

            # print(cut_name)

            # sd.dropna(inplace=True)
            # print(sd)
            final_df = final_df.append(sd, ignore_index=True)

    print(final_df.head(10))
    final_df.reset_index(inplace=True, drop=True)

    final_df.to_csv("1ct_5ctup.csv")


def fancy_base_csv():
    final_df = pd.DataFrame()
    df_list = []

    df = pd.read_excel("miscellenious_discounts/input_files/input_price_module_discounts.xlsm",
                       sheet_name='Fancy Shapes')

    # extracting required tables in form of dataframes from spreadsheet
    binary_rep = np.array(df.notnull().astype('int'))
    l = label(binary_rep)
    for s in regionprops(l):
        if df.iloc[s.bbox[0]:s.bbox[2], s.bbox[1]:s.bbox[3]].shape[1] >= 2:
            df_list.append(df.iloc[s.bbox[0]:s.bbox[2], s.bbox[1]:s.bbox[3]])

    # iterating through extracted dataframes
    for d in df_list:
        clarity = []
        Cut = []
        Polish = []
        Symmetry = []
        Fluo = []
        Size = []
        shape = []
        flag = 0

        d.reset_index(drop=True, inplace=True)
        # print(d)

        shape.append(d.columns[0])
        if d.iloc[0][0] == 'EX/EX':
            Size.append(d.iloc[1][0])
            flag = 1
        else:
            Size.append(d.iloc[0][0])

        sd = d.copy()
        sd.reset_index(drop=True, inplace=True)

        # print(Cut)
        if flag == 1:
            sd.columns = sd.loc[1]
            sd = sd.drop([0, 1])
            sd.rename(columns={sd.columns[0]: "Clarity"}, inplace=True)
        else:
            sd.columns = sd.loc[0]
            sd = sd.drop([0])
            sd.rename(columns={sd.columns[0]: "Clarity"}, inplace=True)

        sd['Size'] = Size * len(sd)
        sd['Shape'] = shape * len(sd)

        # print(sd)

        final_df = final_df.append(sd, ignore_index=True)

    final_df.reset_index(inplace=True, drop=True)
    print(final_df.head(10))

    final_df.to_csv("fancy_base.csv")


def graining_csv():
    final_df = pd.DataFrame()
    df_list = []

    df = pd.read_excel("miscellenious_discounts/input_files/input_price_module_discounts.xlsm", sheet_name='Graining')

    # extracting required tables in form of dataframes from spreadsheet
    binary_rep = np.array(df.notnull().astype('int'))
    l = label(binary_rep)
    for s in regionprops(l):
        if df.iloc[s.bbox[0]:s.bbox[2], s.bbox[1]:s.bbox[3]].shape[1] >= 2:
            df_list.append(df.iloc[s.bbox[0]:s.bbox[2], s.bbox[1]:s.bbox[3]])

    # iterating through extracted dataframes
    for d in df_list:

        # print(d)

        if len(d) > 2:
            final_columns = ['Graining', 1, 2, 3, 4, 5, 6, 7, 8, 9]

            graining = d.iloc[:, 0].str.split("-", -1, expand=True)[1]
            graining.reset_index(drop=True, inplace=True)
            graining = pd.Series(["I" + str(word) if str(word).startswith("G") else word for word in graining])
            d.reset_index(drop=True, inplace=True)
            d = d.drop([0])
            d.drop(d.columns[0:3], axis=1, inplace=True)
            d.insert(0, 'Graining', graining)
            d.columns = final_columns
            d.reset_index(drop=True, inplace=True)
            d.dropna(inplace=True)

            final_df = d
    # final_df.reset_index(inplace=True,drop=True)
    print(final_df.head(10))

    final_df.to_csv("graining.csv")


def internal_grading_csv():
    final_df = pd.DataFrame()
    df_list = []

    df = pd.read_excel("input_files/input_price_module_discounts.xlsm", sheet_name='Internal Grading')

    # extracting required tables in form of dataframes from spreadsheet
    binary_rep = np.array(df.notnull().astype('int'))
    l = label(binary_rep)
    for s in regionprops(l):
        if df.iloc[s.bbox[0]:s.bbox[2], s.bbox[1]:s.bbox[3]].shape[1] >= 2:
            df_list.append(df.iloc[s.bbox[0]:s.bbox[2], s.bbox[1]:s.bbox[3]])

    # iterating through extracted dataframes
    for d in df_list:

        shape = []
        # print(d)

        if len(d.columns) > 11:
            d.drop(d.columns[0], axis=1, inplace=True)

        if d.iloc[0][0] != np.nan:
            shape.append(d.iloc[0][0])
        else:
            shape.append(d.iloc[0][1])
        d.columns = d.loc[1]
        d = d.drop([0, 1])
        d.iloc[:, 0] = d.iloc[:, 0].ffill(axis=0)
        d.reset_index(drop=True, inplace=True)

        d['Shape'] = shape * len(d)
        d.rename(columns={d.columns[0]: "Grade", d.columns[1]: "What"}, inplace=True)
        # print(d)

        final_df = final_df.append(d, ignore_index=True)

    final_df.reset_index(inplace=True, drop=True)
    print(final_df.head(10))

    final_df.to_csv("../internal_grading.csv")


def extras_csv():
    xls = pd.ExcelFile("input_files/input_price_module_discounts.xlsm")
    extras_df = pd.read_excel(xls, "Extras")
    extras = extras_df.to_numpy()

    def toDataFrame(nparr: np.array):
        nparrdf = pd.DataFrame(list(nparr))
        nparrdf.columns = nparrdf.iloc[0]
        nparrdf = nparrdf.drop(nparrdf.index[0])
        for i in range(len(nparrdf.columns.values)):
            if isinstance(nparrdf.columns.values[i], numbers.Number):
                nparrdf.columns.values[i] = int(nparrdf.columns.values[i])
        return nparrdf

    def gsCellToXIndex(x1: str, x2: str):
        xx1 = 0
        xx2 = 0
        if len(x1) > 1:
            xx1 += 26 * (len(x1) - 1)
        if len(x2) > 1:
            xx2 += 26 * (len(x1) - 1)

        xx1 += ord(x1[-1]) - ord("A")
        xx2 += ord(x2[-1]) - ord("A")

        return range(xx1, xx2 + 1)

    def saveExtrasCSV(extras):

        if not (extras[0, ord("B") - ord("A")] == "Round" and
                extras[0, ord("D") - ord("A")] == extras[0, ord("P") - ord("A")] == "Section" and
                extras[0, ord("N") - ord("A")] == "Fancy" and extras[2, 1] == "H&A"):
            raise Exception("Incorrect Format for Extras Discount Sheet")

        ro = extras[1:10, gsCellToXIndex("B", "L")]
        fa = extras[1:10, gsCellToXIndex("N", "X")]

        ro[0, 0] = "Field"
        ro[0, 1] = "FieldValue"
        fa[0, 0] = "Field"
        fa[0, 1] = "FieldValue"

        rodf = toDataFrame(ro)
        fadf = toDataFrame(fa)

        rodf["Field"] = rodf["Field"].fillna(method="ffill")
        fadf["Field"] = fadf["Field"].fillna(method="ffill")

        rodf["Shape"] = "RO"
        fadf["Shape"] = "Fancy"
        rodf.set_index(pd.Index(list(i for i in range(len(rodf)))), inplace=True)
        fadf.set_index(pd.Index(list(i for i in range(
            len(rodf), len(rodf) + len(fadf)))), inplace=True)

        result = pd.concat([rodf, fadf])
        result.to_csv("../extras.csv", index=False)

    saveExtrasCSV(extras)


def bgm_csv():
    final_df = pd.DataFrame()

    df_list = []

    df = pd.read_excel("input_files/input_price_module_discounts.xlsm", sheet_name='BGM')

    # extracting required tables in form of dataframes from spreadsheet
    binary_rep = np.array(df.notnull().astype('int'))
    l = label(binary_rep)
    for s in regionprops(l):
        if df.iloc[s.bbox[0]:s.bbox[2], s.bbox[1]:s.bbox[3]].shape[1] >= 2:
            df_list.append(df.iloc[s.bbox[0]:s.bbox[2], s.bbox[1]:s.bbox[3]])

    flag = set()

    # iterating through extracted dataframes
    for d in df_list:

        # d.reset_index(drop=True,inplace=True)
        # print(d)

        # print(d.columns[0])

        if d.columns[0] not in flag:
            cut_name = d.columns[0]
        else:
            cut_name = 'Rounds Otherwise'

        if d.columns[0] == 'Rounds 3VG+ /Non-Med':
            flag.add(d.columns[0])

        d[d.columns[0]] = d[d.columns[0]].ffill(axis=0)

        d.columns = ['BGM', 'BGM Type', 1, 2, 3, 4, 5, 6, 7, 8, 9]
        d.dropna(inplace=True)
        d.reset_index(inplace=True, drop=True)
        # print(cut_name)
        # print(d)

        if "Rounds 3VG+" in cut_name:
            d.to_csv("../BGM_3VG.csv")

        elif "Rounds Otherwise" in cut_name:
            d.to_csv("../BGM_RO.csv")

        elif "Fancy" in cut_name:
            d.to_csv("../BGM_Fancy.csv")

        elif "Dossier" in cut_name:
            d.to_csv("../BGM_dossier.csv")


def finishing_csv():
    xls = pd.ExcelFile("input_files/input_price_module_discounts.xlsm")
    finishing_df = pd.read_excel(xls, "Finishing")
    finishing = finishing_df.to_numpy()

    # defining extra columns
    cols = ["Cut", "Polish", "Sym", "Shape"]
    colvalues_roex = ["EX", "", "", "RO"]
    colvalues_rovg = ["VG", "", "", "RO"]
    colvalues_rog = ["G", "", "", "RO"]
    colvalues_faex = ["EX", "EX", "EX", "Fancy"]
    colvalues_favg = ["", "VG", "VG", "Fancy"]
    colvalues_dossiers = ["", "", "", "Dossiers"]

    # helper functions

    def gsCellToXIndex(x1: str, x2: str):
        xx1 = 0
        xx2 = 0
        if len(x1) > 1:
            xx1 += 26 * (len(x1) - 1)
        if len(x2) > 1:
            xx2 += 26 * (len(x1) - 1)

        xx1 += ord(x1[-1]) - ord("A")
        xx2 += ord(x2[-1]) - ord("A")

        return range(xx1, xx2 + 1)

    def toDataFrame(nparr: np.array):
        nparr[0, 0] = "What"
        nparr[0, 1] = "Value"
        nparr[0, 2] = "Location"
        nparr[1, 1] = "HO"
        nparrdf = pd.DataFrame(list(nparr))
        nparrdf.columns = nparrdf.iloc[0]
        nparrdf = nparrdf.drop(nparrdf.index[0])
        for i in range(len(nparrdf.columns.values)):
            if isinstance(nparrdf.columns.values[i], numbers.Number):
                nparrdf.columns.values[i] = int(nparrdf.columns.values[i])
        return nparrdf

    def cleanDF(nparr):
        nparrdf = toDataFrame(nparr)
        nparrdf["What"] = nparrdf["What"].fillna(method="ffill")
        nparrdf["Value"] = nparrdf["Value"].fillna(method="ffill")
        nparrdf["Location"] = nparrdf["Location"].fillna(method="ffill")
        droppableIndices = []
        for i in range(len(nparrdf)):
            isDroppable = True
            for j in range(1, 10):
                isDroppable = isDroppable and np.array(nparrdf[j].isnull())[i]
            if isDroppable:
                droppableIndices.append(i + 1)
        nparrdf.drop(droppableIndices, axis=0, inplace=True)
        return nparrdf

    def fillExtraCols(df: pd.DataFrame, cols: list, colvalues: list):
        for i in range(len(cols)):
            df[f"{cols[i]}"] = colvalues[i]

    def saveFinishingCSV(finishing):

        freq = {}
        included = ["Section", "HO", "Open", "Natural", "Small", "Medium", "Big",
                    "Indented Natural", "Table", "Girdle", "Crown", "Pavilion", "Top"]
        for row in finishing:
            for ele in row:
                if ele not in included:
                    continue
                if ele in freq:
                    freq[ele] += 1
                else:
                    freq[ele] = 1
        temp = list(freq.keys())
        included.sort()
        temp.sort()
        if not (temp == included and
                (freq["Section"] == freq["HO"] == freq["Open"] == freq["Medium"] == freq["Big"] == freq[
                    "Indented Natural"] == freq["Top"] == 6) and
                (freq["Table"] == freq["Crown"] == freq["Girdle"] == 45) and
                freq["Small"] == 9 and freq["Natural"] == 12 and freq["Pavilion"] == 51):
            raise Exception("Invalid Format for Finishing Discount Sheet")

        # defining regions of interest
        roex = finishing[1:52, gsCellToXIndex("B", "M")]
        rovg = finishing[56:107, gsCellToXIndex("B", "M")]
        rog = finishing[111:162, gsCellToXIndex("B", "M")]

        faex = finishing[1:52, gsCellToXIndex("O", "Z")]
        favg = finishing[56:107, gsCellToXIndex("O", "Z")]

        dossiers = finishing[1:36, gsCellToXIndex("AB", "AM")]

        # converting the data into correct format using helper functions
        roexdf = cleanDF(roex)
        roexdf.set_index(
            pd.Index(list(i for i in range(len(roexdf)))), inplace=True)
        fillExtraCols(roexdf, cols, colvalues_roex)

        rovgdf = cleanDF(rovg)
        rovgdf.set_index(pd.Index(list(i for i in range(
            len(roexdf), 2 * len(rovgdf)))), inplace=True)
        fillExtraCols(rovgdf, cols, colvalues_rovg)

        rogdf = cleanDF(rog)
        rogdf.set_index(pd.Index(list(i for i in range(
            2 * len(rovgdf), 3 * len(rogdf)))), inplace=True)
        fillExtraCols(rogdf, cols, colvalues_rog)

        faexdf = cleanDF(faex)
        faexdf.set_index(pd.Index(list(i for i in range(
            3 * len(rogdf), 4 * len(faexdf)))), inplace=True)
        fillExtraCols(faexdf, cols, colvalues_faex)

        favgdf = cleanDF(favg)
        favgdf.set_index(pd.Index(list(i for i in range(
            4 * len(faexdf), 5 * len(favgdf)))), inplace=True)
        fillExtraCols(favgdf, cols, colvalues_favg)

        dossiersdf = cleanDF(dossiers)
        dossiersdf.set_index(pd.Index(list(i for i in range(
            5 * len(favgdf), 5 * len(favgdf) + len(dossiersdf)))), inplace=True)
        fillExtraCols(dossiersdf, cols, colvalues_dossiers)

        # combining the different dataframes
        result = pd.concat([roexdf, rovgdf, rogdf, faexdf, favgdf, dossiersdf])

        # saving as csv file
        result.to_csv("../finishing.csv", index=False)

    saveFinishingCSV(finishing)


# central_mapping()
# diameter_premium()
# size_premium()
# doss_base()
# black_csv()
# depth_csv()
# cut_csv()
# cut_1_5_base_csv()
# fancy_base_csv()
# graining_csv()
# internal_grading_csv()
# extras_csv()
# bgm_csv()
finishing_csv()