print ("\nNow we will calculate your market basket\n-----------------------------------------\ntomato = 3 NIS\ncucumber = 2 NIS\nCola = 5 NIS\nchicken = 20 NIS")
tomato = int(input("\nHow many KG of tomato do your want to buy ?"))
cucumber = int(input("\nHow many KG of cucumber do your want to buy ?"))
cola = int(input("\nHow many KG of cola do your want to buy ?"))
chicken = int(input("\nHow many KG of chicken do your want to buy ?"))

print ("\nSunmmary of your orders : \n------------------------\nTomato : " + str (tomato) + "\nCucumber : " + str(cucumber) + "\nCola : " + str(cola) + "\nChicken : " + str(chicken))

summary = tomato*3 + cucumber*2 + cola*5 + chicken*20

print ("\nYou need to pay : " + str("%.2f" % (summary)) + " NIS without TAX")
print ("\nYou need to pay : " + str("%.2f" % (summary*1.17)) + " NIS include TAX")
