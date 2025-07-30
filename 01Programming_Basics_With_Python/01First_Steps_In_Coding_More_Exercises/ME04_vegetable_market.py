eur_bgn = 1.94
vegetables_price_bgn = float(input())
fruits_price_bgn = float(input())
vegetables_amoutn = int(input())
fruits_amount = int(input())

income = (vegetables_amoutn * vegetables_price_bgn +
          fruits_amount * fruits_price_bgn) / eur_bgn

print(f'{income:.2f}')