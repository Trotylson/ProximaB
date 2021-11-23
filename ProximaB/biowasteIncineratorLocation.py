import player
import time
import map

class BiowasteIncinerator:
    pass

localization = 'Biowaste incinerator'

def setCoordinates():
    map.forwardLocation = map.disposalRoom.localization
    map.backwardLocation = map.collisionObjects.localization
    map.leftLocation = map.collisionObjects.localization
    map.rightLocation = map.collisionObjects.localization

def enter():
    print("You entering to " + player.location + "...")
    time.sleep(1)

    if map.MAA.Availabilty.BiowasteIncinerator == True:
        print("You are in " + player.location + " now...")

    else:
        print("You can't enter to " + player.location + "! Door are closed...")
        player.location = player.lastLocation
        time.sleep(1)
