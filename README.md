# Olympics App

## Demo

![Olympics App](olympics-demo.gif)


## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Data Source](#data-source)
- [Libraries Used](#libraries-used)
- [App Pages](#app-pages)
- [Important Notes](#important-notes)
- [Feedback and Contribution](#feedback-and-contribution)

## Introduction

Welcome to the Olympics Data Analysis App! This web application is designed to analyze the historical data of Olympic athletes and medal results spanning 120 years from Athens 1896 to Rio 2016. It provides insights into various aspects of the Olympics, such as medal tallies, overall analysis, country-wise performance, and athlete-wise analysis.

## Installation

Before running the app, you need to install the required libraries. Please ensure you have the following libraries installed:

```
pip install streamlit pandas plotly matplotlib seaborn
```

## How to Use

To run the app, navigate to the directory containing the code and execute the following command in the terminal:

```
streamlit run app.py
```

The app will launch in your default web browser, and you can interact with it using the user interface.

## Data Source

The dataset used in this app was obtained from Kaggle and includes basic bio data on athletes and medal results from Athens 1896 to Rio 2016. You can access the dataset from the following link:

[Kaggle Dataset - 120 Years of Olympic History: Athletes and Results](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)

## Libraries Used

The app is built using several Python libraries to process and visualize the data:

- **Streamlit**: Used to create the web application and user interface.
- **Pandas**: Utilized for data manipulation and analysis.
- **Plotly**: Used for interactive and visually appealing plots and charts.
- **Matplotlib**: Employed for creating static visualizations.
- **Seaborn**: Utilized for creating statistical visualizations.

## App Pages

The app is divided into four pages, each offering specific analysis and insights:

1. **Medal Tally**: This page allows you to search for medal tallies based on the selected country and the year of the Olympic Games.

2. **Overall Analysis**: On this page, you can explore various overall statistics related to the Olympics. It includes the most successful athletes by sports name, the number of countries that hosted the Olympics over the years, the number of countries that participated in the Olympics over the years, and the number of athletes who participated in the Olympics over the years.

3. **Country-wise Analysis**: In this section, you can analyze the performance of a specific country in the Olympics. You can select a country to view its medal tally over the years, discover the sports in which the country performed well, and see a table of its top athletes.

4. **Athlete-wise Analysis**: This page offers insights into athlete-wise analysis. You can explore the distribution of athlete ages, the probability of winning gold medals at different ages, men vs. women participation over the years, and the height vs. weight distribution of athletes.

## Important Notes

- The data used in this app is based on historical Olympic records up to the Rio 2016 Olympics. For more recent data, you may need to update the dataset accordingly.

- The app is meant for educational and exploratory purposes only. The analysis and insights provided should not be considered official or exhaustive.

## Feedback and Contribution

Your feedback and contributions are highly appreciated. If you have any suggestions, improvements, or feature requests, please feel free to raise an issue or create a pull request on the GitHub repository.
