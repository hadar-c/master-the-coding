import implementations.array as array

print('\033[1m' + '\033[94m' + "DATA STRUCTURES ACTIONS:" + '\033[0m')
running = True

while running:
    print('\033[1m' + '\033[92m' + "Actions menu:" + '\033[0m')
    print("0. Exit\n"
          "1. Reverse string")
    choice = int(input("\nChoose action:"))

    if choice == 0:
        running = False
    elif choice == 1:
        array.reverse()







