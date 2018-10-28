import os
num=0

for nome in os.listdir('./explosao'):
	print(str(nome))
	new=str(num)+".png"
	os.rename("./explosao/"+str(nome), "./explosao/"+str(new))
	print("antigo: "+ str(nome) + "novo: "+ str(new))
	num+=1