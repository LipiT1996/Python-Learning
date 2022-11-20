"""
A method to implement try, except, else and finally keyword in a metho which asks for user input(an integer), 
but if the user adds a string or alphabet, leads to an error.
also the method keeps on running on a loop until the break command is reached.
"""

def interact():
    while True:
        try:
            user_input = int(input('Please input an integer:'))     # try to turn user input into an integer
        except ValueError:
            print('Please input integers only.')  # print a message if user didn't input an integer
        else:
            print('{} is {}.'.format(user_input, 'even' if user_input % 2 == 0 else 'odd'))     # print even/odd if the user input an integer
        finally:    # regardless of the previous input being valid or not
            user_input = input('Do you want to play again? (y/N):')     # ask if the user wants to play again
            if user_input != 'y':       # quit if the user didn't input `y`
                print('Goodbye.')
                break   # break the while loop to quit
interact()
