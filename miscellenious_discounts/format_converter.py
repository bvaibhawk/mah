import pandas as pd


def write_excel(filename, sheet_name, dataframe):
    with pd.ExcelWriter(filename, engine='openpyxl', mode='a') as writer:
        workBook = writer.book
        try:
            workBook.remove(workBook[sheet_name])
        except:
            print("Worksheet does not exist")
        finally:
            dataframe.to_excel(writer, sheet_name=sheet_name, index=False)
            writer.save()


def diameter_premium():
    data = pd.read_excel('input_files/input_price_module_discounts.xlsm', sheet_name='Diameter Premiums',
                         usecols=[16, 17, 18, 19, 20])
    diameter_dict = {'CUT': [], 'POLY': [], 'SYM': [], 'FLUO': [],
                     'SIZE': [], 'DIAMETER': [], 'CLARITY': [], 'DISCOUNT': []}

    print(data)

    # for i in range(2, len(data)):
    #     for j in range(1, len(data.columns)):
    #         print(data.iloc[i, j])


diameter_premium()
