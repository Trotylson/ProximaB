import Player.player as player
import World.itemList as itemList
import devTools as console

emptyDict = {} # element that trashing the code...

def schowInventory():
    if player.Inventory == emptyDict:
        print('INVENTORY: EMPTY')
    else:
        print('INVENTORY:\n')
        for i, v in player.Inventory.items():
            print('\t' + str(i), '('+str(v), 'pcs)')
    input('\nPress any key to close your drone inventory...')
    console.clear()

def tradeItem(editingItem, value):
    addItem(editingItem, 0)
    checkAmount = player.Inventory[editingItem] + value

    if checkAmount >= 0:
        player.Inventory[editingItem] += value
    else: print("You don't have that much", editingItem + "'s")

    if checkAmount <= 0:
        del(player.Inventory[editingItem])


def addItem(editingItem, value):
    if editingItem not in player.Inventory.keys():
        player.Inventory[editingItem] = value
    else: player.Inventory[editingItem] += value