# Machine Learning Group Project: Ironhack Week 7

## Team Members (listed alphabetically)

- Hoang Le Duc
- Raynard Flores
- Bryan Frank
- Alex Lopez
- Josean Maldonado

## Project Purpose

The purpose of this project was to apply skills gained from in-class lessons and labs regarding Machine Learning in Python. We chose to apply these skills to seek to build the best model possible for predicting power flows based on weather conditions, month of the year, day of the week, and time of the day. 

## Technologies

Most of our work was done in Python, and we relied heavily on packages such as pandas, numpy, seaborn, matplotlib and sklearn. 

## Our Dataset

This project focused on creating the best predictive model possible for power consumption in different zones of Tetouan City. We pulled data for this project from the University of California Irvine Machine Learning Repository (UCIML Repo). Our dataset originally consisted of information collected every 10 minutes beginning Jan 1, 2017 and ending Dec 31, 2017. Information collected included weather conditions (temperature, humidity, and windspeed), general and diffuse electricity flows, and power consumption in 3 different zones of Tetouan City. We were drawn to this dataset because of the realworld application of using data such as this to build a predictive model. A similar model could be useful (if similar data were collected) for any city in the world that struggles with maintaining power supply, as it would allow them to plan how to best distribute power at times of peak usage and need. 

## Cleaning 

All cleaning activities for this dataset were conducted in the data_cleaning_nb.ipynb Python notebook. Relevant cleaning actions were then transferred into a plain python file (data_cleaning.py) to be used as a script. When opening the "Machine Learning.ipynb", the initial cell will pull cleaned and prepared data from the data cleaning script file. 

Our data had no nulls or duplicates, so none need to be removed. Our data cleaning entailed the following:
- combining data provided by the UCIML Repo into a usable dataframe
- converting the timestamps provided into a useable pandas datetime
- creating categorical variables from the datetime for month of the year, day of the week, and time of day (morning, afternoon, evening, and night) before removing that column altogether
- converting the days of the week and time of day variables to boolean dummies, and then converting those booleans to integers
- simplifying naming conventions across columns
- converting Celsius to Fahrenheit

## Variables

The dependent variables we wanted to explore were the power consumption levels in Zones 1, 2, and 3 of Tetouan city.

Also included in the data cleaning notebook is a correlation heatmap of our variables to determine that none were overly correlated. We found that only the power consumption in Zones 2 and 3 were heavily correlated. We therefore consider the rest of our variables independents. 

## Data Engineering

The only data engineering performed in the Machine Learning notebook (prior to building and testing our machine learning models) was min/max scaling our feature variables for better usage.

## Model Building

We initially considered all variables besides the targeted dependent variables as test variables. We also set our dataset to train on 80% of the data, and to test 20% of it. 

Of all the tests we ran initially, the best three were the AdaBoost Regression Model, the Random Forest Model, and the Gradient Boosting Model. 

