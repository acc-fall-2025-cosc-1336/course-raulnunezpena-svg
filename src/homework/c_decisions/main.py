from src.homework.c_decisions.decisions import get_letter_grade

def main():
    print("Main Menu")
    print("1. Get Letter Grade")
    print("2.letter grade using switch")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ") 
  
    if choice == '1':
        num= int(input("Enter numerical grade:(0-100) "))
        print(get_letter_grade(num)if 0<=num<=100 else "Invalid grade")

    elif choice == '2':
        num= int(input("Enter numerical grade:(0-100) "))
        match num:
            case n if 90 <= n <= 100:
                print("A")
            case n if 80 <= n < 90:
                print("B")
            case n if 70 <= n < 80:
                print("C")
            case n if 60 <= n < 70:
                print("D")
            case n if 0 <= n < 60:
                print("F")
   else: print("Number out of range")

    elif choice == '3':
        print("Goodbye!")

else("invalid choice. Please select a valid option.")

if __name__ == "__main__":
      
