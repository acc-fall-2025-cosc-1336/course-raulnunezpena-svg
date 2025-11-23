

from strings import get_hamming_distance , get_dna_complement


def main():
    while True:
        print("\n1-Hamming Distance")
        print("2-Dna Complement")
        print("3-Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            dna1 = input("Enter first DNA string: ")
            dna2 = input("Enter second DNA string: ")

            if len(dna1) != len(dna2):
                print("Error: DNA strings must be the same length.")
            else:
                distance = get_hamming_distance(dna1, dna2)
                print("Hamming Distance:", distance)

        elif choice == "2":
            dna = input("Enter DNA string: ")
            complement = get_dna_complement(dna)
            print("Reverse Complement:", complement)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
