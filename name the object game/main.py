import tkinter as tk
from PIL import Image, ImageTk
import os
import pygame
import random


ASSETS_FOLDER = "assets"
IMAGE_FOLDER = os.path.join(ASSETS_FOLDER, "images")
SOUND_FOLDER = os.path.join(ASSETS_FOLDER, "sounds")

imagini_cu_cuvinte = {
    "fructe": {
        'kivi.jpg': 'Kiwi',
        'ananas.jpg': 'Ananas',
        'mar.jpg': 'Mar',
        'banana.jpg': 'Banana',
        'cocos.jpg': 'Cocos',
        'cirese.jpg': 'Cirese',
        'capsuna.jpg': 'Capsuna',
        'strugure.jpg': 'Strugure',
        'para.jpg': 'Para'
    },
    "legume": {
        'ardei.jpg': 'Ardei',
        'rosie.jpg': 'Rosie',
        'morcov.jpg': 'Morcov',
        'cartof.jpg': 'Cartof',
        'varza.jpg': 'Varza',
        'castravete.jpg': 'Castravete',
        'dovleac.jpg': 'Dovleac',
        'pepene.jpg': 'Pepene',
        'ceapa.jpg': 'Usturoi',
        'brocoli.jpg': 'Brocoli'
    },
    "culori": {
        'verde.jpg': 'Verde',
        'albastru.jpg': 'Albastru',
        'violet.jpg': 'Violet',
        'rosu.jpg': 'Rosu',
        'roz.jpg': 'Roz',
        'portocaliu.jpg': 'Portocaliu',
        'galben.jpg': 'Galben'
    },
    "obiecte": {
        'carte.jpg': 'Carte',
        'ceas.jpg': 'Ceas',
        'computer.jpg': 'Computer',
        'dulap_cu_haine.jpg': 'Dulap cu haine',
        'frigider.jpg': 'Frigider',
        'ghiozdan.jpg': 'Ghiozdan',
        'ghiveci_flori.jpg': 'Ghiveci cu flori',
        'minge.jpg': 'Minge',
        'pahar_de_suc.jpg': 'Pahar de suc',
        'pat.jpg': 'Pat',
        'periuta_de_dinti.jpg': 'Periuta de dinti',
        'perna.jpg': 'Perna',
        'sapun.jpg': 'Sapun',
        'scaun.jpg': 'Scaun',
        'ursulet_de_plus.jpg': 'Ursulet de plus'
    },
    "animale": {
        'pisica.jpg': 'Pisica',
        'soarece.jpg': 'Soarece',
        'zebra.jpg': 'Zebra',
        'vultur.jpg': 'Vultur',
        'elefant.jpg': 'Elefant',
        'leu.jpg': 'Leu',
        'tigru.jpg': 'Tigru',
        'girafa.jpg': 'Girafa',
        'caine.jpg': 'Caine',
        'cal.jpg': 'Cal',
        'vaca.jpg': 'Vaca',
        'rata.jpg': 'Rata',
        'gaina.jpg': 'Gaina'
    }
}


imagini_ramase = []


pygame.init()


def play_sound(file_name):
    pygame.mixer.music.load(os.path.join(SOUND_FOLDER, file_name))
    pygame.mixer.music.play()


def afisare_pagina_joc():
    for widget in root.winfo_children():
        widget.pack_forget()
    buton_inapoi.pack(side="top", anchor="nw", padx=10, pady=10)
    titlu_label.pack()

    panel.pack(side="top", fill="both", expand="yes")
    feedback_label.pack()
    scor_label.pack()
    button_frame.pack()
    for button in butoane_raspuns:
        button.pack(side="left", padx=10, pady=10)
    urmatoarea_buton.pack(side="bottom", padx=10, pady=10)


def buton_inapoi_la_categorii():
    global scor_corect, scor_gresit, runda
    runda = 0
    scor_corect = 0
    scor_gresit = 0
    imagini_ramase = []
    categoria_curenta = []
    for widget in root.winfo_children():
        widget.pack_forget()
    afisare_meniu_categorii()


def sfarsitul_jocului():
    global scor_corect, scor_gresit, runda
    for widget in root.winfo_children():
        widget.pack_forget()
    tk.Label(root, text=f"Sfarsitul Jocului! Scorul tau este: {scor_corect}, ai avut {scor_gresit} raspunsuri gresite",
             font=font_titlu, bg='light blue').pack(pady=10)
    tk.Button(root, text="Intoarce-te la Alege Categoria", command=buton_inapoi_la_categorii, height=2, width=40,
              font=font_text, bg='light green').pack(pady=10)
    scor_corect = 0
    scor_gresit = 0
    runda = 0
    play_sound("sfarsit.mp3")
    imagini_ramase.clear()


def buton_animatie(buton):
    buton.config(bg='dark green')
    root.after(200, lambda: buton.config(bg='light green'))


def verifica_raspuns(index):
    global scor_corect, scor_gresit, imagini_ramase
    buton_animatie(butoane_raspuns[index])
    if optiuni[index] == raspuns_corect:
        scor_corect += 1
        play_sound("corect.mp3")
        animatie_confetii()
        feedback_label.config(text="Corect!", fg="green")
        imagini_ramase.remove(imagine_aleasa)
        scor_label.config(text=f"Scor: {scor_corect} Corecte, {scor_gresit} Gresite")

        for button in butoane_raspuns:
            button.config(state="disabled")

        if not imagini_ramase:
            root.after(1500, sfarsitul_jocului)
        else:
            root.after(1500, urmatoare_intrebare)
    else:
        scor_gresit += 1
        play_sound("wrong.mp3")
        feedback_label.config(text="Gresit! Incearca din nou.", fg="red")
        scor_label.config(text=f"Scor: {scor_corect} Corecte, {scor_gresit} Gresite")


def urmatoare_intrebare():
    global raspuns_corect, optiuni, image_references, runda, imagini, imagini_ramase, imagine_aleasa
    runda += 1
    titlu_label.config(text=f"Jocul Cuvintelor - Runda {runda}")

    if not imagini_ramase:
        imagini_ramase = list(imagini_cu_cuvinte[categoria_curenta].keys())

    imagine_aleasa = random.choice(imagini_ramase)
    raspuns_corect = imagini_cu_cuvinte[categoria_curenta][imagine_aleasa]
    cuvinte_gresite = list(imagini_cu_cuvinte[categoria_curenta].values())
    cuvinte_gresite.remove(raspuns_corect)
    optiuni = random.sample(cuvinte_gresite, 2) + [raspuns_corect]
    random.shuffle(optiuni)

    image_path = os.path.join(IMAGE_FOLDER, imagine_aleasa)
    img = Image.open(image_path)
    img = img.resize((300, 300), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    panel.config(image=photo)
    panel.image = photo
    image_references.append(photo)

    for i, button in enumerate(butoane_raspuns):
        button.config(text=optiuni[i], state=tk.NORMAL)

    feedback_label.config(text='')


def incepe_jocul(categorie_aleasa):
    global categoria_curenta, imagini_ramase
    categoria_curenta = categorie_aleasa
    imagini_ramase = list(imagini_cu_cuvinte[categoria_curenta].keys())
    scor_label.config(text=f"Scor: 0 Corecte, 0 Gresite")
    titlu_label.config(text=f"Jocul Cuvintelor - Runda 1")
    afisare_pagina_joc()
    urmatoare_intrebare()


def update_frame(index, stop):
    try:
        frame = frames[index]
        confetti_label.configure(image=frame)
        stop += 1
        if stop < 100:
            root.after(50, update_frame, (index+1) % 10, stop)
    except StopIteration:
        pass


def animatie_confetii():
    global confetti_label, frames
    file_path = 'confetti.gif'
    confetti_gif = tk.PhotoImage(file=file_path)
    frames = [tk.PhotoImage(file=file_path, format=f'gif -index {i}') for i in range(10)]

    confetti_label = tk.Label(root, bg='light blue')
    confetti_label.place(x=0, y=0, relwidth=1, relheight=1)
    update_frame(0, 0)

    def ascunde_confetti():
        confetti_label.place_forget()

    root.after(1500, ascunde_confetti)


def afisare_meniu_categorii():
    for widget in root.winfo_children():
        widget.pack_forget()

    label_meniu = tk.Label(root, text="*Alege Categoria*", font=font_titlu, bg='light blue')
    label_meniu.pack(pady=10)

    for categorie in imagini_cu_cuvinte.keys():
        buton = tk.Button(root, text=categorie.capitalize(), command=lambda cat=categorie: incepe_jocul(cat),
                          height=2, width=20, font=font_text, bg='light green')
        buton.pack(pady=10)

    buton_exit.pack(side="bottom")


root = tk.Tk()
root.title("Ghiceste Cuvantul")
root.attributes('-fullscreen', True)
root.configure(bg='light blue')

font_titlu = ("Comic Sans MS", 24, "bold")
font_text = ("Comic Sans MS", 16)

titlu_label = tk.Label(root, text="Jocul Cuvintelor", font=font_titlu, bg='light blue', fg='dark blue')
panel = tk.Label(root, bg='light blue')
feedback_label = tk.Label(root, text="", font=font_text, bg='light blue')
scor_label = tk.Label(root, text="Scor: 0 Corecte, 0 Gresite", font=font_text, bg='light blue')

button_frame = tk.Frame(root, bg='light blue')
butoane_raspuns = []

for i in range(3):
    button = tk.Button(button_frame, command=lambda i=i: verifica_raspuns(i), height=2, width=20,
                       font=font_text, bg='light green', fg='dark green')
    butoane_raspuns.append(button)

urmatoarea_buton = tk.Button(root, text="Urmatorul", command=urmatoare_intrebare, height=2, width=65,
                             font=font_text, bg='light yellow', fg='dark red')
buton_inapoi = tk.Button(root, text="Inapoi", command=buton_inapoi_la_categorii, height=2, width=20,
                         font=font_text, bg='light yellow', fg='dark red')
buton_exit = tk.Button(root, text="Iesire", command=root.destroy, height=2, width=20,
                       font=font_text, bg='red', fg='white')

scor_corect = 0
scor_gresit = 0
runda = 0
image_references = []
categoria_curenta = ''

afisare_meniu_categorii()
play_sound("welcome.mp3")

root.mainloop()
