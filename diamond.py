

import streamlit as st 
import dill as pickle
import pandas as pd
import cv2

st.set_page_config(page_title="Discount Calculator", page_icon='💎', layout="wide", initial_sidebar_state="collapsed", menu_items=None)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

footer="""<style>
a:link , a:visited{
color: #006DCC;
background-color: transparent;
text-decoration: underline;
font-weight: bold;
}

a:link , a:unvisited{
color: #006DCC;
background-color: transparent;
text-decoration: underline;
font-weight: bold;
}

a:hover,  a:active {
color: #2E8BC0;
background-color: transparent;
text-decoration: underline;
font-weight: bold;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
padding-top: 15px;
width: 100%;
background-color: #d4af37;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Powered by <a href = 'https://www.ripik.ai' target='_blank'>Ripik.ai</a></p>
</div>
"""



logo = cv2.imread("logo.png")
logo = cv2.cvtColor(logo, cv2.COLOR_BGR2RGB)
logo = cv2.resize(logo, (300,100))
st.image(logo)
st.text("\n")

def page1():

    with open('diamond.pkl', 'rb') as handle:
        model = pickle.load(handle)

    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)
    col11, col12, col13, col14, col15 = st.columns(5)
    col16, col17, col18, col19, col20 = st.columns(5)
    col21, col22, col23, col24, col25 = st.columns(5)
    col26, col27, col28, col29, col30 = st.columns(5)
    col31, col32, col33, col34, col35 = st.columns(5)

    color_dict = {"D":10,"E":9,"F":8,"G":7,"H":6,"I":5,"J":4,"K":3,"L":2,"M":1}
    clarity_dict = {"IF":8,"VVS1":7,"VVS2":6,"VS1":5,"VS2":4,"SI1":3,"SI2":2,"I1":1}
    fluo_dict = {"FNT":1,"MED":2,"NON":3,"SIG":4,"VST":5}

    with col1:
        szgr = st.selectbox("SZ GR",options=['0.30-0.34', '0.35-0.39', '0.40-0.44', '0.45-0.49', '0.50-0.59',
        '0.60-0.69', '0.70-0.74', '0.75-0.79', '0.80-0.89', '0.90-0.94',
        '1.00-1.19', '1.20-1.29', '1.30-1.39', '1.40-1.49', '1.50-1.69',
        '1.70-1.79', '1.80-1.89', '1.90-1.99', '2.00-2.19', '2.50-2.69',
        '2.70-2.79'])

    with col2:
        certct = st.number_input("CERTCT")

    with col3:
        color = st.selectbox("Color",options=list(color_dict.keys()))

    with col4:
        clarity = st.selectbox("Clarity",options=list(clarity_dict.keys()))

    with col5:
        cut = st.number_input("Cut")

    with col6:
        polish = st.number_input("Polish")

    with col7:
        symmetry = st.number_input("Symmetry")

    with col8:
        cert = st.selectbox("CERT",options=['GIA', 'FACT', 'FM', 'IIDGR'])

    with col9:
        rap = st.number_input("RAP")

    with col10:
        pur_rap_dis = st.number_input("PCS")
    with col11:
        ha = st.selectbox("HA",options=['YES', 'NO']) 
    with col12:
        td = st.number_input("TD")   
    with col13:
        tabl = st.number_input("TABL")
    with col14:
        mindiam = st.number_input("MIN_DIAM")
    with col15:
        maxdiam = st.number_input("MAX_DIAM")
    with col16:
        height = st.number_input("HEIGHT")
    with col17:
        ratio = st.number_input("RATIO")
    with col18:
        colshad = st.selectbox("COL_SHADE",options=['B1', 'B2', 'MT1', 'NN'])
    with col19:
        milky = st.selectbox("MILKY",options=['M1', 'M2', 'M1+', 'NN'])  
    with col20:
        tableblack = st.selectbox("TABLE_BLACK",options=['BT1', 'BT1+', 'BT2', 'NN'])
    with col21:
        sideblack= st.selectbox("SIDE_BLACK",options=['BC1', 'BC1+', 'BC2', 'BC3','NN'])  
    with col22:
        whiteinc = st.selectbox("WHT_INC",options=['NN', 'WC1', 'WC2', 'WC3','WP1','WP2','WT1','WT2','WT3'])  
    with col23:
        crangle = st.number_input("CR_ANGLE")
    with col24:
        crheight = st.number_input("CR_HEIGHT")
    with col25:
        pvangle = st.number_input("PV_ANGLE") 
    with col26:
        pvdepth = st.number_input("PV_DEPTH")
    with col27:
        girdleper = st.number_input("GIRDLE_PERCENTAGE")
    with col28:
        girdlecondi = st.selectbox("GIRDLE_CONDITION",options=['Faceted', 'Polished'])
    with col29:
        starlength = st.number_input("STAR_LENGTH")
    with col30:
        lowerhalf = st.number_input("LOWER_HALF")
    with col31:
         cavity= st.selectbox("CAVITY",options=['CTC', 'CTG','CTP','NN'])    
    with col32:
        culet = st.selectbox("CULET",options=['NON', 'PTD', 'VSM'])
    with col33:
        eyeclean = st.selectbox("EYE_CLEAN",options=['YES', 'NO'])
    with col34:
        tableclean = st.selectbox("TABLE_CLEAN",options=['YES', 'NO'])   
    with col35:
        fluo = st.number_input("FLUO")                                          

    test_df = pd.DataFrame({'SZ GR':[szgr], 'CERTCT':[certct], 'COLOR':[color_dict[color]], 'CLARITY':[clarity_dict[clarity]], 'CUT':[cut],
                            'POLISH':[polish], 'SYMMETRY':[symmetry], 'FLUO':[fluo], 'rap':[rap], 'PUR RAP DIS':[pur_rap_dis]})

    result = model.predict(test_df)[0]
    st.text("\n")

    if st.button("Calculate Discount"):
        if int(rap)!=0:
            st.markdown(f"<big><b>Discount(in Percentage wrt RAP):</b> </big><font color='green' size=6>{int(result)}% </font>",unsafe_allow_html=True)
        else:
            st.error("Please input proper values")




page_names = {
    "Newest sheet": page1
 
}

st.sidebar.markdown("<h1>Discount Calculator</h1>",unsafe_allow_html=True)
selected_page = st.sidebar.selectbox("Select Calculator", page_names.keys())
page_names[selected_page]()

st.markdown(footer,unsafe_allow_html=True)