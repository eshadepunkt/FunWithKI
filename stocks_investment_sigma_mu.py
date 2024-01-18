import math

# Gegebene Werte
capital = 23000             # Gegebenes Kapital
price_A = 41.20             # Preis der Aktie A
price_B = 87.50             # Preis der Aktie B
mu_A = 0.10                 # Erwartete Rendite der Aktie A
mu_B = 0.05                 # Erwartete Rendite der Aktie B
sigma_A = 0.30              # Risiko (Standardabweichung) der Aktie A
sigma_B = 0.19              # Risiko (Standardabweichung) der Aktie B
return_mean = 0.06          # Erwartete Rendite des Portfolios - Erwarte Rendite der Aktie B
return_deviation = 0.0140   # Standardabweichung der Rendite des Portfolios
p = 0                       # Korrelationskoeffizient - 0 keine Korrelation, 1 perfekte positive Korrelation, -1 perfekte negative Korrelation
days_of_trading = 250       # Anzahl der Handelstage
max_risk = 0.25             # Maximales Risiko des Portfolios

# a) Risiko und Rendite des Portfolios mit dem kleinstmöglichen Risiko

anteil_A = (sigma_B**2 - p * sigma_A * sigma_B) / (sigma_A**2 + sigma_B**2 - 2 * p * sigma_A * sigma_B)  # Anteil der Aktie A im Portfolio
anteil_B = 1 - anteil_A  # Anteil der Aktie B im Portfolio

risk = math.sqrt(anteil_A**2 * sigma_A**2 + anteil_B**2 * sigma_B**2 + 2 * anteil_A * anteil_B * sigma_A * sigma_B * p)  # Risiko des Portfolios
return_with_correlation = mu_B + ( (mu_A - mu_B) * (sigma_B**2 - p * sigma_A * sigma_B) / (sigma_A**2 + sigma_B**2 - 2 * p * sigma_A * sigma_B) )  # Rendite des Portfolios

print(f"Risiko des Portfolios: {risk* 100:.2f} %")
print(f"Rendite des Portfolios: {return_with_correlation*100:.2f} %")

# b) Anteil am Vermögensportfolio A & B
XA = (return_with_correlation - mu_B) / (mu_A - mu_B)  # Anteil der Aktie A im Portfolio
XB = 1 - XA  # Anteil der Aktie B im Portfolio

print(f"Anteil der Aktie A im Portfolio: {XA}")
print(f"Anteil der Aktie B im Portfolio: {XB}")

# c) Anzahl Aktien A&B bei geringstem Risiko bei gegebenen Kapital
num_stocks_A = (XA * capital) / price_A  # Anzahl der Aktien A
num_stocks_B = (XB * capital) / price_B  # Anzahl der Aktien B

# round both stocks to the nearest integer

num_stocks_A = round(num_stocks_A)
num_stocks_B = round(num_stocks_B)

print(f"Anzahl der Aktien A: {num_stocks_A}")
print(f"Anzahl der Aktien B: {num_stocks_B}")