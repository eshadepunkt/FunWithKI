import pandas as pd

# Constants
loan_amount = 280000
interest_rate = 0.06
leasing_rate = 0.14
annual_revenue = 120000
years = 4
is_term_loan = True

# Initialize the data structures for storing the results
loan_liquidity = [0] * years
leasing_liquidity = [0] * years

# Perform the calculations
for i in range(years):
    # Calculate the cumulative liquidity for the loan
    if i == 0:
        loan_liquidity[i] = annual_revenue - (loan_amount * interest_rate)
    if i == years - 1:
        loan_liquidity[i] = loan_liquidity[i-1] + annual_revenue - (loan_amount * interest_rate) - loan_amount
    else:
        loan_liquidity[i] = loan_liquidity[i-1] + annual_revenue - (loan_amount * interest_rate)
    
    # Calculate the cumulative liquidity for leasing
    leasing_liquidity[i] = leasing_liquidity[i-1] + annual_revenue - (loan_amount * leasing_rate)

# Convert the results into a DataFrame
result_df = pd.DataFrame({
    'Ende des Jahres': range(1, years + 1),
    'bei Darlehensfinanzierung (in Tausend €)': [x / 1000 for x in loan_liquidity],
    'bei Leasing (in Tausend €)': [x / 1000 for x in leasing_liquidity]
})

# Display the result
print(result_df)