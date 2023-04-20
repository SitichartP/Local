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
    
    df_elec =
    df_elec.drop 
    df_elec_man = 
    df_elec_op = 

    df_civ = 
    df_civ.drop 
    df_civ_man = 
    df_civ_op = 

    df_ec = 
    df_ec.drop 
    df_ec_man = 
    df_ec_op = 

    df_pec =
    df_pec.drop
    df_pec_man = 
    df_ec_op = 



    ######################################## SIDE BAR FILERS ######################################## 
    st.sidebar.header('PM Optional Tasks')
    selected_pm = st.sidebar.selectbox('Select a optional task', ['Please Select'] + list(df_pm_op['Artefact'].unique()))
    # selected_elec =
    # selected_civ =
    # selected_ec = 
    # selected_pec = 

    ## TITLE ##
    st.title("Delivery Schedule")

    ## PROJECT MANAGEMENT SECTION ##
    st.subheader("Project Management")

    if selected_pm == "All":
        st.table(df_pm_man)
        st.markdown(f"Total Estimated Labour Hours: **{df_pm_man['Est Labour Hours'].sum()}**")
        st.markdown(f"Total Timeline: **{df_pm_man['Timeline'].sum()}**")
        
    else: 
        df_concat = pd.concat([df_pm_man,df_pm.loc[df_pm["Artefact"] == selected_pm]])
        st.table(df_concat)
        st.markdown(f"Total Estimated Labour Hours: **{df_concat['Est Labour Hours'].sum()}**")
        st.markdown(f"Total Timeline: **{df_concat['Timeline'].sum()}**")

    st.subheader("Project Management")

    

## Electrical ## 

# st.title("Electrical")
# df_el = df.loc[(df["PM "] != "X") & (df["Electrical Team"] == "X") & (df["Civl Structural Team"] != "X")]
# df_el.drop(["PM ","Civl Structural Team"],axis=1,inplace=True)
# st.table(df_el)


## If optional user can choose ## 





