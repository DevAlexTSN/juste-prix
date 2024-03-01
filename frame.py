import tkinter
import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app1=customtkinter.CTk()
app1.geometry("400x400")

frame=customtkinter.CTkFrame(master=app1,
                             width=200,
                             height=200,
                             corner_radius=10,
                             bg_color="white")

frame.pack(padx=20, pady=20)

button1 =customtkinter.CTkButton(master=app1, text="Jouer")
button1.place(relx=0.5, rely=0.6,anchor=tkinter.CENTER)

button2 =customtkinter.CTkButton(master=app1, text="Recommencer")
button2.place(relx=0.5, rely=0.7,anchor=tkinter.CENTER)

app1.mainloop()