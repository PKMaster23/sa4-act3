number = 10

i = 3

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")

while guess != 'q':
    guess = int(guess)

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif i == 0:
        print(f"Sorry, but the number was {number}.")
        break
    else:
        print(f"Sorry, that's not the right number. You have {i:.0f} attempts remaining.")
        i = i - 1
    guess = input("What number am I thinking of? ")

if guess == 'q':
    print('See you next time!')
