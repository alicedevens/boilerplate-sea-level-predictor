import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    plt.scatter(x, y)


    # Create first line of best fit

# Perform linear regression
    fit1 = linregress(x, y)

# Plotting the data points
    plt.scatter(x, y)

# Sample data
    x_new = pd.Series(range(1880,2051))

# Use the slope and intercept to construct the best fit line
    y_new = fit1.intercept + fit1.slope * x_new

# Plotting the best fit line
    plt.plot(x_new, y_new)


    

    # Create second line of best fit

# Filtering the data that we want to use 
    new_df = df[df['Year'] >= 2000]
    x2 = new_df['Year']
    y2 = new_df['CSIRO Adjusted Sea Level']

# Perform linear regression
    fit2 = linregress(x2, y2) 

# Sample data
    x_newtwo = pd.Series(range(2000, 2051))

# Use the slope and intercept to construct the best fit line
    y_newtwo = fit2.intercept + fit2.slope * x_newtwo

# Plotting the best fit line
    plt.plot(x_newtwo, y_newtwo)


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()