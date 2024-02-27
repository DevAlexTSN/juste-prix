import random

#Choix du nom

name = input("Quel est votre nom ?")
print("Bonjour,"+ name +"!. Jouons ensemble! ")

#Choix par le jeu de la variable prix ( valeur entière entre 1 et 20)

random_1 = int(input("Choisis la valeur basse du prix "))
random_2 = int(input("Choisis la valeur haute du prix "))

prix = random.randint(random_1,random_2)
# print(prix) #le print prix sera a supprimer

while True : 
    choix=int(input("Quel est le prix de l'objet ?  " ))
    if choix == prix : 
        print('vous avez gagné')
        break
    elif choix < prix :
        print("c'est plus!")
    else : 
        print("c'est moins!")

