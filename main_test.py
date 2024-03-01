import random
import customtkinter
import tkinter
import webbrowser


#création du launcher

customtkinter.set_appearance_mode("system")
app=customtkinter.CTk()
app.title("Le Juste Prix")
app.geometry("400x400")

tabView = customtkinter.CTkTabview(app)
tabView.pack(padx=20,pady=20)

tabView.add("Menu Principal")
tabView.add("High-Score")
tabView.add("Contact")

tabView.set("Menu Principal")

label = customtkinter.CTkLabel(master=app,text="")
label.pack(pady=0)
label_plusmoins = customtkinter.CTkLabel(master=app,text="")
label_plusmoins.pack(pady=5)
label_win = customtkinter.CTkLabel(master=app,text="")
label_win.pack(pady=5)

#code pour le jeu juste prix
    
def jeu():    

    dialog= customtkinter.CTkInputDialog(text="Quel est ton nom ? : ",title="Nom") 
    nom = dialog.get_input()
    if len(nom)<=0:
        label.configure(text="Sans ton nom pas de jeu !") 
        exit 
    else:
        label.configure(text=f"Bonjour {nom} jouons ensemble !")
        while True : 
            dialog= customtkinter.CTkInputDialog(text="Quel est le prix de l'objet ?   :",title="Prix") 
            choix = dialog.get_input()
            if int(choix) == prix : 
                print(count)
                count = count+1
                score_final = score-count+1
                label_plusmoins.configure(text=f"Vous avez gagné en {count} coups !")
                label_win.configure(text=f"Votre score est de {score_final} sur {score} !")
                
                break
            elif int(choix) < prix :
                count = count+1
                score_final = score-count+1
                label_plusmoins.configure(text="C'est plus !")
            else : 
                count = count+1
                score_final = score-count+1
                label_plusmoins.configure(text="C'est moins !")
        
   
    
    # jeu
    dialog= customtkinter.CTkInputDialog(text="Choisis la valeur basse du prix : ",title="Valeur basse") 
    random_1 = dialog.get_input()
    
    dialog= customtkinter.CTkInputDialog(text="Choisis la valeur haute du prix : ",title="Valeur haute") 
    random_2 = dialog.get_input()

    count = 0
    score = int(random_2)-int(random_1)

    prix = random.randint(int(random_1),int(random_2))
    # print(prix) #le print prix sera a supprimer


#bouton pour le lancement du juste prix

boutton_jouer = customtkinter.CTkButton(tabView.tab("Menu Principal"), text="Jouer",command= jeu)
boutton_jouer.pack(padx=20,pady=20)


# code pour le renvois du bouton Contact

def contact(): 
    webbrowser.open('https://github.com/DevAlexTSN')

#bouton pour le lancement du contact

boutton_contact = customtkinter.CTkButton(tabView.tab("Contact"), text="Contactez-moi", command=contact)
boutton_contact.pack(padx=20,pady=20)



app.mainloop()




# customtkinter.set_appearance_mode("system")
# customtkinter.set_default_color_theme("blue")

# app1=customtkinter.CTk()
# app1.geometry("400x400")

# frame=customtkinter.CTkFrame(master=app1,
#                              width=200,
#                              height=200,
#                              corner_radius=10,
#                              bg_color="white")

# frame.pack(padx=20, pady=20)

# button1 =customtkinter.CTkButton(master=app1, text="Jouer")
# button1.place(relx=0.5, rely=0.6,anchor=tkinter.CENTER)

# button2 =customtkinter.CTkButton(master=app1, text="Recommencer")
# button2.place(relx=0.5, rely=0.7,anchor=tkinter.CENTER)

# app1.mainloop()









