import pandas as pd
import math as math

# Gegebene Werte
current_production = 300000  # Aktuelle Produktion pro Monat
current_machines = 30  # Anzahl der derzeitigen Maschinen
machine_cost = 45000  # Kosten einer neuen Maschine
depreciation_years = 5  # Abschreibungsjahre für eine neue Maschine

# Berechnung der Produktionskapazität pro Maschine
production_per_machine = current_production / current_machines

# Lohmann-Ruchti-Effekt
capacity_increase_factor = 2  / ( 1 + (1 / depreciation_years))

print(f"Der Lohmann-Ruchti-Effekt beträgt: {capacity_increase_factor:.2f}")
print(f"Die Anzahl an Machinen im eingeschwungenen Zustand beträgt: {math.floor(current_machines * capacity_increase_factor):.2f})")

# Gegebene Daten
data = {
    "Jahr": [1, 2, 3, 4],
    "Maschinen zu Beginn": [30, 36, 43, 51],
    "Anschaffungskosten (Tausend €)": [1350, 1620, 1935, 2295],
    "Abschreibungen (Tausend €)": [270, 324, 387, 459],
    "Verfügbare liquide Mittel (Tausend €)": [270, 324, 396, 495],
    "Gekaufte Maschinen": [6, 7, 8, 11],
    "Abgehende Maschinen": [0, 0, 0, 0],
    "Verbleibende liquide Mittel (Tausend €)": [0, 9, 36, 0],
    "Anzahl Maschinen zum Jahresende": [36, 43, 51, 62]
}

df = pd.DataFrame(data)

def calculate_followup_years(df, machine_cost, depreciation_years, followup_years):
    total_machines_deprecated = 0
    for i in range(followup_years):
        last_row = df.iloc[-1]
        new_row = last_row.copy()
        new_row["Jahr"] += 1
        new_row["Maschinen zu Beginn"] = last_row["Anzahl Maschinen zum Jahresende"] 
        new_row["Anschaffungskosten (Tausend €)"] = new_row["Maschinen zu Beginn"] * machine_cost
        new_row["Abschreibungen (Tausend €)"] = new_row["Anschaffungskosten (Tausend €)"] / depreciation_years
        new_row["Verfügbare liquide Mittel (Tausend €)"] = last_row["Verbleibende liquide Mittel (Tausend €)"] + new_row["Abschreibungen (Tausend €)"]
        new_row["Gekaufte Maschinen"] = new_row["Verfügbare liquide Mittel (Tausend €)"] // machine_cost
        if new_row["Jahr"] >= depreciation_years:
           machines_deprecated = df.loc[df["Jahr"] == new_row["Jahr"]+1 - depreciation_years, "Maschinen zu Beginn"].values[0] - total_machines_deprecated
           total_machines_deprecated += machines_deprecated
           new_row["Abgehende Maschinen"] = machines_deprecated
        else:
            new_row["Abgehende Maschinen"] = 0
        new_row["Verbleibende liquide Mittel (Tausend €)"] = new_row["Verfügbare liquide Mittel (Tausend €)"] - new_row["Gekaufte Maschinen"] * machine_cost
        new_row["Anzahl Maschinen zum Jahresende"] = new_row["Maschinen zu Beginn"] + new_row["Gekaufte Maschinen"] - new_row["Abgehende Maschinen"]
        df = df.append(new_row, ignore_index=True)
    return df

# Verwenden Sie die Funktion, um die Tabelle für eine bestimmte Anzahl von Folgejahren zu berechnen
machine_cost = machine_cost / 1000  # Kosten einer Maschine in Tausend €
depreciation_years = 5  # Abschreibungsjahre für eine Maschine
followup_years = 3  # Anzahl der Folgejahre, die berechnet werden sollen

df = calculate_followup_years(df, machine_cost, depreciation_years, followup_years)
print(df)
