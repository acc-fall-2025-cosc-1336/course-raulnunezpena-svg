from src.homework.c_decisions.decisions import get_letter_grade

def main():
    print("Main Menu")
    print("1. Get Letter Grade")
    print("2.letter grade using switch")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ") 
  
    if choice == '1':
        num= int(input("Enter numerical grade:(0-100) "))
      
