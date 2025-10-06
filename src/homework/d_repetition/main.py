from repetition import get_factorial, sum_odd_numbers

def get_int_in_range(prompt: str, lo: int, hi: int) -> int:
    """
    Prompt until an integer in [lo, hi] is provided.
    """
    while True:
        try:
            val = int(input(prompt).strip())
            if lo <= val <= hi:
                return val
            print(f"Please enter an integer between {lo} and {hi}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    while True:
        print("\nHomework 4 Menu")
        print("1-Factorial")
        print("2-Sum odd numbers")
        print("3-Exit")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            # 1 < n < 10  (you said greater than 0 and less than 10)
            n = get_int_in_range("Enter an integer (1-9): ", 1, 9)
            result = get_factorial(n)
            print(f"{n}! = {result}")

        elif choice == "2":
            # 0 < n < 100  (greater than 0 and less than 100)
            n = get_int_in_range("Enter an integer (1-99): ", 1, 99)
            result = sum_odd_numbers(n)
            print(f"Sum of odd numbers up to {n} = {result}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
