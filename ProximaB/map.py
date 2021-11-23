import player
import mapAreaAvailability as MAA
import collisionObjects
import etherLocation as ether
import medicalRoomLocation as medRoom
import engineeringRoomLocation as engiRoom
import disposalRoomLocalization as disposalRoom
import changingRoomLocation as changingRoom
import coreWarehouseLocation as coreWarehouse
import bioengineeringComponentsWarehouseLocation as BCWarehouse
import biowasteIncineratorLocation as biowasteIncinerator
import desinfectionRoomLocation as desinfectionRoom
import warehouseOfRecoveredComponentsLocation as WORC
import mainControlRoomLocation as MCRoom
import powerStationLocation as powerStation

class Map(MAA.Availabilty): # inherits by boolean variables class!!!
    pass

forwardLocation = ''
backwardLocation = ''
leftLocation = ''
rightLocation = ''

def newLocation(playerChoose):
    if playerChoose == 'forward':
        player.location = forwardLocation
        return forwardLocation
    elif playerChoose == 'backward':
        player.location = backwardLocation
        return backwardLocation
    elif playerChoose == 'left':
        player.location = leftLocation
        return leftLocation
    elif playerChoose == 'right':
        player.location = rightLocation
        return rightLocation


def newCoordinates(playerLocation):
    if playerLocation == ether.localization:
        ether.setCoordinates()

    elif playerLocation == medRoom.localization:
        medRoom.setCoordinates()

    elif playerLocation == engiRoom.localization:
        engiRoom.setCoordinates()

    elif playerLocation == disposalRoom.localization:
        disposalRoom.setCoordinates()

    elif playerLocation == changingRoom.localization:
        changingRoom.setCoordinates()

    elif playerLocation == coreWarehouse.localization:
        coreWarehouse.setCoordinates()

    elif playerLocation == BCWarehouse.localization:
        BCWarehouse.setCoordinates()

    elif playerLocation == biowasteIncinerator.localization:
        biowasteIncinerator.setCoordinates()

    elif playerLocation == desinfectionRoom.localization:
        desinfectionRoom.setCoordinates()

    elif playerLocation == WORC.localization:
        WORC.setCoordinates()

    elif playerLocation == MCRoom.localization:
        MCRoom.setCoordinates()

    elif playerLocation == powerStation.localization:
        powerStation.setCoordinates()

def tryEnter(playerLocation):
    if playerLocation == ether.localization:
        ether.enter()

    elif playerLocation == medRoom.localization:
        medRoom.enter()

    elif playerLocation == engiRoom.localization:
        engiRoom.enter()

    elif playerLocation == disposalRoom.localization:
        disposalRoom.enter()

    elif playerLocation == changingRoom.localization:
        changingRoom.enter()

    elif playerLocation == coreWarehouse.localization:
        coreWarehouse.enter()

    elif playerLocation == BCWarehouse.localization:
        BCWarehouse.enter()

    elif playerLocation == biowasteIncinerator.localization:
        biowasteIncinerator.enter()

    elif playerLocation == desinfectionRoom.localization:
        desinfectionRoom.enter()

    elif playerLocation == WORC.localization:
        WORC.enter()

    elif playerLocation == MCRoom.localization:
        MCRoom.enter()

    elif playerLocation == powerStation.localization:
        powerStation.enter()

    elif playerLocation == collisionObjects.localization:
        collisionObjects.checkCollision()
