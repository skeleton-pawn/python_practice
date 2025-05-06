import random

target = random.randint(1, 30)
attempts = 0

while True:
    try:
        guess_input = input("Guess the number (1 to 30) or type 'quit' to exit: ")
        if guess_input.lower() == 'quit':
            print("Game ended. The number was", target)
            break
        
        guess = int(guess_input)
        if guess < 1 or guess > 30:
            print("Please enter a number between 1 and 30.")
            continue
        
        attempts += 1
        if guess == target:
            print(f"Correct! It took you {attempts} attempt{'s' if attempts != 1 else ''}")
            break
        elif guess < target:
            print("The number is higher")
        else:
            print("The number is lower")
    except ValueError:
        print("Invalid input. Please enter a number or 'quit'.")