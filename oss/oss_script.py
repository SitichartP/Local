import pandas as pd
import numpy  as np
import streamlit as st 

st.set_page_config(page_title="Oss Task", page_icon=None, layout="wide", initial_sidebar_state="auto")

## Import dataframe in each section ## 

## Overall DF ## 
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    # df = pd.read_excel("OSS Concept Design Delivery Guide.xlsx",index_col=False,sheet_name="Sheet1")
    # df.drop(df.columns[[0,1]],axis=1,inplace=True)


    ######################################## DATAFRAMES FOR EACH SECTION ######################################## 
    df_pm = df.loc[(df["PM "] == "X") & (df["Electrical Team"] != "X") & (df["Civl Structural Team"] != "X")]
    df_pm.drop(["Civl Structural Team","Electrical Team"],axis = 1 , inplace=True)
    df_pm_man = df_pm.loc[df_pm["Classification"] == "Mandatory"]
    df_pm_op = df_pm.loc[df_pm["Classification"] == "Optional"]
    
    # df_elec =
    # df_elec.drop 
    # df_elec_man = 
    # df_elec_op = 

    # df_civ = 
    # df_civ.drop 
    # df_civ_man = 
    # df_civ_op = 

    # df_ec = 
    # df_ec.drop 
    # df_ec_man = 
    # df_ec_op = 

    # df_pec =
    # df_pec.drop
    # df_pec_man = 
    # df_pec_op = 



    ######################################## SIDE BAR FILERS ######################################## 
    st.sidebar.header('PM Optional Tasks')
    selected_pm = st.sidebar.selectbox('Select a optional task', ['Please Select'] + list(df_pm_op['Artefact'].unique()))
    # selected_elec =
    # selected_civ =
    # selected_ec = 
    # selected_pec = 

    ## TITLE ##
    st.title("Delivery Schedule")


    ######################################## TABLES ######################################## 
    ##### PROJECT MANAGEMENT SECTION #####
    st.subheader("Project Management")

    if selected_pm:
        df_concat_pm = pd.concat([df_pm_man,df_pm.loc[df_pm["Artefact"] == selected_pm]])
        st.table(df_concat_pm)
        st.markdown(f"Total Estimated Labour Hours: **{df_concat_pm['Est Labour Hours'].sum()}**")
        st.markdown(f"Total Timeline: **{df_concat_pm['Timeline'].sum()}**")

    ##### ELECTRICAL SECTION #####
    st.subheader("Electrical")

    if selected_elec:
        df_concat_elec = pd.concat([df_elec_man,df_elec.loc[df_elec["Artefact"] == selected_elec]])
        st.table(df_concat_elec)
        st.markdown(f"Total Estimated Labour Hours: **{df_elec['Est Labour Hours'].sum()}**")
        st.markdown(f"Total Timeline: **{df_elec['Timeline'].sum()}**")

    ##### CIVIL AND STRUCTURAL #####
    st.subheader("Civil and Structural")

    if selected_civ:
        df_concat_civ = pd.concat([df_civ_man,df_civ.loc[df_civ["Artefact"] == selected_civ]])
        st.table(df_concat_civ)
        st.markdown(f"Total Estimated Labour Hours: **{df_civ['Est Labour Hours'].sum()}**")
        st.markdown(f"Total Timeline: **{df_civ['Timeline'].sum()}**")

    ##### Budget Estimation of OSS Costs #####
    st.subheader("Budget Estimation of OSS Costs")

    if selected_ec:
        df_concat_civ = pd.concat([df_ec_man,df_ec.loc[df_ec["Artefact"] == selected_ec]])
        st.table(df_concat_ec)
        st.markdown(f"Total Estimated Labour Hours: **{df_ec['Est Labour Hours'].sum()}**")
        st.markdown(f"Total Timeline: **{df_ec['Timeline'].sum()}**")

    ##### Prequalifications of OEMS, FEED Consultants and EPC contractors & Tender support #####
    st.subheader("Prequalifications of OEMS, FEED Consultants and EPC(I) contractors & Tender support")

    if selected_pec:
        df_concat_civ = pd.concat([df_pec_man,df_pec.loc[df_pec["Artefact"] == selected_pec]])
        st.table(df_concat_pec)
        st.markdown(f"Total Estimated Labour Hours: **{df_pec['Est Labour Hours'].sum()}**")
        st.markdown(f"Total Timeline: **{df_pec['Timeline'].sum()}**")
        

    





