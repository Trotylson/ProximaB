import move

location = "Ether - Drone bay"
lastLocation = ""
healthPoints = 100

def playerMove():
    while True:
        if True:
            move.moveSelection(location)
        else: break

def schowStats():
    print('\n\nDrone location: ' + location.upper())
    print('Drone condition: ' + str(healthPoints) + '%')