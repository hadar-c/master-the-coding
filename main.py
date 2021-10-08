import implementations.array as array
from implementations.colors import Bcolors as color

print(color.BOLD + color.BLUE + "DATA STRUCTURES ACTIONS:" + color.END)
running = True

while running:
    print(color.BOLD + color.YELLOW + "Actions menu:" + color.END)
    print("  0. Exit\n"
          "  1. Reverse string")
    choice = int(input(color.BOLD + color.RED + "\nChoose action:" + color.END))

    if choice == 0:
        running = False
    elif choice == 1:
        array.reverse()







