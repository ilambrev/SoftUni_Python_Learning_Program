def loading_bar(number):
    progress_units = int(number / 10)
    progress = "%" * progress_units
    remainder = "." * (10 - progress_units)

    bar = f"[{progress}{remainder}]"

    if progress_units < 10:
        print(f"{number}% {bar}")
        print("Still loading...")
    else:
        print(f"{number}% Complete!")
        print(bar)

    return

number = int(input())

loading_bar(number)