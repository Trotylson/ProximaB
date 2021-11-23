import player
import time
import map

class MainControlRoom():
    pass

localization = 'Main control room'

def setCoordinates():
    map.forwardLocation = map.collisionObjects.localization
    map.backwardLocation = map.collisionObjects.localization
    map.leftLocation = map.desinfectionRoom.localization
    map.rightLocation = map.powerStation.localization

def enter():
    print("You entering to " + player.location + "...")
    time.sleep(1)

    if map.MAA.Availabilty.MainControlRoom == True:
        print("You are in " + player.location + " now...")

    else:
        print("You can't enter to " + player.location + "! Door are closed...")
        player.location = player.lastLocation
        time.sleep(1)
