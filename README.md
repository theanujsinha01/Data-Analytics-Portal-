# Data Analytics Portal

Welcome to the **Data Analytics Portal**! This web application allows users to upload datasets, perform exploratory data analysis, and visualize data through interactive charts. It is built using Streamlit, Pandas, and Plotly, making data analysis accessible and interactive.

LIVE : https://data-analytics-webtool.streamlit.app/

![Dashboard View](https://github.com/user-attachments/assets/924c6458-8c4d-43f8-b1a9-7ed05750bfc4)



## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)

## Features

1. **Dataset Upload**
   - **Supported Formats**: Upload datasets in CSV or Excel (.xlsx) format for easy access and compatibility.
   - **File Size Limit**: Supports large datasets up to 200MB for comprehensive analysis.

2. **Data Exploration**
   - **Statistical Summary**: View key statistics like count, mean, standard deviation, minimum, maximum, and percentiles for numerical columns.
   - **Top and Bottom Rows**: Quickly inspect the first and last few rows of the dataset to understand its structure.
   - **Data Types**: Identify data types for each column to understand the dataset’s composition.
   - **Column List**: Access a full list of all columns in the dataset for easy data exploration.

3. **Count Column Values**
   - **Frequency Count**: Get a count of unique values in any column to understand distribution patterns within the dataset.

4. **Group By and Aggregation**
   - **Group By Columns**: Group data by one or more columns to explore specific categories or subsets.
   - **Aggregation Functions**: Perform aggregations like `count`, `sum`, `mean`, `min`, and `max` to derive insights from grouped data.

5. **Data Visualization with Plotly**
   - **Interactive Charts**: Generate a variety of interactive charts powered by Plotly to visualize data:
     - **Bar Chart**: Compare quantities across different categories.
     - **Pie Chart**: Show proportions and percentage breakdowns.
     - **Line Chart**: Track changes over time or continuous data.
     - **Scatter Plot**: Visualize relationships between two variables.
     - **Sunburst Chart**: Represent hierarchical data for a detailed breakdown of nested categories.

These features allow for easy data exploration, analysis, and visualization without requiring complex coding skills.

## Project is Live
https://data-analytics-webtool.streamlit.app/

## Technologies Used

- **Streamlit**: Framework for building the web application interface, making it interactive and user-friendly.
- **Pandas**: Library for data manipulation and analysis, enabling data loading, cleaning, and summarizing.
- **Plotly**: Visualization library to create interactive charts like bar, pie, line, scatter, and sunburst charts.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/data-analytics-portal.git
   cd data-analytics-portal
