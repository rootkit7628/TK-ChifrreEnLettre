from tkinter import *
import webbrowser
import translator 

def profil_fb():
    webbrowser.open_new("https://www.github.com/rootkit7628")
def translation():
        res=translator.main(dvar.get())
        reponse.config(text="In Letter : "+res)
        reponse.update()        

#créer fntre
Window = Tk()
reponse=NONE

#Custom fenetre*
Window.title('Convertisseur chiffre en lettre')
Window.geometry("600x400+400+200")
Window.minsize(900, 200)
Window.maxsize(1366, 768) 
Window.config(background ='black')
#Window.iconbitmap("icon.png")

#créer une boîte
boite=Frame(Window, bg='black')

#Créer image
w=100
h=100
image=PhotoImage(file="home.gif").zoom(10).subsample(32)
canva=Canvas(boite, width=w, height=h, bg='black', bd=0, highlightthickness=0 )
canva.create_image(w/2, h/2, image=image)
canva.pack()

#Ajout de texte
soratra = Label(boite, text="Welcome In this App", font=("Helvetica", 30), bg='black', fg='aqua') 
soratra.pack() 

#Ajout de texte
soratra2 = Label(boite, text="This is a translator of number in letter", font=("Courrier", 15), bg='black', fg='aqua') 
soratra2.pack()

#Ajout de texte
helpi = Label(boite, text="Enter a number below", font=("Arial", 10), bg='black', fg='white') 
helpi.pack()

#créer une imput pour entrer le nombre
dvar = IntVar()
nb = Entry(boite, textvariable=dvar, font=("Arial", 10), bg='white', fg='black') 
nb.pack(fill=X)

#un espace
blank = Label(boite, text="", bg="black")
blank.pack()

#Bouton de conversion
bton2 = Button(boite, text="Translate", font=("Courrier", 10), bg='black', fg='aqua', command=translation) 
bton2.pack(fill=X)

#Ajout de la boite
boite.pack(expand=YES)

#Ajout un lien
bton2 = Button(Window, text="About me", font=("Courrier", 10), bg='black', fg='aqua', command=profil_fb) 
bton2.pack(expand=YES)

#menu_bar
barmenu=Menu(Window)

#1er menu
menu1=Menu(barmenu, tearoff=0)
menu1.add_command(label="Restart")
menu1.add_command(label="Quit", command=Window.quit)
barmenu.add_cascade(label="File", menu="menu1")

#un espace
blank = Label(boite, text="", bg="black")
blank.pack()

#Afficher la reponse
reponse=Label(boite, text='', bg="black", fg="aqua", font=("Arial", 12))
reponse.pack()

#Afficher sur la fenetre
Window.config(menu="barmenu")

#affiche la fenetre
Window.mainloop()
