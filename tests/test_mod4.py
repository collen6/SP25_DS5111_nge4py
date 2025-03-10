import sys
import os
import numpy as np
import matplotlib.pyplot as plt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bin.sample_code import plot_regression_line  # ✅ Correct function

def test_plot_regression_line():
    # Sample data
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 5, 4, 5])
    b = [1, 0.8]  # Example coefficients

    # Test if function runs without errors
    try:
        plot_regression_line(x, y, b)
        assert True  # ✅ If it runs without errors, the test passes
    except Exception as e:
        assert False, f"plot_regression_line() raised an error: {e}"
