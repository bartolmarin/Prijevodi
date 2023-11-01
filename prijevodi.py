#2023 GPL
#Autor: Krešimir Gracin
import sys #za restartanje programa
import os #za relativni path u koji će se spremati testovi
from random import * #za nasumičan odabir zadatka
from tkinter import *


#POKUŠAJ DA MI .EXE MOŽE OTVARATI .TXT FAJLOVE STRPANE U JEDAN .EXE JER SE OTVARAJU U /TMP PA IH NE MOŽE VIDJETI
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)




prozor=Tk()
prozor.title('Prijevodi')
prozor.config(width=1500, height=900)
prozor.resizable(True, True)

o1=Label(prozor,text="Prijevodi: jezik logike prvog reda - prirodni jezik",font=("Roboto", 25))
o1.place(x=450,y=50)
o2=Label(prozor,text="Zadana je rečenica:",font=("Roboto", 13))
o2.place(x=50,y=300)
ob=Label(prozor,text="Napišite prijevod rečenice koja je zadana: ",font=("Roboto", 13))
ob.place(x=50, y=350)
b=Entry(prozor,width=50,font=15)
b.place(x=400,y=350)
o3=Label(prozor,text="Vaš odgovor:",font=("Roboto", 15))
o3.place(x=50,y=500)
o4=Label(prozor,text="Očekivani odgovor:",font=("Roboto",15))
o4.place(x=50,y=600)






#Da bi mi se Label apdejtao, tj. da ne bi išao tekst preko teksta, pa ako je dulji ostajao, već kako bi se svakim novim klikom brisao moram: 
#1. u glavnom dijelu napraviti Label s praznim tekstom; 
#2. u funkciji (u ovom slučaju glavno(), napraviti lejbl globalnim: global lejbl, te zadati naredbu: lejbl.place_forget() - da ga zaboravi, te nakon toga 
#3. ponovo ga postaviti lejbl=Label.. unutar funkcije s željenim tekstom - 
# To ovdje možeš pratiti s ozadatak, oodgovor i oocekivano
ozadatak=Label(prozor,text='',font=("Roboto",20))
ozadatak.place(x=250,y=300)
oodgovor=Label(prozor,text='',font=("Roboto",20))
oodgovor.place(x=310,y=500)
oocekivano=Label(prozor,text='',font=("Roboto",18))
oocekivano.place(x=310,y=600)

#f = open("e.txt", "w") 
#Otvori ili napravi fajl u koji ćeš upisivati rezultate
o0=Label(prozor, text="Napišite ime fajla u koji želite spremiti rezultate (na kraju stitnite <Enter>)", font=15)
o0.place(x=50, y=220)
mojfajl=Entry(prozor,width=20,font=25)
mojfajl.place(x=650,y=220)

#Otvori dva dokumenta iz kojih uzimaš retke
k = open(resource_path('kvantificirane.txt'), 'r', encoding="UTF8")#ovo je za .exe fajl koji sprema u /temp da bi mu kvantificirane i obicne.txt bile dostupne!!

#k = resource_path('kvantificirane.txt')
sadrzajk=k.read()
o = open(resource_path('obicne.txt'), 'r', encoding="UTF8")
#o = resource_path('obicne.txt') 
sadrzajo=o.read()

def brisi():
    mojfajl.place_forget()
    o0.place_forget()

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

def lprnaobicni():
    def glavno():
        global fajl
        global f
        global ozadatak
        global oodgovor
        global oocekivano
        oodgovor.place_forget()
        oocekivano.place_forget()
        ozadatak.place_forget()
        global odaberi
        global zadatak
        odaberi=randint(1,182)
        lista1=list(map(str,sadrzajk.splitlines()))
        zadatak=lista1[odaberi]
        ozadatak=Label(prozor,text=str(zadatak),font=("Roboto",15))
        ozadatak.place(x=250,y=300)
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
        oodgovor.place_forget()
        oocekivano.place_forget()

        odgovor=str(b.get())
        oodgovor=Label(prozor,text=str(odgovor),font=("Roboto",20))
        oodgovor.place(x=310,y=500)
        #Upisuje u fajl
        f.write("Vaš odgovor je: "+ "\""+str(odgovor)+"\""+'\n')
        #Traži očekivani odgovor
        lista2=list(map(str,sadrzajo.splitlines()))
        ocekivaniOdgovor=lista2[odaberi]
        oocekivano=Label(prozor,text=str(ocekivaniOdgovor),font=("Roboto",18))
        oocekivano.place(x=310,y=600)
        #Piše očekivani odgovor
        f.write("Očekivani odgovor je: "+ str(ocekivaniOdgovor) +'\n\n\n')
        
        b.delete(0,END)
    def zavrsi():
        global f
        f.write('\n\n\n'+"============ Kraj ============= "+'\n\n\n')
    z=Button(prozor, text="PritisniMe", font=("Roboto"), command=glavno)
    z.place(x=900,y=300)
    g=Button(prozor, text="Priloži rješenje", command=rezultat)
    g.place(x=900,y=350)
    kraj=Button(prozor, text="Ako ti  je dosta, prvo mene stisni pa utipkaj 'q'!", command=zavrsi)
    kraj.place(x=100,y=800)
    #Ovo bi trebalo nakon <Return> pokrenuti glavno() ili rezultat(), ne znam... u svakom slučaju, da ne klikamo gumb, nego tipke
    b.bind('<Return>',lambda event: rezultat())


    prozor.bind('q', lambda event:prozor.destroy()) 




######   OBIČNI NA LPR ###########




def obicninalpr():
    def glavno():
        global fajl
        global f
        global ozadatak
        global oodgovor
        global oocekivano
        #brojač broji broj klikova na PritisniMe i time numerira zadatke u dokumentu
        global brojac
        brojac=brojac + 1

        oodgovor.place_forget()
        oocekivano.place_forget()
        ozadatak.place_forget()
        global odaberi
        global zadatak
        odaberi=randint(1,182)
        lista1=[]
        lista1=list(map(str,sadrzajo.splitlines()))
        zadatak=lista1[odaberi]
        ozadatak=Label(prozor,text=str(zadatak),font=("Roboto",15))
        ozadatak.place(x=250,y=300)

        #Upisuje se u odabrani dokument u ./testovi/mojfajl.txt
        f.write('\n\n\n' + str(brojac) +". ZADATAK"+'\n\n')
        f.write(str(zadatak)+'\n')

    def rezultat():    
        #Ovo više ne znam trebaju li mi ove iste globalne varijable u glavno(). Sad se briše stari ulaz nakon što se pokrene glavno() s novim zadatkom
        global fajl
        global f
        global oodgovor
        global oocekivano
        oodgovor.place_forget()
        oocekivano.place_forget()

        odgovor=str(b.get())
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
        odgovor=''.join(odgovor)
        oodgovor=Label(prozor,text=str(odgovor),font=("Roboto",20))
        oodgovor.place(x=310,y=500)
        #Upisuje u fajl
        f.write("Vaš odgovor je: "+ "\""+str(odgovor)+"\""+'\n')
        #Traži očekivani odgovor
        lista2=list(map(str,sadrzajk.splitlines()))
        ocekivaniOdgovor=lista2[odaberi]

        oocekivano=Label(prozor,text=str(ocekivaniOdgovor),font=("Roboto",18))
        oocekivano.place(x=310,y=600)
        #Piše očekivani odgovor
        f.write("Očekivani odgovor je: "+ str(ocekivaniOdgovor) +'\n\n\n')
        
        b.delete(0,END)
    def zavrsi():
        global f
        f.write('\n\n\n'+"============ Kraj ============= "+'\n\n\n')
    z=Button(prozor, text="PritisniMe", font=("Roboto"), command=glavno)
    z.place(x=900,y=300)
    g=Button(prozor, text="Priloži rješenje", command=rezultat)
    g.place(x=900,y=350)
    kraj=Button(prozor, text="Ako ti  je dosta, prvo mene stisni pa utipkaj 'q'!", command=zavrsi)
    kraj.place(x=100,y=800)
    #Ovo bi trebalo nakon <Return> pokrenuti glavno() ili rezultat(), ne znam... u svakom slučaju, da ne klikamo gumb, nego tipke
    b.bind('<Return>',lambda event: rezultat())


    prozor.bind('q', lambda event:prozor.destroy()) 

    #UPUTE ZA UNOS SIMBOLA - dolje desno

    kljuc=Label(prozor,text='Ključ upisivanja:',font=("Roboto",10))
    kljuc.place(x=850,y=400)
    svi=Label(prozor,text='svi = ∀',font=("Roboto",10))
    svi.place(x=950,y=430)
    postoji=Label(prozor,text='postoji = ∃',font=("Roboto",10))
    postoji.place(x=950,y=460)
    ne=Label(prozor,text='ne = ¬',font=("Roboto",10))
    ne.place(x=950,y=490)
    i=Label(prozor,text='i = ∧',font=("Roboto",10))
    i.place(x=950,y=520)
    ili=Label(prozor,text='ili = ∨',font=("Roboto",10))
    ili.place(x=950,y=550)
    samoako=Label(prozor,text='samoako = →',font=("Roboto",10))
    samoako.place(x=950,y=580)
    akoisamoako=Label(prozor,text='akoisamoako = ↔',font=("Roboto",10))
    akoisamoako.place(x=950,y=610)
    nejed=Label(prozor,text='nejed = ≠',font=("Roboto",10))
    nejed.place(x=950,y=640)
    primjer=Label(prozor,text='Primjer: "svi x svi y ((x nejed y i ne postoji zRzx) samoako (Syy ili ne ne ne Sxx))"',font=("Roboto",10))
    primjer.place(x=750,y=670)
    izgled=Label(prozor,text='Proizvodi: "∀x∀y((x≠y∧¬∃zRzx)→(Syy∨¬¬¬Sxx))"',font=("Roboto",10))
    izgled.place(x=750,y=700)


#Odabirenje vrste igre
lprob=Button(prozor, text="Lpr na obični", font=("Roboto",13), command=lprnaobicni)
lprob.place(x=480,y=150)

oblpr=Button(prozor, text="Obični na Lpr", font=("Roboto",13),command=obicninalpr)
oblpr.place(x=680,y=150)

prozor.mainloop()

k.close()
o.close()
