#from src.homework.c_decisions.decisions import get_letter_grade

def test_get_letter_grade():
    assert get_letter_grade(95) == "A"
    assert get_letter_grade(85) == "B"
    assert get_letter_grade(75) == "C"
    assert get_letter_grade(65) == "D"
    assert get_letter_grade(50) == "F"
    # edge cases
    assert get_letter_grade(100) == "A"
    assert get_letter_grade(0) == "F"
    assert get_letter_grade(-5) == "Invalid grade"
    assert get_letter_grade(105) == "Invalid grade"