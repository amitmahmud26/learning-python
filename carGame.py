continuing = True
while continuing:
    inputed = input(">")
    if inputed.lower() == "start":
        print("Car started... Ready to go")
    elif inputed.lower() == "stop":
        print("Car stopped")
    elif inputed.lower() == "quit":
        break
    else:
        print("I don't understand that")
