def get_letter_grade(numerical_grade:int)->str:
    if 90 <= numerical_grade <= 100:
        return "A"
    elif 80 <= numerical_grade <= 90:
        return "B"
    elif 70 <= numerical_grade <= 80:
        return "C"
    elif 60 <= numerical_grade <= 70:
        return "D"
    elif 0 <= numerical_grade <= 60:
        return "F"
    else:
        return "Invalid grade"

    