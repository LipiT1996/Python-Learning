"""
In this exercise you'll be implementing a simple user menu.

A menu is something that repeats over and over again until the user types something that makes the program terminate.

In our menu, the user will be able to choose from two options:

If they type p , we will print "Hello"

If they type q , we will terminate the program

How will we go about it?

First, we'll ask the user for what they want to do first. Do they want to print (p ), or do they want to exit without printing (q )?

Then we'll have a while  loop that will repeat until the user types q .

Inside the while loop, we'll have an if  statement that checks whether the user typed p . If they did, we'll print "Hello" .

Inside the loop but outside the if statement, we'll ask the user again whether they want to print or quit.
"""

user_input = input("Enter your choice, p for Hello or q to quit: ")

while user_input != 'q':
  if user_input == 'p':
    print("Hello")
    
  user_input = input("Enter your choice, p for Hello or q to quit: ")
