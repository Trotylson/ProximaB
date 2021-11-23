import player
import time
import map

class Ether():
    pass

localization = 'Ether - Drone bay'

def setCoordinates():
    map.forwardLocation = map.changingRoom.localization
    map.backwardLocation = map.coreWarehouse.localization
    map.leftLocation = map.disposalRoom.localization
    map.rightLocation = map.medRoom.localization

def enter():
    print("You entering to " + player.location + "...")
    time.sleep(1)

    if map.MAA.Availabilty.Ether == True:
        print("You are in " + player.location + " now...")

    else:
        print("You can't enter to " + player.location + "! Door are closed...")
        player.location = player.lastLocation
        time.sleep(1)