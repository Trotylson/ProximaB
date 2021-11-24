import Player.player as player
import time
import World.Map.map as map

class Ether():
    pass

localization = 'Ether - Drone bay'

def setCoordinates():
    map.forwardLocation = map.changingRoom.localization
    map.backwardLocation = map.coreWarehouse.localization
    map.leftLocation = map.disposalRoom.localization
    map.rightLocation = map.medRoom.localization

def enter():
    print("You entering to " + player.Location + "...")
    time.sleep(1)

    if map.MAA.Availabilty.Ether == True:
        print("You are in " + player.Location + " now...")

    else:
        print("You can't enter to " + player.Location + "! Door are closed...")
        player.Location = player.LastLocation
        time.sleep(1)