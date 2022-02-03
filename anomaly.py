
# import modules
import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import datetime

# importing custom .py files
import holt_winters_algo
import categorization
import plotholtwinters


st.title("Anomaly Detection")

dataset_name = st.sidebar.text_input("Name of Dataset")


def fix_dataset(data):
    
    """
    this function drops unnecessary columns
    append seconds values to timestamp 
    remove all negative latencies
    """

    data.drop(data.columns[[0]], axis = 1,inplace=True)
    data['timestamp'] = data['timestamp'].astype(str)+":00"
    data['timestamp'] = pd.to_datetime(data['timestamp'],dayfirst = True)
    data = data[data['Latency'] > 0]
    return data



def get_dates():
    """
    select the start date and end date using streamlit slider
    """
    format = 'MMM DD, YYYY'  # format output
    start_date = datetime.date(year=2021,month=10,day=1) 
    end_date = datetime.date(year=2022,month=1,day=21) 
    max_days = end_date-start_date

    # slider = st.sidebar.slider('Select date', min_value=start_date, value=(start_date,end_date ),max_value=end_date, format=format)
    
    ## Sanity check
    start = st.sidebar.date_input("Start Date", value=pd.to_datetime(start_date, format="%Y-%m-%d"))
    end = st.sidebar.date_input("End Date", value=pd.to_datetime(end_date, format="%Y-%m-%d"))

    return start,end



def get_dataset(dataset_name,check):

    data = ''
    df = None
    terminal = None
    model,returned_data = None, None

    if dataset_name == "Latency Dataset":
        data = pd.read_csv("latency_ship_vsat_10k.csv")
        df = fix_dataset(data)
        st.write(f"Shape of dataset - {df.shape}")

        if check:
            #for categorizing data
            df = categorization.categorization(df)
        
        if not isinstance(df, type(None)):
            st.dataframe(df)
        
        terminal = st.sidebar.selectbox('Select a Terminal',('MY-StaySalty', 'MY-Abydos', 'Marjorie-c', 'MY-Namaste',
                                                    'MY-Alegria', 'MY-FountainHead1'))
        
        # for extracting start and dates
        start_date, end_date = get_dates()
        
        if(start_date < end_date):
            # plot anomalies
            if st.sidebar.button('Find The Anomalies'):
                st.write( """ ## Calculating For Terminal - """,terminal)

                # Finding anomalies using Holt-Winters algo
                model,series = holt_winters_algo.find_anomalies(start_date, end_date, df, terminal)

                # Plotting those anomalies
                plotholtwinters.plotholtwinters(model,series)

            else:
                st.write(""" ## Cant find unless you press the button """)
        else:
            st.write(""" ## End date should be greater than Start date """)

    else:
        st.write(""" ## Enter Valid Dataset """)    

    return df,terminal

check = st.sidebar.checkbox("Categorization")    
data,terminal = get_dataset(dataset_name,check)











