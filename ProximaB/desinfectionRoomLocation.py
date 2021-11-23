import player
import time
import map

class DesingectionRoom():
    pass

localization = 'Desinfection room'

def setCoordinates():
    map.forwardLocation = map.collisionObjects.localization
    map.backwardLocation = map.changingRoom.localization
    map.leftLocation = map.WORC.localization
    map.rightLocation = map.MCRoom.localization

def enter():
    print("You entering to " + player.location + "...")
    time.sleep(1)

    if map.MAA.Availabilty.DesinfectionRoom == True:
        print("You are in " + player.location + " now...")

    else:
        print("You can't enter to " + player.location + "! Door are closed...")
        player.location = player.lastLocation
        time.sleep(1)
