from random import randint
from time import sleep

def menu():
    while (True):
        choice = input("Menu : \n-----------------\n1. Dog's Details\n2. Friends list\n3. N azzeret\n")
        if (choice == "1") :
            Dogs()
        elif (choice == "2") :
            Friends()
        elif (choice == "3"):
            Azzert()
        else:
            print("Enter 1-3 only !!!\n")
            continue
        exit = input("Do you want to exit y / n ?\n")
        if (exit=="y" or exit=="yes"):
            print("Bye Bye ! ! !\n")
            break
        else:
            print("Welcome back")

def Dogs():
    name = input("Enter dog's name : \n")
    age = int(input("Enter dog's age : \n"))
    print("Dog's name : " + name + " Dog's age : " + str(age*7) + "\n")
def Friends():
    list_friends=[]
    for i in range(5):
        list_friends.append(input("Enter a friend's name: \n" ))
    name = input("Enter new name :\n ")
    if (name in list_friends):
        print (name + " is allready in ths list ! ! !\n")
    else:
        print(name + " isn't in ths list\n")
def Azzert():
    num = int(input("Enter a number please :\n"))
    sum = 1
    for i in range(1,num+1):
        sum*= i
    print(str(num) + " Azzert is " + str(sum))

menu()