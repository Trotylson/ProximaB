import Player.player as player
import time
import World.Map.map as map

class ChanginRoom:
    pass

localization = 'Changing room'

def setCoordinates():
    map.forwardLocation = map.desinfectionRoom.localization
    map.backwardLocation = map.ether.localization
    map.leftLocation = map.collisionObjects.localization
    map.rightLocation = map.collisionObjects.localization

def enter():
    print("You entering to " + player.Location + "...")
    time.sleep(1)

    if map.MAA.Availabilty.ChangingRoom == True:
        print("You are in " + player.Location + " now...")

    else:
        print("You can't enter to " + player.Location + "! Door are closed...")
        player.Location = player.LastLocation
        time.sleep(1)