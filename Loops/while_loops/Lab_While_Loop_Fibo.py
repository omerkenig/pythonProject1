from random import randint


while("True"):
    choise = input(print("Menu :\n-------------\n1. Print 100 numbers.\n2. Checking Fibo."
          "\n3. Random numbers until we get 12 or count 10 times\n"))
    if(choise == "1"):
        for i in range(100):
            print(i)

###################################################

    elif (choise == "2"):
        # fibo = [1, 2, 3, 5, 8, 13, 21]
        fibo = []
        for i in range (7):
            fibo.append(int(input("Enter a number : \n")))
        bool = "True"
        for i in range(2, len(fibo)):
            print(fibo[i])
            print(fibo[i - 1])
            print(fibo[i - 2])
            print("\n")
            if (fibo[i] == (fibo[i - 1] + fibo[i - 2])):
                continue
            else:
                bool = "False"
                break
        if (bool == "True"):
            print("This is fibo series")
        if (bool == "False"):
            print("This is not fibo series")

###################################################

    elif(choise == "3"):
        for counter in range(10):
            num = randint(1, 12)
            print(num)
            if (num == 12):
                print("We get the number 12")
                break
            else:
                print("Counter : " + str(counter) + " Number : " + str(num) + "\n")
        else:
            print("Choose only 1 - 3 ! ! !\n")
    exit = input("Do you want to exit y / n ?\n")
    if(exit == "y" or exit == "Y"):
        print("Thank you and bye bye ...\n")
        break


