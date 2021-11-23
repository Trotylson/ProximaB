import player
import time
import map

class EngineeringRoom:
    pass

def setCoordinates():
    map.forewardLocation = 'Wall'
    map.backwardLocation = 'Wall'
    map.leftLocation = 'Medical room'
    map.rightLocation = 'Wall'

def enter():
    print("You entering to " + player.location + "...")
    time.sleep(1)

    if map.MAA.MapAreaAvailability.EngineeringRoom == True:
        print("You are in " + player.location + " now...")
    else:
        print("You can't enter to " + player.location + "!")
        player.location = player.lastLocation
        time.sleep(1)