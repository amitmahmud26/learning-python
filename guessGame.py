guess_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = input("Your number?")
    if int(guess) == guess_number:
        print("Your Won!")
        break
    guess_count += 1
else:
    print("You lost")

