book_pages = int(input())
pages_read_per_hour = int(input())
days_for_reading = int(input())

hours_for_reading_per_day = book_pages // pages_read_per_hour // days_for_reading

print(hours_for_reading_per_day)