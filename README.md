# Anomaly-Detection
* Given a Latency dataset of internet connectivity in maritime ships.
* Conducted Explorartory Data Analysis of given dataset. It involves various plots for outlier detection.
* Built Isolation Forest ML model for Timeseries Anomaly Detection using Pycaret module in Jupyter NB.
* Discarded Isolation Forest ML model and first found seasonality in data then used Holt_Winters algorithm for Anomaly Detection
* Used streamlit open source framework for building Web App .

# What Streamlit App does :- 
  * We need to enter the name of dataset(in this case Latency Dataset)
  * We need to select a particular terminal and specify start dates and end dates , between which latency needs to be found
  * We can even select Categorization check box to display quality of Latency for each terminal . 
  * Categorization are done as :- 
      1) below 25% Excellent
      2) 25% to 50% Good
      3) 50% to 75% Fair
      4) Above 75% Poor
  
  * Finally the App runs the Holt_winters algorithm after finding seasonal lengths. Uses matplotlib abd streamlit pyplot() function to display the anomalies plot of selected terminal.
    
