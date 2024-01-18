
#define a function
def convert_pennies(amount):

#define constants for each coins value   
    twenties_calc = 20 * 100
    tens_calc = 10 * 100
    fives_calc = 5 * 100
    dollars_calc = 100
    quarters_calc = 25
    dimes_calc = 10
    nickels_calc = 5

#each coins number
    twenties = amount // twenties_calc
    amount %= twenties_calc

    tens = amount // tens_calc
    amount %= tens_calc

    fives = amount // fives_calc
    amount %= fives_calc

    dollars = amount // dollars_calc
    amount %= dollars_calc

    quarters = amount // quarters_calc
    amount %= quarters_calc

    dimes = amount // dimes_calc
    amount %= dimes_calc

    nickels = amount // nickels_calc
    amount %= nickels_calc

    pennies = amount

    # Print
    print(f"{pennies_number} pennies is equal to:")
    print(f"{twenties} twenties, {tens} tens, {fives} fives, {dollars} dollars, {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies")


# User input
pennies_number = int(input("Enter a value as a number of pennies: "))
convert_pennies(pennies_number)
