import player
import etherLocation as ether
import medicalRoomLocation as medRoom
import engineeringRoom as enRoom
import mapAreaAvailability as MAA

class Map(MAA.MapAreaAvailability): # inherits by boolean variables in class!!!
    pass

forewardLocation = ''
backwardLocation = ''
leftLocation = ''
rightLocation = ''

def newLocation(playerChoose):
    if playerChoose == 'FORWARD':
        player.location = forewardLocation
        return forewardLocation
    elif playerChoose == 'BACKWARD':
        player.location = backwardLocation
        return backwardLocation
    elif playerChoose == 'LEFT':
        player.location = leftLocation
        return leftLocation
    elif playerChoose == 'RIGHT':
        player.location = rightLocation
        return rightLocation


def newCoordinates(playerLocation):
    if playerLocation == 'Ether':
        ether.setCoordinates()

    elif playerLocation == 'Medical room':
        medRoom.setCoordinates()

    elif playerLocation == 'Engineering room':
        enRoom.setCoordinates()


def tryEnter(playerLocation):
    if playerLocation == 'Ether':
        ether.enter()

    elif playerLocation == 'Medical room':
        medRoom.enter()

    elif playerLocation == 'Engineering room':
        enRoom.enter()
