

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
    col36, col37, col38, col49, col40 = st.columns(5)

    # color_dict = {"D":10,"E":9,"F":8,"G":7,"H":6,"I":5,"J":4,"K":3,"L":2,"M":1}
    # clarity_dict = {"IF":8,"VVS1":7,"VVS2":6,"VS1":5,"VS2":4,"SI1":3,"SI2":2,"I1":1}
    # fluo_dict = {"FNT":1,"MED":2,"NON":3,"SIG":4,"VST":5}

    with col1:
        szgr= st.selectbox("SIZE RANGE",options=['1.01-1.09','1.50-1.69','2.01-2.09','3.01-3.09','4.01-4.09','5.01-5.09'])

    with col2:
        sizeprec = st.number_input("PRECISE SIZE")

    with col3:
        color = st.selectbox("COLOUR",options=['D', 'E', 'F','G','H','I','J','K','L','M'])

    with col4:
        clarity = st.selectbox("CLARITY",options=['IF', 'VVS1', 'VVS2','VS1','VS2','S1','S2','I1'])

    with col5:
        cut = st.selectbox("CUT",options=['EX', 'GD', 'VG'])

    with col6:
        polish =st.selectbox("POLISH",options=['EX', 'GD', 'VG'])

    with col7:
        symmetry = st.selectbox("SYMMETRY",options=['EX', 'GD', 'VG'])

    with col8:
        cert = st.selectbox("CERT",options=['GIA', 'FACT', 'FM', 'IIDGR'])

    with col9:
        rap = st.number_input("RAP")

    with col10:
        ktos = st.number_input("KTOS")
    with col11:
        shape = st.selectbox("SHAPE",options=['RO', 'CS','EM','HT','MAO','PR','PRINCESS','OV']) 
    with col12:
        td = st.number_input("TD")   
    with col13:
        tabl = st.number_input("TABL")
    with col14:
        mindiam = st.number_input("MIN_DIAM")
    with col15:
        maxdiam = st.number_input("MAX_DIAM")
    with col16:
        diameter = st.number_input("DIAMETER")
    with col17:
        ratio = st.number_input("RATIO")
    with col18:
        colshad = st.selectbox("COL_SHADE",options=['B1', 'B2', 'MT1', 'NN'])
    with col19:
        pavilionintensity = st.selectbox("PAVILION_INTENSITY",options=['0', '1', '2', '3','4'])  
    with col20:
        tableintensity = st.selectbox("TABLE_INTENSITY",options=['0', '1', '2', '3','4'])
    with col21:
       crownintensity= st.selectbox("CROWN_INTENSITY",options=['0', '1', '2', '3','4'])
    with col22:
        girdleintensity = st.selectbox("GIRDLE_INTENSITY",options=['0', '1', '2', '3','4'])
    with col23:
        girdle_inc = st.selectbox("GIRDLE_INCLUSION",options=['PP1', 'PP2', 'F1', 'F2','F3','F4','TW1','TW2','TW3','N1','N2','N3','N4','C1','C2','C3','CO1','CO2','CO3','CL1','CL2','CL3','None']) 
    with col24:
        tableinc = st.selectbox("TABLE_INCLUSION",options=['PP1', 'PP2', 'F1', 'F2','F3','F4','TW1','TW2','TW3','N1','N2','N3','N4','C1','C2','C3','CO1','CO2','CO3','CL1','CL2','CL3','None']) 
    with col25:
        crowninc= st.selectbox("CROWN_INCLUSION",options=['PP1', 'PP2', 'F1', 'F2','F3','F4','TW1','TW2','TW3','N1','N2','N3','N4','C1','C2','C3','CO1','CO2','CO3','CL1','CL2','CL3','None'])  
    with col26:
        pavilioninc = st.selectbox("PAVILION_INCLUSION",options=['PP1', 'PP2', 'F1', 'F2','F3','F4','TW1','TW2','TW3','N1','N2','N3','N4','C1','C2','C3','CO1','CO2','CO3','CL1','CL2','CL3','None']) 
    with col27:
        girdleper = st.number_input("GIRDLE_PERCENTAGE")
    with col28:
        girdlecondi = st.selectbox("GIRDLE_CONDITION",options=['Faceted', 'Polished'])
    with col29:
        starlength = st.number_input("STAR_LENGTH")
    with col30:
        cutcomments = st.selectbox("CUT_COMMENTS",options=['3EX->EX1','3EX->EX2','EX->EX1','EX->EX2','VG->VG1','VG->VG2','G->GD1','G->GD2','Fancy->Ideal','Fancy->Premium','Fancy->Very Good'])
    with col31:
         cavity= st.selectbox("CAVITY",options=['CTC', 'CTG','CTP','NN'])    
    with col32:
        graining = st.selectbox("GRAINING",options=['Internal->None', 'Internal->GR1', 'Internal->GR2','Internal->GR3','Surface->None','Surface->SGR1','Surface->SGR2'])
    with col33:
        extras = st.selectbox("EXTRAS",options=['YES', 'NO'])
    with col34:
        bgm = st.selectbox("BGM",options=['B1', 'B2','B3','B4','G1','G2','G3','G4','GR1','GR2','GR3','GR4','M1','M2','M3','M4','OC1','OC2'])   
    with col35:
        fluo = st.selectbox("FLUO",options=['Faint', 'Medium','None','Strong','Very Strong'])    
    with col36:
        ha = st.selectbox("H&A",options=['H&A A+', '100%','90%','No'])
    with col37:
        eyeclean = st.selectbox("EYE_CLEAN",options=['100%','90%','No'])    
    with col37:
        tableclean = st.selectbox("TABLE_CLEAN",options=['100%','90%','No'])


    #test_df = pd.DataFrame({'SZ GR':[szgr], 'CERTCT':[certct], 'COLOR':[color_dict[color]], 'CLARITY':[clarity_dict[clarity]], 'CUT':[cut],
     #                       'POLISH':[polish], 'SYMMETRY':[symmetry], 'FLUO':[fluo], 'rap':[rap], 'PUR RAP DIS':[pur_rap_dis]})

    #result = (-1*(1-((model.predict(test_df)[0])/rap)))*100
    df = pd.read_csv('Toamin.csv')
    result = 0.00
    ff=0
    xx=0
    if (clarity=='IF' or clarity=='VVS1' or clarity=='VVS2'):
        if color=='D' or color=='E' or color=='F': 
            xx=1
        if color=='G' or color=='H' or color=='I': 
            xx=2
        if color=='J' or color=='K' or color=='L' or color=='M': 
            xx=3    
    if (clarity=='VS1' or clarity=='VS2'):
        if color=='D' or color=='E' or color=='F': 
            xx=4
        if color=='G' or color=='H' or color=='I': 
            xx=5
        if color=='J' or color=='K' or color=='L' or color=='M': 
            xx=6
    if (clarity=='SI1' or clarity=='SI2' or clarity=='I1'):
        if color=='D' or color=='E' or color=='F': 
            xx=7
        if color=='G' or color=='H' or color=='I': 
            xx=8
        if color=='J' or color=='K' or color=='L' or color=='M': 
            xx=9 
    for i in range(len(df)):
        if shape == df['Shape'][i] and color == df['COLOR'][i] and clarity == df['CLARITY'][i] and cut == df['CUT'][i] and polish == df['POL'][i] and symmetry == df['SYM'][i] and fluo == df['FLUO'][i] and szgr == df['Size'][i] : 
            result=df['Discount'][i]
            ff=1
            break
    if ff==1:
        result=result*100 
        
               
        if shape=='RO':
            if xx==1:
                if ktos==1:
                    result=result+1.0
                elif ktos>=5:
                    result=-1.0+result  
            elif xx==2:
                if ktos==1:
                    result=result+1.0
                elif ktos>=5:
                    result=-1.0+result 
            elif xx==3:
                if ktos==1:
                    result=result+1.0
                elif ktos>=5:
                    result=-1.0+result
            elif xx==4:
                if ktos==1:
                    result=result+1.5
                elif ktos>=5:
                    result=-1.0+result         
            elif xx==5:
                if ktos==1:
                    result=result+1.5
                if ktos>=5:
                    result=-1.0+result 
            elif xx==6:
                if ktos==1:
                    result=result+1.0
                if ktos>=5:
                    result=0.0+result 
            elif xx==1:
                if ktos==1:
                    result=result+3.0
                if ktos>=5:
                    result=0.0+result 


            #colour
            if color=='M':
                if szgr=='1.01-1.09' or szgr=='2.01-2.09' or szgr=='1.50-1.69': 
                    if cut=='EX':
                        result=-7+result


            # if szgr=='1.01-1.09' or szgr=='1.50-1.69' or szgr=='2.01-2.09':
            #     if cut=='VG':
    else:
        df2 = pd.read_csv('toaminfancy.csv')
        result = 0.00
        
        for i in range(len(df2)):
            if clarity=='IF':
                if shape == df2['Shape'][i] and color == df2['EX'][i] and cut == 'EX' and szgr == df2['Size'][i] : 
                    result=df2['IF'][i]
                    ff=2
                    break
            elif clarity=='VVS1':
                if shape == df2['Shape'][i] and color == df2['EX'][i] and cut == 'EX' and szgr == df2['Size'][i] : 
                    result=df2['VVS1'][i]
                    ff=2
                    break        
            elif clarity=='VVS2':
                if shape == df2['Shape'][i] and color == df2['EX'][i] and cut == 'EX' and szgr == df2['Size'][i] : 
                    result=df2['VVS2'][i]
                    ff=2
                    break        
            elif clarity=='VS1':
                if shape == df2['Shape'][i] and color == df2['EX'][i] and cut == 'EX' and szgr == df2['Size'][i] : 
                    result=df2['VS1'][i]
                    ff=2
                    break    
            elif clarity=='VS2':
                if shape == df2['Shape'][i] and color == df2['EX'][i] and cut == 'EX' and szgr == df2['Size'][i] : 
                    result=df2['VS2'][i]
                    ff=2
                    break    
            elif clarity=='SI1':
                if shape == df2['Shape'][i] and color == df2['EX'][i] and cut == 'EX' and szgr == df2['Size'][i] : 
                    result=df2['SI1'][i]
                    ff=2
                    break    
            elif clarity=='SI2':
                if shape == df2['Shape'][i] and color == df2['EX'][i] and cut == 'EX' and szgr == df2['Size'][i] : 
                    result=df2['SI2'][i]
                    ff=2
                    break    


    #DIAMETER                
    if(shape=='RO'):
        if sizeprec>=1.0 and sizeprec<=1.49:
            if cut=='VG':
                if(xx==1):
                    if diameter<=6.2:
                        result=result-0.5
                    elif diameter>=6.3:
                        result=result+1.5
                elif(xx==2):
                    if diameter<=6.2:
                        result=result-0.5
                    elif diameter>=6.3:
                        result=result+1.5        
                elif(xx==3 or xx==4):
                    if diameter<=6.2:
                        result=result-0.5
                    elif diameter>=6.3:
                        result=result+1.5        
                elif(xx==5):
                    if diameter<=6.2:
                        result=result-0.1
                    elif diameter>=6.3:
                        result=result+1.5
                elif(xx==6):
                    if diameter<=6.2:
                        result=result-0.5
                    elif diameter>=6.3:
                        result=result+1.5
                elif(xx==7):
                    if diameter<=6.2:
                        result=result-0.0
                    elif diameter>=6.3:
                        result=result+1.0
                elif(xx==8):
                    if diameter<=6.2:
                        result=result-0.0
                    elif diameter>=6.3:
                        result=result+1.0                                
    #add dossiers

    #bgm- Note- need to ask whether it is one exculsive table or multiple table combined- currently considered one exclusive table
    if (cut=='EX' or cut=='VG') and (fluo=='None' or fluo=='MED') :
        df3=pd.read_csv('bgmvg.csv')
        for i in range(len(df3)):
            if shape == 'RO' and xx == df3['Section'][i] and bgm == df3['bgm'][i] and df3['Shape']=='RO': 
                result=result+df3['Discount'][i]
                break
            elif shape!='RO' and xx == df3['Section'][i] and bgm == df3['bgm'][i] and df3['Shape']=='FANCY':
                result=result+df3['Discount'][i]
                break
    else:
        df3=pd.read_csv('bgmroelse.csv')
        for i in range(len(df3)):
            if shape == 'RO' and xx == df3['Section'][i] and bgm == df3['bgm'][i]: 
                result=result+df3['Discount'][i]    
                break            
    #add dossiers as well


    #Cut
    if ((fluo=='MED') and (cutcomments=='VG->VG2' or cutcomments=='G->GD2')) or shape!='RO':
        result=result
    else:
        if cutcomments=='3EX->EX2':
            if(xx==1):
                result=result-2.0	
            elif(xx==2):
                result=result-2.0	
            elif(xx==3):
                result=result-1.0
            elif(xx==4):
                result=result-2.0	
            elif(xx==5):    
                result=result-2.0	
            elif(xx==6):    
                result=result-1.0	
            elif(xx==7):    
                result=result-1.0	
            elif(xx==8):    
                result=result-1.0	
            elif(xx==9):    
                result=result-0.5
    
        if cutcomments=='EX->EX2':
            if(xx==1):
                result=result-2.0	
            elif(xx==2):
                result=result-2.0	
            elif(xx==3):
                result=result-1.0
            elif(xx==4):
                result=result-2.0	
            elif(xx==5):    
                result=result-2.0	
            elif(xx==6):    
                result=result-1.0	
            elif(xx==7):    
                result=result-1.5	
            elif(xx==8):    
                result=result-1.5	
            elif(xx==9):    
                result=result-0.5        
        if cutcomments=='VG->VG1':
            if(xx==1):
                result=result+2.0	
            elif(xx==2):
                result=result+2.0	
            elif(xx==3):
                result=result+2.0
            elif(xx==4):
                result=result+2.0	
            elif(xx==5):    
                result=result+2.0	
            elif(xx==6):    
                result=result+1.5	
            elif(xx==7):    
                result=result+1.5	
            elif(xx==8):    
                result=result+1.0	
            elif(xx==9):    
                result=result+1.0


    #Graining- add vg+ condition and the extra comment
    if graining=='Internal->GR2':
        if xx==1 or xx==2:
            result=result-1.5
        elif xx==3 or xx==4 or xx==5:
            result=result-1.0
        elif xx==6:
            result=result-0.5
    elif graining =='Internal->GR3':
        if xx==1 or xx==2:
            result=result-3.0
        elif xx==3 or xx==4 or xx==5:
            result=result-3.0
        elif xx==6:
            result=result-1.0
    elif graining=='Surface->SGR2':
        if xx ==1 or xx==2:
            result=result-1.5
        elif xx==3 or xx==5 or xx==6:
            result=result-1


    #extras- NOT properly written- change line 445
    df4=pd.read_csv('extras.csv')
    for i in range(len(df4)):
        if(shape=='RO'):
            if(df4['extras'][i]=='H&A' and df4['shape'][i]=='RO'):
                if(df4['value'][i]==ha):
                    if xx==1:
                        result=result+df4['1'][i] 
                    if xx==2:
                        result=result+df4['2'][i]    
                    if xx==3:
                        result=result+df4['3'][i]
                    if xx==4:
                        result=result+df4['4'][i]    
                    if xx==5:
                        result=result+df4['5'][i]
                    if xx==6:
                        result=result+df4['6'][i]
                    if xx==7:
                        result=result+df4['7'][i]
                    if xx==8:
                        result=result+df4['8'][i] 
                    if xx==9:
                        result=result+df4['9'][i]

                if(df4['value'][i]==eyeclean):
                    if xx==1:
                        result=result+df4['1'][i] 
                    elif xx==2:
                        result=result+df4['2'][i]    
                    elif xx==3:
                        result=result+df4['3'][i]
                    elif xx==4:
                        result=result+df4['4'][i]    
                    elif xx==5:
                        result=result+df4['5'][i]
                    elif xx==6:
                        result=result+df4['6'][i]
                    elif xx==7:
                        result=result+df4['7'][i]
                    elif xx==8:
                        result=result+df4['8'][i] 
                    elif xx==9:
                        result=result+df4['9'][i]  

                if(df4['value'][i]==tableclean):
                    if xx==1:
                        result=result+df4['1'][i] 
                    elif xx==2:
                        result=result+df4['2'][i]    
                    elif xx==3:
                        result=result+df4['3'][i]
                    elif xx==4:
                        result=result+df4['4'][i]    
                    elif xx==5:
                        result=result+df4['5'][i]
                    elif xx==6:
                        result=result+df4['6'][i]
                    elif xx==7:
                        result=result+df4['7'][i]
                    elif xx==8:
                        result=result+df4['8'][i] 
                    elif xx==9:
                        result=result+df4['9'][i]          

        if(shape!='RO'):
            if(df4['extras[i]']=='H&A' and df4['shape'][i]=='Fancy'):
                if(df4['value'][i]==ha):
                    if xx==1:
                        result=result+df4['1'][i] 
                    if xx==2:
                        result=result+df4['2'][i]    
                    if xx==3:
                        result=result+df4['3'][i]
                    if xx==4:
                        result=result+df4['4'][i]    
                    if xx==5:
                        result=result+df4['5'][i]
                    if xx==6:
                        result=result+df4['6'][i]
                    if xx==7:
                        result=result+df4['7'][i]
                    if xx==8:
                        result=result+df4['8'][i] 
                    if xx==9:
                        result=result+df4['9'][i]

                if(df4['value'][i]==eyeclean):
                    if xx==1:
                        result=result+df4['1'][i] 
                    if xx==2:
                        result=result+df4['2'][i]    
                    if xx==3:
                        result=result+df4['3'][i]
                    if xx==4:
                        result=result+df4['4'][i]    
                    if xx==5:
                        result=result+df4['5'][i]
                    if xx==6:
                        result=result+df4['6'][i]
                    if xx==7:
                        result=result+df4['7'][i]
                    if xx==8:
                        result=result+df4['8'][i] 
                    if xx==9:
                        result=result+df4['9'][i]  

                if(df4['value'][i]==tableclean):
                    if xx==1:
                        result=result+df4['1'][i] 
                    if xx==2:
                        result=result+df4['2'][i]    
                    if xx==3:
                        result=result+df4['3'][i]
                    if xx==4:
                        result=result+df4['4'][i]    
                    if xx==5:
                        result=result+df4['5'][i]
                    if xx==6:
                        result=result+df4['6'][i]
                    if xx==7:
                        result=result+df4['7'][i]
                    if xx==8:
                        result=result+df4['8'][i] 
                    if xx==9:
                        result=result+df4['9'][i]          
                



    #Inclusion Grading
    df5=pd.read_csv('inc_grad.csv')
    for i in range(len(df5)):
        #table
        if(df5['Location'][i]=='Table'):
            if(df5['Shape'][i]==shape and (clarity==df5['CL1'][i] or clarity==df5['CL2'][i]) and df5['Inclusion'][i]==tableinc):
                if xx==1:
                    result=result+df5['1'][i] 
                if xx==2:
                    result=result+df5['2'][i]    
                if xx==3:
                    result=result+df5['3'][i]
                if xx==4:
                    result=result+df5['4'][i]    
                if xx==5:
                    result=result+df5['5'][i]
                if xx==6:
                    result=result+df5['6'][i]
                if xx==7:
                    result=result+df5['7'][i]
                if xx==8:
                    result=result+df5['8'][i] 
                if xx==9:
                    result=result+df5['9'][i]
                break
    for i in range(len(df5)):
        #crown
        if(df5['Location'][i]=='Crown'):
            if(df5['Shape'][i]==shape and (clarity==df5['CL1'][i] or clarity==df5['CL2'][i]) and df5['Inclusion'][i]==crowninc):
                if xx==1:
                    result=result+df5['1'][i] 
                if xx==2:
                    result=result+df5['2'][i]    
                if xx==3:
                    result=result+df5['3'][i]
                if xx==4:
                    result=result+df5['4'][i]    
                if xx==5:
                    result=result+df5['5'][i]
                if xx==6:
                    result=result+df5['6'][i]
                if xx==7:
                    result=result+df5['7'][i]
                if xx==8:
                    result=result+df5['8'][i] 
                if xx==9:
                    result=result+df5['9'][i]
                break        
    for i in range(len(df5)):    
        #girdle
        if(df5['Location'][i]=='Girdle'):
            if(df5['Shape'][i]==shape and (clarity==df5['CL1'][i] or clarity==df5['CL2'][i]) and df5['Inclusion'][i]==girdle_inc):
                if xx==1:
                    result=result+df5['1'][i] 
                if xx==2:
                    result=result+df5['2'][i]    
                if xx==3:
                    result=result+df5['3'][i]
                if xx==4:
                    result=result+df5['4'][i]    
                if xx==5:
                    result=result+df5['5'][i]
                if xx==6:
                    result=result+df5['6'][i]
                if xx==7:
                    result=result+df5['7'][i]
                if xx==8:
                    result=result+df5['8'][i] 
                if xx==9:
                    result=result+df5['9'][i]
                break
    for i in range(len(df5)):    
        #pavilion
        if(df5['Location'][i]=='Pavilion'):
            if(df5['Shape'][i]==shape and (clarity==df5['CL1'][i] or clarity==df5['CL2'][i]) and df5['Inclusion'][i]==pavilioninc):
                if xx==1:
                    result=result+df5['1'][i] 
                if xx==2:
                    result=result+df5['2'][i]    
                if xx==3:
                    result=result+df5['3'][i]
                if xx==4:
                    result=result+df5['4'][i]    
                if xx==5:
                    result=result+df5['5'][i]
                if xx==6:
                    result=result+df5['6'][i]
                if xx==7:
                    result=result+df5['7'][i]
                if xx==8:
                    result=result+df5['8'][i] 
                if xx==9:
                    result=result+df5['9'][i]
                break

    #BLACK
    df6=pd.read_csv('black.csv')
    for i in range(len(df6)):
        #table
        if(df6['Location'][i]=='Table'):
            if(df6['Shape'][i]==shape and shape=='RO'): 
                if(size>=df6['sizemin'][i] and size<=df6['sizemax'][i] and cut==df6['cut'][i]):
                    if fluo=='None' or fluo=='Medium' or fluo=='Faint':

                        if xx==1:
                            result=result+df6['1'][i] 
                        if xx==2:
                            result=result+df6['2'][i]    
                        if xx==3:
                            result=result+df6['3'][i]
                        if xx==4:
                            result=result+df6['4'][i]    
                        if xx==5:
                            result=result+df6['5'][i]
                        if xx==6:
                            result=result+df6['6'][i]
                        if xx==7:
                            result=result+df6['7'][i]
                        if xx==8:
                            result=result+df6['8'][i] 
                        if xx==9:
                            result=result+df6['9'][i]
                        break
                    else:
                        if xx==1:
                            result=result+df6['1'][i]/2 
                        if xx==2:
                            result=result+df6['2'][i]/2     
                        if xx==3:
                            result=result+df6['3'][i]/2 
                        if xx==4:
                            result=result+df6['4'][i]/2  
                        if xx==5:
                            result=result+df6['5'][i]/2 
                        if xx==6:
                            result=result+df6['6'][i]/2 
                        if xx==7:
                            result=result+df6['7'][i]/2 
                        if xx==8:
                            result=result+df6['8'][i]/2  
                        if xx==9:
                            result=result+df6['9'][i]/2 
                        break    
            if(df6['Shape'][i]=='Fancy' and shape!='RO'): 
                if(size>=df6['sizemin'][i] and size<=df6['sizemax'][i] and df6['symmetry'][i]==symmetry and df6['polish'][i]==polish):
                    if xx==1:
                    result=result+df6['1'][i] 
                    if xx==2:
                        result=result+df6['2'][i]    
                    if xx==3:
                        result=result+df6['3'][i]
                    if xx==4:
                        result=result+df6['4'][i]    
                    if xx==5:
                        result=result+df6['5'][i]
                    if xx==6:
                        result=result+df6['6'][i]
                    if xx==7:
                        result=result+df6['7'][i]
                    if xx==8:
                        result=result+df6['8'][i] 
                    if xx==9:
                        result=result+df6['9'][i]
                    break
        #table
    for i in range(len(df6)):
        if(df6['Location'][i]=='Crown'):
            if(df6['Shape'][i]==shape and shape=='RO'): 
                if(size>=df6['sizemin'][i] and size<=df6['sizemax'][i] and cut==df6['cut'][i]):
                    if fluo=='None' or fluo=='Medium' or fluo=='Faint':

                        if xx==1:
                            result=result+df6['1'][i] 
                        if xx==2:
                            result=result+df6['2'][i]    
                        if xx==3:
                            result=result+df6['3'][i]
                        if xx==4:
                            result=result+df6['4'][i]    
                        if xx==5:
                            result=result+df6['5'][i]
                        if xx==6:
                            result=result+df6['6'][i]
                        if xx==7:
                            result=result+df6['7'][i]
                        if xx==8:
                            result=result+df6['8'][i] 
                        if xx==9:
                            result=result+df6['9'][i]
                        break
                    else:
                        if xx==1:
                            result=result+df6['1'][i]/2 
                        if xx==2:
                            result=result+df6['2'][i]/2     
                        if xx==3:
                            result=result+df6['3'][i]/2 
                        if xx==4:
                            result=result+df6['4'][i]/2  
                        if xx==5:
                            result=result+df6['5'][i]/2 
                        if xx==6:
                            result=result+df6['6'][i]/2 
                        if xx==7:
                            result=result+df6['7'][i]/2 
                        if xx==8:
                            result=result+df6['8'][i]/2  
                        if xx==9:
                            result=result+df6['9'][i]/2 
                        break    
            if(df6['Shape'][i]=='Fancy' and shape!='RO'): 
                if(size>=df6['sizemin'][i] and size<=df6['sizemax'][i] and df6['symmetry'][i]==symmetry and df6['polish'][i]==polish):
                    if xx==1:
                    result=result+df6['1'][i] 
                    if xx==2:
                        result=result+df6['2'][i]    
                    if xx==3:
                        result=result+df6['3'][i]
                    if xx==4:
                        result=result+df6['4'][i]    
                    if xx==5:
                        result=result+df6['5'][i]
                    if xx==6:
                        result=result+df6['6'][i]
                    if xx==7:
                        result=result+df6['7'][i]
                    if xx==8:
                        result=result+df6['8'][i] 
                    if xx==9:
                        result=result+df6['9'][i]
                    break            
    for i in range(len(df6)):    
        if(df6['Location'][i]=='Girdle'):
            if(df6['Shape'][i]==shape and shape=='RO'): 
                if(size>=df6['sizemin'][i] and size<=df6['sizemax'][i] and cut==df6['cut'][i]):
                    if fluo=='None' or fluo=='Medium' or fluo=='Faint':

                        if xx==1:
                            result=result+df6['1'][i] 
                        if xx==2:
                            result=result+df6['2'][i]    
                        if xx==3:
                            result=result+df6['3'][i]
                        if xx==4:
                            result=result+df6['4'][i]    
                        if xx==5:
                            result=result+df6['5'][i]
                        if xx==6:
                            result=result+df6['6'][i]
                        if xx==7:
                            result=result+df6['7'][i]
                        if xx==8:
                            result=result+df6['8'][i] 
                        if xx==9:
                            result=result+df6['9'][i]
                        break
                    else:
                        if xx==1:
                            result=result+df6['1'][i]/2 
                        if xx==2:
                            result=result+df6['2'][i]/2     
                        if xx==3:
                            result=result+df6['3'][i]/2 
                        if xx==4:
                            result=result+df6['4'][i]/2  
                        if xx==5:
                            result=result+df6['5'][i]/2 
                        if xx==6:
                            result=result+df6['6'][i]/2 
                        if xx==7:
                            result=result+df6['7'][i]/2 
                        if xx==8:
                            result=result+df6['8'][i]/2  
                        if xx==9:
                            result=result+df6['9'][i]/2 
                        break    
            if(df6['Shape'][i]=='Fancy' and shape!='RO'): 
                if(size>=df6['sizemin'][i] and size<=df6['sizemax'][i] and df6['symmetry'][i]==symmetry and df6['polish'][i]==polish):
                    if xx==1:
                    result=result+df6['1'][i] 
                    if xx==2:
                        result=result+df6['2'][i]    
                    if xx==3:
                        result=result+df6['3'][i]
                    if xx==4:
                        result=result+df6['4'][i]    
                    if xx==5:
                        result=result+df6['5'][i]
                    if xx==6:
                        result=result+df6['6'][i]
                    if xx==7:
                        result=result+df6['7'][i]
                    if xx==8:
                        result=result+df6['8'][i] 
                    if xx==9:
                        result=result+df6['9'][i]
                    break
    for i in range(len(df6)):   
        if(df6['Location'][i]=='Pavilion'):
            if(df6['Shape'][i]==shape and shape=='RO'): 
                if(size>=df6['sizemin'][i] and size<=df6['sizemax'][i] and cut==df6['cut'][i]):
                    if fluo=='None' or fluo=='Medium' or fluo=='Faint':

                        if xx==1:
                            result=result+df6['1'][i] 
                        if xx==2:
                            result=result+df6['2'][i]    
                        if xx==3:
                            result=result+df6['3'][i]
                        if xx==4:
                            result=result+df6['4'][i]    
                        if xx==5:
                            result=result+df6['5'][i]
                        if xx==6:
                            result=result+df6['6'][i]
                        if xx==7:
                            result=result+df6['7'][i]
                        if xx==8:
                            result=result+df6['8'][i] 
                        if xx==9:
                            result=result+df6['9'][i]
                        break
                    else:
                        if xx==1:
                            result=result+df6['1'][i]/2 
                        if xx==2:
                            result=result+df6['2'][i]/2     
                        if xx==3:
                            result=result+df6['3'][i]/2 
                        if xx==4:
                            result=result+df6['4'][i]/2  
                        if xx==5:
                            result=result+df6['5'][i]/2 
                        if xx==6:
                            result=result+df6['6'][i]/2 
                        if xx==7:
                            result=result+df6['7'][i]/2 
                        if xx==8:
                            result=result+df6['8'][i]/2  
                        if xx==9:
                            result=result+df6['9'][i]/2 
                        break    
            if(df6['Shape'][i]=='Fancy' and shape!='RO'): 
                if(size>=df6['sizemin'][i] and size<=df6['sizemax'][i] and df6['symmetry'][i]==symmetry and df6['polish'][i]==polish):
                    if xx==1:
                    result=result+df6['1'][i] 
                    if xx==2:
                        result=result+df6['2'][i]    
                    if xx==3:
                        result=result+df6['3'][i]
                    if xx==4:
                        result=result+df6['4'][i]    
                    if xx==5:
                        result=result+df6['5'][i]
                    if xx==6:
                        result=result+df6['6'][i]
                    if xx==7:
                        result=result+df6['7'][i]
                    if xx==8:
                        result=result+df6['8'][i] 
                    if xx==9:
                        result=result+df6['9'][i]
                    break                       
        
                


    if ff==0:
        rap=0; 










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