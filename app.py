import streamlit as st
import datetime
import requests
import pandas as pd
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''please enter the date'''

# Date
d = st.date_input("Day of Ride?")
st.write('The ride is on the:', d)

# Time
t = st.time_input('At what time?')
st.write('Pickuptime is set for', t)

# Datetime
dt = datetime.datetime.combine(d, t)
st.write('Datetime is now:', dt)

# Pickup longitude
pickup_longitude = st.number_input('Pickup longitude', 40.7614327)
st.write('The current Pickup longitude is ', pickup_longitude)

# Pickup latitude
pickup_latitude = st.number_input('Pickup latitude', 73.9798156)
st.write('The current Pickup latitude is ', pickup_latitude)

# dropoff longitude
dropoff_longitude = st.number_input('dropoff longitude', 40.6513111)
st.write('The current dropoff longitude is ', dropoff_longitude)

# dropoff latitude
dropoff_latitude = st.number_input('dropoff latitude', 73.8803331)
st.write('The current dropoff latitude is ', dropoff_latitude)

passenger_count = st.slider('How many passengers', 1, 10, 3)
st.write('The current passenger_count is ', passenger_count)

# MAP
centralCoordinates = [-74.00597, 40.71427]
def get_map_data():

    return pd.DataFrame(
            [[pickup_latitude, pickup_longitude],[dropoff_latitude, dropoff_longitude]],
            columns=['lat', 'lon']
        )

df = get_map_data()
st.write(df)
st.map(df, zoom=11, use_container_width=True)


## Once we have these, let's call our API in order to retrieve a prediction
'''
See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
# INPUT DICTIONARY
input_dictionary = {
    'pickup_datetime':dt,
    'pickup_longitude':pickup_longitude,
    'pickup_latitude':pickup_latitude,
    'dropoff_longitude':dropoff_longitude,
    'dropoff_latitude':dropoff_latitude,
    'passenger_count':passenger_count    
}

# Call to API
response = requests.get(url,input_dictionary)
fare = response.json()['fare']
#print(response.content()) # Return the raw bytes of the data payload
#print(response.text()) # Return a string representation of the data payload
#print(response.json()) # This method is convenient when the API returns JSON

    
st.success(f'The fare is: {fare}')