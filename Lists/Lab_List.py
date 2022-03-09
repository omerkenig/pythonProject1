
my_information = ["Omer Kenig", 44, "omerkenig@gmail.com", "0525-666336"]
print ("Full name : " + my_information[0] + "\nAge : " + str(my_information[1]) + "\nMail :"
       + my_information[2] + "\nPhone : " + my_information[3])
list_ip = ["192.168.1.1", "1.1.1.1"]
print (list_ip)
list_ip.append("2.2.2.2")
print (list_ip)
list_ip.append("3.3.3.3")
print (list_ip)
list_ip.append("4.4.4.4")
print (list_ip)
list_ip.pop(2)
print (list_ip)
print ("We have " + str(len(list_ip)) + " IP's address\nAnd the list is : " + str(list_ip))