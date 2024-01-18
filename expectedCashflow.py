def berechne_cashflows(absatzmenge, preis_pro_stueck, variable_kosten_pro_stueck, instandhaltungskosten, abbruchkosten, kalkulationszinssatz, investition, jahre):
    cashflows = []
    for jahr in range(1, jahre + 1):
        erloes = absatzmenge * preis_pro_stueck
        variable_kosten = absatzmenge * variable_kosten_pro_stueck
        gesamtkosten = variable_kosten + instandhaltungskosten
        cashflow = erloes - gesamtkosten
        if jahr == jahre:
            cashflow -= abbruchkosten
        cashflows.append(cashflow)
    return cashflows

def berechne_barwert(cashflows, kalkulationszinssatz, investition):
    barwert = -investition
    for jahr, cashflow in enumerate(cashflows, start=1):
        barwert += cashflow / (1 + kalkulationszinssatz) ** jahr
    return barwert

def main():
    absatzmenge = 35000
    preis_pro_stueck = 6
    variable_kosten_pro_stueck = 3.5
    instandhaltungskosten = 7000
    abbruchkosten = 12000
    kalkulationszinssatz = 0.10
    investition = 130000
    jahre = 4

    cashflows = berechne_cashflows(absatzmenge, preis_pro_stueck, variable_kosten_pro_stueck, instandhaltungskosten, abbruchkosten, kalkulationszinssatz, investition, jahre)
    barwert = berechne_barwert(cashflows, kalkulationszinssatz, investition)

    print("Jahr | Cashflow (€)")
    print("---- | ------------")
    for jahr, cashflow in enumerate(cashflows, start=1):
        print(f"{jahr}  | {cashflow:.2f}")
    print(f"Barwert der Investition: {barwert:.2f} €")

if __name__ == "__main__":
    main()
