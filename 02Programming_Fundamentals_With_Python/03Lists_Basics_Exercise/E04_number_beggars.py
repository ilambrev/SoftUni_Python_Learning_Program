donations_str = input()
beggars_count = int(input())

donations = donations_str.split(", ")
beggars_earnings = [0] * beggars_count


for i in range(len(donations)):
    current_begger_index = (i if i < len(beggars_earnings)
                            else i % len(beggars_earnings))
    beggars_earnings[current_begger_index] += int(donations[i])

print(beggars_earnings)