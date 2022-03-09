from random import randint
from time import sleep

money = (int(input("Please enter your money?\n")))
turns = (money//3)
print ("You have : " + str(turns) + " turns !\nYour change is : " + str(money%3) + " ILs\n")
prize = 0
for i in range( turns ):
    print("Round Number : " + str(i) + "\n---------------\n")
    cube1 = randint(1,6)
    cube2 = randint(1,6)
    print("Cube 1 is : " + str(cube1) + "\nCube 2 is : " + str(cube2) + "\n")

    if ( cube1 == cube2 ):
        if  ( cube1 == 6 ):
            print("\nYou won 1000 ILs\n")
            prize += 1000
        else:
            print("\nYou won 100 ILs\n")
            prize += 100
    elif (cube1 == 1):
            print("\nYou won 20 ILs\n")
            prize += 20
    elif (cube1 == 1):
            print("\nYou won 40 ILs\n")
            prize += 40

print("\nYou prize : " + str(prize) + " ILs")



