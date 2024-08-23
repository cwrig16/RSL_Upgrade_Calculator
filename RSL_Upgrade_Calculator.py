"""Program to calculate how many 2 star champions are required
to upgrage a champion to 6 star based on how many food champions 
at each level are current on an account.

This calculator assumes that the desired champion to upgrade to 6 star is already at 5 star and level 50."""

"Input type validation function to ensure only integers are used as input."
def input_is_integer(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            return value
        except ValueError:
            print('Invalid input. Please enter an integer.')

needed_two_star = 3
needed_three_star = 4
needed_four_star = 5
needed_five_star = 5

two_star = 1  #Champion to upgrade
three_star = two_star * needed_two_star #Upgrade from 2 star to 3 star
four_star = three_star * needed_three_star  #Upgrade from 3 star to 4 star
five_star = four_star * needed_four_star  #Upgrade from 4 star to 5 star
six_star = five_star * needed_five_star  #Upgrade from 5 star to 6 star

total_needed = 300

"""Function to calculate the number of 2 star food champions needed
based on the user input of the number of food champions at each level"""
def num_of_twos():
    two_star_lvl_1 = input_is_integer('How many 2 star champions will be fed? ')
    #two_star_lvl_30 = input_is_integer('How many two star champions are at level 20? ')
    three_star_lvl_1 = input_is_integer('How many 3 star champions will be fed? ')
    #three_star_lvl_30 = input_is_integer('How many three star champions are at level 30? ')
    four_star_lvl_1 = input_is_integer('How many 4 star champions will be fed? ')
    #four_star_lvl_30 = input_is_integer('How many four star champions are at level 40? ')
    five_star_lvl_1 = input_is_integer('How many 5 star champions will be fed? ')
    #five_star_lvl_30 = input_is_integer('How many five star champions are at level 50? ')
    twos_needed_for_six = total_needed - (two_star_lvl_1) - (three_star_lvl_1 * three_star) - (four_star_lvl_1 * four_star) - (five_star_lvl_1 * five_star)
    
    if twos_needed_for_six <= 0:
        print('Congratulations! You have enough food to upgrade a champion to 6 star!')
    else:
        print(f'You need {twos_needed_for_six} more 2 star champions to make a 6 star champion.')

print(' ')
num_of_twos()     
print(' ')   




