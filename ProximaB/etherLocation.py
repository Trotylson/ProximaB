import player
import time
import map

class Ether:
    pass

def setCoordinates():
    map.forewardLocation = 'Changing room'
    map.backwardLocation = 'Core warehouse'
    map.leftLocation = 'Utilization'
    map.rightLocation = 'Medical room'

def enter():
    print("You entering to " + player.location + "...")
    time.sleep(1)

    if map.MAA.MapAreaAvailability.Ether == True:
        print("You are in " + player.location + " now...")
    else:
        print("You can't enter to " + player.location + "!")
        player.location = player.lastLocation
        time.sleep(1)