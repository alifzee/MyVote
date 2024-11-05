import streamlit as st
import pandas as pd
import os

# File to store votes
VOTE_FILE = 'votes.csv'

# Predefined list of valid phone numbers
VALID_PHONE_NUMBERS = ['03125378196', '03012017605', '03032373373', '03044880718', '03323078108', '03432588211', '03456432348']  # Add valid numbers here

# Function to initialize votes file
def init_votes():
    if not os.path.isfile(VOTE_FILE):
        df = pd.DataFrame(columns=['phone_number', 'vote'])
        df.to_csv(VOTE_FILE, index=False)

# Function to check if a phone number has already voted
def has_voted(phone_number):
    df = pd.read_csv(VOTE_FILE)
    return phone_number in df['phone_number'].values

# Function to save a vote
def save_vote(phone_number, vote):
    df = pd.read_csv(VOTE_FILE)
    new_vote = pd.DataFrame([[phone_number, vote]], columns=['phone_number', 'vote'])
    df = pd.concat([df, new_vote], ignore_index=True)
    df.to_csv(VOTE_FILE, index=False)

# Initialize votes file
init_votes()

st.title("Simple Voting App")

# Input for voter phone number
phone_number = st.text_input("Enter your phone number (this will remain anonymous):")

options = ["Personalized Investment Advisor\n
Purpose: Generate personalized investment advice based on user profiles, economic indicators, and forecasted market trends.\n
Application: Helps individuals make informed investment decisions based on generative predictions of future economic conditions.\n
Model: Use a transformer-based model fine-tuned on financial advice data and economic indicators to generate investment recommendations.\n\n",

"Sentiment Analysis on Economic News\n
Project: Perform sentiment analysis on economic news or central bank announcements to gauge market sentiment and its potential influence on the economy.\n
Tools: Use NLP models (like VADER for simple sentiment or BERT for advanced analysis) and scrape news data using Beautiful Soup or an API.\n
Benefit: This project demonstrates your understanding of text analysis and its application in economics, as well as your programming skills.\n\n",

"Personalized Policy Recommendation System\n
Purpose: Create a model that suggests policy changes tailored to specific regions, sectors, or demographics, based on economic goals like reducing unemployment or increasing GDP.\n
Application: Useful for policymakers to quickly see which policies might work best for different economic challenges in specific areas.\n
Model: Use a recommender system approach (similar to those used in e-commerce) trained on historical policy outcomes to make data-driven recommendations.\n\n",

"Virtual Economy Simulator for Testing Monetary Policies\n
Purpose: Simulate an entire virtual economy to test the impact of different monetary policies, such as changing interest rates or altering reserve requirements.\n
Application: Can help policymakers and economists understand complex monetary policy effects without real-world risks.\n
Model: Build an agent-based model with different types of agents (consumers, firms, banks) governed by economic rules and policies, with reinforcement learning to fine-tune policy impacts.\n\n",

"Synthetic Data Generator for Training Models\n
Purpose: Generate synthetic datasets for training AI models in cases where real data is scarce or sensitive, such as in healthcare, finance, or education.\n
Tools: Use GANs or Variational Autoencoders (VAEs) to generate realistic synthetic data.\n
Applications: Useful in any data-driven field where data privacy or limited data availability is an issue, allowing for model training and testing without privacy concerns\n\n",

"Customized Product Description Generator\n
Purpose: Automatically generate product descriptions based on specific attributes like material, color, and style, tailored to different target audiences or market segments.\n
Tools: Use a fine-tuned language model like GPT to generate relevant and engaging descriptions.\n
Applications: Useful for e-commerce platforms that want to quickly generate unique descriptions for large inventories\n\n", "Two", "Three", "Four"]

selected_option = st.selectbox("Select your option:", options)

if st.button("Vote"):
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
