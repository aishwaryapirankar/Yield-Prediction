import streamlit as st
import pickle
import time
import pandas as pd
import numpy as np
model = pickle.load(open('model.pkl', 'rb'))

def predict_promotion(id, farm_area, temp_obs, wind_direction, dew_temp, pressure_sea_level, precipitation, wind_speed, unix_sec, ingredient_type, farming_company):
    if ingredient_type == 'ing_w':
        ingredient_type = 0
    elif ingredient_type == 'ing_x':
        ingredient_type = 1
    elif ingredient_type == 'ing_z':
        ingredient_type = 2

    if farming_company == 'Obery Farms':
        farming_company = 0
    elif farming_company == 'Wayne Farms':
        farming_company = 1
    elif farming_company == 'Dole Food Company':
        farming_company = 2
    elif farming_company == 'Sanderson Farms':
        farming_company = 3
    elif farming_company == 'Del Monte Foods':
        farming_company = 4
    elif farming_company == 'Freight Farms':
        farming_company = 5
    elif farming_company == 'Tyson Foods':
        farming_company = 6
    elif farming_company == 'Other':
        farming_company = 7
    elif farming_company == 'Perdue Farms':
        farming_company = 8
    elif farming_company == 'Mountaire Farms':
        farming_company = 9
    elif farming_company == 'Foster Farms':
        farming_company = 10
    elif farming_company == 'Southern Confederate Farms':
        farming_company = 11

    deidentified_location = 0

    prediction = model.predict(pd.DataFrame([[id, farm_area, temp_obs, wind_direction, dew_temp, pressure_sea_level, precipitation, wind_speed, unix_sec, ingredient_type, farming_company, deidentified_location]], columns=['id', 'farm_area', 'temp_obs', 'wind_direction', 'dew_temp', 'pressure_sea_level', 'precipitation', 'wind_speed', 'Unix Sec', 'ingredient_type', 'farming_company', 'deidentified_location']))
    return prediction

#st.title("Robust Yield Prediction for Farm Processing Units")
html_temp = """ <div style="background-color:#8F75AD;padding:10px">
    <h2 style="color:white;text-align:center;">Robust Yield Prediction
 </h2>

    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)

id = st.number_input("Farm ID")
farm_area = st.number_input("Farm Area")
temp_obs = st.number_input("Temperature Observations")
wind_direction = st.number_input("Wind Direction")
dew_temp = st.number_input("Dew Temperature")
pressure_sea_level = st.number_input("Sea level pressure")
precipitation = st.number_input("Precipitation")
wind_speed = st.number_input("Speed of the wind")
date_input = st.date_input("Date")
ingredient_type = st.selectbox("Ingredient Type", ['ing_w', 'ing_x', 'ing_z'])
farming_company = st.selectbox("Farming company", ['Obery Farms', 'Wayne Farms', 'Dole Food Company', 'Sanderson Farms', 'Del Monte Foods', 'Freight Farms', 'Tyson Foods', 'Other', 'Perdue Farms', 'Mountaire Farms', 'Foster Farms', 'Southern Confederate Farms'])
#deidentified_location = st.number_input("Deidentified Location")

unix_sec = time.mktime(date_input.timetuple())

result=""
if st.button("Predict"):
    result=predict_promotion(id, farm_area, temp_obs, wind_direction, dew_temp, pressure_sea_level, precipitation, wind_speed, unix_sec, ingredient_type, farming_company)
    st.success('The yield is {}'.format(result))



