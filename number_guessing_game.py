import random

random_number = random.randint(1, 100)

while True:
    try:
        guess_number = int(input("Enter number between 1 to 100:"))
        if guess_number < 1 or guess_number > 100:
            print("Please enter a number between 1 and 100.")
            continue
        if guess_number < random_number:
            print("Too Low")
        elif guess_number > random_number:
            print("Too High")
        else:
            print("Congratulations!, you guesses the number.")
            break
    except ValueError:
        print('Please Enter a Valid Number')
    

