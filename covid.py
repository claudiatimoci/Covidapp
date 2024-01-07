

import os
import sys
import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
import openai
from datetime import datetime

# Add the parent directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)

# Now import the module
from pipelines import DataBase

# Set up your OpenAI API key
openai.api_key = '....'

# Path to the database file
db_path = 'C:/Users/timoc/Downloads/WebCrawler/WebCrawler/spiders/Covid'

# Create an instance of the DataBase class
data_base = DataBase(db_path)
df = pd.DataFrame(data_base.select_table('CovidCases'))

# Function to get or create SessionState
def get_session_state():
    return st.session_state

def generate_news_prompt(dataframe):
    prompt = "COVID-19 Update:\n\n"
    for index, row in dataframe.iterrows():
        prompt += f"In {row['country']}, there have been {row['deaths']} deaths with a death rate of {row['death_rate']}%, totaling {row['total_cases']} confirmed cases.\n\n"
    return prompt

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300  # Adjust the number of tokens based on the desired length of generated text
    )
    return response.choices[0].text.strip()

def main():
    session_state = st.session_state

    if 'selected_countries_history' not in session_state:
        session_state.selected_countries_history = []

    st.set_page_config(
        page_title="Covid map",
        page_icon="favicon.ico"
    )

    st.title("Coronavirus deaths by country")
    # Your description or content here

    st.sidebar.title("Timoci Claudia")

    page = st.sidebar.selectbox(
        "Select Page",
        ["Homepage", "History"]
    )

    if page == "Homepage":
        st.write(
        "This application allows you to download a CSV with the total number of COVID cases in the world. "
        "In the table below, countries can be reordered by alphabetical order, deaths, death rate, and total cases."
        "I chose the BBC page (https://www.bbc.com/news/world-51235105) because it contains reliable information"
        "I chose scrapy because it is a library that I have never used before and it was an opportunity to learn it now, also considering the fact that it is recommended to use this library when working in a team."
    )
        st.write(df)  # Display the whole table by default
        selected_countries = st.multiselect('Select Countries', df['country'].unique())
        if st.button('Display Selection'):
            if selected_countries:
                selected_data = df[df['country'].isin(selected_countries)]
                st.write(selected_data)
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                session_state.selected_countries_history.append((selected_countries, now))

        if st.button("Generate COVID-19 News"):
            news_prompt = generate_news_prompt(df)
            generated_text = generate_text(news_prompt)
            st.write("COVID-19 News Update:")
            st.write(generated_text)

            try:
                # Try to get coordinates for a location
                location = geolocator.geocode("New York City")
        
                if location:
                    st.map(location.point)
                else:
                    st.write("Location not found.")
            except Exception as e:
                st.write("Error:", e)
                st.write("Map display not available.")
    

    elif page == "History":
        st.title("Selection History")
        for selected_countries, timestamp in session_state.selected_countries_history:
            st.write(f"{timestamp}: {selected_countries}")

    geolocator = Nominatim(user_agent="my_geocoder")



if __name__ == "__main__":
    main()



