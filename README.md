# Airbnb Data Analysis with MongoDB Atlas and Visualization Tools

## Project Overview

This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends. The objectives are to:

1. Establish a MongoDB connection, retrieve the Airbnb dataset, and ensure efficient data retrieval for analysis.
2. Clean and prepare the dataset, addressing missing values, duplicates, and data type conversions for accurate analysis.
3. Develop a Streamlit web application with interactive maps showcasing the distribution of Airbnb listings, allowing users to explore prices, ratings, and other relevant factors.
4. Conduct price analysis and visualization, exploring variations based on location, property type, and seasons using dynamic plots and charts.
5. Analyze availability patterns across seasons, visualizing occupancy rates and demand fluctuations using suitable visualizations.
6. Investigate location-based insights by extracting and visualizing data for specific regions or neighborhoods.
7. Create interactive visualizations that enable users to filter and drill down into the data.
8. Build a comprehensive dashboard using Tableau or Power BI, combining various visualizations to present key insights from the analysis.

## Setup Instructions

### 1. Create a MongoDB Atlas Account and Load Data

1. **Create a MongoDB Atlas Account**:
    - Sign up for a MongoDB Atlas account [here](https://www.mongodb.com/cloud/atlas).
    - Follow the registration process to set up your account and create a new project.

2. **Set Up a Cluster**:
    - Within your MongoDB Atlas project, set up a cluster.
    - Choose the cloud provider and region for hosting your data, configure the cluster specifications, and create the cluster.

3. **Load the Airbnb Sample Data**:
    - Access the MongoDB Atlas dashboard and navigate to "Database Access" to create a database user with appropriate permissions.
    - Select "Network Access" to set up IP whitelisting or configure other security measures.
    - Import the Airbnb sample dataset by navigating to the "Clusters" page, clicking on your cluster, selecting the "Collections" tab, and choosing the "Load Sample Dataset" option.

### 2. Environment Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/airbnb-data-analysis.git
    cd airbnb-data-analysis
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:
    - Create a `.env` file in the root directory and add your MongoDB connection string:
    ```plaintext
    MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/test?retryWrites=true&w=majority
    ```

## Running the Project

### 1. MongoDB Connection and Data Retrieval

Establish a connection to your MongoDB Atlas database using the provided connection string. Retrieve the Airbnb dataset from your cluster and load it into a DataFrame for analysis.

### 2. Data Cleaning and Preparation

Handle missing values by either filling or dropping them as necessary. Remove any duplicate records from the dataset. Transform the data types of relevant columns to ensure accurate analysis, such as converting prices from string to numeric values.

### 3. Geospatial Visualization with Streamlit

Develop a Streamlit web application to visualize the geospatial data. Convert the dataset into a GeoDataFrame and create an interactive map using Folium, displaying the distribution of Airbnb listings. The map allows users to explore different aspects such as prices and ratings.

### 4. Price Analysis and Visualization

Analyze how prices vary across different locations and property types. Use visualization libraries like Matplotlib and Seaborn to create dynamic plots, such as box plots and scatter plots, to illustrate these variations and identify trends.

### 5. Availability Analysis by Season

Examine the seasonal availability patterns of Airbnb listings. Convert the relevant date columns to datetime format and analyze the occupancy rates and booking patterns over different months. Visualize these trends using line charts or heatmaps.

### 6. Location-Based Insights

Investigate price variations across specific regions or neighborhoods. Use MongoDB aggregation queries to extract relevant information and analyze it. Visualize these insights with appropriate charts to highlight regional differences.

### 7. Interactive Visualizations

Develop interactive visualizations using libraries like Plotly. Allow users to filter and drill down into the data based on their preferences, such as exploring specific regions, property types, or time periods.

### 8. Dashboard Creation

Import the cleaned dataset into visualization tools like Tableau or Power BI. Create a comprehensive dashboard combining various visualizations, such as maps, charts, and tables, to present key insights from the analysis in an integrated and interactive manner.

## Conclusion

This project provides a comprehensive analysis of Airbnb data using MongoDB Atlas, Python, and visualization tools like Streamlit and Tableau/Power BI. By following the steps outlined, you can gain valuable insights into Airbnb listings, pricing variations, and availability patterns.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- MongoDB Atlas for providing a robust and scalable database solution.
- Streamlit for the easy-to-use web application framework.
- Plotly for interactive plotting capabilities.
- The open-source community for continuous support and contributions.

Feel free to contribute to this project by opening issues or submitting pull requests. Your feedback and contributions are highly appreciated!
