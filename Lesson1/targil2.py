num = int(input("Enter number iwth 4 digits: "))


'''
Alafim = 4
Meot = 5
Asarot = 6
Ahadot = 7
'''

print ("\nalafim is : " + str(num//1000))
print ("Meot is : " + str((num%1000)//100))
print ("Asarot is : " + str((num%100)//10))
print ("Ahadot is : " + str(num%10))

print ("\nalafim is : " + str(num//1000) + "\nMeot is : " + str((num%1000)//100) + "\nAsarot is : " + str((num%100)//10) + "\nAhadot is : " + str(num%10))