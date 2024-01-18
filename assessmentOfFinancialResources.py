# Gegebene Daten
restlaufzeit = 6  # Restlaufzeit in Jahren
zinsen = 4  # Jährliche Zinszahlungen in €
rueckzahlungskurs = 100  # Rückzahlungskurs in €
aktueller_preis = 109  # Aktueller Preis in €

# Berechnung der einfachen Effektivverzinsung
effektivverzinsung = ((zinsen * restlaufzeit + rueckzahlungskurs - aktueller_preis) / (restlaufzeit * aktueller_preis)) * 100

effektivverzinsung_output = f"Die einfache Effektivverzinsung beträgt {effektivverzinsung:.2f} %."
print(f"{effektivverzinsung_output}")


def berechne_dividendenwachstum(aktueller_preis, naechste_dividende, zinsniveau):
    """
    Berechnet das erwartete Dividendenwachstum basierend auf dem Dividendendiskontierungsmodell.

    :param aktueller_preis: Der aktuelle Preis der Aktie.
    :param naechste_dividende: Die Dividende, die im nächsten Jahr erwartet wird.
    :param zinsniveau: Das aktuelle Zinsniveau als Dezimalzahl (z.B. 0.07 für 7%).
    :return: Das erwartete Dividendenwachstum als Dezimalzahl.
    """
    # Dividendendiskontierungsmodell: Preis = Dividende / (Zinsniveau - Wachstum)
    # Umgestellt nach Wachstum: Wachstum = Zinsniveau - Dividende / Preis
    wachstum = zinsniveau - (naechste_dividende / aktueller_preis)
    return wachstum

# gegebenen Daten
aktueller_preis = 180  # Aktueller Preis der Aktie in €
naechste_dividende = 4.50  # Erwartete Dividende in einem Jahr in €
zinsniveau = 0.07  # Zinsniveau pro Jahr als Dezimalzahl (7%)

# Berechnung des erwarteten Dividendenwachstums
dividendenwachstum = berechne_dividendenwachstum(aktueller_preis, naechste_dividende, zinsniveau)

dividendenwachstum_percentage = dividendenwachstum * 100  # Umwandlung in Prozent
print(f"erwartetes Dividendenwachstum: {dividendenwachstum_percentage:.2f}%")
