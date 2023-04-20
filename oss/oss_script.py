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


    ## Create list of df for each seg ## 
    df_pm = df.loc[(df["PM "] == "X") & (df["Electrical Team"] != "X") & (df["Civl Structural Team"] != "X")]
    df_pm.drop(["Civl Structural Team","Electrical Team"],axis = 1 , inplace=True)

    df_pm_all = df_pm.loc[df_pm["Classification"] == "Mandatory"]

    # Dataframe to sum hours for PM
    pm_sum_df = pd.DataFrame 

    ## Create Optional Task ## 
    df_pm_op = df_pm.loc[df_pm["Classification"] == "Optional"]

    ## Create Side bar filter ## 
    st.sidebar.header('PM Optional Tasks')
    selected_pm = st.sidebar.selectbox('Select a optional task', ['Please Select'] + list(df_pm_op['Artefact'].unique()))

    ## Task Project Management ##
    st.title("Delivery Schedule")
    st.subheader("Project Management")

    if selected_pm == "All":
        st.table(df_pm_all)
        # pm_sum_df['Total Estimated Labour Hours'] = [df_pm_all['Est Labour Hours'].sum()]
        # pm_sum_df['Total Timeline'] = [df_pm_all['Timeline'].sum()]
        st.markdown(f"Total Estimated Labour Hours: **{df_pm_all['Est Labour Hours'].sum()}**")
        st.markdown(f"Total Timeline: **{df_pm_all['Timeline'].sum()}**")
        
    else: 
        df_concat = pd.concat([df_pm_all,df_pm.loc[df_pm["Artefact"] == selected_pm]])
        st.table(df_concat)
        # pm_sum_df['Total Estimated Labour Hours'] = [df_concat['Est Labour Hours'].sum()]
        # pm_sum_df['Total Timeline'] = [df_concat['Timeline'].sum()]
        st.markdown(f"Total Estimated Labour Hours: **{df_concat['Est Labour Hours'].sum()}**")
        st.markdown(f"Total Timeline: **{df_concat['Timeline'].sum()}**")


## Electrical ## 

# st.title("Electrical")
# df_el = df.loc[(df["PM "] != "X") & (df["Electrical Team"] == "X") & (df["Civl Structural Team"] != "X")]
# df_el.drop(["PM ","Civl Structural Team"],axis=1,inplace=True)
# st.table(df_el)


## If optional user can choose ## 





