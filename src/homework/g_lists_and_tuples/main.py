from lists import get_p_distance_matrix

def get_dna_lists_from_user():
    dna_lists = []
    n = int(input("how many DNA string?(n <= 10): "))

    for i in range(n):
        dna_str = input(f"Enter DNA string {i + 1}: ")
        dna_lists.append(list(dna_str))

    return dna_lists
    
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def run_option_1():
    dna_lists = get_dna_lists_from_user()
    p_distance_matrix = get_p_distance_matrix(dna_lists)
    print_matrix(p_distance_matrix)

def main():
    while True:
        print("Select an option:")
        print("1. Calculate P-distance matrix for DNA strings")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            run_option_1()
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()