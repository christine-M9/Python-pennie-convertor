# define a function 
def convert_pennies(value):
    # Constants representing the value of each coin/bill in pennies
    twenties_value = 20 * 100
    tens_value = 10 * 100
    fives_value = 5 * 100
    dollars_value = 100
    quarters_value = 25
    dimes_value = 10
    nickels_value = 5

    # Calculate the number of each coin/bill
    twenties = value // twenties_value
    value %= twenties_value

    tens = value // tens_value
    value %= tens_value

    fives = value // fives_value
    value %= fives_value

    dollars = value // dollars_value
    value %= dollars_value

    quarters = value // quarters_value
    value %= quarters_value

    dimes = value // dimes_value
    value %= dimes_value

    nickels = value // nickels_value
    value %= nickels_value

    pennies = value

    # Print 
    print(f"{pennies_value} pennies is equal to:")
    print(f"{twenties} twenties, {tens} tens, {fives} fives, {dollars} dollars, {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies")


# User keyboard input
pennies_value = int(input("Enter a value as a number of pennies: "))
convert_pennies(pennies_value)
