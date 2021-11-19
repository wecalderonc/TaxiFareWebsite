import datetime
import streamlit as st
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
API W
''')


d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

pickup_longitude = st.number_input('Insert a pickup longitude')
st.write('The current pickup longitude is ', pickup_longitude)
pickup_latitude = st.number_input('Insert a pickup latitude')
st.write('The current pickup latitude is ', pickup_latitude)
dropoff_longitude = st.number_input('Insert a dropoff longitude')
st.write('The current dropoff longitude is ', dropoff_longitude)
dropoff_latitude = st.number_input('Insert a dropoff latitude')
st.write('The current dropoff latitude is ', dropoff_latitude)
passenger_count = st.number_input('Insert a passenger count')
st.write('The current passenger_count is ', passenger_count)


url = 'https://taxifare.lewagon.ai/predict'

second_part_url = f"?pickup_latitude={int(pickup_latitude)}&pickup_longitude={int(pickup_longitude)}&dropoff_latitude={int(dropoff_latitude)}&dropoff_longitude={int(dropoff_longitude)}&passenger_count={int(passenger_count)}&pickup_datetime=2021-11-19%2015:48:24"

if st.button('click me'):
    # print is visible in the server output, not in the page
    print('button clicked!')
    st.write(url + second_part_url)
    response = requests.get(url + second_part_url)
    st.write(response)
else:
    st.write('I was not clicked 😞')



