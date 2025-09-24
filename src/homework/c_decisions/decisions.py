def get_letter_grade(numerical_grade:int)->str:
    if numerical_grade >= 90:
        return "A"
    elif numerical_grade >= 80:
        return "B"
    elif numerical_grade >= 70:
        return "C"
    elif numerical_grade >= 60:
        return "D"
    elif numerical_grade >=59:
        return "F"
    else:
        return "Invalid grade"

    