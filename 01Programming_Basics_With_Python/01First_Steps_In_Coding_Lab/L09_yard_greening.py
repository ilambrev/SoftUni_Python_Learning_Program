price_per_sq_meter = 7.61
landscaping_area = float(input())
discount_percentage = 18

total_price = landscaping_area * price_per_sq_meter
discount = total_price * discount_percentage / 100
total_price_with_discount = total_price - discount

print(f'The final price is: {total_price_with_discount} lv.')
print(f'The discount is: {discount} lv.')