import sys
import devTools as console
import mainMenu
import time

def open():
    while True:
        print('\n\n\tMENU:\n\n\t\tSave game (to save your actual game)\n' +
              '\t\tLoad game (to load last save)\n' +
              '\t\tMain Menu (to open main menu)\n\n' +
              '\t\tExit (to exit from menu panel)\n' +
              '\t\tQUIT (to quit drone terminal)\n\n\n')
        choice = input('Type your choice: ').lower()
        
        if choice == 'main menu':
            console.clear()
            mainMenu.open()
        elif choice == 'save game':
            console.clear()
            break
        elif choice == 'load game':
            console.clear()
            break
        elif choice == 'exit':
            console.clear()
            break
        elif choice == 'quit':
            sys.exit()
        else: print('There is no option:', choice)
        time.sleep(2)
        console.clear()
