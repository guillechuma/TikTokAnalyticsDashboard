# Import base streamlit dependency
import streamlit as st
# Import pandas to load analytics data
import pandas as pd
# Import subprocess to run tiktok script from command line
from subprocess import call
# Import plotly for viz
import plotly.express as px

# Set page width to wide
st.set_page_config(layout='wide')

# Create sidebar
st.sidebar.image('logo.png',width=150)
st.sidebar.markdown('# Tiktok Analytics')
st.sidebar.markdown("This dashboard allows you to analyse trending 📈 tiktoks using Python and Streamlit.")
st.sidebar.markdown("To get started <ol><li>Enter the <i>hashtag</i> you with to analyse</li> <li>Hit <i>Get Data</i>.</li> <li>Get analyzing</li></ol>", unsafe_allow_html=True)
st.sidebar.markdown("Author: Guillermo Chumaceiro")
st.sidebar.markdown("Adaptation and improvement of Nicholas Renotte's implementation. This version implements the V5 of TikTokApi")
st.sidebar.markdown("Watch on youtube and support Nicholas Renotte: https://www.youtube.com/watch?v=E6B3uWF-V7w")
# Input
hashtag = st.text_input('Search for a hashtag here', value='')

# Button
if st.button('Get Data'): # Trigger something
    # Run get data function in command line to write csv
    call(['python', 'tiktok.py', hashtag, '50'])

    # Load in existing data to test it out
    df = pd.read_csv('tiktokdata.csv')

    # Plotly viz here
    fig = px.histogram(df, x='author_nickname', hover_data=['desc'], y='stats_diggCount', height=300)
    st.plotly_chart(fig, use_container_width=True)

    # Split columns
    left_col, right_col = st.columns(2)

    # First Chart - video stats
    scatter1 = px.scatter(df, x='stats_shareCount', y='stats_commentCount', hover_data=['desc'], size='stats_playCount', color='stats_playCount')
    left_col.plotly_chart(scatter1, use_container_width=True)

    # Second Chart - author stats
    scatter2 = px.scatter(df, x='authorStats_videoCount', y='authorStats_heartCount', hover_data=['author_nickname'], size='authorStats_followerCount', color='authorStats_followerCount')
    right_col.plotly_chart(scatter2, use_container_width=True)



    # Show tabular dataframe on streamlit
    df