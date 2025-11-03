def grade_to_words(grade):
    text = ""

    if 2.0 <= grade <= 2.99:
        text = "Fail"
    elif 3.0 <= grade <= 3.49:
        text = "Poor"
    elif 3.5 <= grade <= 4.49:
        text = "Good"
    elif 4.5 <= grade <= 5.49:
        text = "Very Good"
    elif 5.5 <= grade <= 6.0:
        text = "Excellent"

    return text

grade = float(input())

print(grade_to_words(grade))