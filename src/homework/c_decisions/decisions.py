def(get_letter_grade(numerical_grade: float) -> str:
    """Convert a numerical grade into a letter grade.

    Letter grades are assigned as follows:
    - 90 and above: 'A'
    - 80 to 89: 'B'
    - 70 to 79: 'C'
    - 60 to 69: 'D'
    - Below 60: 'F'

    Args:
        numerical_grade (float): The numerical grade to convert.

    Returns:
        str: The corresponding letter grade.
    """
    if numerical_grade >= 90:
        return 'A'
    elif numerical_grade >= 80:
        return 'B'
    elif numerical_grade >= 70:
        return 'C'
    elif numerical_grade >= 60:
        return 'D'
    else:
        return 'F'
    