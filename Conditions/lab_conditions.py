from time import sleep

print ("\n1. Instert number and ** it by 3")
print ("2. Insert 4 IP's to list and print it")
print ("3. Insert 4 entries to DNS_Dictionary and print it")
print ("4. Check if a string is Polindrom")
choice = input("your option is :\n")
if (choice=="1"):
    print ("The new number is : "+ str(int(input("Enter a number "))**3))
elif (choice=="2"):
    list_ip = []
    list_ip.append(input("Enter new IP: \n"))
    list_ip.append(input("Enter new IP: \n"))
    list_ip.append(input("Enter new IP: \n"))
    list_ip.append(input("Enter new IP: \n"))
    print ("\nThe new list is : \n---------------\n" + str(list_ip))
elif (choice == "3"):
    dns_dict={}
    dns_dict.update({input("Enter URL : ") : input( "Enter IP : ")})
    dns_dict.update({input("Enter URL : ") : input( "Enter IP : ")})
    dns_dict.update({input("Enter URL : ") : input( "Enter IP : ")})
    dns_dict.update({input("Enter URL : ") : input( "Enter IP : ")})
    print("\nThe new dns_dict is : \n---------------\n" + str(dns_dict))
elif (choice=="4"):
    word = input("\nEnter a word : ")
    if (word == word[::-1]):
        print("This word is Polindrom !")
    else:
        print("This word isn't Polindrom !")

else:
    print("Enter 1-4 only ! ! !\n")
