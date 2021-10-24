print("*****************************")
print("Welcome to the guessing game!")
print("*****************************")

secret_number = 42

guess_str = input("Enter your number: ")

print("You typed ", guess_str)

guess = int(guess_str)

got_the_guess_right = guess == secret_number

the_guess_is_higher = guess > secret_number

if got_the_guess_right:
    print("You got it right!")
else:
    if the_guess_is_higher:
        print("You made a mistake! Your guess was higher than the secret number!")
    else:
        print("You made a mistake! Your guess was less than the secret number!")

print("End of game!")
