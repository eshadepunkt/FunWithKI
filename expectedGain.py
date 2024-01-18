import pandas as pd

# Gegebene Daten
data = {
    'Probabilities': [0.03, 0.09, 0.13, 0.19, 0.30, 0.26],
    'Revenues': [100, 190, 420, 540, 660, 840]
}
df = pd.DataFrame(data)

# Kosten
costs = 330

# Berechnung der Gewinne durch Subtraktion der Kosten von den Einnahmen
df['Gains'] = df['Revenues'] - costs

# Berechnung des erwarteten Gewinns
expected_gain = (df['Probabilities'] * df['Gains']).sum()

# Berechnung der Varianz des Gewinns
variance_gain = (df['Probabilities'] * (df['Gains'] - expected_gain)**2).sum()

# Berechnung der Standardabweichung des Gewinns
std_deviation_gain = variance_gain**0.5

# Berechnung des Variationskoeffizienten des Gewinns
coefficient_of_variation = std_deviation_gain / expected_gain

print(f"Erwartungswert: {round(expected_gain,4)}, Standardabweichung: {round(std_deviation_gain,4)}, Variationskoeffizient: {round(coefficient_of_variation,4)}")
