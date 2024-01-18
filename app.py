def convert_pennies(amount):
    # Constants representing the value of each coin/bill in pennies
    twenties_value = 20 * 100
    tens_value = 10 * 100
    fives_value = 5 * 100
    dollars_value = 100
    quarters_value = 25
    dimes_value = 10
    nickels_value = 5

    # Calculate the number of each coin/bill
    twenties = amount // twenties_value
    amount %= twenties_value

    tens = amount // tens_value
    amount %= tens_value

    fives = amount // fives_value
    amount %= fives_value

    dollars = amount // dollars_value
    amount %= dollars_value

    quarters = amount // quarters_value
    amount %= quarters_value

    dimes = amount // dimes_value
    amount %= dimes_value

    nickels = amount // nickels_value
    amount %= nickels_value

    pennies = amount

    # Print
    print(f"{pennies_value} pennies is equal to:")
    print(f"{twenties} twenties, {tens} tens, {fives} fives, {dollars} dollars, {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies")


# User keyboard input
pennies_value = int(input("Enter a value as a number of pennies: "))
convert_pennies(pennies_value)
