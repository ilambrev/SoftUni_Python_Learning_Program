tickets = [ticket.strip() for ticket in input().split(", ")]

def check_if_ticket_is_wining(ticket):
    symbols = "@#$^"
    result = ""
    first_half = ticket[:10]
    second_half = ticket[10:]

    for symbol in symbols:
        for i in range(10, 5, -1):
            pattern = symbol * i

            if pattern in first_half and pattern in second_half:
                result = pattern
                break

        if result:
            break

    return result

for ticket in tickets:
    if not len(ticket) == 20:
        print("invalid ticket")
        continue

    result = check_if_ticket_is_wining(ticket)

    if len(result) == 10:
        print(f'ticket "{ticket}" - {len(result)}{result[0]} Jackpot!')
    elif len(result) > 5:
        print(f'ticket "{ticket}" - {len(result)}{result[0]}')
    else:
        print(f'ticket "{ticket}" - no match')