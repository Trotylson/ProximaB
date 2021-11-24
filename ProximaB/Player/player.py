import Player.move as move
import World.itemList as itemList

Location = "Ether - Drone bay"
LastLocation = ""
HealthPoints = 100
Biocomponents = 100
PowerSupply = 100

Inventory = {itemList.GoldCoin:100, itemList.Plate:10}

def playerMove():
    while True:
        if True:
            move.moveSelection(Location)
        else: break

def schowStats():
    print('\n\nDrone localization: ' 
          + Location.upper())
    print('-----------------------------------')
    print('Drone vitality condition: ' + str(HealthPoints) + '%')
    print('Drone efficiency of biocomponents: ' + str(Biocomponents) + '%')
    print('Drone power supply: ' + str(PowerSupply) + '%')
    print('-----------------------------------\n')


