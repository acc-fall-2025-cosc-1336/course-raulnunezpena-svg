
from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating

def main():
    print("Faculty Rating Calculator")
    try:
        options = float(input("Enter the number of 'options' (e.g., favorable responses): ").strip())
        total = float(input("Enter the total number: ").strip())
        ratio = get_options_ratio(options, total)
        rating = get_faculty_rating(ratio)
        print(f"\nRatio: {ratio:.4f}")
        print(f"Rating: {rating}")
    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
