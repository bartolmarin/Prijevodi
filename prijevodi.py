#2023 GPL
#Autor: Krešimir Gracin 2023
import sys #za restartanje programa
import os #za relativni path u koji će se spremati testovi
from random import * #za nasumičan odabir zadatka
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#POKUŠAJ DA MI .EXE MOŽE OTVARATI .TXT FAJLOVE STRPANE U JEDAN .EXE JER SE OTVARAJU U /TMP PA IH NE MOŽE VIDJETI
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class MjestoMoje(Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg="#1F3951", fg="#fcfeab")

class Gumb(Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg="#1F3951", activebackground="#1F3951", activeforeground="#1F3951")




prozor=Tk()
prozor.title('Prijevodi')
#prozor.config(width=1000, height=500, bg="#423287")
prozor.config(width=1000, height=500, bg="#1F3951")
prozor.resizable(True, True)


# === MENI ===


def about():
    messagebox.showinfo('O Prijevodima', 'Program za vježbanje prevođenja rečenica prirodnog jezika na jezik logike prvog reda i obratno.\n Program možete vidjeti na:\n https://github.com/bartolmarin/Prijevodi')

def pomoc():
    messagebox.showinfo('Pomoć', '0. Očekivani odgovori (pogotovo oni izraženi prirodnim jezikom) samo su jedna mogućnost iskazivanja zadanog logičkog oblika. \n 1. Upišite ime datoteke u koju će se zapisivati vaši odgovori i očekivani odgovori. \n 2. Pritisnite tipku <Enter>. \n 3. Pritiskom gumba odaberite hoćete li prevoditi s prirodnog ili na prirodni jezik.\n 4. Ako ćete prevoditi s prirodnog na jezik logike prvog reda, pogledajte desno kako ćete upisati veznike i kvantifikatore (važno je da oko svake riječi ostanu praznine).\n 5. Pritisnite gumb "PritisniMe".\n 6. Za prihvaćanje vašeg odgovora dovoljno je nakon unosa pritisnuti tipku <Enter>.\n 7. Na kraju pritisnite gumb na dnu lijevo i pritisnite "q" za izlaz iz programa ')

menubar = Menu(prozor, bg="#eff0b9")  
menubar.add_command(label="Pomoć", command=pomoc)
menubar.add_command(label="O programu", command=about)  
prozor.config(menu=menubar)


# =====KRAJ MENIJA========




# ==== TEKST NA PROZORU =====
naslov = ImageTk.PhotoImage(Image.open(resource_path("naslov.png")))
naslov1 = MjestoMoje(prozor, image = naslov,borderwidth=0, highlightthickness=0, padx=0, pady=0)
naslov1.grid(row=0,column=0, columnspan=4,sticky="ns", pady=20)

#   o1=MjestoMoje(prozor,text="Prijevodi: jezik logike prvog reda - prirodni jezik",font=("Roboto", 25))
#   o1.grid(row=0 ,columnspan=3, pady=20)
o2=MjestoMoje(prozor,text="Zadana je rečenica:",font=("Roboto", 13))
o2.grid(row=3 ,column=0, sticky='w', pady=20, padx=15)
ob=MjestoMoje(prozor,text="Vaš prijevod: ",font=("Roboto", 13),borderwidth=0, )
ob.grid(row=4 ,column=0, sticky='w', pady=20, padx=15)
b=Entry(prozor,width=50,font=15)
b.grid(row=4 ,column=1)
o3=MjestoMoje(prozor,text="Vaš odgovor:",font=("Roboto", 13))
o3.grid(row=5 ,column=0, sticky='w', pady=20, padx=15)
o4=MjestoMoje(prozor,text="Očekivani odgovor:",font=("Roboto",13))
o4.grid(row=6 ,column=0, sticky='w', pady=20, padx=15)


#Da bi mi se Label apdejtao, tj. da ne bi išao tekst preko teksta, pa ako je dulji ostajao, već kako bi se svakim novim klikom brisao moram: 
#1. u glavnom dijelu napraviti Label s praznim tekstom; 
#2. u funkciji (u ovom slučaju glavno(), napraviti lejbl globalnim: global lejbl, te zadati naredbu: lejbl.place_forget() - da ga zaboravi, te nakon toga 
#3. ponovo ga postaviti lejbl=Label.. unutar funkcije s željenim tekstom - 
# To ovdje možeš pratiti s ozadatak, oodgovor i oocekivano
ozadatak=MjestoMoje(prozor,text="",font=("Roboto",20))
ozadatak.grid(row=3 ,column=1)
oodgovor=MjestoMoje(prozor,text='',font=("Roboto",20))
oodgovor.grid(row=4 ,column=1)
oocekivano=MjestoMoje(prozor,text='',font=("Roboto",18))
oocekivano.grid(row=5 ,column=1)

#f = open("e.txt", "w") 
#Otvori ili napravi fajl u koji ćeš upisivati rezultate
o0=MjestoMoje(prozor, text="Napišite ime fajla u koji želite spremiti rezultate\n (na kraju stitnite <Enter>)", font=13)
o0.grid(row=2 ,column=0, sticky='w', padx=15)
mojfajl=Entry(prozor,width=20,font=25)
mojfajl.grid(row=2 ,column=1, sticky='w')


# ===== KRAJ TEKSTA NA PROZORU =====





#Otvori dva dokumenta iz kojih uzimaš retke
k = open(resource_path('kvantificirane.txt'), 'r', encoding="UTF8")#ovo je za .exe fajl koji sprema u /temp da bi mu kvantificirane i obicne.txt bile dostupne!! encoding treba specificirati zbog toga što Windowsi neće moći pročitati ako im nije rečeno

#k = resource_path('kvantificirane.txt')
sadrzajk=k.read()
o = open(resource_path('obicne.txt'), 'r', encoding="UTF8")
#o = resource_path('obicne.txt') 
sadrzajo=o.read()

def brisi():
    mojfajl.grid_forget()
    o0.grid_forget()

fajl=str()

def upis():
    global fajl
    global f
    fajl=mojfajl.get()
    fajl=str(fajl)+str(".txt")
#    f=open(os.path.join('./testovi', fajl), 'a')
    f=open(fajl, 'a', encoding="UTF8")

    if fajl[-1]=="t":
        brisi()

mojfajl.bind('<Return>',lambda event: upis())

brojac=0

#================ OBOSTRANO S IF FUNKCIJAMA U KLJUČNIM TRENUCIMA  ====================


def smjer(s_jezika,na_jezik):
    def glavno():
        global fajl
        global f
        global ozadatak
        global oodgovor
        global oocekivano
        oodgovor.grid_forget()
        oocekivano.grid_forget()
        ozadatak.grid_forget()
        global odaberi
        global zadatak
        odaberi=randint(1,182)
        
        if s_jezika == "obicni" and na_jezik == "lpr":
            lista1=[]
            lista1=list(map(str,sadrzajo.splitlines()))
        else:
            lista1=list(map(str,sadrzajk.splitlines()))
        zadatak=lista1[odaberi]
        ozadatak=MjestoMoje(prozor,text=str(zadatak),font=("Roboto",15), bg="#e7c96b")
        ozadatak.grid(row=3 ,column=1)
        #brojač broji broj klikova na PritisniMe i time numerira zadatke u dokumentu
        global brojac
        brojac=brojac + 1
        #Upisuje se u odabrani dokument u ./testovi/mojfajl.txt
        f.write('\n\n\n' + str(brojac) +". ZADATAK"+'\n\n')
        f.write(str(zadatak)+'\n')

    def rezultat():
        #Ovo više ne znam trebaju li mi ove iste globalne varijable u glavno(). Sad se briše stari ulaz nakon što se pokrene glavno() s novim zadatkom
        global fajl
        global f
        global oodgovor
        global oocekivano
        oodgovor.grid_forget()
        oocekivano.grid_forget()

        odgovor=str(b.get())

        if s_jezika == "obicni" and na_jezik == "lpr":
            odgovor=list(map(str,odgovor.split()))
            for j in range(len(odgovor)):
                if odgovor[j]=='svi':
                    odgovor[j]='∀'
                elif odgovor[j]=='postoji':
                    odgovor[j]='∃'
                elif odgovor[j]=='i':
                    odgovor[j]='∧'
                elif odgovor[j]=='ili':
                    odgovor[j]='∨'
                elif odgovor[j]=='samoako':
                    odgovor[j]='→'
                elif odgovor[j]=='ne':
                    odgovor[j]='¬'
                elif odgovor[j]=='akoisamoako':
                    odgovor[j]='↔'
                elif odgovor[j]=='nejed':
                    odgovor[j]='≠'
                elif odgovor[j]=='protuslovlje':
                    odgovor[j]='⊥'
            odgovor=''.join(odgovor)

        oodgovor=MjestoMoje(prozor,text=str(odgovor),font=("Roboto",20), bg="#e7c96b")
        oodgovor.grid(row=5 ,column=1)
        #Upisuje u fajl
        f.write("Vaš odgovor je: "+ "\""+str(odgovor)+"\""+'\n')
        #Traži očekivani odgovor
        if s_jezika == "obicni" and na_jezik == "lpr":
            lista2=list(map(str,sadrzajk.splitlines()))
        else:    
            lista2=list(map(str,sadrzajo.splitlines()))
        ocekivaniOdgovor=lista2[odaberi]
        oocekivano=MjestoMoje(prozor,text=str(ocekivaniOdgovor),font=("Roboto",18), bg="#e7c96b")
        oocekivano.grid(row=6 ,column=1)


        #Piše očekivani odgovor
        f.write("Očekivani odgovor je: "+ str(ocekivaniOdgovor) +'\n\n\n')

        b.delete(0,END)
    def zavrsi():
        global f
        f.write('\n\n\n'+"============ Kraj ============= "+'\n\n\n')



#====== Odabirenje vrste igre ===========


lprob=Gumb(prozor, image=p2, cursor="hand1", text="Lpr na obični", font=("Roboto",13), command=lprnaobicni)
lprob.config(borderwidth=0,  highlightthickness=0, pady=0, padx=0)
lprob.grid(row=1 ,column=1, pady=20, sticky='W', padx=15)

oblpr=Gumb(prozor, image=p1, cursor="hand1", text="Obični na Lpr", font=("Roboto",13),command=obicninalpr)
oblpr.config(borderwidth=0,  highlightthickness=0, pady=0, padx=0)
oblpr.grid(row=1 ,column=0, sticky='E', padx=15)

prozor.mainloop()
k.close()
o.close()
