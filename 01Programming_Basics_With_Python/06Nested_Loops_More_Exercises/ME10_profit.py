one_lev_coin_count = int(input())
two_leva_coin_count = int(input())
five_leva_banknote_count = int(input())
target_sum = int(input())

for one_lev_coins in range(one_lev_coin_count + 1):
    for two_leva_coins in range(two_leva_coin_count + 1):
        for five_leva_banknotes in range(five_leva_banknote_count + 1):
            sum = (one_lev_coins * 1
                   + two_leva_coins * 2
                   + five_leva_banknotes * 5)
            
            if sum == target_sum:
                print(f'{one_lev_coins} * 1 lv. + {two_leva_coins} * 2 lv. + {five_leva_banknotes} * 5 lv. = {sum} lv.')