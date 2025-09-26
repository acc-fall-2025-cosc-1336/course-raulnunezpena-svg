from src.homework.c_decisions.decisions import get_letter_grade

def main():
    print("MAIN MENU")
    print("1 - Letter grade using if")
    print("2 - Letter grade using switch")
    print("3 - Exit")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        num = int(input("Enter numerical grade (0-100): "))
        print(get_letter_grade(num) if 0 <= num <= 100 else "Number out of range")

    elif choice == "2":
        num = int(input("Enter numerical grade (0-100): "))
        match num:
            case n if 90 <= n <= 100:
                print("A")
            case n if 80 <= n <= 89:
                print("B")
            case n if 70 <= n <= 79:
                print("C")
            case n if 60 <= n <= 69:
                print("D")
            case n if 0 <= n <= 59:
                print("F")
            case _:
                print("Number out of range")

    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()

    main()
