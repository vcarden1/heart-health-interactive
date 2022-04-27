import streamlit as st
from pycaret.classification import *
import pandas as pd


class TheHomePage:
    def __init__(self, model) -> None:
        # TODO: Define page-specific variables here
        self.model = model

    def display(self):
        # TODO: define the streamlit view here
        st.header("Predicting Heart Desease")

        st.write(
            "We are looking for correlations in the data that may lead to heart diesase"
        )

        st.write(pd.read_csv("./Data/heart_2020.csv"))

        BMI = st.number_input('Insert your BMI')
        option = st.selectbox(
            'How would you like to be contacted?', ('Yes', 'No'))
        option1 = st.selectbox('Do you have Heart Disease', ('Yes', 'No'))

        # Prepare the model's input data
        input_data = pd.DataFrame({
            "BMI": 34.3,
            "Smoking": "Yes",
            "AlcoholDrinking": "Yes",
            "Stroke": "Yes",
            "PhysicalHealth": 0.0,
            "MentalHealth": 30,
            "DiffWalking": "No",
            "Sex": "Male",
            "AgeCategory": "18-24",
            "Race": "White",
            "Diabetic": "No",
            "PhysicalActivity": "Yes",
            "GenHealth": "Good",
            "SleepTime": 15,
            "Asthma": "No",
            "KidneyDisease": "No",
            "SkinCancer": "No"
        }, index=[0])

        # Transform the input to one-hot encode categorical variables
        prep_pipe = get_config('prep_pipe')
        transformed_unseen_data = prep_pipe.transform(input_data)

        # Make a Prediction
        prediction = self.model.predict(transformed_unseen_data)[0]

        # Display the diagnosis
        diagnosis = "Heart Disease" if prediction == 1 else "No Heart Disease"
        st.write(f"Your diagnosis: {diagnosis}")
