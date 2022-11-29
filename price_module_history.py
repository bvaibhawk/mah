import streamlit as st
import glob
import pandas as pd

def page6():

    st.subheader("Price Module Upload History")

    # st.markdown(st.session_state['footer'], unsafe_allow_html=True)

    total_files = glob.glob("miscellenious_discounts/input_files/input_price_module_discounts_*.xlsm")
    print(total_files)
    # total_files = sorted(total_files)
    total_files.sort(key = lambda x: x.split("@")[-1])

    file_names = [name.split("/")[-1] for name in total_files]
    uploaded_file = st.selectbox("Select File to download (sorted by oldest first)",["--Select--"]+file_names)
    if uploaded_file!="--Select--":
        # df = pd.read_excel("./miscellenious_discounts/input_files/"+uploaded_file)
        with open("./miscellenious_discounts/input_files/"+uploaded_file, "rb") as fp:
            st.download_button(
                label="📥 Download",
                data=fp,
                file_name=uploaded_file,
                mime="application/vnd.ms-excel"
            )

    hist_df = pd.DataFrame()
    hist_df['Latest File'] = pd.Series(total_files[-1].split("/")[-1])
    st.table(hist_df)