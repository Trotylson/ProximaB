import Player.player as player
import time
import World.Map.map as map

class BiowasteIncinerator:
    pass

localization = 'Biowaste incinerator'

def setCoordinates():
    map.forwardLocation = map.disposalRoom.localization
    map.backwardLocation = map.collisionObjects.localization
    map.leftLocation = map.collisionObjects.localization
    map.rightLocation = map.collisionObjects.localization

def enter():
    print("You entering to " + player.Location + "...")
    time.sleep(1)

    if map.MAA.Availabilty.BiowasteIncinerator == True:
        print("You are in " + player.Location + " now...")

    else:
        print("You can't enter to " + player.Location + "! Door are closed...")
        player.Location = player.LastLocation
        time.sleep(1)
