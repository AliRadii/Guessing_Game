import random

def guess():
    user_guess = int(input("Enter any integer number in range [0,10]: "))
    random_number = random.randint(0, 10)
    if user_guess == random_number:
        print("You won!")
        return True
    else:
        print(f"You lost! The correct number was {random_number}.")
        return False

# Let the user play multiple times
while True:
    play_again = input("Do you want to play the game? (yes/no) : ").lower()
    if play_again == 'yes':
        guess()
    elif play_again == 'no':
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("Invalid response! Please enter 'yes' or 'no'.")