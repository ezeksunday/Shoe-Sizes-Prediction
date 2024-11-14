import streamlit as st
import pickle 
import numpy as np
from datetime import datetime


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Introduction", "Shoe Size Prediction"])


if page == "Introduction":
    st.markdown("""
    <div style='text-align: center; color:white;background-color:black;'>
    <h1 style='color:white;'>Shoe Size Prediction App</h1>
    <h5 style='color:white;'>Built by Ezekiel Akuso</h5>
    </div>
    """, unsafe_allow_html=True)
    st.image('shoe_size.jpg', use_column_width=True)
    st.markdown("""
    <h5 style='text-align: center; color: Blue;'>This app predicts shoe size based on height and gender input.</h5>
    """, unsafe_allow_html=True)
    
    
    
    

elif page == "Shoe Size Prediction":
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)


    st.title("Shoe Size Prediction App")
    st.write("Enter your height and gender to predict your shoe size.")

    height = st.number_input("Height (in cm):", min_value=100, max_value=1000, value=150)
    gender = st.selectbox("Gender:", ("Male", "Female"))
    gender_code = 1 if gender == "Male" else 2


    prediction = model.predict([[height, gender_code]])[0]
    prediction = str(int(prediction.round()))
    if st.button("Predict Shoe Size"):
        st.write("Predicted Shoe Size: " + prediction)



    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.write("Was this prediction accurate?")
    feedback = st.radio("Feedback:", ("Yes", "No"))
    if feedback == 'No':
        correct_size = st.text_input("Enter Correct Size:")
    else:
        correct_size = None
    if st.button("Submit Feedback"):
        with open("feedback.csv", "a") as f:
            if feedback == 'Yes':
                f.write(f"{timestamp},{height},{gender_code},{prediction}\n")
                st.write("Thank you for your feedback!👏👏👏")
            elif feedback == 'No' and correct_size:
                f.write(f"{timestamp},{height},{gender_code},{correct_size}\n")
                st.write("Thank you for your feedback🙏🙏🙏. This response is vital for future improvement!")
