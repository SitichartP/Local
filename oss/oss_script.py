import pandas as pd
import numpy  as np
import streamlit as st 

st.set_page_config(page_title="Oss Task", page_icon=None, layout="wide", initial_sidebar_state="auto")

## Import dataframe in each section ## 

## Overall DF ## 
df = pd.read_excel("OSS Concept Design Delivery Guide.xlsx",index_col=False,sheet_name="Sheet1")
df.drop(df.columns[[0,1]],axis=1,inplace=True)

## Create list of df for each seg ## 
df_pm = df.loc[(df["PM "] == "X") & (df["Electrical Team"] != "X") & (df["Civl Structural Team"] != "X")]
df_pm.drop(["Civl Structural Team","Electrical Team"],axis = 1 , inplace=True)

df_pm_all = df_pm.loc[df_pm["Classification"] == "Mandatory"]


## Create Optional Task ## 
df_pm_op = df_pm.loc[df_pm["Classification"] == "Optional"]

## Create Side bar filter ## 
st.sidebar.header('PM Optional Tasks')
selected_pm = st.sidebar.selectbox('Select a optional task', ['All'] + list(df_pm_op['Artefact'].unique()))

## Task Project Management ##
st.title("Project Management")

if selected_pm == "All":
    st.table(df_pm_all)
else: 
    df_concat = pd.concat([df_pm_all,df_pm.loc[df_pm["Artefact"] == selected_pm]])
    st.table(df_concat)



## Electrical ## 

# st.title("Electrical")
# df_el = df.loc[(df["PM "] != "X") & (df["Electrical Team"] == "X") & (df["Civl Structural Team"] != "X")]
# df_el.drop(["PM ","Civl Structural Team"],axis=1,inplace=True)
# st.table(df_el)


## If optional user can choose ## 





