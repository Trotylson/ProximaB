import player
import mapAreaAvailability as MAA
import etherLocation as ether
import medicalRoomLocation as medRoom
import engineeringRoomLocation as engiRoom
import disposalRoomLocalization as disposalRoom
import chaningRoomLocation as changingRoom
import coreWarehouseLocation as coreWarehouse
import bioengineeringComponentsWarehouseLocation as BCWarehouse
import biowasteIncineratorLocation as biowasteIncinerator

class Map(MAA.MapAreaAvailability): # inherits by boolean variables in class!!!
    pass

forwardLocation = ''
backwardLocation = ''
leftLocation = ''
rightLocation = ''

def newLocation(playerChoose):
    if playerChoose == 'FORWARD':
        player.location = forwardLocation
        return forwardLocation
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
        engiRoom.setCoordinates()

    elif playerLocation == 'Disposal room':
        disposalRoom.setCoordinates()

    elif playerLocation == 'Changing room':
        changingRoom.setCoordinates()

    elif playerLocation == 'Core warehouse':
        coreWarehouse.setCoordinates()

    elif playerLocation == 'Bioengineering components warehouse':
        BCWarehouse.setCoordinates()

    elif playerLocation == 'Biowaste incinerator':
        biowasteIncinerator.setCoordinates()

def tryEnter(playerLocation):
    if playerLocation == 'Ether':
        ether.enter()

    elif playerLocation == 'Medical room':
        medRoom.enter()

    elif playerLocation == 'Engineering room':
        engiRoom.enter()

    elif playerLocation == 'Disposal room':
        disposalRoom.enter()

    elif playerLocation == 'Changing room':
        changingRoom.enter()

    elif playerLocation == 'Core warehouse':
        coreWarehouse.enter()

    elif playerLocation == 'Bioengineering components warehouse':
        BCWarehouse.enter()

    elif playerLocation == 'Biowaste incinerator':
        biowasteIncinerator.enter()
