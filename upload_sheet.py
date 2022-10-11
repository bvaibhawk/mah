import streamlit as st
import datetime
import pandas as pd
from pathlib import Path
from openpyxl import load_workbook
import glob
import os


def page8():

    current_datetime = datetime.datetime.now()
    final_datetime = str(current_datetime.date())+"_"+str(current_datetime.hour)+"_"+str(current_datetime.minute)+"_"+str(current_datetime.second)
    # file_name = f'miscellenious_discounts/input_files/main_sheet_{final_datetime}.xlsx'
    total_files = glob.glob(f"miscellenious_discounts/input_files/individual_uploads/*.xls"+"*")

    price_module_list = glob.glob(f'miscellenious_discounts/input_files/pricing_module/*.xlsx')

    # my_file = Path(file_name)
    # if my_file.is_file()==False:
    

    # total_files = sorted(total_files)
    total_files.sort(key = lambda x: x.split("@")[-1])

    if len(total_files)==5:
        # st.text(total_files[0])
        # st.text(f"removing {total_files[0]}")
        os.remove(total_files[0])
        del total_files[0]


    sheet_list = ['Upload New Sheet','Parameters', 'Central', 'Parameters Fancy', '1.01-1.09', '1.50-1.69', '2.01-2.09', 'Parameters Dossiers', 'Prices Below 30Pts', 'PriceSheet -1Ct Uncertified', 'Mixing Groups -1Ct Uncertified', '3.01-3.09', '4.01-4.09', '5.01-5.09', 'Fancy Shapes', 'Size Premiums', 'Diameter Premiums', 'Depth', 'KtoS Premiums', 'Discounts N Colors', 'RapNet', '+1Ct SI3- Loose', '0.30-0.34', '0.35-0.39', '0.40-0.44', '0.45-0.49', '0.50-0.59', '0.60-0.69', '0.70-0.74', '0.75-0.79', '0.80-0.89', '0.90-0.94', '0.95-0.99', 'Black', 'BGM', 'Cut & MFG Rules', 'Cut', 'Inclusion Grading', 'Finishing', 'Internal Grading', 'Graining', 'Extras', 'Certificate Costs']

    st.subheader("Upload Sheet")

    st.markdown(st.session_state['footer'], unsafe_allow_html=True)

    selected_sheet = st.selectbox("Select Sheet to upload",options=sheet_list)
    if selected_sheet=='Upload New Sheet':
        new_sheet_name = st.text_input("Enter name for new sheet")
        new_sheet = st.file_uploader("Upload New Excel Sheet",type=['xlsx','xls'])
        
        if st.button("Start Upload"):
            with st.spinner("Uploading..."):
                if new_sheet is not None:
                    new_df = pd.read_excel(new_sheet)

                    new_sheet_name_final = f'miscellenious_discounts/input_files/individual_uploads/{new_sheet_name}@{final_datetime}.xlsx'
                    df = pd.DataFrame() 
                    df.to_excel(new_sheet_name_final,sheet_name=new_sheet_name_final,index=False)

                    with pd.ExcelWriter(new_sheet_name_final, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
                        new_df.to_excel(writer, sheet_name=new_sheet_name, index=False)

            st.info(f"{new_sheet_name} Sheet uploaded succesfully!")

    else:
        new_sheet = st.file_uploader(f"Upload {selected_sheet} Sheet",type=['xlsx','xlsm','xls'])

        if st.button("Start Upload"):
            with st.spinner("Uploading..."):
                if new_sheet is not None:
                    new_df = pd.read_excel(new_sheet)

                    selected_sheet_final = f'miscellenious_discounts/input_files/individual_uploads/{selected_sheet}@{final_datetime}.xlsx'

                    df = pd.DataFrame() 
                    df.to_excel(selected_sheet_final,sheet_name=selected_sheet,index=False)

                    with pd.ExcelWriter(selected_sheet_final, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
                        new_df.to_excel(writer, sheet_name=selected_sheet, index=False)

                    with pd.ExcelWriter(price_module_list[-1], engine="openpyxl", mode="a", if_sheet_exists="replace") as writer2:
                        new_df.to_excel(writer2, sheet_name=selected_sheet, index=False)



            st.info(f"{selected_sheet} Sheet uploaded succesfully!")

    




