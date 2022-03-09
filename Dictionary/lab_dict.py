#dictionary

dict_money = {"omer":10000, "liat":20000, "or":30000,"shir":40000, "ziv":50000}
print (dict_money)
summary = ((dict_money["omer"] + dict_money["ziv"]))
print ("The summary is : " + str(dict_money["omer"] + dict_money["ziv"] ))
#dict_money["ran"] =summary
#print (dict_money)
dict_money.update({"ran":summary})
print (dict_money)
print ("The number of entries is : " + str(len(dict_money)))
print ("omer" in dict_money)