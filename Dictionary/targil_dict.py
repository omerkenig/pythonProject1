#dictionary

my_dict = {"www.google.com":"8.8.8.8", "www.youtube":"7.7.7.7", "www.ynet.co.il":["2.2.2.2","3.3.3.3"]}
print (my_dict)

my_dict2 = {"www.facebook.com":"7.7.7.7", "www.groo.coil":"9.9.9.9"}
my_dict.update(my_dict2)

print (my_dict)

print ("The number of entries is : "+ str(len(my_dict)))
print (my_dict["www.google.com"])
print (my_dict.values())
my_dict["www.google.com"]="1.2.3.4"
print (my_dict["www.google.com"])
print (my_dict.values())

print ("www.google.com" in my_dict)
print ("1.2.3.4" in my_dict)
print ("1.2.3.4" in my_dict.values())