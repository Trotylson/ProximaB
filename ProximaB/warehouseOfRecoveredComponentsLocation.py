import player
import time
import map

class WarehouseOfRecoveredComponents():
    pass

localization = 'Warehouse of recovered components'

def setCoordinates():
    map.forwardLocation = map.collisionObjects.localization
    map.backwardLocation = map.disposalRoom.localization
    map.leftLocation = map.collisionObjects.localization
    map.rightLocation = map.desinfectionRoom.localization

def enter():
    print("You entering to " + player.location + "...")
    time.sleep(1)

    if map.MAA.Availabilty.WarehouseOfRecoveredComponents == True:
        print("You are in " + player.location + " now...")

    else:
        print("You can't enter to " + player.location + "! Door are closed...")
        player.location = player.lastLocation
        time.sleep(1)