from lists import get_lowest_list_value, get_highest_list_value

def run_option_1():
    values = []

    while True:
        user_input = input("Enter a list value: ")

        try:
            num = float(user_input)
            values.append(num)
        except ValueError:
            print("Enter a valid number")
            continue

        if len(values) >= 3:
            again = input("Do you want to add more values? (y/n): ")
            if again.lower() != 'y':
                break

    if values:
        lowest = get_lowest_list_value(values)
        highest = get_highest_list_value(values)

        print("List values:", values)
        print("Lowest value:", lowest)
        print("Highest value:", highest)
    else:
        print("No values entered.")

def main():
    while True:
        print("Select an option:")
        print("1. Enter list values to find lowest and highest")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            run_option_1()
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()



        


