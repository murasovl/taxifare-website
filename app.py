import streamlit as st
import requests
from datetime import datetime
import pandas as pd

'''
# TaxiFareModel front
'''

st.markdown('''
Blubb
''')

# Display a map of New York City
nyc_center = pd.DataFrame({
    'lat': [40.7128],
    'lon': [-74.0060]
})
st.map(nyc_center, zoom=10)

'''
## Blabla
'''

# Input controllers

time_of_ride = st.time_input('Insert Your Pickup Time')
date_of_ride = st.date_input('Insert Your Pickup Date', value="default_value_today", format="DD/MM/YYYY")
pickup_longitude = st.number_input('Pickup longitude', format="%.6f")
pickup_latitude = st.number_input('Pickup latitude', format="%.6f")
dropoff_longitude = st.number_input('Dropoff longitude', format="%.6f")
dropoff_latitude = st.number_input('Dropoff latitude', format="%.6f")
#passenger_count = st.number_input('Passenger count', min_value=1, max_value=8, step=1)
passenger_count = st.slider('Passenger count', min_value=1, max_value=8, step=1)


'''
##
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':
    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# Build a dictionary containing the parameters for our API
ride_params = {
    'pickup_datetime': datetime.combine(date_of_ride, time_of_ride).strftime("%Y-%m-%d %H:%M:%S"),
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}

'''
##
'''

# Call the API and display the prediction
if st.button('Get Fare Prediction'):
    response = requests.get(url, params=ride_params)
    if response.status_code == 200:
        prediction = response.json()['fare']
        st.write(f'The predicted fare is ${prediction:.2f}')
    else:
        st.write('Error in API call')
