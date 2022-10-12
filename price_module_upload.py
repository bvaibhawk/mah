import traceback

import streamlit as st
import dill as pickle
import pandas as pd
import cv2
import logging
import os
import datetime
import glob
import miscellenious_discounts.format_converter as conv

from Discount import calcDiscount

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S', filename='discount-tool.log', filemode='w')


def page3():
    # st.markdown(st.session_state['footer'], unsafe_allow_html=True)
    price_module_file = st.file_uploader("Choose a csv file to update price module file", type='xlsm')
    if price_module_file:
        start_conversion = st.button('Start Upload')
        if start_conversion:
            try:
                # if os.path.exists("miscellenious_discounts/input_files/pricing_module/input_price_module_discounts.xlsmbak"):
                #     os.remove("miscellenious_discounts/input_files/pricing_module/input_price_module_discounts.xlsmbak")
                # old_name = os.path.join('miscellenious_discounts/input_files/pricing_module', 'input_price_module_discounts.xlsm')
                # new_name = os.path.join('miscellenious_discounts/input_files/pricing_module', 'input_price_module_discounts.xlsmbak')
                # os.rename(old_name, new_name)
                current_datetime = datetime.datetime.now()
                final_datetime = str(current_datetime.date()) + "_" + str(current_datetime.hour) + "_" + str(
                    current_datetime.minute) + "_" + str(current_datetime.second)
                total_files = glob.glob("miscellenious_discounts/input_files/input_price_module_discounts_*.xlsx")
                st.session_state['final_datetime'] = final_datetime

                total_files = sorted(total_files)

                if len(total_files) == 5:
                    # st.text(total_files[0])
                    # st.text(f"removing {total_files[0]}")
                    os.remove(total_files[0])
                    del total_files[0]

                with open(os.path.join('miscellenious_discounts/input_files', f'input_price_module_discounts_{final_datetime}.xlsx'), "wb") as f:
                    f.write(price_module_file.getbuffer())
                with open(os.path.join('miscellenious_discounts/input_files', f'input_price_module_discounts.xlsm'), "wb") as f:
                    f.write(price_module_file.getbuffer())
                conv.central_mapping(final_datetime)
                conv.diameter_premium(final_datetime)
                conv.size_premium(final_datetime)
                conv.doss_base(final_datetime)
                conv.black_csv(final_datetime)
                conv.depth_csv(final_datetime)
                conv.cut_csv(final_datetime)
                conv.cut_1_5_base_csv(final_datetime)
                conv.fancy_base_csv(final_datetime)
                conv.graining_csv(final_datetime)
                conv.internal_grading_csv(final_datetime)
                conv.extras_csv(final_datetime)
                conv.bgm_csv(final_datetime)
                conv.finishing_csv(final_datetime)
                conv.ktos_csv(final_datetime)
                conv.mncolor_csv(final_datetime)
                conv.days_csv(final_datetime)
                conv.very_strong_fluo(final_datetime)
                conv.params_fancy(final_datetime)
                conv.polish_sym_csv(final_datetime)
                conv.fl_premium_csv(final_datetime)
                conv.polish_sym_csv_one_cut_up(final_datetime)
                st.write('Successfully uploaded and updated')
            except BaseException as e:
                # if os.path.exists("miscellenious_discounts/input_files/pricing_module/input_price_module_discounts.xlsm"):
                #     os.remove("miscellenious_discounts/input_files/pricing_module/input_price_module_discounts.xlsm")
                # old_name = os.path.join('miscellenious_discounts/input_files/pricing_module', 'input_price_module_discounts.xlsmbak')
                # new_name = os.path.join('miscellenious_discounts/input_files/pricing_module', 'input_price_module_discounts.xlsm')
                # os.rename(old_name, new_name)
                logging.error(traceback.format_exc())
                st.write('Error :: ' + str(e))
