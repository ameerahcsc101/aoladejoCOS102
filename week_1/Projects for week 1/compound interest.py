principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate (in percentage): "))
number_of_years = int(input("Enter the number of years: "))
compound_interest = principal_amount * (1 + interest_rate/100) ** number_of_years - principal_amount
print("Compound Interest: ", compound_interest)