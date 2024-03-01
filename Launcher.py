import random, customtkinter, tkinter,webbrowser
import PIL
from PIL import Image

customtkinter.set_appearance_mode("light")
app=customtkinter.CTk()

image = PIL.Image.open("fond_1.png")
background_image = customtkinter.CTkImage(image, size=(800, 800))

app.title("Launcher Mini-Game")
app.geometry("800x800")

tabView = customtkinter.CTkTabview(app)
tabView.pack(padx=20,pady=20)

tabView.add("Menu Principal")
# tabView.add("High-Score")
tabView.add("Contact")

tabView.set("Menu Principal")

#partie Contact

def contact(): 
    webbrowser.open('https://github.com/DevAlexTSN')

boutton_contact = customtkinter.CTkButton(tabView.tab("Contact"), text="Contactez-moi",command= contact)
boutton_contact.pack(padx=20,pady=20)

#partie Menu Principal

#Bouton qui ouvre une nouvelle frame "Juste Prix"
def launcher_JP():
    customtkinter.set_appearance_mode("system")
    game_jp=customtkinter.CTk()
    game_jp.title("Le Juste Prix")
    game_jp.geometry("400x400")
    
    label_name = customtkinter.CTkLabel(game_jp,text="")
    label_name.pack(pady=0)
    
    label_plusmoins = customtkinter.CTkLabel(game_jp,text="")
    label_plusmoins.pack(pady=5)
    
    label_win = customtkinter.CTkLabel(game_jp,text="")
    label_win.pack(pady=5)

    def jeu_jp():
        
        dialog= customtkinter.CTkInputDialog(text="Quel est ton nom ? : ",title="Nom") 
        nom = dialog.get_input()
        if len(nom)<=0:
            label_name.configure(text="Sans nom pas de jeu")
            return
        else :
            label_name.configure(text=f"Bonjour {nom} jouons ensemble !")
        count = 0
        
    
        dialog= customtkinter.CTkInputDialog(text="Choisis la valeur basse du prix : ",title="Valeur basse") 
        random_1 = dialog.get_input()
        
        dialog= customtkinter.CTkInputDialog(text="Choisis la valeur haute du prix : ",title="Valeur haute") 
        random_2 = dialog.get_input()
        
        score = int(random_2)-int(random_1)
        prix = random.randint(int(random_1),int(random_2))

        while True : 
            dialog= customtkinter.CTkInputDialog(text="Quel est le prix de l'objet ?   :",title="Prix") 
            choix = dialog.get_input()
            
            if int(choix) == prix : 
                count = count+1
                score_final = score-count+1
                label_plusmoins.configure(text=f"Vous avez gagné en {count} coups !")
                label_plusmoins.pack(pady=5)
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



    boutton_game_JP = customtkinter.CTkButton(game_jp,text="Lancez le Juste Prix",command=jeu_jp)
    boutton_game_JP.pack(padx=20,pady=20)
    
    game_jp.mainloop()

boutton_play_JP = customtkinter.CTkButton(tabView.tab("Menu Principal"), text="Jouez au Juste Prix",command= launcher_JP)
boutton_play_JP.pack(padx=20,pady=20)

def quitter():
    quit()
    




#Bouton qui ouvre une nouvelle frame "Tic-Tac-Toe"

boutton_play_TTT = customtkinter.CTkButton(tabView.tab("Menu Principal"), text="Jouez Tic-tac-Toe")
boutton_play_TTT.pack(padx=20,pady=20)

boutton_quit=customtkinter.CTkButton(tabView.tab("Menu Principal"), text="Quitter",command=quitter)
boutton_quit.pack(padx=20,pady=20)

app.mainloop()