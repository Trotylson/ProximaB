import player
import time
import map

class DisposalRoom:
    pass

def setCoordinates():
    map.forwardLocation = 'Warehouse of recovered components'
    map.backwardLocation = 'Biowaste incinerator'
    map.leftLocation = 'Wall'
    map.rightLocation = 'Ether'

def enter():
    print("You entering to " + player.location + "...")
    time.sleep(1)

    if map.MAA.MapAreaAvailability.DisposalRoom == True:
        print("You are in " + player.location + " now...")

    else:
        print("You can't enter to " + player.location + "! Door are closed...")
        player.location = player.lastLocation
        time.sleep(1)
