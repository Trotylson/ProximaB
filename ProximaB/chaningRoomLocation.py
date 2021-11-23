import player
import time
import map

class ChanginRoom:
    pass

def setCoordinates():
    map.forwardLocation = 'Desinfection room'
    map.backwardLocation = 'Ether'
    map.leftLocation = 'Wall'
    map.rightLocation = 'Wall'

def enter():
    print("You entering to " + player.location + "...")
    time.sleep(1)

    if map.MAA.MapAreaAvailability.ChangingRoom == True:
        print("You are in " + player.location + " now...")

    else:
        print("You can't enter to " + player.location + "! Door are closed...")
        player.location = player.lastLocation
        time.sleep(1)