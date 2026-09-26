import random

while True:
    secret_number = random.randint(1, 10)
    attempts = 0
    max_attempts = 5

    print("\nWelcome to Enhanced Number Guessing Game")
    print("I am thinking of a number between 1 and 10")
    print("You have", max_attempts, "attempts")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts = attempts + 1

        if guess == secret_number:
            print("You're correct!", attempts, "attempts used")
            break
        elif guess < secret_number:
            print("Too low, try again.")
        else:
            print("Too high, try again.")

        if attempts == max_attempts:
            print("Out of attempts! The number was", secret_number)

    while True:
        ans = input("\nDo you want to play again? (Y/N): ").lower()
        if ans in ['y', 'n']:
            break
        print("Please enter Y or N.")

    if ans == 'n':
        break

print("\nThanks for playing!")
