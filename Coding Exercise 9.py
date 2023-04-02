"""
Build a simple Artificial Intelligence (AI). Our AI is disguised as a function called interact() which works as follows:

It first asks the user for an integer input.

Then it tells the user whether that integer is even or odd.

Then it asks the user whether she wants to play this game again.

If the user inputs y for yes, then the function repeats.

If the user inputs anything other than y, then it prints out Goodbye. and quits.
"""

def interact():
    while True:
        try:
            user_input = int(input("Please input an integer:"))
        except ValueError:
            print("Please input integers only.")
        else:
            is_even = user_input % 2 == 0
            print('{} is {}.'.format(user_input, 'even' if is_even else 'odd'))
        finally:
            user_input = input('Do you want to play again? (y/N):')

            if user_input != 'y':
                print('Goodbye.')
                break
interact()                
