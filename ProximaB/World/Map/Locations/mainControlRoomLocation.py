import Player.player as player
import time
import World.Map.map as map

class MainControlRoom():
    pass

localization = 'Main control room'

def setCoordinates():
    map.forwardLocation = map.collisionObjects.localization
    map.backwardLocation = map.collisionObjects.localization
    map.leftLocation = map.desinfectionRoom.localization
    map.rightLocation = map.powerStation.localization

def enter():
    print("You entering to " + player.Location + "...")
    time.sleep(1)

    if map.MAA.Availabilty.MainControlRoom == True:
        print("You are in " + player.Location + " now...")

    else:
        print("You can't enter to " + player.Location + "! Door are closed...")
        player.Location = player.LastLocation
        time.sleep(1)
