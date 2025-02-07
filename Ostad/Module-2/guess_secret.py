# Guess the number game
secret_number = 7
attempts = 0

while True:
    guess =int(input('Guess the number (1 - 10)'))
    attempts = attempts + 1

    if guess == secret_number:
        print(f"Great! you got the secret number - {secret_number} in the {attempts} attempts")
        break
    elif guess > secret_number:
        print("Too high, try again")
    elif guess < secret_number:
        print("Too low, try again")
