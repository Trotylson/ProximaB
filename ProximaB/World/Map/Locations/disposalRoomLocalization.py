import Player.player as player
import time
import World.Map.map as map

class DisposalRoom:
    pass

localization = 'Disposal room'

def setCoordinates():
    map.forwardLocation = map.WORC.localization
    map.backwardLocation = map.biowasteIncinerator.localization
    map.leftLocation = map.collisionObjects.localization
    map.rightLocation = map.ether.localization

def enter():
    print("You entering to " + player.Location + "...")
    time.sleep(1)

    if map.MAA.Availabilty.DisposalRoom == True:
        print("You are in " + player.Location + " now...")

    else:
        print("You can't enter to " + player.Location + "! Door are closed...")
        player.Location = player.LastLocation
        time.sleep(1)
