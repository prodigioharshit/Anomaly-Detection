import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def mean_absolute_percentage_error(y_true, y_pred): 
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def plotholtwinters(model, series):
    """
        series - dataset with timeinterval
        model - 
    """
    
    fig = plt.figure(figsize=(30, 15))
    #plt.xticks( site2['Cl'], site2.index.values )
    plt.plot(model.result, label = "Model")
    plt.plot(series.values, label = "Actual")
    error = mean_absolute_percentage_error(series.values, model.result[:len(series)])
    plt.title("Mean Absolute Percentage Error: {0:.2f}%".format(error))
    
    
    anomalies = np.array([np.NaN]*len(series))
    anomalies[series.values<model.LowerBond[:len(series)]] = \
        series.values[series.values<model.LowerBond[:len(series)]]
    anomalies[series.values>model.UpperBond[:len(series)]] = \
        series.values[series.values>model.UpperBond[:len(series)]]
    #print(anomalies)
    plt.plot(anomalies, "o", markersize=10, label = "Anomalies")


    plt.plot(model.UpperBond, "r--", alpha=0.5, label = "Up/Low confidence")
    plt.plot(model.LowerBond, "r--", alpha=0.5)
    plt.fill_between(x=range(0,len(model.result)), y1=model.UpperBond, 
                        y2=model.LowerBond, alpha=0.2, color = "grey")    
        
    plt.vlines(len(series), ymin=min(model.LowerBond), ymax=max(model.UpperBond), linestyles='dashed')
    plt.axvspan(len(series), len(model.result), alpha=0.3, color='lightgrey')
    plt.grid(True)
    plt.axis('tight')
    plt.legend(loc="best", fontsize=13);

    st.pyplot(fig)