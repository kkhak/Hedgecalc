def calculate_profits(aum, return_percent, management_fee_percent, performance_fee_percent):
    # Calculate gains
    gains = aum * (return_percent / 100)

    # Calculate profits based on user-defined fees
    management_fee = management_fee_percent / 100 * aum
    performance_fee = performance_fee_percent / 100 * gains

    total_profits = management_fee + performance_fee

    # Return calculated values
    return management_fee, performance_fee, total_profits

def main():
    # Get user input
    try:
        aum = float(input("Enter the Assets Under Management (AUM): "))
        return_percent = float(input("Enter the return for the year (in percent): "))
        management_fee_percent = float(input("Enter the total management fee (in percent): "))
        performance_fee_percent = float(input("Enter the performance fee (in percent): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Calculate profits
    management_fee, performance_fee, profits = calculate_profits(aum, return_percent, management_fee_percent, performance_fee_percent)

    # Display results
    print(f"\nProfits for the fund:")
    print(f"Management Fee: ${round(management_fee, 2)}")
    print(f"Performance Fee: ${round(performance_fee, 2)}")
    print(f"Total Profits: ${round(profits, 2)}")

if __name__ == "__main__":
    main()
10
