import math #import math library
import tkinter as tk #import Tkinter library
from tkinter import messagebox #import alert messages library
from tkinter import * #import option menu library
import os 

# -------------------- LE CODE --------------------

current_path = os.path.dirname(__file__)

côtétrouvépythrobottrouvercôté = 0

def est_nombre(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

def lancerpythagore():
    txtmathrobot.place_forget()
    descriptionbrève.place_forget()
    selectionsousrobot.place_forget()
    boutonpythagore.place_forget()
    boutontrigonométrie.place_forget()
    boutonpythrobottrouvercôté.place(x=270, y=135)
    boutonpythrobottrouvercôté.update_idletasks()
    boutonpythrobottrouverrectangularité.place(x=500, y=135)
    boutonpythrobottrouverrectangularité.update_idletasks()
    boutonquitterpythrobot.place(x=800, y=735)
    boutonquitterpythrobot.update_idletasks()
    txtdebienvenuepythrobotdescription.place(x=245, y=50)
    txtdebienvenuepythrobotdescription.update_idletasks()
    selectionpythrobotaction.place(x=335, y=85)
    selectionpythrobotaction.update_idletasks()
    txtpythrobot.place(x=400, y=15)
    txtpythrobot.update_idletasks()

def quittermathrobot():
    MathRobot.after(1000, quit)

def trouverlalongueurduncôté():
    txtdebienvenuepythrobotdescription.place_forget()
    selectionpythrobotaction.place_forget()
    boutonpythrobottrouvercôté.place_forget()
    boutonpythrobottrouverrectangularité.place_forget()
    boutonquitterpythrobot.place_forget()
    menuangledroitpythrobottrouvermesurelongueur.place(x=100, y=150)
    menuangledroitpythrobottrouvermesurelongueur.update_idletasks()
    txtdescriptionpythrobottrouvermesurecôté.place(x=300, y=50)
    txtdescriptionpythrobottrouvermesurecôté.update_idletasks()
    boutonvaliderchoixangledroitpythrobottrouvermesurelongueur.place(x=120, y=185)
    boutonvaliderchoixangledroitpythrobottrouvermesurelongueur.update_idletasks()

def trouversiuntriangleestrectangle():
    txtdebienvenuepythrobotdescription.place_forget()
    selectionpythrobotaction.place_forget()
    boutonpythrobottrouvercôté.place_forget()
    boutonpythrobottrouverrectangularité.place_forget()
    boutonquitterpythrobot.place_forget()
    entréeABpythrobotrectangularité.delete(0, 'end')
    entréeABpythrobotrectangularité.place(x=110, y=150)
    entréeABpythrobotrectangularité.update_idletasks()
    entréeACpythrobotrectangularité.delete(0, 'end')
    entréeACpythrobotrectangularité.place(x=400, y=150)
    entréeACpythrobotrectangularité.update_idletasks()
    entréeBCpythrobotrectangularité.delete(0, 'end')
    entréeBCpythrobotrectangularité.place(x=750, y=150)
    entréeBCpythrobotrectangularité.update_idletasks()
    txtABégalpythrobotrectangularité.place(x=70, y=150)
    txtABégalpythrobotrectangularité.update_idletasks()
    txtcmABégalpythrobotrectangularité.place(x=282, y=150)
    txtcmABégalpythrobotrectangularité.update_idletasks()
    txtACégalpythrobotrectangularité.place(x=360, y=150)
    txtACégalpythrobotrectangularité.update_idletasks()
    txtcmACégalpythrobotrectangularité.place(x=572, y=150)
    txtcmACégalpythrobotrectangularité.update_idletasks()
    txtBCégalpythrobotrectangularité.place(x=710, y=150)
    txtBCégalpythrobotrectangularité.update_idletasks()
    txtcmBCégalpythrobotrectangularité.place(x=922, y=150)
    txtcmBCégalpythrobotrectangularité.update_idletasks()
    txtdescriptionpythrobotrectangularité.place(x=350, y=75)
    txtdescriptionpythrobotrectangularité.update_idletasks()
    boutonvaliderentréescôtéspythrobotrectangularité.place(x=445, y=200)
    boutonvaliderentréescôtéspythrobotrectangularité.update_idletasks()

def validerentréescôtéspythrobotrectangularité():
    ABrectangularitépythrobot = entréeABpythrobotrectangularité.get()
    ACrectangularitépythrobot = entréeACpythrobotrectangularité.get()
    BCrectangularitépythrobot = entréeBCpythrobotrectangularité.get()
    if not est_nombre(ABrectangularitépythrobot):
        messagebox.showwarning("Warning", "Unencrypted input on input AB. Try again")
        entréeABpythrobotrectangularité.delete(0, tk.END)
        entréeABpythrobotrectangularité.focus()
        return
    if not est_nombre(ACrectangularitépythrobot):
        messagebox.showwarning("Warning", "Unencrypted input on input AC. Try again")
        entréeACpythrobotrectangularité.delete(0, tk.END)
        entréeACpythrobotrectangularité.focus()
        return
    if not est_nombre(BCrectangularitépythrobot):
        messagebox.showwarning("Warning", "Unencrypted input on input BC. Try again")
        entréeBCpythrobotrectangularité.delete(0, tk.END)
        entréeBCpythrobotrectangularité.focus()
        return
    entréeABpythrobotrectangularité.config(state="disabled")
    entréeACpythrobotrectangularité.config(state="disabled")
    entréeBCpythrobotrectangularité.config(state="disabled")
    boutonvaliderentréescôtéspythrobotrectangularité.place_forget()
    ABrectangularitépythrobot = float(ABrectangularitépythrobot)
    ACrectangularitépythrobot = float(ACrectangularitépythrobot)
    BCrectangularitépythrobot = float(BCrectangularitépythrobot)
    listecôtéspythrobotrectangularité = [ABrectangularitépythrobot, ACrectangularitépythrobot, BCrectangularitépythrobot]
    listetricôtéspythrobotrectangularité = sorted(listecôtéspythrobotrectangularité)
    plusgrandcôtépythrobotrectangularité = max(ABrectangularitépythrobot, ACrectangularitépythrobot, BCrectangularitépythrobot)
    if plusgrandcôtépythrobotrectangularité == ABrectangularitépythrobot:
        anglepythrobotrectangularité = " C"
    elif plusgrandcôtépythrobotrectangularité == ACrectangularitépythrobot:
        anglepythrobotrectangularité = " B"
    elif plusgrandcôtépythrobotrectangularité == BCrectangularitépythrobot:
        anglepythrobotrectangularité = " A"
    deuxautrescôtéspythrobotrectangularité = listetricôtéspythrobotrectangularité[:2]
    carréplusgdcôtépythrobotrectangularité = round(plusgrandcôtépythrobotrectangularité**2, 2)
    carréautrecôté1pythrobotrectangularité = deuxautrescôtéspythrobotrectangularité[0]**2
    carréautrecôté2pythrobotrectangularité = deuxautrescôtéspythrobotrectangularité[1]**2
    sommecarrésautrescôtésavecarrondipythrobotrectangularité = round(carréautrecôté1pythrobotrectangularité + carréautrecôté2pythrobotrectangularité, 2)
    sommecarrésautrescôtéssansarrondipythrobotrectangularité = carréautrecôté1pythrobotrectangularité + carréautrecôté2pythrobotrectangularité
    if int(carréplusgdcôtépythrobotrectangularité * 1000) / 1000 == int(sommecarrésautrescôtésavecarrondipythrobotrectangularité * 1000) / 1000 or int(carréplusgdcôtépythrobotrectangularité * 1000) / 1000 == int(sommecarrésautrescôtéssansarrondipythrobotrectangularité * 1000) / 1000:
        txtsirectangleoupaspythrobotrectanglarité.config(text="Triangle ABC is right-angled in" + anglepythrobotrectangularité)
        txtsirectangleoupaspythrobotrectanglarité.place(x=350, y=250)
        txtsirectangleoupaspythrobotrectanglarité.update_idletasks()
    elif plusgrandcôtépythrobotrectangularité**2 != deuxautrescôtéspythrobotrectangularité[0]**2 + deuxautrescôtéspythrobotrectangularité[1]**2:
        txtsirectangleoupaspythrobotrectanglarité.config(text="Triangle ABC is not a right triangle")
        txtsirectangleoupaspythrobotrectanglarité.place(x=350, y=250)
        txtsirectangleoupaspythrobotrectanglarité.update_idletasks()
    boutonquitterrectangularitépythrobot.place(x=750, y=735)
    boutonquitterrectangularitépythrobot.update_idletasks()

def revenirmenupythrobotaprèsrectangularité():
    entréeABpythrobotrectangularité.config(state="normal")
    entréeACpythrobotrectangularité.config(state="normal")
    entréeBCpythrobotrectangularité.config(state="normal")
    boutonquitterrectangularitépythrobot.place_forget()
    txtsirectangleoupaspythrobotrectanglarité.place_forget()
    entréeABpythrobotrectangularité.place_forget()
    entréeACpythrobotrectangularité.place_forget()
    entréeBCpythrobotrectangularité.place_forget()
    txtABégalpythrobotrectangularité.place_forget()
    txtACégalpythrobotrectangularité.place_forget()
    txtBCégalpythrobotrectangularité.place_forget()
    txtcmABégalpythrobotrectangularité.place_forget()
    txtcmACégalpythrobotrectangularité.place_forget()
    txtcmBCégalpythrobotrectangularité.place_forget()
    txtdescriptionpythrobotrectangularité.place_forget()
    boutonpythrobottrouvercôté.place(x=270, y=135)
    boutonpythrobottrouvercôté.update_idletasks()
    boutonpythrobottrouverrectangularité.place(x=500, y=135)
    boutonpythrobottrouverrectangularité.update_idletasks()
    boutonquitterpythrobot.place(x=800, y=735)
    boutonquitterpythrobot.update_idletasks()
    txtdebienvenuepythrobotdescription.place(x=275, y=50)
    txtdebienvenuepythrobotdescription.update_idletasks()
    selectionpythrobotaction.place(x=325, y=85)
    selectionpythrobotaction.update_idletasks()

def quitterpythrobot():
    txtpythrobot.place_forget()
    boutonpythrobottrouvercôté.place_forget()
    boutonpythrobottrouverrectangularité.place_forget()
    txtdebienvenuepythrobotdescription.place_forget()
    boutonquitterpythrobot.place_forget()
    selectionpythrobotaction.place_forget()
    txtmathrobot.place(x=400, y=15)
    txtmathrobot.update_idletasks()
    descriptionbrève.place(x=250, y=50)
    descriptionbrève.update_idletasks()
    selectionsousrobot.place(x=395, y=85)
    selectionsousrobot.update_idletasks()
    boutonpythagore.place(x=355, y=135)
    boutonpythagore.update_idletasks()
    boutontrigonométrie.place(x=507, y=135)
    boutontrigonométrie.update_idletasks()
    selectionsousrobot.place(x=395, y=85)
    selectionsousrobot.update_idletasks()

def validerangledroitpythrobottrouvercôté():
    menuangledroitpythrobottrouvermesurelongueur.bind("<Button-1>", lambda e: "break")
    menucôtéquoncherchepythrobot.place(x=400, y=150)
    menucôtéquoncherchepythrobot.update_idletasks()
    boutonvaliderchoixangledroitpythrobottrouvermesurelongueur.place_forget()
    boutonvalidercôtéquoncherchepythrobot.place(x=450, y=185)
    boutonvalidercôtéquoncherchepythrobot.update_idletasks()

def validercôtéquoncherchepythrobot():
    menucôtéquoncherchepythrobot.bind("<Button-1>", lambda e: "break")
    boutonvalidercôtéquoncherchepythrobot.place_forget()
    choixcôtéquoncherche = côtéquoncherchepythrobot.get()
    entrée1ercôtépythrobottrouvercôté.delete(0, "end")
    entrée1ercôtépythrobottrouvercôté.place(x=750, y=135)
    entrée1ercôtépythrobottrouvercôté.update_idletasks()
    entrée2ecôtépythrobottrouvercôté.delete(0, "end")
    entrée2ecôtépythrobottrouvercôté.place(x=750, y=165)
    entrée2ecôtépythrobottrouvercôté.update_idletasks()
    txtcmcôtéentrée1pythrobottrouvercôté.place(x=925, y=135)
    txtcmcôtéentrée1pythrobottrouvercôté.update_idletasks()
    txtcmcôtéentrée2pythrobottrouvercôté.place(x=925, y=165)
    txtcmcôtéentrée2pythrobottrouvercôté.update_idletasks()
    boutonvaliderentréescôtéspythrobottrouvercôté.place(x=800, y=200)
    boutonvaliderentréescôtéspythrobottrouvercôté.update_idletasks()
    if choixcôtéquoncherche == "Side we are looking for : AB":
        txtACcôtéhautentrée1pythrobottrouvercôté.place(x=710, y=135)
        txtACcôtéhautentrée1pythrobottrouvercôté.update_idletasks()
        txtBCcôtéhautentrée2pythrobottrouvercôté.place(x=710, y=165)
        txtBCcôtéhautentrée2pythrobottrouvercôté.update_idletasks()
    elif choixcôtéquoncherche == "Side we are looking for : AC":
        txtABcôtéentrée1pythrobottrouvercôté.place(x=710, y=135)
        txtABcôtéentrée1pythrobottrouvercôté.update_idletasks()
        txtBCcôtéhautentrée2pythrobottrouvercôté.place(x=710, y=165)
        txtBCcôtéhautentrée2pythrobottrouvercôté.update_idletasks()
    else:
        txtABcôtéentrée1pythrobottrouvercôté.place(x=710, y=135)
        txtABcôtéentrée1pythrobottrouvercôté.update_idletasks()
        txtACcôtéentrée2pythrobottrouvercôté.place(x=710, y=165)
        txtACcôtéentrée2pythrobottrouvercôté.update_idletasks()

def validerentréescôtéspythrobottrouvercôté():
    choixangledroitpythrobot = angledroitchoisipythrobottrouvermesurelongueur.get()
    choixcôtéquoncherche = côtéquoncherchepythrobot.get()
    entrée1 = entrée1ercôtépythrobottrouvercôté.get()
    entrée2 = entrée2ecôtépythrobottrouvercôté.get()
    if not est_nombre(entrée1):
        messagebox.showwarning("Warning", "Unencrypted input on top line. Try again")
        entrée1ercôtépythrobottrouvercôté.delete(0, tk.END)
        entrée1ercôtépythrobottrouvercôté.focus()
        return
    if not est_nombre(entrée2):
        messagebox.showwarning("Warning", "Unencrypted entry on the bottom line. Try again")
        entrée2ecôtépythrobottrouvercôté.delete(0, tk.END)
        entrée2ecôtépythrobottrouvercôté.focus()
        return
    entrée1 = float(entrée1)
    entrée2 = float(entrée2)
    boutonvaliderentréescôtéspythrobottrouvercôté.place_forget()
    entrée1ercôtépythrobottrouvercôté.config(state="disabled")
    entrée2ecôtépythrobottrouvercôté.config(state="disabled")
    boutonquitteraprèsavoirtrouvécôtépythrobot.place(x=750, y=735)
    boutonquitteraprèsavoirtrouvécôtépythrobot.update_idletasks()
    if choixangledroitpythrobot == "Right angle : A":
        if choixcôtéquoncherche == "Side we are looking for : BC":
            côtétrouvé = math.sqrt(entrée1**2 + entrée2**2)
            txtBCrésultatcôtépythrobottrouvercôté.config(text=f"BC = {côtétrouvé} cm")
            txtBCrésultatcôtépythrobottrouvercôté.place(relx=0.5, rely=0.5, anchor="center", y=-175)
            txtBCrésultatcôtépythrobottrouvercôté.update_idletasks()
        elif choixcôtéquoncherche == "Side we are looking for : AB":
            côtétrouvé = math.sqrt(max(entrée1, entrée2)**2 - min(entrée1, entrée2)**2)
            txtABrésultatcôtépythrobottrouvercôté.config(text=f"AB = {côtétrouvé} cm")
            txtABrésultatcôtépythrobottrouvercôté.place(relx=0.5, rely=0.5, anchor="center", y=-175)
            txtABrésultatcôtépythrobottrouvercôté.update_idletasks()
        elif choixcôtéquoncherche == "Side we are looking for : AC":
            côtétrouvé = math.sqrt(max(entrée1, entrée2)**2 - min(entrée1, entrée2)**2)
            txtACrésultatcôtépythrobottrouvercôté.config(text=f"AC = {côtétrouvé} cm")
            txtACrésultatcôtépythrobottrouvercôté.place(relx=0.5, rely=0.5, anchor="center", y=-175)
            txtACrésultatcôtépythrobottrouvercôté.update_idletasks()
    elif choixangledroitpythrobot == "Right angle : B":
        if choixcôtéquoncherche == "Side we are looking for : AC":
            côtétrouvé = math.sqrt(entrée1**2 + entrée2**2)
            txtACrésultatcôtépythrobottrouvercôté.config(text=f"AC = {côtétrouvé} cm")
            txtACrésultatcôtépythrobottrouvercôté.place(relx=0.5, rely=0.5, anchor="center", y=-175)
            txtACrésultatcôtépythrobottrouvercôté.update_idletasks()
        elif choixcôtéquoncherche == "Side we are looking for : AB":
            côtétrouvé = math.sqrt(max(entrée1, entrée2)**2 - min(entrée1, entrée2)**2)
            txtABrésultatcôtépythrobottrouvercôté.config(text=f"AB = {côtétrouvé} cm")
            txtABrésultatcôtépythrobottrouvercôté.place(relx=0.5, rely=0.5, anchor="center", y=-175)
            txtABrésultatcôtépythrobottrouvercôté.update_idletasks()
        elif choixcôtéquoncherche == "Side we are looking for : BC":
            côtétrouvé = math.sqrt(max(entrée1, entrée2)**2 - min(entrée1, entrée2)**2)
            txtBCrésultatcôtépythrobottrouvercôté.config(text=f"BC = {côtétrouvé} cm")
            txtBCrésultatcôtépythrobottrouvercôté.place(relx=0.5, rely=0.5, anchor="center", y=-175)
            txtBCrésultatcôtépythrobottrouvercôté.update_idletasks()
    elif choixangledroitpythrobot == "Right angle : C":
        if choixcôtéquoncherche == "Side we are looking for : AB":
            côtétrouvé = math.sqrt(entrée1**2 + entrée2**2)
            txtABrésultatcôtépythrobottrouvercôté.config(text=f"AB = {côtétrouvé} cm")
            txtABrésultatcôtépythrobottrouvercôté.place(relx=0.5, rely=0.5, anchor="center", y=-175)
            txtABrésultatcôtépythrobottrouvercôté.update_idletasks()
        elif choixcôtéquoncherche == "Side we are looking for : AC":
            côtétrouvé = math.sqrt(max(entrée1, entrée2)**2 - min(entrée1, entrée2)**2)
            txtACrésultatcôtépythrobottrouvercôté.config(text=f"AC = {côtétrouvé} cm")
            txtACrésultatcôtépythrobottrouvercôté.place(relx=0.5, rely=0.5, anchor="center", y=-175)
            txtACrésultatcôtépythrobottrouvercôté.update_idletasks()
        elif choixcôtéquoncherche == "Side we are looking for : BC":
            côtétrouvé = math.sqrt(max(entrée1, entrée2)**2 - min(entrée1, entrée2)**2)
            txtBCrésultatcôtépythrobottrouvercôté.config(text=f"BC = {côtétrouvé} cm")
            txtBCrésultatcôtépythrobottrouvercôté.place(relx=0.5, rely=0.5, anchor="center", y=-175)
            txtBCrésultatcôtépythrobottrouvercôté.update_idletasks()

def revenirmenupythrobotaprèstrouvécôté():
    menuangledroitpythrobottrouvermesurelongueur.unbind("<Button-1>")
    menucôtéquoncherchepythrobot.unbind("<Button-1>")
    entrée1ercôtépythrobottrouvercôté.config(state="normal")
    entrée2ecôtépythrobottrouvercôté.config(state="normal")
    menuangledroitpythrobottrouvermesurelongueur.place_forget()
    txtdescriptionpythrobottrouvermesurecôté.place_forget()
    boutonvaliderchoixangledroitpythrobottrouvermesurelongueur.place_forget()
    menucôtéquoncherchepythrobot.place_forget()
    boutonvalidercôtéquoncherchepythrobot.place_forget()
    entrée1ercôtépythrobottrouvercôté.place_forget()
    entrée2ecôtépythrobottrouvercôté.place_forget()
    txtABrésultatcôtépythrobottrouvercôté.place_forget()
    txtACrésultatcôtépythrobottrouvercôté.place_forget()
    txtBCrésultatcôtépythrobottrouvercôté.place_forget()
    txtABcôtéentrée1pythrobottrouvercôté.place_forget()
    txtACcôtéhautentrée1pythrobottrouvercôté.place_forget()
    txtACcôtéentrée2pythrobottrouvercôté.place_forget()
    txtBCcôtéhautentrée2pythrobottrouvercôté.place_forget()
    txtcmcôtéentrée1pythrobottrouvercôté.place_forget()
    txtcmcôtéentrée2pythrobottrouvercôté.place_forget()
    boutonquitteraprèsavoirtrouvécôtépythrobot.place_forget()
    boutonpythrobottrouvercôté.place(x=270, y=135)
    boutonpythrobottrouvercôté.update_idletasks()
    boutonpythrobottrouverrectangularité.place(x=500, y=135)
    boutonpythrobottrouverrectangularité.update_idletasks()
    boutonquitterpythrobot.place(x=800, y=735)
    boutonquitterpythrobot.update_idletasks()
    txtdebienvenuepythrobotdescription.place(x=275, y=50)
    txtdebienvenuepythrobotdescription.update_idletasks()
    selectionpythrobotaction.place(x=325, y=85)
    selectionpythrobotaction.update_idletasks()
    

def lancertrigonométrie():
    txtmathrobot.place_forget()
    descriptionbrève.place_forget()
    selectionsousrobot.place_forget()
    txttrigobot.place(x=400, y=15)
    txttrigobot.update_idletasks()
    boutonpythagore.place_forget()
    boutontrigonométrie.place_forget()
    boutontrigobottrouvercôté.place(x=270, y=135)
    boutontrigobottrouvercôté.update_idletasks()
    boutontrigobottrouverangle.place(x=500, y=135)
    boutontrigobottrouverangle.update_idletasks()
    txttrigobotdesciption.place(x=250, y=50)
    txttrigobotdesciption.update_idletasks()
    selectiontrigobotaction.place(x=310, y=85)
    selectiontrigobotaction.update_idletasks()
    boutonquittertrigobot.place(x=810, y=735)
    boutonquittertrigobot.update_idletasks()

def quitterTrigoBot():
    txttrigobot.place_forget()
    txttrigobotdesciption.place_forget()
    selectiontrigobotaction.place_forget()
    boutontrigobottrouvercôté.place_forget()
    boutontrigobottrouverangle.place_forget()
    boutonquittertrigobot.place_forget()
    txtmathrobot.place(x=400, y=15)
    txtmathrobot.update_idletasks()
    descriptionbrève.place(x=250, y=50)
    descriptionbrève.update_idletasks()
    selectionsousrobot.place(x=395, y=85)
    selectionsousrobot.update_idletasks()
    boutonpythagore.place(x=355, y=135)
    boutonpythagore.update_idletasks()
    boutontrigonométrie.place(x=507, y=135)
    boutontrigonométrie.update_idletasks()
    selectionsousrobot.place(x=395, y=85)
    selectionsousrobot.update_idletasks()


def trouvercôtétrigobot():
    boutontrigobottrouvercôté.place_forget()
    boutontrigobottrouverangle.place_forget()
    boutonquittertrigobot.place_forget()
    txttrigobotdesciption.place_forget()
    selectiontrigobotaction.place_forget()
    txtdescriptiontrigobottrouvercôté.place(x=290, y=50)
    txtdescriptiontrigobottrouvercôté.update_idletasks()
    menuangledroittigobottrouvercôté.place(x=20, y=150)
    menuangledroittigobottrouvercôté.update_idletasks()
    boutonvaliderangledroitrigobottrouvercôté.place(x=40, y=185)
    boutonvaliderangledroitrigobottrouvercôté.update_idletasks()

def validerangledroittrigobottrouvercôté():
    menuangledroittigobottrouvercôté.bind("<Button-1>", lambda e: "break")
    boutonvaliderangledroitrigobottrouvercôté.place_forget()
    menucôtéquonatrigobottrouvercôté.place(x=185, y=150)
    menucôtéquonatrigobottrouvercôté.update_idletasks()
    boutonvalidercôtéquatrigobottrouvercôtéaveclongueur.place(x=370, y=185)
    boutonvalidercôtéquatrigobottrouvercôtéaveclongueur.update_idletasks()
    entréelongueurcôtéquatrigobottrouvercôté.place(x=360, y=149.5)
    entréelongueurcôtéquatrigobottrouvercôté.update_idletasks()
    txtégalcôtéquonatrigobottrouvercôté.place(x=340, y=148.5)
    txtégalcôtéquonatrigobottrouvercôté.update_idletasks()
    txtcmcôtéquonatrigobottrouvercôté.place(x=535, y=148)
    txtcmcôtéquonatrigobottrouvercôté.update_idletasks()

def validercôtéquonatrigobottrouvercôtéaveclongueur():
    entréecôtéquonatrigobottrouvercôté = entréelongueurcôtéquatrigobottrouvercôté.get()
    try:
        float(entréecôtéquonatrigobottrouvercôté)
    except ValueError:
        messagebox.showwarning("Warning", "Unencrypted input. Try again")
        entréelongueurcôtéquatrigobottrouvercôté.delete(0, tk.END)
        entréelongueurcôtéquatrigobottrouvercôté.focus()
        return
    menucôtéquonatrigobottrouvercôté.bind("<Button-1>", lambda e: "break")
    entréelongueurcôtéquatrigobottrouvercôté.config(state="disabled")
    boutonvalidercôtéquatrigobottrouvercôtéaveclongueur.place_forget()
    menuanglequonatrigobottrouvercôté.place(x=585, y=148.5)
    menuanglequonatrigobottrouvercôté.update_idletasks()
    boutonvalideranglequonatrigobottrouvercôté.place(x=740, y=185)
    boutonvalideranglequonatrigobottrouvercôté.update_idletasks()
    entréeanglequonatrigobottrouvercôté.place(x=790, y=147.5)
    entréeanglequonatrigobottrouvercôté.update_idletasks()
    txtégalanglequonatrigobottrouvercôté.place(x=770, y=147.5)
    txtégalanglequonatrigobottrouvercôté.update_idletasks()
    txtdegréanglequonatrigobottrouvercôté.place(x=965, y=147.5)
    txtdegréanglequonatrigobottrouvercôté.update_idletasks()

def valideranglequonatrigobottrouvercôté():
    angledroitchoisitrigobottrouvercôté = angledroittriangletrigobottrouvercôté.get()
    anglequonachoisitrigobottrouvercôté = anglequonatrigobottrouvercôté.get()
    if anglequonachoisitrigobottrouvercôté[-1:] == angledroitchoisitrigobottrouvercôté[-1:]:
        messagebox.showwarning("Warning", "The chosen angle corresponds to the right angle. Please choose another angle")
        return
    choixentréeanglequonatrigobottrouvercôté = entréeanglequonatrigobottrouvercôté.get()
    try:
        float(choixentréeanglequonatrigobottrouvercôté)
    except ValueError:
        messagebox.showwarning("Warning", "Unencrypted input. Try again")
        entréeanglequonatrigobottrouvercôté.delete(0, tk.END)
        entréeanglequonatrigobottrouvercôté.focus()
        return
    choixentréeanglequonatrigobottrouvercôté = float(choixentréeanglequonatrigobottrouvercôté)
    if choixentréeanglequonatrigobottrouvercôté >= 90:
        messagebox.showwarning("Warning", "Angle value not correct. Please enter a value less than 90°")
        return
    boutonvalideranglequonatrigobottrouvercôté.place_forget()
    menuanglequonatrigobottrouvercôté.bind("<Button-1>", lambda e: "break")
    entréeanglequonatrigobottrouvercôté.config(state="disabled")
    menucôtéquoncherchetrigobottrouvercôté.place(x=400, y=225)
    menucôtéquoncherchetrigobottrouvercôté.update_idletasks()
    boutonvalidercôtéquoncherchetrigobottrouvercôté.place(x=455, y=260)
    boutonvalidercôtéquoncherchetrigobottrouvercôté.update_idletasks()
    
def validercôtéquoncherchetrigobottrouvercôté():
    choixcôtéquoncherchetrigobottrouvercôté = côtéquoncherchetrigobottrouvercôté.get()
    côtéquonachoisitrigobottrouvercôté = côtéquonatrigobottrouvercôté.get()
    if choixcôtéquoncherchetrigobottrouvercôté[-2:] == côtéquonachoisitrigobottrouvercôté[-2:]:
        messagebox.showwarning("Warning", "The side you have chosen corresponds to the one you have. Please change sides.")
        return
    boutonvalidercôtéquoncherchetrigobottrouvercôté.place_forget()
    menucôtéquoncherchetrigobottrouvercôté.bind("<Button-1>", lambda e: "break")
    angledroitchoisitrigobottrouvercôté = angledroittriangletrigobottrouvercôté.get()
    côtéquonachoisitrigobottrouvercôté = côtéquonatrigobottrouvercôté.get()
    entréecôtéquonatrigobottrouvercôté = entréelongueurcôtéquatrigobottrouvercôté.get()
    anglequonachoisitrigobottrouvercôté = anglequonatrigobottrouvercôté.get()
    choixentréeanglequonatrigobottrouvercôté = entréeanglequonatrigobottrouvercôté.get()
    if angledroitchoisitrigobottrouvercôté == "Right angle : A":
        if côtéquonachoisitrigobottrouvercôté == "Side we have : AB":
            if anglequonachoisitrigobottrouvercôté == "Angle that we have : B":
                if choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AC":
                    angleautiliser1 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser1 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian1 = math.radians(angleautiliser1)
                    AC1trig = math.tan(angleradian1) * longueurautiliser1
                    AC1trig = round(AC1trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"BC = {AC1trig} cm")
                elif choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : BC":
                    angleautiliser2 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser2 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian2 = math.radians(angleautiliser2)
                    BC1trig = longueurautiliser2 / math.cos(angleradian2)
                    BC1trig = round(BC1trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"BC = {BC1trig} cm")
            elif anglequonachoisitrigobottrouvercôté == "Angle we have : C":
                if choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AC":
                    angleautiliser3 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser3 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian3 = math.radians(angleautiliser3)
                    AC2trig = longueurautiliser3 / math.tan(angleradian3)
                    AC2trig = round(AC2trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AC = {AC2trig} cm")
                elif choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : BC":
                    angleautiliser4 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser4 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian4 = math.radians(angleautiliser4)
                    BC2trig = longueurautiliser4 / math.sin(angleradian4)
                    BC2trig = round(BC2trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"BC = {BC2trig} cm")
        elif côtéquonachoisitrigobottrouvercôté == "Side we have : AC":
            if anglequonachoisitrigobottrouvercôté == "Angle that we have : B":
                if choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AB":
                    angleautiliser5 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser5 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian5 = math.radians(angleautiliser5)
                    AB1trig = longueurautiliser5 / math.tan(angleradian5)
                    AB1trig = round(AB1trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AB = {AB1trig} cm")
                elif choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : BC":
                    angleautiliser6 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser6 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian6 = math.radians(angleautiliser6)
                    BC3trig = longueurautiliser6 / math.sin(angleradian6)
                    BC3trig = round(BC1trig)
                    txtrésultattrigobottrouvercôté.config(text=f"BC = {BC3trig} cm")
            elif anglequonachoisitrigobottrouvercôté == "Angle we have : C":
                if choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AB":
                    angleautiliser7 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser7 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian7 = math.radians(angleautiliser7)
                    AB2trig = longueurautiliser7 * math.tan(angleradian7)
                    AB2trig = round(AB2trig)
                    txtrésultattrigobottrouvercôté.config(text=f"AB = {AB2trig} cm")
                elif choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : BC":
                    angleautiliser8 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser8 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian8 = math.radians(angleautiliser8)
                    BC4trig=  longueurautiliser8 / math.cos(angleradian8)
                    BC4trig = round(BC4trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"BC = {BC4trig} cm")
        elif côtéquonachoisitrigobottrouvercôté == "Side we have : BC":
            if anglequonachoisitrigobottrouvercôté == "Angle that we have : B":
                if choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AB":
                    angleautiliser9 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser9 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian9 = math.radians(angleautiliser9)
                    AB3trig = longueurautiliser9 * math.cos(angleradian9)
                    AB3trig = round(AB3trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AB = {AB3trig} cm")
                elif choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AC":
                    angleatuiliser10 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser10 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian10 = math.radians(angleatuiliser10)
                    AC3trig = math.sin(angleradian10) * longueurautiliser10
                    AC3trig = round(AC3trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AC = {AC3trig} cm")
            elif anglequonachoisitrigobottrouvercôté == "Angle we have : C":
                if choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AB":
                    angleatuiliser11 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser11 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian11 = math.radians(angleatuiliser11)
                    AB4trig = math.sin(angleradian11) * longueurautiliser11
                    AB4trig = round(AB4trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AB = {AB4trig} cm")
                elif choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AC":
                    angleautiliser12 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser12 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian12 = math.radians(angleautiliser12)
                    AC4trig = math.cos(angleradian12) * longueurautiliser12
                    AC4trig = round(AC4trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AC = {AC4trig} cm")
    elif angledroitchoisitrigobottrouvercôté == "Right angle : B":
        if côtéquonachoisitrigobottrouvercôté == "Side we have : AB":
            if anglequonachoisitrigobottrouvercôté == "Right angle : A":
                if choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AC":
                    angleautiliser13 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser13 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian13 = math.radians(angleautiliser13)
                    AC5trig = longueurautiliser13 / math.cos(angleradian13)
                    AC5trig = round(AC5trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AC = {AC5trig} cm")
                elif choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : BC":
                    angleautiliser14 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser14 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian14 = math.radians(angleautiliser14)
                    BC5trig = math.tan(angleradian14) * longueurautiliser14
                    BC5trig = round(BC5trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"BC = {BC5trig} cm")
            elif anglequonachoisitrigobottrouvercôté == "Angle we have : C":
                if choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AC":
                    angleautiliser15 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser15 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian15 = math.radians(angleautiliser15)
                    AC6trig = longueurautiliser15 / math.sin(angleradian15)
                    AC6trig = round(AC6trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AC = {AC6trig} cm")
                elif choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : BC":
                    angleautiliser16 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser16 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian16 = math.radians(angleautiliser16)
                    BC6trig = longueurautiliser16 / math.tan(angleradian16)
                    BC6trig = round(BC6trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"BC = {BC6trig} cm")
        elif côtéquonachoisitrigobottrouvercôté == "Side we have : AC":
            if anglequonachoisitrigobottrouvercôté == "Right angle : A":
                if choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AB":
                    angleautiliser17 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser17 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian17 = math.radians(angleautiliser17)
                    AB5trig = longueurautiliser17 * math.cos(angleradian17)
                    AB5trig = round(AB5trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AB = {AB5trig} cm")
                elif choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : BC":
                    angleautiliser18 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser18 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian18 = math.radians(angleautiliser18)
                    BC7trig = longueurautiliser18 * math.sin(angleradian18)
                    BC7trig = round(BC7trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"BC = {BC7trig} cm")
            elif anglequonachoisitrigobottrouvercôté == "Angle we have : C":
                if choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AB":
                    angleautiliser19 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser19 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian19 = math.radians(angleautiliser19)
                    AB6trig = longueurautiliser19 * math.sin(angleradian19)
                    AB6trig = round(AB6trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AB = {AB6trig} cm")
                elif choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : BC":
                    angleautiliser20 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser20 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian20 = math.radians(angleautiliser20)
                    BC8trig = longueurautiliser20 * math.cos(angleradian20)
                    BC8trig = round(BC8trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"BC = {BC8trig} cm")
        elif côtéquonachoisitrigobottrouvercôté == "Side we have : BC":
            if anglequonachoisitrigobottrouvercôté == "Right angle : A":
                if choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AB":
                    angleautiliser21 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser21 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian21 = math.radians(angleautiliser21)
                    AB7trig = longueurautiliser21 / math.tan(angleradian21)
                    AB7trig = round(AB7trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AB = {AB7trig} cm")
                elif choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AC":
                    angleautiliser22 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser22 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian22 = math.radians(angleautiliser22)
                    AC7trig = longueurautiliser22 / math.sin(angleradian22)
                    AC7trig = round(AC7trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AC = {AC7trig} cm")
            elif anglequonachoisitrigobottrouvercôté == "Angle we have : C":
                if choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AB":
                    angleautiliser23 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser23 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian23 = math.radians(angleautiliser23)
                    AB8trig = longueurautiliser23 * math.tan(angleradian23)
                    AB8trig = round(AB8trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AB = {AB8trig} cm")
                elif choixentréeanglequonatrigobottrouvercôté == "Side we are looking for : AC":
                    angleautiliser24 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser24 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian24 = math.radians(angleautiliser24)
                    AC8trig = longueurautiliser24 / math.cos(angleradian24)
                    AC8trig = round(AC8trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AC = {AC8trig} cm")
    elif angledroitchoisitrigobottrouvercôté == "Right angle : C":
        if côtéquonachoisitrigobottrouvercôté == "Side we have : AB":
            if anglequonachoisitrigobottrouvercôté == "Right angle : A":
                if choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AC":
                    angleautiliser25 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser25 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian25 = math.radians(angleautiliser25)
                    AC9trig = longueurautiliser25 * math.cos(angleradian25)
                    AC9trig = round(AC9trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AC = {AC9trig} cm")
                elif choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : BC":
                    angleautiliser26 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser26 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian26 = math.radians(angleautiliser26)
                    BC9trig = longueurautiliser26 * math.sin(angleradian26)
                    BC9trig = round(BC9trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"BC = {BC9trig} cm")
            elif anglequonachoisitrigobottrouvercôté == "Angle that we have : B":
                if choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AC":
                    angleautiliser27 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser27 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian27 = math.radians(angleautiliser27)
                    AC10trig = longueurautiliser27 * math.sin(angleradian27)
                    AC10trig = round(AC10trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AC = {AC10trig} cm")
                elif choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : BC":
                    angleautiliser28 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser28 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian28 = math.radians(angleautiliser28)
                    BC10trig = longueurautiliser28 * math.cos(angleradian28)
                    BC10trig = round(BC10trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"BC = {BC10trig} cm")
        elif côtéquonachoisitrigobottrouvercôté == "Side we have : AC":
            if anglequonachoisitrigobottrouvercôté == "Right angle : A":
                if choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AB":
                    angleautiliser29 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser29 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian29 = math.radians(angleautiliser29)
                    AB9trig = longueurautiliser29 / math.cos(angleradian29)
                    AB9trig = round(AB9trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AB = {AB9trig} cm")
                elif choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : BC":
                    angleautiliser30 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser30 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian30 = math.radians(angleautiliser30)
                    BC11trig = longueurautiliser30 * math.tan(angleradian30)
                    BC11trig = round(BC11trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"BC = {BC11trig} cm")
            elif anglequonachoisitrigobottrouvercôté == "Angle that we have : B":
                if choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AB":
                    angleautiliser31 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser31 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian31 = math.radians(angleautiliser31)
                    AB10trig = longueurautiliser31 / math.sin(angleradian31)
                    AB10trig = round(AB10trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AB = {AB10trig} cm")
                elif choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : BC":
                    angleautiliser32 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser32 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian32 = math.radians(angleautiliser32)
                    BC12trig = longueurautiliser32 / math.tan(angleradian32)
                    BC12trig = round(BC12trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"BC = {BC12trig} cm")
        elif côtéquonachoisitrigobottrouvercôté == "Side we have : BC":
            if anglequonachoisitrigobottrouvercôté == "Right angle : A":
                if choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AB":
                    angleautiliser33 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser33 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian33 = math.radians(angleautiliser33)
                    AB11trig = longueurautiliser33 / math.sin(angleradian33)
                    AB11trig = round(AB11trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AB = {AB11trig} cm")
                elif choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AC":
                    angleautiliser34 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser34 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian34 = math.radians(angleautiliser34)
                    AC11trig = longueurautiliser34 / math.tan(angleradian34)
                    AC11trig = round(AC11trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AC = {AC11trig} cm")
            elif anglequonachoisitrigobottrouvercôté == "Angle that we have : B":
                if choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AB":
                    angleautiliser35 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser35 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian35 = math.radians(angleautiliser35)
                    AB12trig = longueurautiliser35 / math.cos(angleradian35)
                    AB12trig = round(AB12trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AB = {AB12trig} cm")
                elif choixcôtéquoncherchetrigobottrouvercôté == "Side we are looking for : AC":
                    angleautiliser36 = float(choixentréeanglequonatrigobottrouvercôté)
                    longueurautiliser36 = float(entréecôtéquonatrigobottrouvercôté)
                    angleradian36 = math.radians(angleautiliser36)
                    AC12trig = longueurautiliser36 * math.tan(angleradian36)
                    AC12trig = round(AC12trig, 4)
                    txtrésultattrigobottrouvercôté.config(text=f"AC = {AC12trig} cm")
    txtrésultattrigobottrouvercôté.place(relx=0.5, rely=0.5, anchor="center", y=-100)
    txtrésultattrigobottrouvercôté.update_idletasks()
    boutonquitteraprèstrouvécôtétrigobot.place(x=750, y=735)
    boutonquitteraprèstrouvécôtétrigobot.update_idletasks()

def quitteraprèstrouvécôté():
    menuangledroittigobottrouvercôté.unbind("<Button-1>")
    menuangledroittigobottrouvercôté.place_forget()
    menucôtéquonatrigobottrouvercôté.unbind("<Button-1>")
    menucôtéquonatrigobottrouvercôté.place_forget()
    txtégalcôtéquonatrigobottrouvercôté.place_forget()
    entréelongueurcôtéquatrigobottrouvercôté.config(state="normal")
    entréelongueurcôtéquatrigobottrouvercôté.place_forget()
    txtcmcôtéquonatrigobottrouvercôté.place_forget()
    menuanglequonatrigobottrouvercôté.unbind("<Button-1>")
    menucôtéquonatrigobottrouvercôté.place_forget()
    txtégalanglequonatrigobottrouvercôté.place_forget()
    entréeanglequonatrigobottrouvercôté.config(state="normal")
    entréeanglequonatrigobottrouvercôté.place_forget()
    txtdegréanglequonatrigobottrouvercôté.place_forget()
    menucôtéquoncherchetrigobottrouvercôté.unbind("<Button-1>")
    menucôtéquoncherchetrigobottrouvercôté.place_forget()
    txtrésultattrigobottrouvercôté.place_forget()
    txtdescriptiontrigobottrouvercôté.place_forget()
    menuanglequonatrigobottrouvercôté.place_forget()
    menuanglequonatrigobottrouvercôté.unbind("<Button-1>")
    boutonquitteraprèstrouvécôtétrigobot.place_forget()
    boutontrigobottrouvercôté.place(x=270, y=135)
    boutontrigobottrouvercôté.update_idletasks()
    boutontrigobottrouverangle.place(x=500, y=135)
    boutontrigobottrouverangle.update_idletasks()
    txttrigobotdesciption.place(x=250, y=50)
    txttrigobotdesciption.update_idletasks()
    selectiontrigobotaction.place(x=310, y=85)
    selectiontrigobotaction.update_idletasks()
    boutonquittertrigobot.place(x=810, y=735)
    boutonquittertrigobot.update_idletasks()
    entréelongueurcôtéquatrigobottrouvercôté.delete(0, "end")
    entréeanglequonatrigobottrouvercôté.delete(0, "end")

def trouverangletrigobot():
    boutontrigobottrouvercôté.place_forget()
    boutontrigobottrouverangle.place_forget()
    boutonquittertrigobot.place_forget()
    txttrigobotdesciption.place_forget()
    selectiontrigobotaction.place_forget()
    txtdescriptiontrigobottrouverangle.place(x=283, y=50)
    txtdescriptiontrigobottrouverangle.update_idletasks()
    menuangledroittrigobottrouverangle.place(x=20, y=150)
    menuangledroittrigobottrouverangle.update_idletasks()
    boutonvaliderangledroitrigobottrouverangle.place(x=40, y=185)
    boutonvaliderangledroitrigobottrouverangle.update_idletasks()

def validerangledroittrigobottrouverangle():
    menuangledroittrigobottrouverangle.bind("<Button-1>", lambda e: "break")
    boutonvaliderangledroitrigobottrouverangle.place_forget()
    menupremiercôtéquonatrigobottrouverangle.place(x=170, y=150)
    menupremiercôtéquonatrigobottrouverangle.update_idletasks()
    txtégalpremiercôtéquonatrigobottrouverangle.place(x=345, y=148.5)
    txtégalpremiercôtéquonatrigobottrouverangle.update_idletasks()
    entréelongueurpremiercôtéquonatrigobottrouverangle.place(x=365, y=149.5)
    entréelongueurpremiercôtéquonatrigobottrouverangle.update_idletasks()
    txtcmlongueurpremiercôtéquonatrigobottrouverangle.place(x=540, y=150)
    txtcmlongueurpremiercôtéquonatrigobottrouverangle.update_idletasks()
    boutonvaliderentréepremiercôtétrigobottrouverangle.place(x=370, y=185)
    boutonvaliderentréepremiercôtétrigobottrouverangle.update_idletasks()

def validerentréepremiercôtétrigobottrouverangle():
    entrée1ercôtéquonatrigobottrouvercôté = entréelongueurpremiercôtéquonatrigobottrouverangle.get()
    try:
        float(entrée1ercôtéquonatrigobottrouvercôté)
    except ValueError:
        messagebox.showwarning("Warning", "Unencrypted input. Try again")
        entréelongueurpremiercôtéquonatrigobottrouverangle.delete(0, tk.END)
        entréelongueurpremiercôtéquonatrigobottrouverangle.focus()
        return
    boutonvaliderentréepremiercôtétrigobottrouverangle.place_forget()
    menupremiercôtéquonatrigobottrouverangle.bind("<Button-1>", lambda e: "break")
    entréelongueurpremiercôtéquonatrigobottrouverangle.config(state="disabled")
    menudeuxièmecôtéquonatrigobottrouverangle.place(x=585, y=152)
    menudeuxièmecôtéquonatrigobottrouverangle.update_idletasks()
    txtégaldeuxièmecôtéquonatrigobottrouverangle.place(x=760, y=149)
    txtégaldeuxièmecôtéquonatrigobottrouverangle.update_idletasks()
    boutonvaliderdeuxièmecôtétrigobottrouverangle.place(x=770, y=185)
    boutonvaliderdeuxièmecôtétrigobottrouverangle.update_idletasks()
    entréedeuxièmecôtétrigobottrouverangle.place(x=780, y=150)
    entréedeuxièmecôtétrigobottrouverangle.update_idletasks()
    txtcmdeuxièmecôtéquonatrigobottrouvercôté.place(x=955, y=149)
    txtcmdeuxièmecôtéquonatrigobottrouvercôté.update_idletasks()

def validerentréedeuxièmecôtétrigobottrouvercôté():
    premiercôtéquonachoisitrigobottrouverangle = premiercôtéquonatrigobottrouverangle.get()    
    deuxièmecôtéquonachoisitrigobottrouverangle = deuxièmecôtéquonatrigobottrouverangle.get()
    if deuxièmecôtéquonachoisitrigobottrouverangle[-2:] == premiercôtéquonachoisitrigobottrouverangle[-2:]:
        messagebox.showwarning("Warning", "The chosen side is the same as the first. Try again")
        return
    entréechoisiedeuxièmecôtétrigobottrouverangle = entréedeuxièmecôtétrigobottrouverangle.get()
    try:
        float(entréechoisiedeuxièmecôtétrigobottrouverangle)
    except ValueError:
        messagebox.showwarning("Warning", "Unencrypted input. Try again")
        entréedeuxièmecôtétrigobottrouverangle.delete(0, tk.END)
        entréedeuxièmecôtétrigobottrouverangle.focus()
        return
    boutonvaliderdeuxièmecôtétrigobottrouverangle.place_forget()
    menudeuxièmecôtéquonatrigobottrouverangle.bind("<Button-1>", lambda e:"break")
    entréedeuxièmecôtétrigobottrouverangle.config(state="disabled")
    menuanglequoncherchetrigobottrouverangle.place(x=400, y=225)
    menuanglequoncherchetrigobottrouverangle.update_idletasks()
    boutonvalideranglequoncherchetrigobottrouverangle.place(x=455, y=260)
    boutonvalideranglequoncherchetrigobottrouverangle.update_idletasks()

def valideranglequoncherchetrigobottrouverangle():
    entrée1ercôtéquonatrigobottrouvercôté = entréelongueurpremiercôtéquonatrigobottrouverangle.get()
    entréechoisiedeuxièmecôtétrigobottrouverangle = entréedeuxièmecôtétrigobottrouverangle.get()
    premiercôtéquonachoisitrigobottrouverangle = premiercôtéquonatrigobottrouverangle.get()    
    deuxièmecôtéquonachoisitrigobottrouverangle = deuxièmecôtéquonatrigobottrouverangle.get()
    angledroitchoisitrigobottrouverangle = angledroittrigobottrouverangle.get()
    anglequoncherchechoisitrigobottrouverangle = anglequoncherchetrigobottrouverangle.get()
    if angledroitchoisitrigobottrouverangle[-1:] == anglequoncherchechoisitrigobottrouverangle[-1:]:
        messagebox.showwarning("Warning", "The chosen angle is the same as the right angle. Try again")
        return
    menuanglequoncherchetrigobottrouverangle.bind("<Button-1>", lambda e:"break")
    boutonvalideranglequoncherchetrigobottrouverangle.place_forget()
    angledroitautilisertrigobottrouverangle = angledroitchoisitrigobottrouverangle[-1:]
    côtéquona1 = premiercôtéquonachoisitrigobottrouverangle[-2:]
    côtéquona2 = deuxièmecôtéquonachoisitrigobottrouverangle[-2:]
    côtéquonamesure1 = float(entrée1ercôtéquonatrigobottrouvercôté)
    côtéquonamesure2 = float(entréechoisiedeuxièmecôtétrigobottrouverangle)
    anglequoncherche = anglequoncherchechoisitrigobottrouverangle[-1:]
    if angledroitautilisertrigobottrouverangle == "A":
        if côtéquona1 == "AB" and côtéquona2 == "AC":
            if anglequoncherche == "B":
                angletrouvé1 = math.atan(côtéquonamesure2 / côtéquonamesure1)
                angletrouvé1degré = math.degrees(angletrouvé1)
                txtrésultattrigobottrouverangle.config(text=f"B = {angletrouvé1degré} °")
            elif anglequoncherche == "C":
                angletrouvé2 = math.atan(côtéquonamesure1 / côtéquonamesure2)
                angletrouvé2degré = math.degrees(angletrouvé2)
                txtrésultattrigobottrouverangle.config(text=f"C = {angletrouvé2degré} °")
        elif côtéquona1 == "AB" and côtéquona2 == "BC":
            if anglequoncherche == "B":
                angletrouvé3 = math.acos(côtéquonamesure1 / côtéquonamesure2)
                angletrouvé3degré = math.degrees(angletrouvé3)
                txtrésultattrigobottrouverangle.config(text=f"B = {angletrouvé3degré} °")
            elif anglequoncherche == "C":
                angletrouvé4 = math.asin(côtéquonamesure1 / côtéquonamesure2)
                angletrouvé4degré = math.degrees(angletrouvé4)
                txtrésultattrigobottrouverangle.condif(text=f"C = {angletrouvé4degré} °")
        elif côtéquona1 == "AC" and côtéquona2 == "BC":
            if anglequoncherche == "B":
                angletrouvé5 = math.asin(côtéquonamesure1 / côtéquonamesure2)
                angletrouvé5degré = math.degrees(angletrouvé5)
                txtrésultattrigobottrouverangle.config(text=f"B = {angletrouvé5degré} °")
            elif anglequoncherche == "C":
                angletrouvé6 = math.acos(côtéquonamesure1 / côtéquonamesure2)
                angletrouvé6degré = math.degrees(angletrouvé6)
                txtrésultattrigobottrouverangle.config(text=f"C = {angletrouvé6degré} °")
        elif côtéquona1 == "AC" and côtéquona2 == "AB":
            if anglequoncherche == "B":
                angletrouvé7 = math.atan(côtéquonamesure1 / côtéquonamesure2)
                angletrouvé7degré = math.degrees(angletrouvé7)
                txtrésultattrigobottrouverangle.config(text=f"B = {angletrouvé7degré} °")
            elif anglequoncherche == "C":
                angletrouvé8 = math.atan(côtéquonamesure2 / côtéquonamesure1)
                angletrouvé8degré = math.degrees(angletrouvé8)
                txtrésultattrigobottrouverangle.config(text=f"C = {angletrouvé8degré} °")
        elif côtéquona1 == "BC" and côtéquona2 == "AB":
            if anglequoncherche == "B":
                angletrouvé9 = math.acos(côtéquonamesure2 / côtéquonamesure1)
                angletrouvé9degré = math.degrees(angletrouvé9)
                txtrésultattrigobottrouverangle.config(text=f"B = {angletrouvé9degré} °")
            elif anglequoncherche == "C":
                angletrouvé10 = math.asin(côtéquonamesure2 / côtéquonamesure1)
                angletrouvé10degré = math.degrees(angletrouvé10)
                txtrésultattrigobottrouverangle.config(text=f"C = {angletrouvé10degré} °")
        elif côtéquona1 == "BC" and côtéquona2 == "AC":
            if anglequoncherche == "B":
                angletrouvé11 = math.asin(côtéquonamesure2 / côtéquonamesure1)
                angletrouvé11degré = math.degrees(angletrouvé11)
                txtrésultattrigobottrouverangle.config(text=f"B = {angletrouvé11degré} °")
            elif anglequoncherche == "C":
                angletrouvé12 = math.acos(côtéquonamesure2 / côtéquonamesure1)
                angletrouvé12degré = math.degrees(angletrouvé12)
                txtrésultattrigobottrouverangle.config(text=f"C = {angletrouvé12degré} °")
    elif angledroitautilisertrigobottrouverangle == "B":
        if côtéquona1 == "AB" and côtéquona2 == "AC":
            if anglequoncherche == "A":
                angletrouvé13 = math.acos(côtéquonamesure1 / côtéquonamesure2)
                angletrouvé13degré = math.degrees(angletrouvé13)
                txtrésultattrigobottrouverangle.config(text=f"A = {angletrouvé13degré} °")
            elif anglequoncherche == "C":
                angletrouvé14 = math.asin(côtéquonamesure1 / côtéquonamesure2)
                angletrouvé14degré = math.degrees(angletrouvé14)
                txtrésultattrigobottrouverangle.config(text=f"C = {angletrouvé14degré} °")
        elif côtéquona1 == "AB" and côtéquona2 == "BC":
            if anglequoncherche == "A":
                angletrouvé15 = math.atan(côtéquonamesure2 / côtéquonamesure1)
                angletrouvé15degré = math.degrees(angletrouvé15)
                txtrésultattrigobottrouverangle.config(text=f"A = {angletrouvé15degré} °")
            elif anglequoncherche == "C":
                angletrouvé16 = math.atan(côtéquonamesure1 / côtéquonamesure2)
                angletrouvé16degré = math.degrees(angletrouvé16)
                txtrésultattrigobottrouverangle.config(text=f"C = {angletrouvé16degré} °")
        elif côtéquona1 == "AC" and côtéquona2 == "BC":
            if anglequoncherche == "A":
                angletrouvé17 = math.asin(côtéquonamesure2 / côtéquonamesure1)
                angletrouvé17degré = math.degrees(angletrouvé17)
                txtrésultattrigobottrouverangle.config(text=f"A = {angletrouvé17degré} °")
            elif anglequoncherche == "C":
                angletrouvé18 = math.acos(côtéquonamesure2 / côtéquonamesure1)
                angletrouvé18degré = math.degrees(angletrouvé18)
                txtrésultattrigobottrouverangle.config(text=f"C = {angletrouvé18degré} °")
        elif côtéquona1 == "AC" and côtéquona2 == "AB":
            if anglequoncherche == "A":
                angletrouvé19 = math.acos(côtéquonamesure2 / côtéquonamesure1)
                angletrouvé19degré = math.degrees(angletrouvé19)
                txtrésultattrigobottrouverangle.config(text=f"A = {angletrouvé19degré} °")
            elif anglequoncherche == "C":
                angletrouvé20 = math.asin(côtéquonamesure2 / côtéquonamesure1)
                angletrouvé20degré = math.degrees(angletrouvé20)
                txtrésultattrigobottrouverangle.config(text=f"C = {angletrouvé20degré} °")
        elif côtéquona1 == "BC" and côtéquona2 == "AB":
            if anglequoncherche == "A":
                angletrouvé21 = math.atan(côtéquonamesure1 / côtéquonamesure2)
                angletrouvé21degré = math.degrees(angletrouvé21)
                txtrésultattrigobottrouverangle.config(text=f"A = {angletrouvé21degré} °")
            elif anglequoncherche == "C":
                angletrouvé22 = math.atan(côtéquonamesure2 / côtéquonamesure1)
                angletrouvé22degré = math.degrees(angletrouvé22)
                txtrésultattrigobottrouverangle.config(text=f"C = {angletrouvé22degré} °")
        elif côtéquona1 == "BC" and côtéquona2 == "AC":
            if anglequoncherche == "A":
                angletrouvé23 = math.asin(côtéquonamesure1 / côtéquonamesure2)
                angletrouvé23degré = math.degrees(angletrouvé23)
                txtrésultattrigobottrouverangle.config(text=f"A = {angletrouvé23degré} °")
            elif anglequoncherche == "C":
                angletrouvé24 = math.acos(côtéquonamesure1 / côtéquonamesure2)
                angletrouvé24degré = math.degrees(angletrouvé24)
                txtrésultattrigobottrouverangle.config(text=f"C = {angletrouvé24degré} °")
    elif angledroitautilisertrigobottrouverangle == "C":
        if côtéquona1 == "AB" and côtéquona2 == "AC":
            if anglequoncherche == "A":
                angletrouvé25 = math.acos(côtéquonamesure2 / côtéquonamesure1)
                angletrouvé25degré = math.degrees(angletrouvé25)
                txtrésultattrigobottrouverangle.config(text=f"A = {angletrouvé25degré} °")
            elif anglequoncherche == "B":
                angletrouvé26 = math.asin(côtéquonamesure2 / côtéquonamesure1)
                angletrouvé26degré = math.degrees(angletrouvé26)
                txtrésultattrigobottrouverangle.config(text=f"B = {angletrouvé26degré} °")
        elif côtéquona1 == "AB" and côtéquona2 == "BC":
            if anglequoncherche == "A":
                angletrouvé27 = math.asin(côtéquonamesure2 / côtéquonamesure1)
                angletrouvé27degré = math.degrees(angletrouvé27)
                txtrésultattrigobottrouverangle.config(text=f"A = {angletrouvé27degré} °")
            elif anglequoncherche == "B":
                angletrouvé28 = math.acos(côtéquonamesure2 / côtéquonamesure1)
                angletrouvé28degré = math.degrees(angletrouvé28)
                txtrésultattrigobottrouverangle.config(text=f"B = {angletrouvé28degré} °")
        elif côtéquona1 == "AC" and côtéquona2 == "BC":
            if anglequoncherche == "A":
                angletrouvé29 = math.atan(côtéquonamesure2 / côtéquonamesure1)
                angletrouvé29degré = math.degrees(angletrouvé29)
                txtrésultattrigobottrouverangle.config(text=f"A = {angletrouvé29degré} °")
            elif anglequoncherche == "B":
                angletrouvé30 = math.atan(côtéquonamesure1 / côtéquonamesure2)
                angletrouvé30degré = math.degrees(angletrouvé30)
                txtrésultattrigobottrouverangle.config(text=f"B = {angletrouvé30degré} °")
        elif côtéquona1 == "AC" and côtéquona2 == "AB":
            if anglequoncherche == "A":
                angletrouvé31 = math.acos(côtéquonamesure1 / côtéquonamesure2)
                angletrouvé31degré = math.degrees(angletrouvé31)
                txtrésultattrigobottrouverangle.config(text=f"A = {angletrouvé31degré} °")
            elif anglequoncherche == "B":
                angletrouvé32 = math.asin(côtéquonamesure1 / côtéquonamesure2)
                angletrouvé32degré = math.degrees(angletrouvé32)
                txtrésultattrigobottrouverangle.config(text=f"B = {angletrouvé32degré} °")
        elif côtéquona1 == "BC" and côtéquona2 == "AB":
            if anglequoncherche == "A":
                angletrouvé33 = math.asin(côtéquonamesure1 / côtéquonamesure2)
                angletrouvé33degré = math.degrees(angletrouvé33)
                txtrésultattrigobottrouverangle.config(text=f"A = {angletrouvé33degré} °")
            elif anglequoncherche == "B":
                angletrouvé34 = math.acos(côtéquonamesure1 / côtéquonamesure2)
                angletrouvé34degré = math.degrees(angletrouvé34)
                txtrésultattrigobottrouverangle.config(text=f"B = {angletrouvé34degré} °")
        elif côtéquonamesure1 == "BC" and côtéquonamesure2 == "AC":
            if anglequoncherche == "A":
                angletrouvé35 = math.atan(côtéquonamesure1 / côtéquonamesure2)
                angletrouvé35degré = math.degrees(angletrouvé35)
                txtrésultattrigobottrouverangle.config(text=f"A = {angletrouvé35degré} °")
            elif anglequoncherche == "B":
                angletrouvé36 = math.atan(côtéquonamesure2 / côtéquonamesure1)
                angletrouvé36degré = math.degrees(angletrouvé36)
                txtrésultattrigobottrouverangle.config(text=f"B = {angletrouvé36degré} °")
    txtrésultattrigobottrouverangle.place(relx=0.5, rely=0.5, anchor="center", y=-100)
    txtrésultattrigobottrouverangle.update_idletasks()
    boutonquitteraprèstrouvéangle.place(x=750, y=735)
    boutonquitteraprèstrouvéangle.update_idletasks()

def revenirmenutrigobottrouvéangle():
    txtdescriptiontrigobottrouverangle.place_forget()
    menuangledroittrigobottrouverangle.place_forget()
    menuangledroittrigobottrouverangle.unbind("<Button-1>")
    menupremiercôtéquonatrigobottrouverangle.place_forget()
    menupremiercôtéquonatrigobottrouverangle.unbind("<Button-1>")
    txtégalpremiercôtéquonatrigobottrouverangle.place_forget()
    entréelongueurpremiercôtéquonatrigobottrouverangle.config(state="normal")
    entréelongueurpremiercôtéquonatrigobottrouverangle.place_forget()
    txtcmlongueurpremiercôtéquonatrigobottrouverangle.place_forget()
    menudeuxièmecôtéquonatrigobottrouverangle.place_forget()
    menudeuxièmecôtéquonatrigobottrouverangle.unbind("<Button-1>")
    txtégaldeuxièmecôtéquonatrigobottrouverangle.place_forget()
    entréedeuxièmecôtétrigobottrouverangle.config(state="normal")
    entréedeuxièmecôtétrigobottrouverangle.place_forget()
    txtcmdeuxièmecôtéquonatrigobottrouvercôté.place_forget()
    menuanglequoncherchetrigobottrouverangle.unbind("<Button-1>")
    menuanglequoncherchetrigobottrouverangle.place_forget()
    txtrésultattrigobottrouverangle.place_forget()
    boutonquitteraprèstrouvéangle.place_forget()
    boutontrigobottrouvercôté.place(x=270, y=135)
    boutontrigobottrouvercôté.update_idletasks()
    boutontrigobottrouverangle.place(x=500, y=135)
    boutontrigobottrouverangle.update_idletasks()
    txttrigobotdesciption.place(x=250, y=50)
    txttrigobotdesciption.update_idletasks()
    selectiontrigobotaction.place(x=310, y=85)
    selectiontrigobotaction.update_idletasks()
    boutonquittertrigobot.place(x=810, y=735)
    boutonquittertrigobot.update_idletasks()
    entréelongueurpremiercôtéquonatrigobottrouverangle.delete(0, "end")
    entréedeuxièmecôtétrigobottrouverangle.delete(0, "end")

# -------------------- L'INTERFACE --------------------
                
MathRobot = tk.Tk()
MathRobot.title("MathRobot")
MathRobot.geometry("1000x800")

txtmathrobot = tk.Label(MathRobot, text="Welcome to MathRobot!", font=("Digital-7", 20, "bold"), fg="red")
txtmathrobot.place(x=400, y=15)

descriptionbrève = tk.Label(MathRobot, text="MathRobot is a robot that performs different mathematical functions.", font=("Arial", 15, "italic"))
descriptionbrève.place(x=250, y=50)

selectionsousrobot = tk.Label(MathRobot, text="Click on what you want to do :", font=("Arial", 15, "italic"))
selectionsousrobot.place(x=395, y=85)

boutonpythagore = tk.Button(MathRobot, text="Pythagoras", command=lancerpythagore, fg="blue")
boutonpythagore.place(x=355, y=135)

txtpythrobot = tk.Label(MathRobot, text="Welcome to PythRobot !", font=("Digital-7", 20, "bold"), fg="red")
txtpythrobot.place(x=400, y=15)
txtpythrobot.place_forget()

boutontrigonométrie = tk.Button(MathRobot, text="Trigonometry", command=lancertrigonométrie, fg="blue")
boutontrigonométrie.place(x=507, y=135)

txttrigobot = tk.Label(MathRobot, text="Welcome to TrigoBot !", font=("Digital-7", 20, "bold"), fg="red")
txttrigobot.place(x=400, y=15)
txttrigobot.place_forget()

boutonpythrobottrouvercôté = tk.Button(MathRobot, text="Find the length of a side", command=trouverlalongueurduncôté, fg="green")
boutonpythrobottrouvercôté.place(x=270, y=135)
boutonpythrobottrouvercôté.place_forget()

boutonpythrobottrouverrectangularité = tk.Button(MathRobot, text="Find out if a triangle is right-angled", command=trouversiuntriangleestrectangle, fg="green")
boutonpythrobottrouverrectangularité.place(x=500, y=135)
boutonpythrobottrouverrectangularité.place_forget()

boutonquitterpythrobot = tk.Button(MathRobot, text="Quit PythRobot", command=quitterpythrobot, fg="red")
boutonquitterpythrobot.place(x=800, y=735)
boutonquitterpythrobot.place_forget()

txtdebienvenuepythrobotdescription = tk.Label(MathRobot, text="You are on PythRobot. It performs the Pythagorean theorem on a triangle ABC", font=("Arial", 15, "italic"))
txtdebienvenuepythrobotdescription.place(x=245, y=50)
txtdebienvenuepythrobotdescription.place_forget()

selectionpythrobotaction = tk.Label(MathRobot, text="Choose which option of the theorem you want to perform", font=("Arial", 15, "italic"))
selectionpythrobotaction.place(x=335, y=85)
selectionpythrobotaction.place_forget()

angledroitchoisipythrobottrouvermesurelongueur = tk.StringVar()
angledroitchoisipythrobottrouvermesurelongueur.set("Right angle : A")

menuangledroitpythrobottrouvermesurelongueur = tk.OptionMenu(MathRobot, angledroitchoisipythrobottrouvermesurelongueur, "Right angle : A", "Right angle : B", "Right angle : C")
menuangledroitpythrobottrouvermesurelongueur.place(x=100, y=150)
menuangledroitpythrobottrouvermesurelongueur.place_forget()

txtdescriptionpythrobottrouvermesurecôté = tk.Label(MathRobot, text="Select the right angle, validate, then select the length\nto find, validate and finally, enter the lengths of the sides in\nthe spaces provided for this purpose before validating.", font=("Arial", 15, "italic"))
txtdescriptionpythrobottrouvermesurecôté.place(x=300, y=50)
txtdescriptionpythrobottrouvermesurecôté.place_forget()

boutonvaliderchoixangledroitpythrobottrouvermesurelongueur = tk.Button(MathRobot, text="Validate", command=validerangledroitpythrobottrouvercôté, fg="black")
boutonvaliderchoixangledroitpythrobottrouvermesurelongueur.place(x=120, y=185)
boutonvaliderchoixangledroitpythrobottrouvermesurelongueur.place_forget()

côtéquoncherchepythrobot = tk.StringVar()
côtéquoncherchepythrobot.set("Side we are looking for : AB")

menucôtéquoncherchepythrobot = tk.OptionMenu(MathRobot, côtéquoncherchepythrobot, "Side we are looking for : AB", "Side we are looking for : AC", "Side we are looking for : BC")
menucôtéquoncherchepythrobot.place(x=400, y=150)
menucôtéquoncherchepythrobot.place_forget()

boutonvalidercôtéquoncherchepythrobot = tk.Button(MathRobot, text="Validate", command=validercôtéquoncherchepythrobot, fg="black")
boutonvalidercôtéquoncherchepythrobot.place(x=450, y=185)
boutonvalidercôtéquoncherchepythrobot.place_forget()

entrée1ercôtépythrobottrouvercôté = tk.Entry(MathRobot, font=("Arial"))
entrée1ercôtépythrobottrouvercôté.place(x=750, y=135)
entrée1ercôtépythrobottrouvercôté.place_forget()

entrée2ecôtépythrobottrouvercôté = tk.Entry(MathRobot, font=("Arial"))
entrée2ecôtépythrobottrouvercôté.place(x=750, y=165)
entrée2ecôtépythrobottrouvercôté.place_forget()

txtcmcôtéentrée1pythrobottrouvercôté = tk.Label(MathRobot, text="cm", font=("Arial", 15))
txtcmcôtéentrée1pythrobottrouvercôté.place(x=925, y=135)
txtcmcôtéentrée1pythrobottrouvercôté.place_forget()

txtcmcôtéentrée2pythrobottrouvercôté = tk.Label(MathRobot, text="cm", font=("Arial", 15))
txtcmcôtéentrée2pythrobottrouvercôté.place(x=925, y=165)
txtcmcôtéentrée2pythrobottrouvercôté.place_forget()

txtABcôtéentrée1pythrobottrouvercôté = tk.Label(MathRobot, text="AB =", font=("Arial", 15))
txtABcôtéentrée1pythrobottrouvercôté.place(x=710, y=135)
txtABcôtéentrée1pythrobottrouvercôté.place_forget()

txtACcôtéhautentrée1pythrobottrouvercôté = tk.Label(MathRobot, text="AC =", font=("Arial", 15))
txtACcôtéhautentrée1pythrobottrouvercôté.place(x=710, y=135)
txtACcôtéhautentrée1pythrobottrouvercôté.place_forget()

txtACcôtéentrée2pythrobottrouvercôté = tk.Label(MathRobot, text="AC =", font=("Arial", 15))
txtACcôtéentrée2pythrobottrouvercôté.place(x=710, y=165)
txtACcôtéentrée2pythrobottrouvercôté.place_forget()

txtBCcôtéhautentrée2pythrobottrouvercôté = tk.Label(MathRobot, text="BC =", font=("Arial", 15))
txtBCcôtéhautentrée2pythrobottrouvercôté.place(x=710, y=165)
txtBCcôtéhautentrée2pythrobottrouvercôté.place_forget()

boutonvaliderentréescôtéspythrobottrouvercôté = tk.Button(MathRobot, text="Validate", command=validerentréescôtéspythrobottrouvercôté, fg="black")
boutonvaliderentréescôtéspythrobottrouvercôté.place(x=800, y=200)
boutonvaliderentréescôtéspythrobottrouvercôté.place_forget()

txtABrésultatcôtépythrobottrouvercôté = tk.Label(MathRobot, text="AB =" + str(côtétrouvépythrobottrouvercôté) + "cm", font=("Arial", 20))
txtABrésultatcôtépythrobottrouvercôté.place(x=350, y=250)
txtABrésultatcôtépythrobottrouvercôté.place_forget()

txtACrésultatcôtépythrobottrouvercôté = tk.Label(MathRobot, text="AC =" + str(côtétrouvépythrobottrouvercôté) + "cm", font=("Arial", 20))
txtACrésultatcôtépythrobottrouvercôté.place(x=350, y=250)
txtACrésultatcôtépythrobottrouvercôté.place_forget()

txtBCrésultatcôtépythrobottrouvercôté = tk.Label(MathRobot, text="BC =" + str(côtétrouvépythrobottrouvercôté) + "cm", font=("Arial", 20))
txtBCrésultatcôtépythrobottrouvercôté.place(x=350, y=250)
txtBCrésultatcôtépythrobottrouvercôté.place_forget()

boutonquitteraprèsavoirtrouvécôtépythrobot = tk.Button(MathRobot, text="Return to the Pythrobot menu", command=revenirmenupythrobotaprèstrouvécôté, fg="red")
boutonquitteraprèsavoirtrouvécôtépythrobot.place(x=750, y=735)
boutonquitteraprèsavoirtrouvécôtépythrobot.place_forget()

entréeABpythrobotrectangularité = tk.Entry(MathRobot, font=("Arial"))
entréeABpythrobotrectangularité.place(x=110, y=150)
entréeABpythrobotrectangularité.place_forget()

entréeACpythrobotrectangularité = tk.Entry(MathRobot, font=("Arial"))
entréeACpythrobotrectangularité.place(x=400, y=150)
entréeACpythrobotrectangularité.place_forget()

entréeBCpythrobotrectangularité = tk.Entry(MathRobot, font=("Arial"))
entréeBCpythrobotrectangularité.place(x=750, y=150)
entréeBCpythrobotrectangularité.place_forget()

txtABégalpythrobotrectangularité = tk.Label(MathRobot, text="AB =", font=("Arial", 15))
txtABégalpythrobotrectangularité.place(x=70, y=150)
txtABégalpythrobotrectangularité.place_forget()

txtcmABégalpythrobotrectangularité = tk.Label(MathRobot, text="cm", font=("Arial", 15))
txtcmABégalpythrobotrectangularité.place(x=282, y=150)
txtcmABégalpythrobotrectangularité.place_forget()

txtACégalpythrobotrectangularité = tk.Label(MathRobot, text="AC =", font=("Arial", 15))
txtACégalpythrobotrectangularité.place(x=360, y=150)
txtACégalpythrobotrectangularité.place_forget()

txtcmACégalpythrobotrectangularité = tk.Label(MathRobot, text="cm", font=("Arial", 15))
txtcmACégalpythrobotrectangularité.place(x=572, y=150)
txtcmACégalpythrobotrectangularité.place_forget()

txtBCégalpythrobotrectangularité = tk.Label(MathRobot, text="BC =", font=("Arial", 15))
txtBCégalpythrobotrectangularité.place(x=710, y=150)
txtBCégalpythrobotrectangularité.place_forget()

txtcmBCégalpythrobotrectangularité = tk.Label(MathRobot, text="cm", font=("Arial", 15))
txtcmBCégalpythrobotrectangularité.place(x=922, y=150)
txtcmBCégalpythrobotrectangularité.place_forget()

txtdescriptionpythrobotrectangularité = tk.Label(MathRobot, text="Enter the lengths of AB, AC and BC, then validate.", font=("Arial", 15, "italic"))
txtdescriptionpythrobotrectangularité.place(x=350, y=75)
txtdescriptionpythrobotrectangularité.place_forget()

boutonvaliderentréescôtéspythrobotrectangularité = tk.Button(MathRobot, text="Validate", command=validerentréescôtéspythrobotrectangularité, fg="black")
boutonvaliderentréescôtéspythrobotrectangularité.place(x=445, y=200)
boutonvaliderentréescôtéspythrobotrectangularité.place_forget()

txtsirectangleoupaspythrobotrectanglarité = tk.Label(MathRobot, text="0", font=("Arial", 20))
txtsirectangleoupaspythrobotrectanglarité.place(x=350, y=250)
txtsirectangleoupaspythrobotrectanglarité.place_forget()

boutonquitterrectangularitépythrobot = tk.Button(MathRobot, text="Return to the PyhtRobot menu", command=revenirmenupythrobotaprèsrectangularité, fg="red")
boutonquitterrectangularitépythrobot.place(x=750, y=735)
boutonquitterrectangularitépythrobot.place_forget()

boutontrigobottrouvercôté = tk.Button(MathRobot, text="Find the length of a side", command=trouvercôtétrigobot, fg="green")
boutontrigobottrouvercôté.place(x=270, y=135)
boutontrigobottrouvercôté.place_forget()

boutontrigobottrouverangle = tk.Button(MathRobot, text="Find the measure of an angle", command=trouverangletrigobot, fg="green")
boutontrigobottrouverangle.place(x=500, y=135)
boutontrigobottrouverangle.place_forget()

txttrigobotdesciption = tk.Label(MathRobot, text="You are on Trigobot. It performs trigonometric functions on a triangle ABC.", font=("Arial", 15, "italic"))
txttrigobotdesciption.place(x=250, y=50)
txttrigobotdesciption.place_forget()

selectiontrigobotaction = tk.Label(MathRobot, text="Choose which trigonometry option you want to do", font=("Arial", 15, "italic"))
selectiontrigobotaction.place(x=310, y=85)
selectiontrigobotaction.place_forget()

boutonquittertrigobot = tk.Button(MathRobot, text="Quit TrigoBot", command=quitterTrigoBot, fg="red")
boutonquittertrigobot.place(x=810, y=735)
boutonquittertrigobot.place_forget()

txtdescriptiontrigobottrouvercôté = tk.Label(MathRobot, text="Enter the name of the right angle, validate, then enter the name of the side\nyou have then its length, validate, enter the name of the angle\nyou have, then its measure and validate, finally, enter\nthe name of the side you are looking for and validate", font=("Arial", 15, "italic"))
txtdescriptiontrigobottrouvercôté.place(x=290, y=50)
txtdescriptiontrigobottrouvercôté.place_forget()

angledroittriangletrigobottrouvercôté = tk.StringVar()
angledroittriangletrigobottrouvercôté.set("Right angle : A")

menuangledroittigobottrouvercôté = tk.OptionMenu(MathRobot, angledroittriangletrigobottrouvercôté, "Right angle : A", "Right angle : B", "Right angle : C")
menuangledroittigobottrouvercôté.place(x=20, y=150)
menuangledroittigobottrouvercôté.place_forget()

boutonvaliderangledroitrigobottrouvercôté = tk.Button(MathRobot, text="Validate", command=validerangledroittrigobottrouvercôté, fg="black")
boutonvaliderangledroitrigobottrouvercôté.place(x=40, y=185)
boutonvaliderangledroitrigobottrouvercôté.place_forget()

côtéquonatrigobottrouvercôté = tk.StringVar()
côtéquonatrigobottrouvercôté.set("Side we have : AB")

menucôtéquonatrigobottrouvercôté = tk.OptionMenu(MathRobot, côtéquonatrigobottrouvercôté, "Side we have : AB", "Side we have : AC", "Side we have : BC")
menucôtéquonatrigobottrouvercôté.place(x=185, y=150)
menucôtéquonatrigobottrouvercôté.place_forget()

boutonvalidercôtéquatrigobottrouvercôtéaveclongueur = tk.Button(MathRobot, text="Validate", command=validercôtéquonatrigobottrouvercôtéaveclongueur, fg="black")
boutonvalidercôtéquatrigobottrouvercôtéaveclongueur.place(x=370, y=185)
boutonvalidercôtéquatrigobottrouvercôtéaveclongueur.place_forget()

entréelongueurcôtéquatrigobottrouvercôté = tk.Entry(MathRobot, font=("Arial"))
entréelongueurcôtéquatrigobottrouvercôté.place(x=360, y=149.5)
entréelongueurcôtéquatrigobottrouvercôté.place_forget()

txtégalcôtéquonatrigobottrouvercôté = tk.Label(MathRobot, text="=", font=("Arial", 17))
txtégalcôtéquonatrigobottrouvercôté.place(x=340, y=148.5)
txtégalcôtéquonatrigobottrouvercôté.place_forget()

txtcmcôtéquonatrigobottrouvercôté = tk.Label(MathRobot, text="cm", font=("Arial", 17))
txtcmcôtéquonatrigobottrouvercôté.place(x=535, y=148)
txtcmcôtéquonatrigobottrouvercôté.place_forget()

anglequonatrigobottrouvercôté = tk.StringVar()
anglequonatrigobottrouvercôté.set("Angle that we have : B")

menuanglequonatrigobottrouvercôté = tk.OptionMenu(MathRobot, anglequonatrigobottrouvercôté, "Angle that we have : A", "Angle that we have : B", "Angle that we have : C")
menuanglequonatrigobottrouvercôté.place(x=585, y=148.5)
menuanglequonatrigobottrouvercôté.place_forget()

boutonvalideranglequonatrigobottrouvercôté = tk.Button(MathRobot, text="Validate", command=valideranglequonatrigobottrouvercôté, fg="black")
boutonvalideranglequonatrigobottrouvercôté.place(x=740, y=185)
boutonvalideranglequonatrigobottrouvercôté.place_forget()

entréeanglequonatrigobottrouvercôté = tk.Entry(MathRobot, font=("Arial"))
entréeanglequonatrigobottrouvercôté.place(x=790, y=147.5)
entréeanglequonatrigobottrouvercôté.place_forget()

txtégalanglequonatrigobottrouvercôté = tk.Label(MathRobot, text="=", font=("Arial", 17))
txtégalanglequonatrigobottrouvercôté.place(x=710, y=147.5)
txtégalanglequonatrigobottrouvercôté.place_forget()

txtdegréanglequonatrigobottrouvercôté = tk.Label(MathRobot, text="°", font=("Arial", 17))
txtdegréanglequonatrigobottrouvercôté.place(x=965, y=147.5)
txtdegréanglequonatrigobottrouvercôté.place_forget()

côtéquoncherchetrigobottrouvercôté = tk.StringVar()
côtéquoncherchetrigobottrouvercôté.set("Side we are looking for : AC")

menucôtéquoncherchetrigobottrouvercôté = tk.OptionMenu(MathRobot, côtéquoncherchetrigobottrouvercôté, "Side we are looking for : AB", "Side we are looking for : AC", "Side we are looking for : BC")
menucôtéquoncherchetrigobottrouvercôté.place(x=400, y=225)
menucôtéquoncherchetrigobottrouvercôté.place_forget()

boutonvalidercôtéquoncherchetrigobottrouvercôté = tk.Button(MathRobot, text="Validate", command=validercôtéquoncherchetrigobottrouvercôté, fg="black")
boutonvalidercôtéquoncherchetrigobottrouvercôté.place(x=455, y=260)
boutonvalidercôtéquoncherchetrigobottrouvercôté.place_forget()

txtrésultattrigobottrouvercôté = tk.Label(MathRobot, text="", font=("Arial", 20))
txtrésultattrigobottrouvercôté.place(x=450, y=300)
txtrésultattrigobottrouvercôté.place_forget()

boutonquitteraprèstrouvécôtétrigobot = tk.Button(MathRobot, text="Return to the Trigobot menu", command=quitteraprèstrouvécôté, fg="red")
boutonquitteraprèstrouvécôtétrigobot.place(x=750, y=735)
boutonquitteraprèstrouvécôtétrigobot.place_forget()

txtdescriptiontrigobottrouverangle = tk.Label(MathRobot, text="Choose the right angle, valid, enter the name of the 1st side you have\nthen its length, valid, enter the name of the 2nd side you have\nthen its length, valid, finally, enter the name of the angle you\nare looking for and validate", font=("Arial", 15, "italic"))
txtdescriptiontrigobottrouverangle.place(x=283, y=50)
txtdescriptiontrigobottrouverangle.place_forget()

angledroittrigobottrouverangle = tk.StringVar()
angledroittrigobottrouverangle.set("Right angle : A")

menuangledroittrigobottrouverangle = tk.OptionMenu(MathRobot, angledroittrigobottrouverangle, "Right angle : A", "Right angle : B", "Right angle : C")
menuangledroittrigobottrouverangle.place(x=20, y=150)
menuangledroittrigobottrouverangle.place_forget()

boutonvaliderangledroitrigobottrouverangle = tk.Button(MathRobot, text="Validate", command=validerangledroittrigobottrouverangle, fg="black")
boutonvaliderangledroitrigobottrouverangle.place(x=40, y=185)
boutonvaliderangledroitrigobottrouverangle.place_forget()

premiercôtéquonatrigobottrouverangle = tk.StringVar()
premiercôtéquonatrigobottrouverangle.set("1er Side we have : AB")

menupremiercôtéquonatrigobottrouverangle = tk.OptionMenu(MathRobot, premiercôtéquonatrigobottrouverangle, "1er Side we have : AB", "1er Side we have : AC", "1er Side we have : BC")
menupremiercôtéquonatrigobottrouverangle.place(x=170, y=150)
menupremiercôtéquonatrigobottrouverangle.place_forget()

txtégalpremiercôtéquonatrigobottrouverangle = tk.Label(MathRobot, text="=", font=("Arial", 17))
txtégalpremiercôtéquonatrigobottrouverangle.place(x=345, y=148.5)
txtégalpremiercôtéquonatrigobottrouverangle.place_forget()

entréelongueurpremiercôtéquonatrigobottrouverangle = tk.Entry(MathRobot, font=("Arial"))
entréelongueurpremiercôtéquonatrigobottrouverangle.place(x=465, y=149.5)
entréelongueurpremiercôtéquonatrigobottrouverangle.place_forget()

txtcmlongueurpremiercôtéquonatrigobottrouverangle = tk.Label(MathRobot, text="cm", font=("Arial", 17))
txtcmlongueurpremiercôtéquonatrigobottrouverangle.place(x=540, y=150)
txtcmlongueurpremiercôtéquonatrigobottrouverangle.place_forget()

boutonvaliderentréepremiercôtétrigobottrouverangle = tk.Button(MathRobot, text="Validate", command=validerentréepremiercôtétrigobottrouverangle, fg="black")
boutonvaliderentréepremiercôtétrigobottrouverangle.place(x=370, y=185)
boutonvaliderentréepremiercôtétrigobottrouverangle.place_forget()

deuxièmecôtéquonatrigobottrouverangle = tk.StringVar()
deuxièmecôtéquonatrigobottrouverangle.set("2e Side we have : AC")

menudeuxièmecôtéquonatrigobottrouverangle = OptionMenu(MathRobot, deuxièmecôtéquonatrigobottrouverangle, "2e Side we have : AB", "2e Side we have : AC", "2e Side we have : BC")
menudeuxièmecôtéquonatrigobottrouverangle.place(x=585, y=152)
menudeuxièmecôtéquonatrigobottrouverangle.place_forget()

txtégaldeuxièmecôtéquonatrigobottrouverangle = tk.Label(MathRobot, text="=", font=("Arial", 17))
txtégaldeuxièmecôtéquonatrigobottrouverangle.place(x=760, y=149)
txtégaldeuxièmecôtéquonatrigobottrouverangle.place_forget()

entréedeuxièmecôtétrigobottrouverangle = tk.Entry(MathRobot, font=("Arial"))
entréedeuxièmecôtétrigobottrouverangle.place(x=780, y=150)
entréedeuxièmecôtétrigobottrouverangle.place_forget()

txtcmdeuxièmecôtéquonatrigobottrouvercôté = tk.Label(MathRobot, text="cm", font=("Arial", 17))
txtcmdeuxièmecôtéquonatrigobottrouvercôté.place(x=955, y=149)
txtcmdeuxièmecôtéquonatrigobottrouvercôté.place_forget()

boutonvaliderdeuxièmecôtétrigobottrouverangle = tk.Button(MathRobot, text="Validate", command=validerentréedeuxièmecôtétrigobottrouvercôté, fg="black")
boutonvaliderdeuxièmecôtétrigobottrouverangle.place(x=770, y=185)
boutonvaliderdeuxièmecôtétrigobottrouverangle.place_forget()

anglequoncherchetrigobottrouverangle = tk.StringVar()
anglequoncherchetrigobottrouverangle.set("Angle we are looking for : B")

menuanglequoncherchetrigobottrouverangle = tk.OptionMenu(MathRobot, anglequoncherchetrigobottrouverangle, "Angle we are looking for : A", "Angle we are looking for : B", "Angle we are looking for : C")
menuanglequoncherchetrigobottrouverangle.place(x=400, y=225)
menuanglequoncherchetrigobottrouverangle.place_forget()

boutonvalideranglequoncherchetrigobottrouverangle = tk.Button(MathRobot, text="Validate", command=valideranglequoncherchetrigobottrouverangle, fg=("black"))
boutonvalideranglequoncherchetrigobottrouverangle.place(x=455, y=260)
boutonvalideranglequoncherchetrigobottrouverangle.place_forget()

txtrésultattrigobottrouverangle = tk.Label(MathRobot, text="", font=("Arial", 20))
txtrésultattrigobottrouverangle.place(x=450, y=300)
txtrésultattrigobottrouverangle.place_forget()

boutonquitteraprèstrouvéangle = tk.Button(MathRobot, text="Return to the Trigobot menu", command=revenirmenutrigobottrouvéangle, fg="red")
boutonquitteraprèstrouvéangle.place(x=750, y=735)
boutonquitteraprèstrouvéangle.place_forget()

MathRobot.mainloop() 

#END