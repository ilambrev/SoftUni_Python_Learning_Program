deposit = float(input())
deposit_term_in_months = int(input())
annual_interest_rate = float(input())

deposit_after_interest = deposit + deposit_term_in_months * \
    ((deposit * annual_interest_rate / 100) / 12)

print(deposit_after_interest)