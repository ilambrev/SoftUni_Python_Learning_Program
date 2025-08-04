from math import floor, ceil

vineyard_area_in_sq_meters = int(input())
grape_harvest_per_sq_meter = float(input())
required_amount_of_wine_in_liters = int(input())
workers_number = int(input())

grape_harvest_percentage_for_wine = 40
grape_amount_in_kg_for_one_liter_of_vine = 2.5

grape_harvest = (grape_harvest_per_sq_meter 
                 * vineyard_area_in_sq_meters)

grape_harvest_for_wine = (grape_harvest 
                          * grape_harvest_percentage_for_wine / 100)

wine_production_in_liters = (grape_harvest_for_wine
                             / grape_amount_in_kg_for_one_liter_of_vine)

difference = wine_production_in_liters - required_amount_of_wine_in_liters

if (difference < 0):
    print(f'It will be a tough winter! More {floor(abs(difference))} liters wine needed.')
else:
    wine_per_worker = difference / workers_number
    print(f'Good harvest this year! Total wine: {floor(wine_production_in_liters)} liters.')
    print(f'{ceil(difference)} liters left -> {ceil(wine_per_worker)} liters per person.')