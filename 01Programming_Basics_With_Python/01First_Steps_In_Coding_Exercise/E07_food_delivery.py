chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15
dessert_price_percentage = 0.2
delivery_price = 2.5

chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

menus_total_price = chicken_menus * chicken_menu_price + fish_menus * \
    fish_menu_price + vegetarian_menus * vegetarian_menu_price

dessert_price = menus_total_price * dessert_price_percentage

order_price = menus_total_price + dessert_price + delivery_price

print(order_price)