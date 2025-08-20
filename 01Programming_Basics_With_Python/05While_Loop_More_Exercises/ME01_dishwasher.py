detergent_bottles = int(input())

detergent_bottle_quantity_in_ml = 750
detergent_for_plate_in_ml = 5
detergent_for_pot_in_ml = 15

loads_counter = 0
detergent_quantity = detergent_bottles * detergent_bottle_quantity_in_ml
plates_count = 0
pots_count = 0

input_line = input()

while input_line != 'End':
    loads_counter += 1
    number_of_dishes = int(input_line)

    if loads_counter % 3 == 0:
        detergent_quantity -= number_of_dishes * detergent_for_pot_in_ml
        pots_count += number_of_dishes
    else:
        detergent_quantity -= number_of_dishes * detergent_for_plate_in_ml
        plates_count += number_of_dishes
    
    if detergent_quantity < 0:
        print(f'Not enough detergent, {-detergent_quantity} ml. more necessary!')
        break

    input_line = input()

else:
    print('Detergent was enough!')
    print(f'{plates_count} dishes and {pots_count} pots were washed.')
    print(f'Leftover detergent {detergent_quantity} ml.')