
import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(page_title="Airbnb", page_icon=":house:", 
                   layout="wide")

st.title(":house: Airbnb Analysis")
st.markdown("<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)

selected = option_menu(
        None,["Home", "Geospatial Analysis", "Visualization"], 
        icons=['house-fill', 'map-fill', "bar-chart-fill"], 
        menu_icon="cast", 
        default_index=0,
        orientation="horizontal",
        styles={"container": {"padding": "0!important", "background-color": "orange"},
                "icon": {"color": "red", "font-size": "1.5rem"}, 
                "nav-link": {"font-size": "1.25rem", "text-align": "left", "margin":"0px", "--hover-color": "#6F8FAF", "background-color": "orange"},
                "nav-link-selected": {"background-color": "green"}}) 

#-------------------------Home---------------------------------------------#
if selected == "Home":
    
    # Set the title of the home page
    st.title("Welcome to the Airbnb Analysis App")

    st.header("About Airbnb")
    st.markdown("""Airbnb is a global online marketplace that connects people looking to rent out their homes with those seeking accommodations. 
                Founded in 2008, Airbnb offers a diverse range of lodging options, including single rooms, entire apartments, houseboats, and even castles. 
                With its user-friendly platform, Airbnb allows hosts to list their properties and guests to find unique stays across the globe. 
                The platform has transformed the travel and hospitality industry by providing more personalized and affordable alternatives to traditional hotels, 
                fostering a sense of community and shared experiences among travelers.""")

    # Add some introductory content
    st.markdown("""
    ## Explore Airbnb Listings with Interactive Visualizations

    This interactive web application, created using Streamlit, offers a comprehensive analysis of Airbnb listings. 
    Our aim is to provide users with insightful geospatial visualizations, enabling a deeper understanding of key metrics such as prices, 
    ratings, and other relevant factors.

    ### Key Features:
    - **Geospatial Visualizations**: Explore the distribution of Airbnb listings on interactive maps.
    - **Price Analysis**: Understand how prices vary across different locations and property types.
    - **Rating Insights**: Analyze ratings to find the best places to stay.
    - **Seasonal Trends**: Discover how availability and prices fluctuate throughout the year.
    - **Interactive Filtering**: Drill down into the data based on your preferences, such as location, property type, and time period.

    ### How to Use:
    1. **Home**: Get an overview of the app and its features.
    2. **EDA (Exploratory Data Analysis)**: Dive into the data with basic exploratory analyses.
    3. **Visualization**: View detailed visualizations and interact with the data.

    This app aims to provide valuable insights for travelers looking for the best deals and hosts aiming to optimize their listings.

    ### Getting Started:
    - Use the sidebar to navigate between different sections of the app.
    - Interact with the maps and charts to explore the data in depth.

    We hope you find this tool useful and insightful. Happy exploring!
    """)
#-------------------------Geospatial Analysis---------------------------------------------#
# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/VivekS-DS/Airbnb_Data_Analysis/main/Airbnb_final_data.csv")

# Geospatial Analysis
if selected == "Geospatial Analysis":
    st.header("Geospatial Analysis")
    st.sidebar.title("Geospatial Analysis")
    price_range = st.sidebar.slider("Select Price Range", min_value=(df['price'].min()), 
                                    max_value=(df['price'].max()),  
                                    step=500.0) 
    country = st.sidebar.selectbox("Select Country",df['country'].unique())
    suburb = st.sidebar.selectbox("Select Suburb", (df[(df['country'] == country) & 
                                                       (df['price'] <= price_range)]['suburb'].unique()))
    
    
    st.subheader(country + ", " + suburb) 
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Price Distribution")
        
        fig = px.density_mapbox(df[df['country'] == country],
                        lat='latitude',
                        lon='longitude',
                        z='price',
                        radius=20,
                        zoom=10, hover_data=['name',"price"],
                        mapbox_style='open-street-map',
                        center=dict(lat=df[(df['country'] == country) & (df['suburb'] == suburb)]['latitude'].mean(),
                                    lon=df[(df['country'] == country) & (df['suburb'] == suburb)]['longitude'].mean()),
                        height=400)

        fig.update_layout(margin={"r":50,"t":50,"l":50,"b":50})
        st.plotly_chart(fig, use_container_width=True, height=200)
        
        #st.write("Price Range: ", price_range)
        price_filter = df[(df['country'] == country) & 
                          (df['suburb'] == suburb) & 
                          (df['price'] <= price_range)].index.tolist()
        
        st.table(df.loc[price_filter, 'name'].unique())

    with col2:
        st.subheader("Rating Distribution")
        fig = px.density_mapbox(df[(df['country'] == country) & (df['suburb'] == suburb)],
                        lat='latitude',
                        lon='longitude',
                        z='rating',
                        radius=20,
                        zoom=10, hover_data=['name',"rating"],
                        mapbox_style='open-street-map',
                        center=dict(lat=df[(df['country'] == country) & (df['suburb'] == suburb)]['latitude'].mean(),
                                    lon=df[(df['country'] == country) & (df['suburb'] == suburb)]['longitude'].mean()),
                        height=400, width=600)

        fig.update_layout(margin={"r":50,"t":50,"l":50,"b":50})
        st.plotly_chart(fig, use_container_width=True, height=600)


#-------------------------Visualization---------------------------------------------#

if selected == "Visualization":
    
    tab1, tab2, tab3 = st.tabs(["Price vs Location", "Price vs Property Type", "Occupancy Rate"])

    with tab1:
        #price vs location
        st.header("Price vs Location")

        country_tab1 = st.selectbox("Select Country",df['country'].unique())
        
        loc_price = df[df['country'] == country_tab1].groupby('suburb')['price'].mean().round(0)
        loc_price = loc_price.sort_values(ascending=False).nlargest(10)

        col1, col2 = st.columns(2)

        with col1:

            colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
            # Use `hole` to create a donut-like pie chart
            fig = go.Figure(data=[go.Pie(labels=loc_price.index, 
                                        values=loc_price.values, 
                                        hole=.3)])
            
            fig.update_traces(hoverinfo='label+value', 
                              textinfo='value', 
                              textfont_size=16,
                               marker=dict(colors=colors, 
                                           line=dict(color='#000000', width=1)))
            
            st.plotly_chart(fig, use_container_width=True, height=600)

        with col2:
            st.subheader(country_tab1 + " Suburbs with Highest Average Price")
            st.table(pd.DataFrame(loc_price.index, index=range(1,11)))  


    with tab2:
        st.header("Price vs Property Type")

        prop_type = st.selectbox("Select Property Type", df['property_type'].unique())

        x_prop_type = df[df['property_type'] == prop_type].groupby('country')['price'].mean()
        x_prop_type = x_prop_type.sort_values(ascending=False)

        fig = go.Figure(go.Bar(
                                x=x_prop_type,
                                y=x_prop_type.index,
                                orientation='h',
                                text=x_prop_type.round(0),
                                textposition='auto', 
                                marker=dict(color='rgba(50, 171, 96, 0.6)', 
                                            line=dict(color='rgba(50, 171, 96, 1.0)', width=1))))

            
        st.plotly_chart(fig, use_container_width=True, height=600)

    with tab3:
              
        st.header("Occupancy Rate")

        occupancy = st.selectbox("Select Time Period", ['occupancy_30',
                                                        'occupancy_60',
                                                        'occupancy_90',
                                                        'occupancy_365'])
        
        x_season_type = df.groupby('country')[occupancy].mean()
            

        fig = go.Figure(go.Bar(x=x_season_type.index,
                                y=x_season_type,
                                orientation='v',
                                text=x_season_type.round(0),
                                textposition='auto', 
                                marker=dict(color='rgba(50, 171, 96, 0.6)', 
                                            line=dict(color='rgba(50, 171, 96, 1.0)', 
                                                      width=1))))
                
        st.plotly_chart(fig, use_container_width=True, height=600)

#-----------------------------END OF CODE-------------------------------------------#
