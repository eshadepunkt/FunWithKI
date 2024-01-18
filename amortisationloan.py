import pandas as pd

# Initialwerte
schuld_jahresanfang = 210000
zinssatz = 0.05
laufzeit = 3

# Berechnung des jährlichen Tilgungsanteils
tilgungsanteil_jaehrlich = schuld_jahresanfang / laufzeit

# Erstellung der Tabelle
data = []
for jahr in range(1, laufzeit + 1):
    zinsanteil = schuld_jahresanfang * zinssatz
    zahlung_an_bank = zinsanteil + tilgungsanteil_jaehrlich
    schuld_jahresende = schuld_jahresanfang + zinsanteil - zahlung_an_bank
    
    data.append([jahr, round(schuld_jahresanfang), round(zahlung_an_bank), 
                 round(zinsanteil), round(tilgungsanteil_jaehrlich), round(schuld_jahresende)])
    
    schuld_jahresanfang = schuld_jahresende

# Erstellung eines DataFrame mit den berechneten Daten und entsprechenden Spaltennamen
df = pd.DataFrame(data, columns=["Jahr", "Schuld Jahresanfang [€]", "Zahlung an Bank [€]", 
                                 "Zinsanteil [€]", "Tilgungsanteil [€]", "Schuld Jahresende [€]"])

print(df)