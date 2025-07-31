import streamlit as s
import numpy as np
import pandas as pd
import pickle as pkl
from predictions import predict

s.title("Linear Regression for Temperature Prediction")

#columns_select = s.multiselect("What column would you like to pick?", ['Humidity', 'Wind Bearing (degrees)', 'rain', 'snow', 'Summary Int'])

#if s.button("Next"):
    #if columns_select == "Humidity":
input_app_temp = s.number_input("What is the apparent temperature?")

input_humidity = s.number_input("What is the humidity?")
    #elif columns_select == "Wind Bearing (degrees)":
input_wind = s.number_input("What is the wind bearing in degrees?")
   # elif columns_select == "rain":
input_rain = s.number_input("If it was raining, please enter 1. If not, enter 0.")
  #  elif columns_select == "snow":
input_snow = s.number_input("If it was snowing, please enter 1. If not, enter 0.")
  #  else:
input_sum_int = s.number_input("What is the summary integer?")

input_vis = s.number_input("What is the min max distribution for visibility?")

input_wind_speed = s.number_input("What is the min max distribution for wind speed in km/h?")

input_pressure = s.number_input("What is the min max distribution for the pressure in millibars?")

if s.button("Predict"):
    result = predict(np.array([[int(input_app_temp), int(input_humidity), int(input_wind), int(input_rain), int(input_snow), int(input_sum_int), int(input_vis), int(input_wind_speed), int(input_pressure)]]))
    s.text(result)