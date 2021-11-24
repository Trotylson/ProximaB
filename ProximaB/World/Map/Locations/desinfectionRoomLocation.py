import Player.player as player
import time
import World.Map.map as map

class DesingectionRoom():
    pass

localization = 'Desinfection room'

def setCoordinates():
    map.forwardLocation = map.collisionObjects.localization
    map.backwardLocation = map.changingRoom.localization
    map.leftLocation = map.WORC.localization
    map.rightLocation = map.MCRoom.localization

def enter():
    print("You entering to " + player.Location + "...")
    time.sleep(1)

    if map.MAA.Availabilty.DesinfectionRoom == True:
        print("You are in " + player.Location + " now...")

    else:
        print("You can't enter to " + player.Location + "! Door are closed...")
        player.Location = player.LastLocation
        time.sleep(1)
