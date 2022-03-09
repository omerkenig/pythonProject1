#for loops
from time import sleep
# for x in range(1,11):
#     print (x)
#
# list_omer=["banaba","apple","mango","ornage"]
# for x in range(len(list_omer)):
#     print(list_omer[x])
#
# for x in range(1,11,2):
#     print (x)
#
print("We will get you infromation from your class :\n")
for i in range(4):
    name = input("Enter an name : " )
    age = input("Enter an age : " )
    phone = input("Enter an phone : " )
    print("Printing student number " + str(i+1) + " details :\n")
    sleep(3)
    print("Full name : " + name + "\nAge : " + str(age) + "\nPhone : " + phone + "\n")