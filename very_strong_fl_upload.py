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


def page5():
    price_module_file = st.file_uploader("Choose a csv file to update Very Strong Fluo Discount file", type='xlsx')
    if price_module_file:
        start_conversion = st.button('Start Upload')
        if start_conversion:
            try:
                if os.path.exists("miscellenious_discounts/input_files/ver_strong_fl.xlsxbak"):
                    os.remove("miscellenious_discounts/input_files/ver_strong_fl.xlsxbak")
                old_name = os.path.join('miscellenious_discounts/input_files', 'ver_strong_fl.xlsx')
                new_name = os.path.join('miscellenious_discounts/input_files', 'ver_strong_fl.xlsxbak')
                os.rename(old_name, new_name)
                with open(os.path.join('miscellenious_discounts/input_files', 'ver_strong_fl.xlsx'), "wb") as f:
                    f.write(price_module_file.getbuffer())
                conv.very_strong_fluo()
                st.write('Successfully uploaded and updated')
            except BaseException as e:
                if os.path.exists("miscellenious_discounts/input_files/ver_strong_fl.xlsx"):
                    os.remove("miscellenious_discounts/input_files/ver_strong_fl.xlsx")
                old_name = os.path.join('miscellenious_discounts/input_files', 'ver_strong_fl.xlsxbak')
                new_name = os.path.join('miscellenious_discounts/input_files', 'ver_strong_fl.xlsx')
                os.rename(old_name, new_name)
                logging.error(traceback.format_exc())
                st.write('Error :: ' + str(e))