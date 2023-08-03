start = False
stop = False
while True:
    type = input(">").lower()

    if type == "help":
        print("""start - to start the car
stop - to stop the car
quit - to exit
""")

    elif type == "stop" and stop == False:
        print("Car stopped... Take a brake :)")
        stop = True
        start = False

    elif type == "stop" and stop == True:
        print("Car has been already stopped!")

    elif type == "start" and start == False:
        print("Car started... Ready to go!")
        start = True
        stop = False

    elif type == "start" and start == True:
        print("Car has been already started!")

    elif type == "quit":
        break

    else:
        print("I dont understand... type help")