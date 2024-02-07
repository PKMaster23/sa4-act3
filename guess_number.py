number = 10

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")

while guess != 'q':
    
    guess = int(guess)

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess < number:
        print("Sorry! Your guess is too low. Try again!")
    elif guess > number:
        print("Sorry! Your guess was too high. Try again!")

    guess = input("What number am I thinking of? ")

if guess == 'q':
    print('See you next time!')