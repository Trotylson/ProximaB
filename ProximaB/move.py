import player
import map
import time
import os

def moveSelection(playerLocation):
    player.lastLocation = player.location
    map.newCoordinates(player.location)
    player.schowStats()

    print('\nSend command to your Drone: \n\n'+
          '\tFORWARD (move to '+ map.forwardLocation + 
          ')\n\tBACKWARD (move to '+ map.backwardLocation +
          ')\n\tLEFT (move to ' + map.leftLocation +
          ')\n\tRIGHT (move to '+ map.rightLocation +
          ')\n\n')
    
    choose = input().lower()
    os.system('cls')

    try:
        print("\nYou are moving " + choose + ' to ' + map.newLocation(choose) + '.')
        time.sleep(1)
        moveEffect(player.location)

    except TypeError:
        print("There is no command: " + choose + '...')
        time.sleep(1)
    

def moveEffect(newLocation):
    map.tryEnter(newLocation)

