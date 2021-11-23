import player
import time
import map

class ChanginRoom:
    pass

localization = 'Changing room'

def setCoordinates():
    map.forwardLocation = map.desinfectionRoom.localization
    map.backwardLocation = map.ether.localization
    map.leftLocation = map.collisionObjects.localization
    map.rightLocation = map.collisionObjects.localization

def enter():
    print("You entering to " + player.location + "...")
    time.sleep(1)

    if map.MAA.Availabilty.ChangingRoom == True:
        print("You are in " + player.location + " now...")

    else:
        print("You can't enter to " + player.location + "! Door are closed...")
        player.location = player.lastLocation
        time.sleep(1)