country = input()
apparatus = input()

maximum_score = 20.0
country_score = 0.0

if country == 'Bulgaria':
    if apparatus == 'ribbon':
        country_score += 9.6 + 9.4
    elif apparatus == 'hoop':
        country_score += 9.55 + 9.75
    elif apparatus == 'rope':
        country_score += 9.5 + 9.4
elif country == 'Russia':
    if apparatus == 'ribbon':
        country_score += 9.1 + 9.4
    elif apparatus == 'hoop':
        country_score += 9.3 + 9.8
    elif apparatus == 'rope':
        country_score += 9.6 + 9.0
elif country == 'Italy':
    if apparatus == 'ribbon':
        country_score += 9.2 + 9.5
    elif apparatus == 'hoop':
        country_score += 9.45 + 9.35
    elif apparatus == 'rope':
        country_score += 9.7 + 9.15

difference_percentage = 100 * (maximum_score - country_score) / maximum_score

print(f'The team of {country} get {country_score:.3f} on {apparatus}.')
print(f'{difference_percentage:.2f}%')