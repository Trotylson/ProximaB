import sys
import devTools as console
import time

def open():
    while True:
        print('\n\n\tMENU:\n\n\t\tNEW GAME\n' +
              '\t\tLOAD GAME\n\n' +
              '\t\tQUIT\n\n\n')
        choice = input('Type your choice: ').lower()

        if choice == 'new game':
            console.clear()
            break
        elif choice == 'load game':
            console.clear()
            break
        elif choice == 'quit':
            sys.exit()
        else: print('There is no option:', choice)
        time.sleep(2)
        console.clear()