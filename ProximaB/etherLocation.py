import player
import time
import map

class Ether:
    pass

localization = 'Ether'

def setCoordinates():
    map.forwardLocation = 'Changing room'
    map.backwardLocation = 'Core warehouse'
    map.leftLocation = 'Disposal room'
    map.rightLocation = 'Medical room'

def enter():
    print("You entering to " + player.location + "...")
    time.sleep(1)

    if map.MAA.MapAreaAvailability.Ether == True:
        print("You are in " + player.location + " now...")

    else:
        print("You can't enter to " + player.location + "! Door are closed...")
        player.location = player.lastLocation
        time.sleep(1)