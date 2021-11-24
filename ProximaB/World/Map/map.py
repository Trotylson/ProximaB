import Player.player as player
import World.mapAreaAvailability as MAA
import World.Map.collisionObjects as collisionObjects
import World.Map.Locations.etherLocation as ether
import World.Map.Locations.medicalRoomLocation as medRoom
import World.Map.Locations.engineeringRoomLocation as engiRoom
import World.Map.Locations.disposalRoomLocalization as disposalRoom
import World.Map.Locations.changingRoomLocation as changingRoom
import World.Map.Locations.coreWarehouseLocation as coreWarehouse
import World.Map.Locations.bioengineeringComponentsWarehouseLocation as BCWarehouse
import World.Map.Locations.biowasteIncineratorLocation as biowasteIncinerator
import World.Map.Locations.desinfectionRoomLocation as desinfectionRoom
import World.Map.Locations.warehouseOfRecoveredComponentsLocation as WORC
import World.Map.Locations.mainControlRoomLocation as MCRoom
import World.Map.Locations.powerStationLocation as powerStation

class Map(MAA.Availabilty): # inherits by boolean variables class!!!
    pass

forwardLocation = ''
backwardLocation = ''
leftLocation = ''
rightLocation = ''

def newLocation(playerChoose):
    if playerChoose == 'forward':
        player.Location = forwardLocation
        return forwardLocation
    elif playerChoose == 'backward':
        player.Location = backwardLocation
        return backwardLocation
    elif playerChoose == 'left':
        player.Location = leftLocation
        return leftLocation
    elif playerChoose == 'right':
        player.Location = rightLocation
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
