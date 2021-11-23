import player
import time
import map

class DisposalRoom:
    pass

localization = 'Disposal room'

def setCoordinates():
    map.forwardLocation = map.WORC.localization
    map.backwardLocation = map.biowasteIncinerator.localization
    map.leftLocation = map.collisionObjects.localization
    map.rightLocation = map.ether.localization

def enter():
    print("You entering to " + player.location + "...")
    time.sleep(1)

    if map.MAA.Availabilty.DisposalRoom == True:
        print("You are in " + player.location + " now...")

    else:
        print("You can't enter to " + player.location + "! Door are closed...")
        player.location = player.lastLocation
        time.sleep(1)
