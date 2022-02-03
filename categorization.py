# Categorization
import numpy as np
import streamlit as st

def calc_percentile(column):
  Q1 = np.percentile(column, 25, interpolation='midpoint') 
  Q2 = np.percentile(column, 50, interpolation='midpoint') 
  Q3 = np.percentile(column, 75, interpolation='midpoint')
  return (Q1,Q2,Q3)



def categorization(df):
    st.write("Categorizing...")
    all_terminals = np.array(df['Terminal'].unique())
    df['Categorization'] = ''

    for terminal in all_terminals:
        Q1,Q2,Q3 = calc_percentile(df[df['Terminal'] == terminal]['Latency'])


        latencies = np.array(df[df['Terminal'] == terminal]['Latency'])
        for l in latencies:
            if(l <= Q1):
                df['Categorization'] = np.where((df['Terminal'] == terminal) & (df['Latency'] == l),'Excellent',df['Categorization'])
            elif (l > Q1 and l <= Q2):
                df['Categorization'] = np.where((df['Terminal'] == terminal) & (df['Latency'] == l),'Good',df['Categorization'])
            elif (l > Q2 and l <= Q3):
                df['Categorization'] = np.where((df['Terminal'] == terminal) & (df['Latency'] == l),'Fair',df['Categorization'])
            elif (l > Q3):
                df['Categorization'] = np.where((df['Terminal'] == terminal) & (df['Latency'] == l),'Poor',df['Categorization'])
    
    return df