
#!/usr/bin/python3.6.4
#print("hello \nmod***f***rs")

''' 
comentaire
sur plusier 
ligne
ligne


a = 10
b = 5
print (a+b)

text ="of \"the\" wa"

print ("hello guys %s" %(text))


mylist =["tat","toto"]
mylist2=myliste
mylist=0
print mylist2


maListe = range (15)

liste = list(range (10)) #liste = range (10) crée un objet de type range dans lequels la fonction extend n'existe pas

liste.extend(maListe)

print (liste)


def myfunction (a=0,b=1):
	print (a+b)

			nbvie-=1
			print ("nombre de vie restantes : "+nbvie)
			print ("essaye encore BAAAKAAA:")
myfunction()
'''
from random import *

def guessn ():
	nbvie=10
	secret=randint(1,10)
	nbusers=int (input("devinez le nombre secret : "))	
	#while (nbvie != 0 and good==false):
	while (nbusers != secret and nbvie!=0):
		if (nbusers < secret):
			print ("trop petit")
		else:
			print ("trop grand")
		nbusers=int (input("devinez le nombre secret : "))
		nbvie-=1
		print ("nombre de vie restantes : "+ str(nbvie)
	
	if (nbvie!=0):
		print("vous avez réussi")
	else:
		print("vous avez perdu")

guessn()
