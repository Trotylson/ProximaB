import player
import time
import map

class MedicalRoom:
    pass

def setCoordinates():
    map.forewardLocation = 'Wall'
    map.backwardLocation = 'Wall'
    map.leftLocation = 'Ether'
    map.rightLocation = 'Engineering room'

def enter():
    print("You entering to " + player.location + "...")
    time.sleep(1)

    if map.MAA.MapAreaAvailability.MedicalRoom == True:
        print("You are in " + player.location + " now...")

    else:
        print("You can't enter to " + player.location + "! Door are closed...")
        player.location = player.lastLocation
        time.sleep(1)