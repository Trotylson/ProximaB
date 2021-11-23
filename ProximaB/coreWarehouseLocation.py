import player
import time
import map

class CoreWarehouse:
    pass

def setCoordinates():
    map.forwardLocation = 'Ether'
    map.backwardLocation = 'Wall'
    map.leftLocation = 'Wall'
    map.rightLocation = 'Bioengineering components warehouse'

def enter():
    print("You entering to " + player.location + "...")
    time.sleep(1)

    if map.MAA.MapAreaAvailability.CoreWarehouse == True:
        print("You are in " + player.location + " now...")

    else:
        print("You can't enter to " + player.location + "! Door are closed...")
        player.location = player.lastLocation
        time.sleep(1)