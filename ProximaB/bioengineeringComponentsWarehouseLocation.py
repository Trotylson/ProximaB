import player
import time
import map

class BioengineeringComponentsWarehouse:
    pass

def setCoordinates():
    map.forwardLocation = 'Wall'
    map.backwardLocation = 'Wall'
    map.leftLocation = 'Core warehouse'
    map.rightLocation = 'Wall'

def enter():
    print("You entering to " + player.location + "...")
    time.sleep(1)

    if map.MAA.MapAreaAvailability.BioengineeringComponentsWarehouse == True:
        print("You are in " + player.location + " now...")

    else:
        print("You can't enter to " + player.location + "! Door are closed...")
        player.location = player.lastLocation
        time.sleep(1)
