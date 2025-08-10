open_tabs_number = int(input())
salary = int(input())

fine_for_facebook = 150
fine_for_instagram = 100
fine_for_reddit = 50

for _ in range(open_tabs_number):
    open_tab = input()
    if open_tab == 'Facebook':
        salary -= fine_for_facebook
    elif open_tab == 'Instagram':
        salary -= fine_for_instagram
    elif open_tab == 'Reddit':
        salary -= fine_for_reddit

    if salary <= 0:
        print('You have lost your salary.')
        break
else:
    print(salary)