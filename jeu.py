import random


random_1 = int(input("Choisis la valeur basse du prix "))
random_2 = int(input("Choisis la valeur haute du prix "))

count = 0
score = random_2-random_1

prix = random.randint(random_1,random_2)
# print(prix) #le print prix sera a supprimer1


while True :
    choix=int(input("Quel est le prix de l'objet ?  " ))
    if choix == prix : 
        print(count)
        count = count+1
        score_final = score-count
        print("vous avez gagné en " + str(count) + " coups !")
        print("Votre score est de " +str(score_final)+ " points sur  " + str(score)+ "!")
        break
    elif choix < prix :
        count = count+1
        score_final = score-count
        print("c'est plus!")
        
    else : 
        count = count+1
        score_final = score-count
        print("c'est moins!")