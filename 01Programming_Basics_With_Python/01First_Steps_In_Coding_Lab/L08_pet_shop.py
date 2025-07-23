dog_food_price_per_pack = 2.5
cat_food_price_per_pack = 4

quantity_of_dog_food_packages = int(input())
quantity_of_cat_food_packages = int(input())

total_food_price = quantity_of_dog_food_packages * dog_food_price_per_pack + \
    quantity_of_cat_food_packages * cat_food_price_per_pack

print(f'{total_food_price} lv.')