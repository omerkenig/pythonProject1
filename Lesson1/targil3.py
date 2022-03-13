
# print ("p1={}, p2={}, p3={}, p4={}".format(1 ,1.0 , "omer", red="BBFD"))

new_list = [2, 6.6, "Omer Kenig", 44]

print (new_list)

new_list2 = new_list + [77]
print (new_list2)

print (new_list[2])

my_list = [1, 2, 3, 44, "omer kenig"]
print ("My name is : "+ my_list[4] + ", And my age is: : " + str(my_list[3]))

my_list1 = list("1234567")
print (my_list1)
my_string = ''.join(my_list1)
print (my_string)
my_string = "Hello omer \n How are you today ?"
print (my_string)
print (my_string.split())
print (my_string.splitlines())

print ("The length is : " + str(len(my_string)))
my_list.append("omer")
my_list.append("kenig")
print(my_list)
