import player
import time
import map

class EngineeringRoom:
    pass

localization = 'Engineering room'

def setCoordinates():
    map.forwardLocation = map.collisionObjects.localization
    map.backwardLocation = map.BCWarehouse.localization
    map.leftLocation = map.medRoom.localization
    map.rightLocation = map.collisionObjects.localization

def enter():
    print("You entering to " + player.location + "...")
    time.sleep(1)

    if map.MAA.Availabilty.EngineeringRoom == True:
        print("You are in " + player.location + " now...")

    else:
        print("You can't enter to " + player.location + "! Door are closed...")
        player.location = player.lastLocation
        time.sleep(1)