continuing = True
start_count = 0
stop_count = 0
while continuing:
    inputed = input(">")
    if inputed.lower() == "start":
        start_count += 1
        if start_count == 1:
            print("Car started... Ready to go")
            stop_count = 0
        else:
            print("Car is already started")
    elif inputed.lower() == "stop":
        stop_count += 1
        if stop_count == 1:
            print("Car stopped")
            start_count = 0
        else:
            print("Car is already stopped")
    elif inputed.lower() == "quit":
        break
    else:
        print("I don't understand that")
