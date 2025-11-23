from src.homework.g_lists_and_tuples import get_lowest_list_value, get_highest_list_value

def run_option_1()
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
            
        


