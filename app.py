import streamlit as st
import pandas as pd
import os

# File to store votes
VOTE_FILE = 'votes.csv'

# Predefined list of valid phone numbers
VALID_PHONE_NUMBERS = [
    '03125378196', '03012017605', '03032373373',
    '03044880718', '03323078108', '03432588211', '03456432348'
]

# Function to initialize the votes file
def init_votes():
    if not os.path.isfile(VOTE_FILE):
        df = pd.DataFrame(columns=['phone_number', 'vote'])
        df.to_csv(VOTE_FILE, index=False)

# Function to check if a phone number has already voted
def has_voted(phone_number):
    df = pd.read_csv(VOTE_FILE, dtype=str)  # Ensure all columns are read as strings
    df['phone_number'] = df['phone_number'].str.strip()  # Remove any leading/trailing whitespace
    return phone_number in df['phone_number'].values
# Function to check if a phone number has already voted

# Function to save a vote
def save_vote(phone_number, vote):
    df = pd.read_csv(VOTE_FILE)
    new_vote = pd.DataFrame([[phone_number, vote]], columns=['phone_number', 'vote'])
    df = pd.concat([df, new_vote], ignore_index=True)
    df.to_csv(VOTE_FILE, index=False)

# Initialize the votes file
init_votes()

st.title("Gen AI Cohort 2 Hackathon - Simple Voting App 6.0")

# Input for voter phone number
phone_number = st.text_input("Enter your phone number (this will remain anonymous):")

# Voting options
options = [
"AI-Driven Project Schedule Optimizer - Objective: Build an AI tool/App to optimize construction project schedules. (Asad Ali)", \
"Mental Health Companion - Objective: Empathetic chatbot for mental wellness support. (Syed Raza Ali)", \
"NewsByte - Problem Identification: Information overload. (Sehresh Mumtaz)", \
"Customized Product Description Generator - Purpose: Automatically generate product descriptions. (M Salman)", \
"AI-Powered Career Counselor App the app will analyze users' interests, skills, and aspirations to offer tailored career recommendations. (Asad Ali)", \
"Sentiment Analysis on Economic News - Project: Perform sentiment analysis on economic news. (Syed Raza Ali)", \
"Virtual Economy Simulator for Testing Monetary Policies- Purpose: Simulate an entire virtual economy. (M Salman)", \
"PakTouristHelper: Help tourists find points of interest in a City in Pakistan. (Noman Riaz)", \
"Synthetic Data Generator for Training Models - Purpose: Generate synthetic datasets for training AI models. (M Salman)", \
"Education Companion - Objective: AI-powered chatbot for personalized, interactive learning support. (Yaqoob Ahmed)" 
]

# Use radio buttons for options
selected_option = st.radio("Select your option:\n For more details about these projects, please check whatApp discussion", options)

# Voting logic
if st.button("Vote"):
    st.write('Phone Numbere: ', phone_number)
    if not phone_number:
        st.error("Please enter your phone number.")
    elif phone_number not in VALID_PHONE_NUMBERS:
        st.error("This phone number is not authorized to vote.")
    elif has_voted(phone_number):
        st.error("This phone number has already voted!")
    else:
        save_vote(phone_number, selected_option)
        st.success(f"Thank you for voting for '{selected_option}'!")

# Display results
if st.button("Show Results"):
    df = pd.read_csv(VOTE_FILE)
    results = df['vote'].value_counts()
    st.write("Current Vote Tally:")
    st.bar_chart(results)
