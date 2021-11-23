import player
import time
import map

class BioengineeringComponentsWarehouse:
    pass

localization = 'Bioengineering components warehouse'

def setCoordinates():
    map.forwardLocation = map.engiRoom.localization
    map.backwardLocation = map.collisionObjects.localization
    map.leftLocation = map.coreWarehouse.localization
    map.rightLocation = map.collisionObjects.localization

def enter():
    print("You entering to " + player.location + "...")
    time.sleep(1)

    if map.MAA.Availabilty.BioengineeringComponentsWarehouse == True:
        print("You are in " + player.location + " now...")

    else:
        print("You can't enter to " + player.location + "! Door are closed...")
        player.location = player.lastLocation
        time.sleep(1)
