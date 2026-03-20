import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():

    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # -------- Line 1: Using all data --------
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    res = linregress(x, y)

    # Predict up to 2050
    x_pred = range(df["Year"].min(), 2051)
    y_pred = res.slope * x_pred + res.intercept

    plt.plot(x_pred, y_pred, color="red")

    # -------- Line 2: From year 2000 onwards --------
    df_recent = df[df["Year"] >= 2000]

    x2 = df_recent["Year"]
    y2 = df_recent["CSIRO Adjusted Sea Level"]

    res2 = linregress(x2, y2)

    x_pred2 = range(2000, 2051)
    y_pred2 = res2.slope * x_pred2 + res2.intercept

    plt.plot(x_pred2, y_pred2, color="green")

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save and return
    plt.savefig("sea_level_plot.png")
    return plt.gca()
