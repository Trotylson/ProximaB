import player
import time
import map

class MedicalRoom:
    pass

localization = 'Medical room'

def setCoordinates():
    map.forwardLocation = map.collisionObjects.localization
    map.backwardLocation = map.collisionObjects.localization
    map.leftLocation = map.ether.localization
    map.rightLocation = map.engiRoom.localization

def enter():
    print("You entering to " + player.location + "...")
    time.sleep(1)

    if map.MAA.Availabilty.MedicalRoom == True:
        print("You are in " + player.location + " now...")

    else:
        print("You can't enter to " + player.location + "! Door are closed...")
        player.location = player.lastLocation
        time.sleep(1)