import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image
from smart_open import smart_open

st.title("Sports Predict App")
st.header("Sports Performace Prediction")
st.write("This web app predicts the overall performance of a player based on particular features")

model = pickle.load(smart_open('https://mlassignment.s3.eu-de.cloud-object-storage.appdomain.cloud/final_model%20(1).save', 'rb'))
image = Image.open("sports.jpg")
st.image(image, use_column_width=True)
st.write("Please insert values to get overall prediction of player")

potential = st.slider("Player Potential: ", 0, 100)
club = st.number_input("Pick Club number based on club description above")
wage = st.number_input("Please enter wage of player")
international_reputation = st.slider("Player International Reputation: ", 0, 5)
short_passing = st.slider("Player Short Passing: ", 0, 100)
reactions = st.slider("Player Reactions: ", 0, 100)
vision = st.slider("Player Vision: ", 0, 100)
composure = st.slider("Player Composure: ", 0, 100)

data = {'Potential' : potential,
 'Club' : club,
 'Wage' : wage,
 'International Reputation' : international_reputation,
 'ShortPassing' : short_passing,
 'Reactions' : reactions,
 'Vision' : vision,
 'Composure' : composure

	}

features = pd.DataFrame(data, index=[0])
Prediction = model.predicy(features)

st.header("Please find predicted value below")
st.write("The overall predicted score for the above player is", prediction)

