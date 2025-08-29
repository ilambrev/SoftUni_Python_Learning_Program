annual_basketball_training_fee = int(input())

basketball_sneakers_price = (100 - 40) * annual_basketball_training_fee / 100
basketball_kit_price = (100 - 20) * basketball_sneakers_price / 100
basketball_price = basketball_kit_price / 4
basketball_accessories_price = basketball_price / 5

total_expenses = (annual_basketball_training_fee
                  + basketball_sneakers_price
                  + basketball_kit_price
                  + basketball_price
                  + basketball_accessories_price)

print(f'{total_expenses:.2f}')