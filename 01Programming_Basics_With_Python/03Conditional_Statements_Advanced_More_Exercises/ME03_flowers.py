chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
is_it_holiday = input()

holiday_price_increase_percentage = 15
arranging_bouquet_price = 2.0

chrysanthemum_price = 0.0
rose_price = 0.0
tulip_price = 0.0

if season == 'Spring' or season == 'Summer':
    chrysanthemum_price = 2.0
    rose_price = 4.1
    tulip_price = 2.5
elif season == 'Autumn' or season == 'Winter':
    chrysanthemum_price = 3.75
    rose_price = 4.5
    tulip_price = 4.15

bouquet_price = (chrysanthemums_count * chrysanthemum_price
                 + roses_count * rose_price
                 + tulips_count * tulip_price)

if is_it_holiday == 'Y':
    bouquet_price *= (100 + 15) / 100

if tulips_count > 7 and season == 'Spring':
    bouquet_price *= (100 - 5) / 100

if roses_count >= 10 and season == 'Winter':
    bouquet_price *= (100 - 10) / 100

flowers_count = chrysanthemums_count + roses_count + tulips_count

if flowers_count > 20:
    bouquet_price *= (100 - 20) / 100

bouquet_price += arranging_bouquet_price

print(f'{bouquet_price:.2f}')