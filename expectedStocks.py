stocks_total = 100
stocks_before = 25
ratio = 6 / 3
preemptive_rights_used = 0.50



def calculate_stocks_after(stocks_before, ratio, preemptive_rights_used):
    stocks_with_preemptive_rights = stocks_before / ratio * preemptive_rights_used
    stocks_after = (stocks_before +  stocks_with_preemptive_rights) / (stocks_before * ratio + stocks_total)
    return stocks_after


def test_calculate_stocks_after():
    stocks_before = 25
    ratio = 6 / 3
    preemptive_rights_used = 0.5
    expected_stocks_after = 20.83
    epsilon = 0.1

    stocks_after = calculate_stocks_after(stocks_before, ratio, preemptive_rights_used)

    assert round(abs((stocks_after * 100) - expected_stocks_after)) < epsilon, f"Expected {expected_stocks_after}, but got {stocks_after}"

stocks_after = calculate_stocks_after(stocks_before, ratio, preemptive_rights_used)
# Run the test
test_calculate_stocks_after()

print(f"The person holds {round(stocks_after*100, 4)} stocks after the company raised their stock count.")