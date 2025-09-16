from output import get_sales_tax_amount, get_tip_amount

def main():
    # Prompt user for meal amount
    meal_amount = float(input("Enter the meal amount: "))

    # Prompt user for tip rate (as a whole number like 15 for 15%)
    tip_percent = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
    tip_rate = tip_percent / 100  # convert to decimal

    # Calculate amounts
    sales_tax = get_sales_tax_amount(meal_amount)
    tip_amount = get_tip_amount(meal_amount, tip_rate)
    total = meal_amount + sales_tax + tip_amount

    # Display receipt
    print("\n----- RECEIPT -----")
    print(f"Meal Amount:   ${meal_amount:.2f}")
    print(f"Sales Tax:     ${sales_tax:.2f}")
    print(f"Tip Amount:    ${tip_amount:.2f}")
    print(f"Total:         ${total:.2f}")

if __name__ == "__main__":
  main()
  
