import devTools as console
import Player.player as player
import World.Map.map as map
import Player.inventory as inventory
import gameMenu
import time


def moveSelection(playerLocation):
    player.LastLocation = player.Location
    map.newCoordinates(player.Location)
    player.schowStats()

    print('Code command to your Drone: \n\n'+
          '\tFORWARD (move to '+ map.forwardLocation + 
          ')\n\tBACKWARD (move to '+ map.backwardLocation +
          ')\n\tLEFT (move to ' + map.leftLocation +
          ')\n\tRIGHT (move to '+ map.rightLocation +
          ')\n\n\tINVENTORY (to open drone inventory)\n'+
          '\n\tETHER (to connect Ether and open game menu)\n')
    
    choose = input('Your command: ').lower()
    console.clear()

    try:
        if choose == 'inventory':
            inventory.schowInventory()
        elif choose == 'ether':
            gameMenu.open()
        else:
            print("\nYou are moving " + choose + ' to ' + map.newLocation(choose) + '.')
            moveEffect(player.Location)

    except TypeError:
        print("There is no command: " + choose + '...')
        time.sleep(1)
    

def moveEffect(newLocation):
    time.sleep(1)
    player.PowerSupply -= 1
    map.tryEnter(newLocation)

