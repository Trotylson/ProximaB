import player
import time
import map

class CollisionObjects():
    pass

localization = 'wall'

def checkCollision():
    if map.MAA.Availabilty.CollisionObjects == True:
        pass

    else:
        print("You cannot go through the " + player.location + "...")
        time.sleep(1)
        player.location = player.lastLocation
