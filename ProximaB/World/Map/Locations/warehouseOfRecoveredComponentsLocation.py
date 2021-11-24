import Player.player as player
import time
import World.Map.map as map

class WarehouseOfRecoveredComponents():
    pass

localization = 'Warehouse of recovered components'

def setCoordinates():
    map.forwardLocation = map.collisionObjects.localization
    map.backwardLocation = map.disposalRoom.localization
    map.leftLocation = map.collisionObjects.localization
    map.rightLocation = map.desinfectionRoom.localization

def enter():
    print("You entering to " + player.Location + "...")
    time.sleep(1)

    if map.MAA.Availabilty.WarehouseOfRecoveredComponents == True:
        print("You are in " + player.Location + " now...")

    else:
        print("You can't enter to " + player.Location + "! Door are closed...")
        player.Location = player.LastLocation
        time.sleep(1)