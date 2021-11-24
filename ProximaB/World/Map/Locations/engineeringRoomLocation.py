import Player.player as player
import time
import World.Map.map as map

class EngineeringRoom:
    pass

localization = 'Engineering room'

def setCoordinates():
    map.forwardLocation = map.collisionObjects.localization
    map.backwardLocation = map.BCWarehouse.localization
    map.leftLocation = map.medRoom.localization
    map.rightLocation = map.collisionObjects.localization

def enter():
    print("You entering to " + player.Location + "...")
    time.sleep(1)

    if map.MAA.Availabilty.EngineeringRoom == True:
        print("You are in " + player.Location + " now...")

    else:
        print("You can't enter to " + player.Location + "! Door are closed...")
        player.Location = player.LastLocation
        time.sleep(1)