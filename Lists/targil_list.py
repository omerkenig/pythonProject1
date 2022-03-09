
my_list = [1, 2, 44, 6.6, "omer kenig"]
print ("My name is : " + my_list[4] + ", and my age is : " + str(my_list[2]))

my_list2 = list("1234567")
print (my_list2)

print (''.join(my_list2))

print (''.join(my_list2).split())

my_string = "Hello omer\nHow are you?"
print (my_string)
print (my_string.splitlines())

my_list = ["hello", 1, 66.6, "omer"]
print("The length is : " + str(len(my_list)))
my_list.append("wow")
my_list.append("Omer")
print("The new length is : " + str(len(my_list)))
my_list.insert(5, 44)
print (my_list)
my_list.pop(3)
print (my_list)

my_list = ["google", "facebook", "ebay", "apple"]
print ("ebay" in my_list)

