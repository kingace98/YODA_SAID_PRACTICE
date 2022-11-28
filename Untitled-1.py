command = ""
started = False

while True:
    command == input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Starting the car vroom")
    else:
        print("Unknown command")