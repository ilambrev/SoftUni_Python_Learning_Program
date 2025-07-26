nylon_price_per_sq_meter = 1.5
paint_price_per_liter = 14.5
paint_thinner_price_per_liter = 5.0

nylon = int(input())
paint = int(input())
paint_thinner = int(input())
hours = int(input())

additional_amount_of_nylon = 2
bags_price = 0.4

nylon_total_price = (nylon + additional_amount_of_nylon) * \
    nylon_price_per_sq_meter
paint_total_price = paint * paint_price_per_liter * 1.1
paint_thinner_total_price = paint_thinner * paint_thinner_price_per_liter

materials_total_price = nylon_total_price + \
    paint_total_price + paint_thinner_total_price + bags_price

work_price_per_hour = 0.3 * materials_total_price

repair_costs = materials_total_price + hours * work_price_per_hour

print(repair_costs)