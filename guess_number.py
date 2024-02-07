number = '10'

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")

while guess != number:
    if guess == number:
        print("Congratulations! You guessed the right number.")
    elif guess == 'q':
        break
    else:
        print(f"Sorry! The number is not {guess}. Try again!")
        guess = input("What number am I thinking of? ")

if guess == number:
    print("Congratulations! You guessed the right number.")
if guess == 'q':
    print('See you next time!')