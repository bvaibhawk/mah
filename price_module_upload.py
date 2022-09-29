import traceback

import streamlit as st
import dill as pickle
import pandas as pd
import cv2
import logging
import os
import miscellenious_discounts.format_converter as conv

from Discount import calcDiscount

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S', filename='discount-tool.log', filemode='w')


def page3():
    price_module_file = st.file_uploader("Choose a csv file to update price module file", type='xlsm')
    if price_module_file:
        start_conversion = st.button('Start Upload')
        if start_conversion:
            try:
                if os.path.exists("miscellenious_discounts/input_files/input_price_module_discounts.xlsmbak"):
                    os.remove("miscellenious_discounts/input_files/input_price_module_discounts.xlsmbak")
                old_name = os.path.join('miscellenious_discounts/input_files', 'input_price_module_discounts.xlsm')
                new_name = os.path.join('miscellenious_discounts/input_files', 'input_price_module_discounts.xlsmbak')
                os.rename(old_name, new_name)
                with open(os.path.join('miscellenious_discounts/input_files', 'input_price_module_discounts.xlsm'), "wb") as f:
                    f.write(price_module_file.getbuffer())
                conv.central_mapping()
                conv.diameter_premium()
                conv.size_premium()
                conv.doss_base()
                conv.black_csv()
                conv.depth_csv()
                conv.cut_csv()
                conv.cut_1_5_base_csv()
                conv.fancy_base_csv()
                conv.graining_csv()
                conv.internal_grading_csv()
                conv.extras_csv()
                conv.bgm_csv()
                conv.finishing_csv()
                conv.ktos_csv()
                conv.mncolor_csv()
                conv.days_csv()
                conv.very_strong_fluo()
                conv.params_fancy()
                conv.polish_sym_csv()
                conv.fl_premium_csv()
                conv.polish_sym_csv_one_cut_up()
                st.write('Successfully uploaded and updated')
            except BaseException as e:
                if os.path.exists("miscellenious_discounts/input_files/input_price_module_discounts.xlsm"):
                    os.remove("miscellenious_discounts/input_files/input_price_module_discounts.xlsm")
                old_name = os.path.join('miscellenious_discounts/input_files', 'input_price_module_discounts.xlsmbak')
                new_name = os.path.join('miscellenious_discounts/input_files', 'input_price_module_discounts.xlsm')
                os.rename(old_name, new_name)
                logging.error(traceback.format_exc())
                st.write('Error :: ' + str(e))
