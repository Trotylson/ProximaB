import Player.player as player
import time
import World.Map.map as map

class CollisionObjects():
    pass

localization = 'wall'

def checkCollision():
    if map.MAA.Availabilty.CollisionObjects == True:
        pass

    else:
        print("You cannot go through the " + player.Location + "...")
        time.sleep(1)
        player.Location = player.LastLocation
