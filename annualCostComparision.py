import pandas as pd

def berechne_kosten(anschaffungskosten, 
                    restwert, 
                    jahresvariable_kosten_vollkapazitaet, 
                    feste_betriebskosten, 
                    jahresnachfrage, 
                    kalkulationszinssatz, 
                    max_produktion, 
                    laufzeit):
    
    # Berechnung der jährlichen Abschreibungen
    abschreibungen_pro_jahr = (anschaffungskosten - restwert) / laufzeit
  

    # Erstellung der Tabelle
    data = []
 
    produktion = min(jahresnachfrage, max_produktion)
    variable_kosten = (produktion / max_produktion) * jahresvariable_kosten_vollkapazitaet
    kalkulatorische_zinsen = ((anschaffungskosten + restwert) / 2) * kalkulationszinssatz
    gesamtkosten = abschreibungen_pro_jahr + feste_betriebskosten + variable_kosten + kalkulatorische_zinsen
    variable_kosten_pro_stueck = variable_kosten / produktion
    data.append([round(gesamtkosten), round(variable_kosten_pro_stueck, 2)])

    # Erstellung eines DataFrame mit den berechneten Daten und entsprechenden Spaltennamen
    df = pd.DataFrame(data, columns=["Gesamtkosten [€]", "Variable Kosten pro Stück [€]"])

    return df

def main():
    # Gegebene Daten für Alternative A
    anschaffungskosten_A = 200000  # Anschaffungskosten der Maschine in Euro
    restwert_A = 5000  # Restwert der Maschine nach fünf Jahren in Euro
    jahresvariable_kosten_vollkapazitaet_A = 170000  # Jährliche variable Betriebskosten bei voller Kapazität in Euro
    feste_betriebskosten_A = 10000  # Feste Betriebskosten pro Jahr in Euro
    jahresnachfrage_A = 70000  # Jährliche Nachfrage nach Halbzeugen
    kalkulationszinssatz_A = 0.12  # Kalkulationszinssatz von 12% p.a.
    max_produktion_A = 50000  # Maximale Produktionskapazität der Maschine pro Jahr
    verkaufspreis_pro_stueck_A = 6  # Verkaufspreis pro Stück in Euro
    laufzeit_A = 5  # Nutzungsdauer der Maschine in Jahren

    # Gegebene Daten für Alternative B
    # Hier setzen wir die Werte für Alternative B ein. Sie können diese Werte an Ihre spezifischen Anforderungen anpassen.
    anschaffungskosten_B = 200000
    restwert_B = 5000
    jahresvariable_kosten_vollkapazitaet_B = 170000
    feste_betriebskosten_B = 10000
    jahresnachfrage_B = 70000
    kalkulationszinssatz_B = 0.12
    max_produktion_B = 50000
    verkaufspreis_pro_stueck_B = 6
    laufzeit_B = 5

    # Berechnung der Kosten für Alternative A und B
    kosten_A = berechne_kosten(anschaffungskosten_A, restwert_A, jahresvariable_kosten_vollkapazitaet_A, feste_betriebskosten_A, jahresnachfrage_A, kalkulationszinssatz_A, max_produktion_A, laufzeit_A)
    kosten_B = berechne_kosten(anschaffungskosten_B, restwert_B, jahresvariable_kosten_vollkapazitaet_B, feste_betriebskosten_B, jahresnachfrage_B, kalkulationszinssatz_B, max_produktion_B, laufzeit_B)

    print("Kosten für Alternative A:")
    print(kosten_A)
    print("\nKosten für Alternative B:")
    print(kosten_B)

if __name__ == "__main__":
    main()
