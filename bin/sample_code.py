"""
This module provides a function to plot a regression line.
"""

import matplotlib.pyplot as plt  # Ensure plt is imported


def plot_regression_line(x, y, b):
    """
    Plots a regression line based on input x, y values, and coefficients.

    Parameters:
    x (array-like): Independent variable values.
    y (array-like): Dependent variable values.
    b (list): Regression coefficients [intercept, slope].
    """

    # Scatter plot of actual data points
    plt.scatter(x, y, color="m", marker="o", s=30, label="Actual Data")

    # Compute predicted values
    y_pred = b[0] + b[1] * x

    # Plot the regression line
    plt.plot(x, y_pred, color="g", label="Regression Line")

    # Labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Regression Line Plot')
    plt.legend()

    # Show the plot
    plt.show()
