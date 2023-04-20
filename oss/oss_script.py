import pandas as pd
import numpy  as np
import streamlit as st 

## PAGE CONFIG ## 

st.set_page_config(page_title="Delivery Schedule", page_icon=None, layout="wide", initial_sidebar_state="auto")

## TITLE ##
st.title("📅Delivery Schedule")

## Import dataframe in each section ## 

## Overall DF ## 
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    # df = pd.read_excel("OSS Concept Design Delivery Guide.xlsx",index_col=False,sheet_name="Sheet1")
    df.drop(df.columns[[0,1]],axis=1,inplace=True)


    ######################################## DATAFRAMES FOR EACH SECTION ######################################## 
    df_pm = df.loc[(df["PM "] == "X") & (df["Electrical Team"] != "X") & (df["Civl Structural Team"] != "X")]
    df_pm.drop(["Civl Structural Team","Electrical Team"],axis = 1 , inplace=True)
    df_pm_man = df_pm.loc[df_pm["Classification"] == "Mandatory"]
    df_pm_op = df_pm.loc[df_pm["Classification"] == "Optional"]
    
    df_elec = df.loc[(df["PM "] != "X") & (df["Electrical Team"] == "X") & (df["Civl Structural Team"] != "X")]
    df_elec.drop(["Civl Structural Team","PM "],axis = 1 , inplace=True)
    df_elec_man = df_elec.loc[df_elec["Classification"] == "Mandatory"]
    df_elec_op = df_elec.loc[df_elec["Classification"] == "Optional"]

    df_civ = df.loc[(df["PM "] != "X") & (df["Electrical Team"] != "X") & (df["Civl Structural Team"] == "X")]
    df_civ.drop(["Electrical Team","PM "],axis = 1 , inplace=True)
    df_civ_man = df_civ.loc[df_civ["Classification"] == "Mandatory"]
    df_civ_op = df_civ.loc[df_civ["Classification"] == "Optional"]

    df_ec = df.loc[(df["PM "] == "X") & (df["Electrical Team"] == "X") & (df["Civl Structural Team"] != "X")]
    df_ec.drop(["Civl Structural Team"],axis = 1 , inplace=True) 
    df_ec_man = df_ec.loc[df_ec["Classification"] == "Mandatory"]
    df_ec_op = df_ec.loc[df_ec["Classification"] == "Optional"]

    df_pec = df.loc[(df["PM "] == "X") & (df["Electrical Team"] == "X") & (df["Civl Structural Team"] == "X")]
    df_pec_man = df_pec.loc[df_pec["Classification"] == "Mandatory"]
    df_pec_op = df_pec.loc[df_pec["Classification"] == "Optional"]



    ######################################## SIDE BAR FILERS ######################################## 

    st.sidebar.title('Optional Task List')
    
    ## PM ##
    st.sidebar.header('PM Optional Tasks')
    selected_pm = st.sidebar.multiselect('Select a optional task', list(df_pm_op['Artefact'].unique()))

    ## Electrical ##
    st.sidebar.header('Electrical Optional Tasks')
    selected_elec = st.sidebar.multiselect('Select a optional task', list(df_elec_op['Artefact'].unique()))   

    ## Civil ##
    st.sidebar.header('Civil and Structural Optional Tasks')
    selected_civ = st.sidebar.multiselect('Select a optional task', list(df_civ_op['Artefact'].unique()))   

    ## Electrical and civil structural ##
    st.sidebar.header('Electrical and civil structural Tasks')
    selected_ec = st.sidebar.multiselect('Select a optional task', list(df_ec_op['Artefact'].unique())) 

    # ## Prequalification of OEMs, FEED Consultants and EPC(I) contractors & Tender support (Electrical and civil structural) ## 
    st.sidebar.header('OEMs,FEED Consultants and EPC(I) Tasks')
    selected_pec = st.sidebar.multiselect('Select an optional task', list(df_pec_op['Artefact'].unique()))


    ######################################## TABLES ######################################## 

    ## SUM VARIABLES ##
    pm_lab = df_pm_man['Est Labour Hours'].sum()
    pm_timeline = df_pm_man['Timeline'].sum()

    elec_lab = df_elec_man['Est Labour Hours'].sum()
    elec_timeline = df_elec_man['Timeline'].sum()

    civ_lab = df_civ_man['Est Labour Hours'].sum()
    civ_timeline = df_civ_man['Timeline'].sum()

    ec_lab = df_ec_man['Est Labour Hours'].sum()
    ec_timeline = df_ec_man['Timeline'].sum()

    pec_lab = df_pec_man['Est Labour Hours'].sum()
    pec_timeline = df_pec_man['Timeline'].sum()

    ##### PROJECT MANAGEMENT SECTION #####
    st.header("Project Management")

    
    if selected_pm:
        df_concat_pm = pd.concat([df_pm_man,df_pm.loc[df_pm["Artefact"].isin(selected_pm)]])
        st.table(df_concat_pm)

        pm_lab = df_concat_pm['Est Labour Hours'].sum()
        pm_timeline = df_concat_pm['Timeline'].sum()

        st.markdown(f"Total Estimated Labour Hours: **{pm_lab}**")
        st.markdown(f"Total Timeline: **{pm_timeline} Days**")

    else: 
        st.table(df_pm_man) 
        st.markdown(f"Total Estimated Labour Hours: **{pm_lab}**")
        st.markdown(f"Total Timeline: **{pm_timeline} Days**")
    


    ##### ELECTRICAL SECTION #####
    st.header("Electrical")

    if selected_elec:
        df_concat_elec = pd.concat([df_elec_man,df_elec.loc[df_elec["Artefact"].isin(selected_elec)]])
        st.table(df_concat_elec)

        elec_lab = df_concat_elec['Est Labour Hours'].sum()
        elec_timeline = df_concat_elec['Timeline'].sum()

        st.markdown(f"Total Estimated Labour Hours: **{elec_lab}**")
        st.markdown(f"Total Timeline: **{elec_timeline} Days**")
    
    else:
        st.table(df_elec_man)
        st.markdown(f"Total Estimated Labour Hours: **{elec_lab}**")
        st.markdown(f"Total Timeline: **{elec_timeline} Days**")

    ##### CIVIL AND STRUCTURAL #####
    st.header("Civil and Structural")

    if selected_civ:
        df_concat_civ = pd.concat([df_civ_man,df_civ.loc[df_civ["Artefact"].isin(selected_civ)]])
        st.table(df_concat_civ)

        civ_lab = df_concat_civ['Est Labour Hours'].sum()
        civ_timeline = df_concat_civ['Timeline'].sum()

        st.markdown(f"Total Estimated Labour Hours: **{civ_lab}**")
        st.markdown(f"Total Timeline: **{civ_timeline} Days**")
    
    else: 
        st.table(df_civ_man)
        st.markdown(f"Total Estimated Labour Hours: **{civ_lab}**")
        st.markdown(f"Total Timeline: **{civ_timeline} Days**")

    ##### Budget Estimation of OSS Costs #####
    st.header("Budget Estimation of OSS Costs")

    if selected_ec:
        df_concat_ec = pd.concat([df_ec_man,df_ec.loc[df_ec["Artefact"].isin(selected_ec)]])
        st.table(df_concat_ec)

        ec_lab = df_concat_ec['Est Labour Hours'].sum()
        ec_timeline = df_concat_ec['Timeline'].sum()
        
        st.markdown(f"Total Estimated Labour Hours: **{ec_lab}**")
        st.markdown(f"Total Timeline: **{ec_timeline} Days**")
    
    else:
        st.table(df_ec_man)
        st.markdown(f"Total Estimated Labour Hours: **{ec_lab}**")
        st.markdown(f"Total Timeline: **{ec_timeline} Days**")

    ##### Prequalifications of OEMS, FEED Consultants and EPC contractors & Tender support #####
    st.header("Prequalifications of OEMS, FEED Consultants and EPC(I) contractors & Tender support")

    if selected_pec:
        df_concat_pec = pd.concat([df_pec_man,df_pec.loc[df_pec["Artefact"].isin(selected_pec)]])
        st.table(df_concat_pec)

        pec_lab = df_concat_pec['Est Labour Hours'].sum()
        pec_timeline = df_concat_pec['Timeline'].sum()

        st.markdown(f"Total Estimated Labour Hours: **{pec_lab}**")
        st.markdown(f"Total Timeline: **{pec_timeline} Days**")

    else:
        st.table(df_pec_man)
        st.markdown(f"Total Estimated Labour Hours: **{pec_lab}**")
        st.markdown(f"Total Timeline: **{pec_timeline} Days**")

    overall_labour = pm_lab + elec_lab + civ_lab + ec_lab + pec_lab
    overall_timeline = pm_timeline + elec_timeline + civ_timeline + ec_timeline + pec_timeline

    st.subheader(f"Overall Total Estimated Labour Hours: **{overall_labour}**")
    st.subheader(f"Overall Total Timeline: **{overall_timeline} Days**")
        

    





