# Importing Libraries
import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the trained model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar for Navigation
with st.sidebar : 
    selected = option_menu("Multiple Disease Prediction System",
            ["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction"],
             icons=['activity','heart','person'],default_index = 0)
    # default_index = 0 means the first option will be selected by default
    # icons can be taken from bootstrap-icons
# Diabetes Prediction Page
if (selected == "Diabetes Prediction"):
    st.title("Diabetes Prediction using ML")
    # Adding column names from the dataset in an order
    # Columns for input fields
    col1,col2,col3 = st.columns(3)
    # Having side by side inputs
    with col1:
        Pregnancies = st.number_input("Number of Pregnancies")
    with col2 :
        Glucose = st.number_input("Glucose Level")
    with col3 :
        BloodPressure = st.number_input("BloodPressure")
    with col1 :
        SkinThickness = st.number_input("SkinThickness")
    with col2 :
        Insulin = st.number_input("Insulin")
    with col3 :
        BMI = st.number_input("BMI")
    with col1 :
        DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction")
    with col2 :
        Age = st.number_input("Age of the Person")


    # Pregnancies = st.number_input("Number of Pregnancies")
    # Glucose = st.number_input("Glucose Level")
    # BloodPressure = st.number_input("BloodPressure")
    # SkinThickness = st.number_input("SkinThickness")
    # Insulin = st.number_input("Insulin")
    # BMI = st.number_input("BMI")
    # DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction")
    # Age = st.number_input("Age of the Person")

    # Code for Prediction
    diab_diagnosis = ''
    # Button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is Diabetic'
        else :
            diab_diagnosis = 'The person is not Diabetic'
    st.success(diab_diagnosis)


if(selected == "Heart Disease Prediction"):
    st.title("Heart Disease Prediction using ML")
    col1,col2,col3 = st.columns(3)
    # Having side by side inputs
    with col1:
        age = st.number_input("Age")
    with col2 :
        sex = st.number_input("Sex")
    with col3 :
        cp = st.number_input("Chest Pain")
    with col1 :
        trestbps = st.number_input("Resting Blood Pressure")
    with col2 :
        chol = st.number_input("Serum Cholestoral")
    with col3 :
        fbs = st.number_input("Fasting Blood Sugar")
    with col1 :
        restecg = st.number_input("Resting Electrocardiographic Results")
    with col2 :
        thalach = st.number_input("Maximum Heart Rate Achieved")
    with col3 :
        exang = st.number_input("Exercise Induced Angina")
    with col1 :
        oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest")
    with col2 :
        slope = st.number_input("Slope of the Peak Exercise ST Segment")
    with col3 :
        ca = st.number_input("Number of Major Vessels")
    with col1 :
        thal = st.number_input("Thalium Stress Test Result")
    # Code for Prediction
    heart_diagnosis = ''
    # Button for Prediction
    if st.button('Heart Disease Test'):
        heart_prediction = heart_disease_model.predict([[
            age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person has Heart Disease'
        else :
            heart_diagnosis = 'The person does not have Heart Disease'
    st.success(heart_diagnosis)

if(selected == "Parkinsons Prediction"):
    st.title("Parkinsons Prediction using ML")
    col1,col2,col3 = st.columns(3)
    # Having side by side inputs