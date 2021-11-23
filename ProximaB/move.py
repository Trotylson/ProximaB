import player
import map
import time

def moveSelection(playerLocation):
    player.lastLocation = player.location
    map.newCoordinates(player.location)
    print('\n\nDrone location: ' + player.location + '\n')

    print('Give the command: \n\n'+
          '\tFORWARD to '+ map.forwardLocation + 
          '\n\tLEFT to '+ map.leftLocation +
          '\n\tRIGHT to '+ map.rightLocation +
          '\n\tBACKWARD to '+ map.backwardLocation +
          '\n\n')
    choose = input().upper()

    try:
        print("\nYou are moving " + choose + ' to ' + map.newLocation(choose) + '.')
        time.sleep(1)
        moveEffect(player.location)

    except TypeError:
        print("There is no command: " + choose + '...')
        time.sleep(1)
    

def moveEffect(newLocation):
    map.tryEnter(newLocation)

