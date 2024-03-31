def get_valid_input(prompt, validator_func):
    while True:
        try:
            user_input = validator_func(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def validate_tip_percentage(input_str):
    tip_percentage = int(input_str)
    if tip_percentage in [10, 12, 15]:
        return tip_percentage
    raise ValueError("Tip percentage must be 10%, 12%, or 15%.")

def main():
    total_bill = get_valid_input("What was the total bill? £", float)
    tip_percentage = get_valid_input("How much would you like to give? 10%, 12%, or 15%? ", validate_tip_percentage)
    bill_split_between = get_valid_input("How many people are splitting the bill? ", int)

    total_bill_with_tip = total_bill * (1 + tip_percentage / 100)
    amount_per_head = total_bill_with_tip / bill_split_between

    print(f"Each person should pay: £{amount_per_head:.2f}")

if __name__ == "__main__":
    main()