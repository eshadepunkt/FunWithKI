import numpy as np

# Given data from the image
probabilities = np.array([3, 9, 13, 19, 30, 26]) / 100  # Probabilities in fraction
revenues = np.array([100, 190, 420, 540, 660, 840])  # Revenues in thousand €
costs = 330  # Costs in thousand €

# Calculate gains by subtracting costs from revenues
gains = revenues - costs

# Calculate the expected value of the gain
expected_gain = np.sum(probabilities * gains)

# Calculate the variance of the gain
variance_gain = np.sum(probabilities * (gains - expected_gain)**2)

# Calculate the standard deviation of the gain
std_deviation_gain = np.sqrt(variance_gain)

# Calculate the coefficient of variation of the gain
coefficient_of_variation = std_deviation_gain / expected_gain

print(expected_gain, std_deviation_gain, coefficient_of_variation)
