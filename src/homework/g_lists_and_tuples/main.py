from lists import get_lowest_list_value
from lists import get_highest_list_value

def run_option_1():
    value = []

    while True:
        user_input = input("enter a list value")

        try: 
            num= float(user_input)
            value.append(num)
        except ValueError:
            print("enter a valid number")
            continue

        if len(value)>=3:
            again = input("do you want to add more values? (y/n): ")
            if again.lower() != 'y':
                break

            lowest = get_lowest_list_value(value)
            highest = get_highest_list_value(value)

            print("list values:", value)
            print("lowest value:", lowest)
            print("highest value:", highest)
            
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


        


