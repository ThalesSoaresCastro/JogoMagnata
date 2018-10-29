import os
num=0

for nome in os.listdir('./health'):
	print(str(nome))
	new=str(num)+".png"
	os.rename("./health/"+str(nome), "./health/"+str(new))
	print("antigo: "+ str(nome) + "novo: "+ str(new))
	num+=1