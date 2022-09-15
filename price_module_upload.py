import streamlit as st
import dill as pickle
import pandas as pd
import cv2

from Discount import calcDiscount


def page3():
    price_module_file = st.file_uploader("Choose a csv file to update price module file", type='xlsm')