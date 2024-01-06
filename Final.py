# Library Imports
from pynput import keyboard
import pyautogui
import threading
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import screeninfo
import random
from tkinter import messagebox
import cv2
import pyperclip as pc
import webbrowser


def copy_clip(text):
    pc.copy(text)




# root assignments

root = tk.Tk()
root.title('WT4.0')
root.iconbitmap('C:/Users/Administrator/Desktop/Main.py/WT4.1.ico')
root.geometry('768x432')
root.resizable(False, False)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


#afk func

def anti_afk(speed=1.9):
    def _anti_afk():
        pyautogui.FAILSAFE = False
        screens = screeninfo.get_monitors()

        listener = keyboard.Listener(on_press=on_press)
        listener.start()

        while True:
            for screen in screens:
                width = screen.width
                height = screen.height
                x = random.randint(screen.x, screen.x + width)
                y = random.randint(screen.y, screen.y + height)

                duration = random.uniform(speed, speed)

                pyautogui.moveTo(x, y, duration=duration)

                if not listener.running:
                    return

    def on_press(key):
        if key == keyboard.Key.space or key == keyboard.Key.esc:
            return False
        return
    messagebox.showinfo("Anti-AFK", "Press 'esc' or 'space' key to stop :)")
    t = threading.Thread(target=_anti_afk)
    t.daemon = True
    t.start()

# Exit btn functions
def close_application():
    root.destroy()



# Intro page

intro_pg = ttk.Frame(root)
intro_pg.grid(row=0, column=0, sticky="nsew")
intro_lb = ttk.Label(intro_pg)
intro_lb.place(relx=0.5, rely=0.5, anchor=CENTER)



# Assigned labels and pages


gif_mainpg = ttk.Frame(root)
gif_mainpg.grid(row=0, column=0, sticky="nsew")
gif_lb = ttk.Label(gif_mainpg)
gif_lb.place(relx=0.5, rely=0.5, anchor=CENTER)

# Main2

mainpg2 = ttk.Frame(root)
mainpg2.grid(row=0, column=0, sticky="nsew")
mp2lb = ttk.Label(mainpg2)
mp2lb.place(relx=0.5, rely=0.5, anchor=CENTER)


# FI page


gif_FIPpg = ttk.Frame(root)
gif_FIPpg.grid(row=0, column=0, sticky="nsew")
gifFIP_lb = ttk.Label(gif_FIPpg)
gifFIP_lb.place(relx=0.5, rely=0.5, anchor=CENTER)

# Braun page

gif_brpg = ttk.Frame(root)
gif_brpg.grid(row=0, column=0, sticky="nsew")
gifbr_lb = ttk.Label(gif_brpg)
gifbr_lb.place(relx=0.5, rely=0.5, anchor=CENTER)


# CPI page

gif_cpipg = ttk.Frame(root)
gif_cpipg.grid(row=0, column=0, sticky="nsew")
gifcpi_lb = ttk.Label(gif_cpipg)
gifcpi_lb.place(relx=0.5, rely=0.5, anchor=CENTER)

# clbr pg

clbrpg = ttk.Frame(root)
clbrpg.grid(row=0, column=0, sticky="nsew")
clbr_lb = ttk.Label(clbrpg)
clbr_lb.place(relx=0.5, rely=0.5, anchor=CENTER)

# Jax pg

jxpg = ttk.Frame(root)
jxpg.grid(row=0, column=0, sticky="nsew")
jx_lb = ttk.Label(jxpg)
jx_lb.place(relx=0.5, rely=0.5, anchor=CENTER)

# qst pg

qstpg = ttk.Frame(root)
qstpg.grid(row=0, column=0, sticky="nsew")
qst_lb = ttk.Label(qstpg)
qst_lb.place(relx=0.5, rely=0.5, anchor=CENTER)

# sbrpg

sbrpg = ttk.Frame(root)
sbrpg.grid(row=0, column=0, sticky="nsew")
sbr_lb = ttk.Label(sbrpg)
sbr_lb.place(relx=0.5, rely=0.5, anchor=CENTER)

# usp pg

uspg = ttk.Frame(root)
uspg.grid(row=0, column=0, sticky="nsew")
us_lb = ttk.Label(uspg)
us_lb.place(relx=0.5, rely=0.5, anchor=CENTER)

# bell

blpg = ttk.Frame(root)
blpg.grid(row=0, column=0, sticky="nsew")
bl_lb = ttk.Label(blpg)
bl_lb.place(relx=0.5, rely=0.5, anchor=CENTER)

# vera pg

vrpg = ttk.Frame(root)
vrpg.grid(row=0, column=0, sticky="nsew")
vr_lb = ttk.Label(vrpg)
vr_lb.place(relx=0.5, rely=0.5, anchor=CENTER)

# Button Images

Introstrtbtn_img = Image.open("C:/Users/Administrator/Desktop/Main.py/start.png")
Introstrtbtn_photo = ImageTk.PhotoImage(Introstrtbtn_img)

IntrostrtHbtn_img = Image.open("C:/Users/Administrator/Desktop/Main.py/starth.png")
IntrostrtHbtn_photo = ImageTk.PhotoImage(IntrostrtHbtn_img)

Introextbtn_img = Image.open("C:/Users/Administrator/Desktop/Main.py/ext.png")
Introextbtn_photo = ImageTk.PhotoImage(Introextbtn_img)

IntroextHbtn_img = Image.open("C:/Users/Administrator/Desktop/Main.py/exth.png")
IntroextHbtn_photo = ImageTk.PhotoImage(IntroextHbtn_img)

# BaCK btn img

back_btnfi_img = Image.open("C:/Users/Administrator/Desktop/Main.py/arrow.png")
back_btnfi_photo = ImageTk.PhotoImage(back_btnfi_img)

back_img = Image.open("C:/Users/Administrator/Desktop/Main.py/back1.png")
backphoto = ImageTk.PhotoImage(back_img)

back2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/back2.png")
back2photo = ImageTk.PhotoImage(back2_img)

next_img = Image.open("C:/Users/Administrator/Desktop/Main.py/next1.png")
nextphoto = ImageTk.PhotoImage(next_img)

next2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/next2.png")
next2photo = ImageTk.PhotoImage(next2_img)

Br_img = Image.open("C:/Users/Administrator/Desktop/Main.py/BRAUN.png")
Brphoto = ImageTk.PhotoImage(Br_img)

Br2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/BRAUN (1).png")
Br2photo = ImageTk.PhotoImage(Br2_img)

cp_img = Image.open("C:/Users/Administrator/Desktop/Main.py/CPI (3).png")
cpphoto = ImageTk.PhotoImage(cp_img)

cp2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/CPI (1) (1).png")
cp2photo = ImageTk.PhotoImage(cp2_img)

clbr_img = Image.open("C:/Users/Administrator/Desktop/Main.py/Clbr.png")
clbrphoto = ImageTk.PhotoImage(clbr_img)

clbr2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/Clbr1.png")
clbr2photo = ImageTk.PhotoImage(clbr2_img)

jax_img = Image.open("C:/Users/Administrator/Desktop/Main.py/jax.png")
jaxphoto = ImageTk.PhotoImage(jax_img)
jax2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/jax2.png")
jax2photo = ImageTk.PhotoImage(jax2_img)

qst_img = Image.open("C:/Users/Administrator/Desktop/Main.py/qst (1).png")
qstphoto = ImageTk.PhotoImage(qst_img)
qst2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/qst2 (1).png")
qst2photo = ImageTk.PhotoImage(qst2_img)

sbr_img = Image.open("C:/Users/Administrator/Desktop/Main.py/sbr.png")
sbrphoto = ImageTk.PhotoImage(sbr_img)
sbr2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/sbr2.png")
sbr2photo = ImageTk.PhotoImage(sbr2_img)

usp_img = Image.open("C:/Users/Administrator/Desktop/Main.py/usp.png")
uspphoto = ImageTk.PhotoImage(usp_img)
usp2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/usp2.png")
usp2photo = ImageTk.PhotoImage(usp2_img)

bell_img = Image.open("C:/Users/Administrator/Desktop/Main.py/bell.png")
bellphoto = ImageTk.PhotoImage(bell_img)
bell2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/bell2.png")
bell2photo = ImageTk.PhotoImage(bell2_img)

vera_img = Image.open("C:/Users/Administrator/Desktop/Main.py/vera.png")
veraphoto = ImageTk.PhotoImage(vera_img)
vera2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/vera2.png")
vera2photo = ImageTk.PhotoImage(vera2_img)

afk_img = Image.open("C:/Users/Administrator/Desktop/Main.py/afk.png")
afkphoto = ImageTk.PhotoImage(afk_img)
afk2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/afk2.png")
afk2photo = ImageTk.PhotoImage(afk2_img)

misc_img = Image.open("C:/Users/Administrator/Desktop/Main.py/misc.png")
miscphoto = ImageTk.PhotoImage(misc_img)
misc2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/misc2.png")
misc2photo = ImageTk.PhotoImage(misc2_img)

FIPbtn_img = Image.open("C:/Users/Administrator/Desktop/Main.py/FI2.png")
FIPbtn_photo = ImageTk.PhotoImage(FIPbtn_img)
FIPHbtn_img = Image.open("C:/Users/Administrator/Desktop/Main.py/FIH.png")
FIPHbtn_photo = ImageTk.PhotoImage(FIPHbtn_img)

# Main menu btns

Brbtn = tk.Button(gif_mainpg, border=0, borderwidth=0, relief="sunken", image=Brphoto, cursor="hand2", compound="left", command=lambda: show_frame(gif_brpg))
Brbtn.place(relx=0.15, rely=0.17, anchor=CENTER, width=80, height=18)

cpbtn = tk.Button(gif_mainpg, border=0, borderwidth=0, relief="sunken", image=cpphoto, cursor="hand2", compound="left", command=lambda: show_frame(gif_cpipg))
cpbtn.place(relx=0.38, rely=0.17, anchor=CENTER, width=80, height=18)

clbrbtn = tk.Button(gif_mainpg, border=0, borderwidth=0, relief="sunken", image=clbrphoto, cursor="hand2", compound="left", command=lambda: show_frame(clbrpg))
clbrbtn.place(relx=0.615, rely=0.17, anchor=CENTER, width=80, height=18)

jxbtn = tk.Button(gif_mainpg, border=0, borderwidth=0, relief="sunken", image=jaxphoto, cursor="hand2", compound="left", command=lambda: show_frame(jxpg))
jxbtn.place(relx=0.15, rely=0.83, anchor=CENTER, width=80, height=18)

qstbtn = tk.Button(gif_mainpg, border=0, borderwidth=0, relief="sunken", image=qstphoto, cursor="hand2", compound="left", command=lambda: show_frame(qstpg))
qstbtn.place(relx=0.38, rely=0.835, anchor=CENTER, width=80, height=18)

sbrbtn = tk.Button(gif_mainpg, border=0, borderwidth=0, relief="sunken", image=sbrphoto, cursor="hand2", compound="left", command=lambda: show_frame(sbrpg))
sbrbtn.place(relx=0.613, rely=0.829, anchor=CENTER, width=80, height=18)

uspbtn = tk.Button(gif_mainpg, border=0, borderwidth=0, relief="sunken", image=uspphoto, cursor="hand2", compound="left", command=lambda: show_frame(uspg))
uspbtn.place(relx=0.84, rely=0.83, anchor=CENTER, width=80, height=18)

bellbtn = tk.Button(mainpg2, border=0, borderwidth=0, relief="sunken", image=bellphoto, cursor="hand2", compound="left", command=lambda: show_frame(blpg))
bellbtn.place(relx=0.38, rely=0.17, anchor=CENTER, width=80, height=18)

verabtn = tk.Button(mainpg2, border=0, borderwidth=0, relief="sunken", image=veraphoto, cursor="hand2", compound="left", command=lambda: show_frame(vrpg))
verabtn.place(relx=0.615, rely=0.17, anchor=CENTER, width=80, height=18)

Startbtn = tk.Button(intro_pg, border=0, borderwidth=0, relief="sunken", image=Introstrtbtn_photo, cursor="hand2", compound="left", command=lambda: show_frame(gif_mainpg))
Startbtn.place(relx=0.5, rely=0.85, anchor=CENTER, width=80, height=18)

Exitbtn = tk.Button(intro_pg, border=0, borderwidth=0, relief="sunken", image=Introextbtn_photo, cursor="hand2", compound="left", command=close_application)
Exitbtn.place(relx=0.5, rely=0.90, anchor=CENTER, width=80, height=18)

FIPbtn = tk.Button(gif_mainpg, border=0, borderwidth=0, relief="sunken", image=FIPbtn_photo, cursor="hand2", compound="left", command=lambda: show_frame(gif_FIPpg))
FIPbtn.place(relx=0.84, rely=0.17, anchor=CENTER, width=80, height=18)

afkbtn = tk.Button(mainpg2, border=0, borderwidth=0, relief="sunken", image=afkphoto, cursor="hand2", compound="left", command=anti_afk)
afkbtn.place(relx=0.38, rely=0.835, anchor=CENTER, width=80, height=18)

miscbtn = tk.Button(mainpg2, border=0, borderwidth=0, relief="sunken", image=miscphoto, cursor="hand2", compound="left")
miscbtn.place(relx=0.613, rely=0.829, anchor=CENTER, width=90, height=18)

# hover/unhover

def Brbtn_hover(event):
    Brbtn.configure(image=Br2photo)
def cpbtn_hover(event):
    cpbtn.configure(image=cp2photo)
def clbrbtn_hover(event):
    clbrbtn.configure(image=clbr2photo)
def jxbtn_hover(event):
    jxbtn.configure(image=jax2photo)
def qstbtn_hover(event):
    qstbtn.configure(image=qst2photo)
def sbrbtn_hover(event):
    sbrbtn.configure(image=sbr2photo)
def uspbtn_hover(event):
    uspbtn.configure(image=usp2photo)
def bellbtn_hover(event):
    bellbtn.configure(image=bell2photo)
def verabtn_hover(event):
    verabtn.configure(image=vera2photo)
def Startbtn_hover(event):
    Startbtn.configure(image=IntrostrtHbtn_photo)
def afkbtn_hover(event):
    afkbtn.configure(image=afk2photo)
def miscbtn_hover(event):
    miscbtn.configure(image=misc2photo)
def Exitbtn_hover(event):
    Exitbtn.configure(image=IntroextHbtn_photo)
def FIPbtn_hover(event):
    FIPbtn.configure(image=FIPHbtn_photo)


def Brbtn_leave(event):
    Brbtn.configure(image=Brphoto)
def cpbtn_leave(event):
    cpbtn.configure(image=cpphoto)
def clbrbtn_leave(event):
    clbrbtn.configure(image=clbrphoto)
def jxbtn_leave(event):
    jxbtn.configure(image=jaxphoto)
def qstbtn_leave(event):
    qstbtn.configure(image=qstphoto)
def sbrbtn_leave(event):
    sbrbtn.configure(image=sbrphoto)
def uspbtn_leave(event):
    uspbtn.configure(image=uspphoto)
def bellbtn_leave(event):
    bellbtn.configure(image=bellphoto)
def verabtn_leave(event):
    verabtn.configure(image=veraphoto)
def Startbtn_leave(event):
    Startbtn.configure(image=Introstrtbtn_photo)
def afkbtn_leave(event):
    afkbtn.configure(image=afkphoto)
def miscbtn_leave(event):
    miscbtn.configure(image=miscphoto)
def Exitbtn_leave(event):
    Exitbtn.configure(image=Introextbtn_photo)
def FIPbtn_leave(event):
    FIPbtn.configure(image=FIPbtn_photo)

# hover/unhover2

Brbtn.bind("<Enter>", Brbtn_hover)
Brbtn.bind("<Leave>", Brbtn_leave)
cpbtn.bind("<Enter>", cpbtn_hover)
cpbtn.bind("<Leave>", cpbtn_leave)
clbrbtn.bind("<Enter>", clbrbtn_hover)
clbrbtn.bind("<Leave>", clbrbtn_leave)
jxbtn.bind("<Enter>", jxbtn_hover)
jxbtn.bind("<Leave>", jxbtn_leave)
qstbtn.bind("<Enter>", qstbtn_hover)
qstbtn.bind("<Leave>", qstbtn_leave)
sbrbtn.bind("<Enter>", sbrbtn_hover)
sbrbtn.bind("<Leave>", sbrbtn_leave)
uspbtn.bind("<Enter>", uspbtn_hover)
uspbtn.bind("<Leave>", uspbtn_leave)
bellbtn.bind("<Enter>", bellbtn_hover)
bellbtn.bind("<Leave>", bellbtn_leave)
verabtn.bind("<Enter>", verabtn_hover)
verabtn.bind("<Leave>", verabtn_leave)
afkbtn.bind("<Enter>", afkbtn_hover)
afkbtn.bind("<Leave>", afkbtn_leave)
miscbtn.bind("<Enter>", miscbtn_hover)
miscbtn.bind("<Leave>", miscbtn_leave)
Startbtn.bind("<Enter>", Startbtn_hover)
Startbtn.bind("<Leave>", Startbtn_leave)
Exitbtn.bind("<Enter>", Exitbtn_hover)
Exitbtn.bind("<Leave>", Exitbtn_leave)
FIPbtn.bind("<Enter>", FIPbtn_hover)
FIPbtn.bind("<Leave>", FIPbtn_leave)

#backbtn and nxtbtn functions



backbtn1 = tk.Button(gif_mainpg, border=0, borderwidth=0, relief="sunken", image=backphoto, cursor="hand2", compound="left", command=lambda: show_frame(intro_pg))
backbtn1.place(relx=0.14, rely=0.5, anchor=CENTER, width=45, height=40)

nxtbtn = tk.Button(gif_mainpg, border=0, borderwidth=0, relief="sunken", image=nextphoto, cursor="hand2", compound="left", command=lambda: show_frame(mainpg2))
nxtbtn.place(relx=0.84, rely=0.5, anchor=CENTER, width=45, height=40)

backbtnfi = tk.Button(gif_FIPpg, border=0, borderwidth=0, relief="sunken", image=backphoto, cursor="hand2", compound="left", command=lambda: show_frame(gif_mainpg))
backbtnfi.place(relx=0.03, rely=0.05, anchor=CENTER, width=45, height=40)

backbtn2 = tk.Button(mainpg2, border=0, borderwidth=0, relief="sunken", image=backphoto, cursor="hand2", compound="left", command=lambda: show_frame(gif_mainpg))
backbtn2.place(relx=0.14, rely=0.5, anchor=CENTER, width=45, height=40)

backbtncp = tk.Button(gif_cpipg, border=0, borderwidth=0, relief="sunken", image=backphoto, cursor="hand2", compound="left", command=lambda: show_frame(gif_mainpg))
backbtncp.place(relx=0.03, rely=0.05, anchor=CENTER, width=45, height=40)

backbtnbr = tk.Button(gif_brpg, border=0, borderwidth=0, relief="sunken", image=backphoto, cursor="hand2", compound="left", command=lambda: show_frame(gif_mainpg))
backbtnbr.place(relx=0.03, rely=0.05, anchor=CENTER, width=45, height=40)

backbtnclbr = tk.Button(clbrpg, border=0, borderwidth=0, relief="sunken", image=backphoto, cursor="hand2", compound="left", command=lambda: show_frame(gif_mainpg))
backbtnclbr.place(relx=0.03, rely=0.05, anchor=CENTER, width=45, height=40)

backbtnjx = tk.Button(jxpg, border=0, borderwidth=0, relief="sunken", image=backphoto, cursor="hand2", compound="left", command=lambda: show_frame(gif_mainpg))
backbtnjx.place(relx=0.03, rely=0.05, anchor=CENTER, width=45, height=40)

backbtnqst = tk.Button(qstpg, border=0, borderwidth=0, relief="sunken", image=backphoto, cursor="hand2", compound="left", command=lambda: show_frame(gif_mainpg))
backbtnqst.place(relx=0.03, rely=0.05, anchor=CENTER, width=45, height=40)

backbtnsbr = tk.Button(sbrpg, border=0, borderwidth=0, relief="sunken", image=backphoto, cursor="hand2", compound="left", command=lambda: show_frame(gif_mainpg))
backbtnsbr.place(relx=0.03, rely=0.05, anchor=CENTER, width=45, height=40)

backbtnus = tk.Button(uspg, border=0, borderwidth=0, relief="sunken", image=backphoto, cursor="hand2", compound="left", command=lambda: show_frame(gif_mainpg))
backbtnus.place(relx=0.03, rely=0.05, anchor=CENTER, width=45, height=40)

backbtnbl = tk.Button(blpg, border=0, borderwidth=0, relief="sunken", image=backphoto, cursor="hand2", compound="left", command=lambda: show_frame(mainpg2))
backbtnbl.place(relx=0.03, rely=0.05, anchor=CENTER, width=45, height=40)

backbtnvr = tk.Button(vrpg, border=0, borderwidth=0, relief="sunken", image=backphoto, cursor="hand2", compound="left", command=lambda: show_frame(mainpg2))
backbtnvr.place(relx=0.03, rely=0.05, anchor=CENTER, width=45, height=40)
def backbtn_hover(event):
    backbtn1.configure(image=back2photo)
    backbtnfi.configure(image=back2photo)
    backbtn2.configure(image=back2photo)
    backbtncp.configure(image=back2photo)
    backbtnbr.configure(image=back2photo)
    backbtnclbr.configure(image=back2photo)
    backbtnjx.configure(image=back2photo)
    backbtnqst.configure(image=back2photo)
    backbtnsbr.configure(image=back2photo)
    backbtnus.configure(image=back2photo)
    backbtnbl.configure(image=back2photo)
    backbtnvr.configure(image=back2photo)


def backbtn_leave(event):
    backbtn1.configure(image=backphoto)
    backbtnfi.configure(image=backphoto)
    backbtn2.configure(image=backphoto)
    backbtncp.configure(image=backphoto)
    backbtnbr.configure(image=backphoto)
    backbtnclbr.configure(image=backphoto)
    backbtnjx.configure(image=backphoto)
    backbtnqst.configure(image=backphoto)
    backbtnsbr.configure(image=backphoto)
    backbtnus.configure(image=backphoto)
    backbtnbl.configure(image=backphoto)
    backbtnvr.configure(image=backphoto)


backbtn1.bind("<Enter>", backbtn_hover)
backbtn1.bind("<Leave>", backbtn_leave)
backbtnfi.bind("<Enter>", backbtn_hover)
backbtnfi.bind("<Leave>", backbtn_leave)
backbtn2.bind("<Enter>", backbtn_hover)
backbtn2.bind("<Leave>", backbtn_leave)
backbtncp.bind("<Enter>", backbtn_hover)
backbtncp.bind("<Leave>", backbtn_leave)
backbtnbr.bind("<Enter>", backbtn_hover)
backbtnbr.bind("<Leave>", backbtn_leave)
backbtnclbr.bind("<Enter>", backbtn_hover)
backbtnclbr.bind("<Leave>", backbtn_leave)
backbtnjx.bind("<Enter>", backbtn_hover)
backbtnjx.bind("<Leave>", backbtn_leave)
backbtnqst.bind("<Enter>", backbtn_hover)
backbtnqst.bind("<Leave>", backbtn_leave)
backbtnsbr.bind("<Enter>", backbtn_hover)
backbtnsbr.bind("<Leave>", backbtn_leave)
backbtnus.bind("<Enter>", backbtn_hover)
backbtnus.bind("<Leave>", backbtn_leave)
backbtnbl.bind("<Enter>", backbtn_hover)
backbtnbl.bind("<Leave>", backbtn_leave)
backbtnvr.bind("<Enter>", backbtn_hover)
backbtnvr.bind("<Leave>", backbtn_leave)


def nxtbtn_hover(event):
    nxtbtn.configure(image=next2photo)


def nxtbtn_leave(event):
    nxtbtn.configure(image=nextphoto)

nxtbtn.bind("<Enter>", nxtbtn_hover)
nxtbtn.bind("<Leave>", nxtbtn_leave)



# Client buttons

# BRImages221

grbr1_img = Image.open("C:/Users/Administrator/Desktop/Main.py/gr1.png")
grbr1photo = ImageTk.PhotoImage(grbr1_img)

grbr2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/gr2.png")
grbr2photo = ImageTk.PhotoImage(grbr2_img)

clbr1_img = Image.open("C:/Users/Administrator/Desktop/Main.py/cl1.png")
clbr1photo = ImageTk.PhotoImage(clbr1_img)

clsbr2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/cl2.png")
clsbr2photo = ImageTk.PhotoImage(clsbr2_img)

cbbr1_img = Image.open("C:/Users/Administrator/Desktop/Main.py/cb1.png")
cbbr1photo = ImageTk.PhotoImage(cbbr1_img)

cbbr2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/cb2.png")
cbbr2photo = ImageTk.PhotoImage(cbbr2_img)

tsbr1_img = Image.open("C:/Users/Administrator/Desktop/Main.py/ts1.png")
tsbr1photo = ImageTk.PhotoImage(tsbr1_img)

tsbr2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/ts2.png")
tsbr2photo = ImageTk.PhotoImage(tsbr2_img)

snbr1_img = Image.open("C:/Users/Administrator/Desktop/Main.py/sn1.png")
snbr1photo = ImageTk.PhotoImage(snbr1_img)

snbr2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/sn2.png")
snbr2photo = ImageTk.PhotoImage(snbr2_img)

apbr1_img = Image.open("C:/Users/Administrator/Desktop/Main.py/ap1.png")
apbr1photo = ImageTk.PhotoImage(apbr1_img)

apbr2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/ap2.png")
apbr2photo = ImageTk.PhotoImage(apbr2_img)

mirbr1_img = Image.open("C:/Users/Administrator/Desktop/Main.py/mir1.png")
mirbr1photo = ImageTk.PhotoImage(mirbr1_img)

mirbr2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/mir2.png")
mirbr2photo = ImageTk.PhotoImage(mirbr2_img)

inbr1_img = Image.open("C:/Users/Administrator/Desktop/Main.py/gi1.png")
inbr1photo = ImageTk.PhotoImage(inbr1_img)

inbr2_img = Image.open("C:/Users/Administrator/Desktop/Main.py/gi2.png")
inbr2photo = ImageTk.PhotoImage(inbr2_img)

# BRButtons221


grbr1btn = tk.Button(gif_brpg, border=0, borderwidth=0, relief="sunken", image=grbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hi, Thank you for re"
   "aching out!\r\n\r\n"
   "This is Hazrat with "
   "Braunability IT Serv"
   "ice Desk. In order t"
   "o be of more assista"
   "nce, could you kindl"
   "y provide me with yo"
   "ur first name, last "
   "name, and preferred "
   "phone number?")])
grbr1btn.place(relx=0.152, rely=0.307, anchor=CENTER, width=80, height=18)

clbr1btn = tk.Button(gif_brpg, border=0, borderwidth=0, relief="sunken", image=clbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("BraunAbility IT Serv"
   "ice Desk appreciates"
   " your communication."
   " If I have addressed"
   " your needs, please "
   "enjoy the rest of yo"
   "ur day. You may rece"
   "ive a survey regardi"
   "ng this interaction."
   " I welcome your feed"
   "back. The ticket num"
   "ber is [ticket] if y"
   "ou need to follow up"
   ".\r\n\r\n"
   "Bye 😄")])
clbr1btn.place(relx=0.832, rely=0.307, anchor=CENTER, width=80, height=18)

cbbr1btn = tk.Button(gif_brpg, border=0, borderwidth=0, relief="sunken", image=cbbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "BraunAbility IT Serv"
   "ice Desk reaching ou"
   "t in regards to tick"
   "et number [ticket], "
   "referencing [issue]."
   " Unfortunately, we w"
   "ere unable to reach "
   "you via phone or ema"
   "il. Please call us b"
   "ack or start a chat "
   "at your earliest con"
   "venience so we may f"
   "urther assist you wi"
   "th resolving this is"
   "sue.\r\n\r\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n\r\n"
   "If you need assistan"
   "ce, we are here to h"
   "elp 24x7!\r\n\r\n"
   "By Phone Toll Free: "
   "866-714-3754 or Loca"
   "l Dial Number: 574-9"
   "46-4139 extension 43"
   "57\r\n\r\n"
   "By Portal: https://b"
   "raunprod.service-now"
   ".com/sp")])
cbbr1btn.place(relx=0.152, rely=0.57, anchor=CENTER, width=80, height=18)

tsbr1btn = tk.Button(gif_brpg, border=0, borderwidth=0, relief="sunken", image=tsbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "BraunAbility IT Serv"
   "ice Desk, contacting"
   " you regarding ticke"
   "t number [ticket] re"
   "ferencing [issue]. U"
   "nfortunately, after "
   "three attempts to re"
   "ach you via phone an"
   "d email, we have bee"
   "n unable to obtain a"
   " response. As a resu"
   "lt, we will need to "
   "close this ticket fo"
   "r the time being. Ho"
   "wever, if the proble"
   "m is still ongoing, "
   "please do not hesita"
   "te to get back in to"
   "uch so we can reopen"
   " the ticket and cont"
   "inue working to reso"
   "lve this matter. Our"
   " team is happy to as"
   "sist. We appreciate "
   "your patience and un"
   "derstanding.\r\n\r\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n\r\n"
   "If you need assistan"
   "ce, we are here to h"
   "elp 24x7!\r\n\r\n"
   "By Phone Toll Free: "
   "866-714-3754 or Loca"
   "l Dial Number: 574-9"
   "46-4139 extension 43"
   "57\r\n\r\n"
   "By Portal: https://b"
   "raunprod.service-now"
   ".com/sp﻿")])
tsbr1btn.place(relx=0.839, rely=0.57, anchor=CENTER, width=99, height=18)

snbr1btn = tk.Button(gif_brpg, border=0, borderwidth=0, relief="sunken", image=snbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Best Regards,\r\n"
   "Hazrat A.\r\n\r\n"
   "If you need assistan"
   "ce, we are here to h"
   "elp 24x7!\r\n\r\n"
   "By Phone Toll Free: "
   "866-714-3754 or Loca"
   "l Dial Number: 574-9"
   "46-4139 extension 43"
   "57\r\n\r\n"
   "By Portal: https://b"
   "raunprod.service-now"
   ".com/sp")])
snbr1btn.place(relx=0.152, rely=0.832, anchor=CENTER, width=83, height=18)

apbr1btn = tk.Button(gif_brpg, border=0, borderwidth=0, relief="sunken", image=apbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "BraunAbility IT Serv"
   "ice Desk reaching ou"
   "t in regards to tick"
   "et number [ticket], "
   "referencing [issue]."
   " [EU] has requested "
   "to have their passwo"
   "rd reset. If you app"
   "rove of this request"
   ", please reply to th"
   "is email with your a"
   "pproval.\r\n\r\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n\r\n"
   "If you need assistan"
   "ce, we are here to h"
   "elp 24x7!\r\n\r\n"
   "By Phone Toll Free: "
   "866-714-3754 or Loca"
   "l Dial Number: 574-9"
   "46-4139 extension 43"
   "57\r\n\r\n"
   "By Portal: https://b"
   "raunprod.service-now"
   ".com/sp﻿")])
apbr1btn.place(relx=0.384, rely=0.832, anchor=CENTER, width=80, height=18)

mirbr1btn = tk.Button(gif_brpg, border=0, borderwidth=0, relief="sunken", image=mirbr1photo, cursor="hand2",
                      compound="left", command=lambda: [webbrowser.open('https://braunprod.service-now.com/sp?sys_kb_id=b8ff86b0939375106c8dfb686cba1083&id=kb_article_view&sysparm_rank=2&sysparm_tsqueryId=53628e7d97abf910b503fbee2153af73'), copy_clip("Clarify what the con"
   "cern is from the per"
   "son reporting the pr"
   "oblem. Is this an ap"
   "plication, network, "
   "or access issue?\r\n"
   " \r\n"
   "Application:\r\n"
   " \r\n"
   "What is the applicat"
   "ion name?\r\n"
   " \r\n"
   "What is the applicat"
   "ion error?\r\n"
   " \r\n"
   " \r\n"
   "Network:\r\n"
   " \r\n"
   "What is the network "
   "type: Internet or Lo"
   "cal?\r\n"
   " \r\n"
   "What is the site loc"
   "ation?\r\n"
   " \r\n"
   "How many users affec"
   "ted?\r\n"
   " \r\n"
   "Access:\r\n"
   " \r\n"
   "Is it an external or"
   " VPN power outage?\r"
   "\n"
   " \r\n"
   "Is it a location pow"
   "er outage?\r\n"
   " \r\n"
   "Is this a phone syst"
   "em outage?")])
mirbr1btn.place(relx=0.61, rely=0.832, anchor=CENTER, width=80, height=18)

inbr1btn = tk.Button(gif_brpg, border=0, borderwidth=0, relief="sunken", image=inbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("EUs name:\r\n"
   "CB #:\r\n"
   "Asset tag:\r\n"
   "Issue:\r\n"
   "Error/ss:\r\n"
   "Location(Optional):"
   "\r\n\r\n"
   "TS:\r\n")])
inbr1btn.place(relx=0.839, rely=0.832, anchor=CENTER, width=99, height=18)


# BRdefine


def grbr1btn_hover(event):
    grbr1btn.configure(image=grbr2photo)


def grbr1btn_leave(event):
    grbr1btn.configure(image=grbr1photo)


def clbr1btn_hover(event):
    clbr1btn.configure(image=clsbr2photo)


def clbr1btn_leave(event):
    clbr1btn.configure(image=clbr1photo)


def cbbr1btn_hover(event):
    cbbr1btn.configure(image=cbbr2photo)


def cbbr1btn_leave(event):
    cbbr1btn.configure(image=cbbr1photo)


def tsbr1btn_hover(event):
    tsbr1btn.configure(image=tsbr2photo)


def tsbr1btn_leave(event):
    tsbr1btn.configure(image=tsbr1photo)


def snbr1btn_hover(event):
    snbr1btn.configure(image=snbr2photo)


def snbr1btn_leave(event):
    snbr1btn.configure(image=snbr1photo)


def apbr1btn_hover(event):
    apbr1btn.configure(image=apbr2photo)


def apbr1btn_leave(event):
    apbr1btn.configure(image=apbr1photo)


def mirbr1btn_hover(event):
    mirbr1btn.configure(image=mirbr2photo)


def mirbr1btn_leave(event):
    mirbr1btn.configure(image=mirbr1photo)


def inbr1btn_hover(event):
    inbr1btn.configure(image=inbr2photo)


def inbr1btn_leave(event):
    inbr1btn.configure(image=inbr1photo)


grbr1btn.bind("<Enter>", grbr1btn_hover)
grbr1btn.bind("<Leave>", grbr1btn_leave)
clbr1btn.bind("<Enter>", clbr1btn_hover)
clbr1btn.bind("<Leave>", clbr1btn_leave)
cbbr1btn.bind("<Enter>", cbbr1btn_hover)
cbbr1btn.bind("<Leave>", cbbr1btn_leave)
tsbr1btn.bind("<Enter>", tsbr1btn_hover)
tsbr1btn.bind("<Leave>", tsbr1btn_leave)
snbr1btn.bind("<Enter>", snbr1btn_hover)
snbr1btn.bind("<Leave>", snbr1btn_leave)
apbr1btn.bind("<Enter>", apbr1btn_hover)
apbr1btn.bind("<Leave>", apbr1btn_leave)
mirbr1btn.bind("<Enter>", mirbr1btn_hover)
mirbr1btn.bind("<Leave>", mirbr1btn_leave)
inbr1btn.bind("<Enter>", inbr1btn_hover)
inbr1btn.bind("<Leave>", inbr1btn_leave)


#CPI buttons221

grcp1btn = tk.Button(gif_cpipg, border=0, borderwidth=0, relief="sunken", image=grbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hi, Thank you for re"
   "aching out!\r\n\r\n"
   "This is Hazrat with "
   "CPI IT Service Desk."
   " In order to be of m"
   "ore assistance, coul"
   "d you kindly provide"
   " me with your first "
   "name, last name, and"
   " preferred phone num"
   "ber?")])
grcp1btn.place(relx=0.152, rely=0.307, anchor=CENTER, width=80, height=18)

clcp1btn = tk.Button(gif_cpipg, border=0, borderwidth=0, relief="sunken", image=clbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("CPI IT Service Desk "
   "appreciates your com"
   "munication. If I hav"
   "e addressed your nee"
   "ds, please enjoy the"
   " rest of your day. Y"
   "ou may receive a sur"
   "vey regarding this i"
   "nteraction. I welcom"
   "e your feedback. The"
   " ticket number is [t"
   "icket] if you need t"
   "o follow up.\r\n\r\n"
   "Bye 😄")])
clcp1btn.place(relx=0.832, rely=0.307, anchor=CENTER, width=80, height=18)

cbcp1btn = tk.Button(gif_cpipg, border=0, borderwidth=0, relief="sunken", image=cbbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "CPI IT Service Desk "
   "reaching out in rega"
   "rds to ticket number"
   " [ticket], referenci"
   "ng [issue]. Unfortun"
   "ately, we were unabl"
   "e to reach you via p"
   "hone or email. Pleas"
   "e call us back or st"
   "art a chat at your e"
   "arliest convenience "
   "so we may further as"
   "sist you with resolv"
   "ing this issue.\r\n"
   "\r\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n"
   "CPI Service Desk\r\n"
   "\r\n"
   "We are available to "
   "assist you 24x7 and "
   "can be reached throu"
   "gh any of the follow"
   "ing methods:\r\n\r\n"
   "Toll-free: (866) 714"
   "-3753.\r\n\r\n"
   "Self-service Portal:"
   " https://cpiiprod.se"
   "rvicenowservices.com"
   "/\r\n\r\n"
   "Chat URL: http://cpi"
   ".belltechlogix.com\r"
   "\n\r\n"
   "Email: cpi.helpdesk@"
   "cpii.com﻿")])
cbcp1btn.place(relx=0.152, rely=0.57, anchor=CENTER, width=80, height=18)

tscp1btn = tk.Button(gif_cpipg, border=0, borderwidth=0, relief="sunken", image=tsbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "CPI IT Service Desk,"
   " contacting you rega"
   "rding ticket number "
   "[ticket] referencing"
   " [issue]. Unfortunat"
   "ely, after three att"
   "empts to reach you v"
   "ia phone and email, "
   "we have been unable "
   "to obtain a response"
   ". As a result, we wi"
   "ll need to close thi"
   "s ticket for the tim"
   "e being. However, if"
   " the problem is stil"
   "l ongoing, please do"
   " not hesitate to get"
   " back in touch so we"
   " can reopen the tick"
   "et and continue work"
   "ing to resolve this "
   "matter. Our team is "
   "happy to assist. We "
   "appreciate your pati"
   "ence and understandi"
   "ng.\r\n\r\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n"
   "CPI Service Desk\r\n"
   "\r\n"
   "We are available to "
   "assist you 24x7 and "
   "can be reached throu"
   "gh any of the follow"
   "ing methods:\r\n\r\n"
   "Toll-free: (866) 714"
   "-3753.\r\n\r\n"
   "Self-service Portal:"
   " https://cpiiprod.se"
   "rvicenowservices.com"
   "/\r\n\r\n"
   "Chat URL: http://cpi"
   ".belltechlogix.com\r"
   "\n\r\n"
   "Email: cpi.helpdesk@"
   "cpii.com﻿")])
tscp1btn.place(relx=0.839, rely=0.57, anchor=CENTER, width=99, height=18)

sncp1btn = tk.Button(gif_cpipg, border=0, borderwidth=0, relief="sunken", image=snbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Best regards,\r\n"
   "Hazrat A.\r\n"
   "CPI Service Desk\r\n"
   "\r\n"
   "We are here to servi"
   "ce you 24x7! If you "
   "need help, we can be"
   " reached in any of t"
   "he following ways:\r"
   "\n\r\n"
   "Toll free at (866)71"
   "4-3753\r\n\r\n"
   "Self-service Portal:"
   " https://cpiiprod.se"
   "rvicenowservices.com"
   "/\r\n\r\n"
   "Chat URL: http://cpi"
   ".belltechlogix.com\r"
   "\n\r\n"
   "Email: cpi.helpdesk@"
   "cpii.com")])
sncp1btn.place(relx=0.152, rely=0.832, anchor=CENTER, width=83, height=18)

apcp1btn = tk.Button(gif_cpipg, border=0, borderwidth=0, relief="sunken", image=apbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "CPI IT Service Desk "
   "reaching out in rega"
   "rds to ticket number"
   " [ticket], referenci"
   "ng [issue]. [EU] has"
   " requested to have t"
   "heir password reset."
   " If you approve of t"
   "his request, please "
   "reply to this email "
   "with your approval."
   "\r\n\r\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n"
   "CPI Service Desk\r\n"
   "\r\n"
   "We are here to servi"
   "ce you 24x7! If you "
   "need help, we can be"
   " reached in any of t"
   "he following ways:\r"
   "\n\r\n"
   "Toll free at (866)71"
   "4-3753\r\n\r\n"
   "Self-service Portal:"
   " https://cpiiprod.se"
   "rvicenowservices.com"
   "/\r\n\r\n"
   "Chat URL: http://cpi"
   ".belltechlogix.com\r"
   "\n\r\n"
   "Email: cpi.helpdesk@"
   "cpii.com﻿")])
apcp1btn.place(relx=0.384, rely=0.832, anchor=CENTER, width=80, height=18)

mircp1btn = tk.Button(gif_cpipg, border=0, borderwidth=0, relief="sunken", image=mirbr1photo, cursor="hand2",
                      compound="left", command=lambda: [webbrowser.open('https://cpiiprod.servicenowservices.com/kb_view.do?sys_kb_id=f300687b87363510b45562c60cbb3565&sysparm_rank=1&sysparm_tsqueryId=ba030ab587233950323c0e950cbb3503'), copy_clip("The Name of the Appl"
   "ication:\r\n"
   "Number of users impa"
   "cted:\r\n"
   "User\'s ID(s) - LAN "
   "ID / Application Spe"
   "cific ID (please lis"
   "t all impacted):\r\n"
   "Explanation of issue"
   ", including impact:"
   "\r\n"
   "Process/function use"
   "r is performing:\r\n"
   "Error Message, if ap"
   "plicable:\r\n"
   "Are any co-workers e"
   "xperiencing the same"
   " issues, if so how m"
   "any are impacted?\r"
   "\n"
   "When was the last ti"
   "me this worked prope"
   "rly?")])
mircp1btn.place(relx=0.61, rely=0.832, anchor=CENTER, width=80, height=18)

incp1btn = tk.Button(gif_cpipg, border=0, borderwidth=0, relief="sunken", image=inbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("The Name of the Appl"
   "ication:\r\n"
   "Number of users impa"
   "cted:\r\n"
   "User\'s ID(s) - LAN "
   "ID / Application Spe"
   "cific ID (please lis"
   "t all impacted):\r\n"
   "Explanation of issue"
   ", including impact:"
   "\r\n"
   "Process/function use"
   "r is performing:\r\n"
   "Error Message, if ap"
   "plicable:\r\n"
   "Are any co-workers e"
   "xperiencing the same"
   " issues, if so how m"
   "any are impacted?\r"
   "\n"
   "When was the last ti"
   "me this worked prope"
   "rly?")])
incp1btn.place(relx=0.839, rely=0.832, anchor=CENTER, width=99, height=18)


# CPIdefine


def grcp1btn_hover(event):
    grcp1btn.configure(image=grbr2photo)


def grcp1btn_leave(event):
    grcp1btn.configure(image=grbr1photo)


def clcp1btn_hover(event):
    clcp1btn.configure(image=clsbr2photo)


def clcp1btn_leave(event):
    clcp1btn.configure(image=clbr1photo)


def cbcp1btn_hover(event):
    cbcp1btn.configure(image=cbbr2photo)


def cbcp1btn_leave(event):
    cbcp1btn.configure(image=cbbr1photo)


def tscp1btn_hover(event):
    tscp1btn.configure(image=tsbr2photo)


def tscp1btn_leave(event):
    tscp1btn.configure(image=tsbr1photo)


def sncp1btn_hover(event):
    sncp1btn.configure(image=snbr2photo)


def sncp1btn_leave(event):
    sncp1btn.configure(image=snbr1photo)


def apcp1btn_hover(event):
    apcp1btn.configure(image=apbr2photo)


def apcp1btn_leave(event):
    apcp1btn.configure(image=apbr1photo)


def mircp1btn_hover(event):
    mircp1btn.configure(image=mirbr2photo)


def mircp1btn_leave(event):
    mircp1btn.configure(image=mirbr1photo)


def incp1btn_hover(event):
    incp1btn.configure(image=inbr2photo)


def incp1btn_leave(event):
    incp1btn.configure(image=inbr1photo)


grcp1btn.bind("<Enter>", grcp1btn_hover)
grcp1btn.bind("<Leave>", grcp1btn_leave)
clcp1btn.bind("<Enter>", clcp1btn_hover)
clcp1btn.bind("<Leave>", clcp1btn_leave)
cbcp1btn.bind("<Enter>", cbcp1btn_hover)
cbcp1btn.bind("<Leave>", cbcp1btn_leave)
tscp1btn.bind("<Enter>", tscp1btn_hover)
tscp1btn.bind("<Leave>", tscp1btn_leave)
sncp1btn.bind("<Enter>", sncp1btn_hover)
sncp1btn.bind("<Leave>", sncp1btn_leave)
apcp1btn.bind("<Enter>", apcp1btn_hover)
apcp1btn.bind("<Leave>", apcp1btn_leave)
mircp1btn.bind("<Enter>", mircp1btn_hover)
mircp1btn.bind("<Leave>", mircp1btn_leave)
incp1btn.bind("<Enter>", incp1btn_hover)
incp1btn.bind("<Leave>", incp1btn_leave)


#clbri buttons221

grclbri1btn = tk.Button(clbrpg, border=0, borderwidth=0, relief="sunken", image=grbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hi, Thank you for re"
   "aching out!\r\n\r\n"
   "This is Hazrat with "
   "OneColibri IT Servic"
   "e Desk. In order to "
   "be of more assistanc"
   "e, could you kindly "
   "provide me with your"
   " first name, last na"
   "me, and preferred ph"
   "one number?")])
grclbri1btn.place(relx=0.152, rely=0.307, anchor=CENTER, width=80, height=18)

clclbri1btn = tk.Button(clbrpg, border=0, borderwidth=0, relief="sunken", image=clbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("OneColibri IT Servic"
   "e Desk appreciates y"
   "our communication. I"
   "f I have addressed y"
   "our needs, please en"
   "joy the rest of your"
   " day. You may receiv"
   "e a survey regarding"
   " this interaction. I"
   " welcome your feedba"
   "ck. The ticket numbe"
   "r is [ticket] if you"
   " need to follow up."
   "\r\n\r\n"
   "Bye 😄")])
clclbri1btn.place(relx=0.832, rely=0.307, anchor=CENTER, width=80, height=18)

cbclbri1btn = tk.Button(clbrpg, border=0, borderwidth=0, relief="sunken", image=cbbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "OneColibri IT Servic"
   "e Desk reaching out "
   "in regards to ticket"
   " number [ticket], re"
   "ferencing [issue]. U"
   "nfortunately, we wer"
   "e unable to reach yo"
   "u via phone or email"
   ". Please call us bac"
   "k or start a chat at"
   " your earliest conve"
   "nience so we may fur"
   "ther assist you with"
   " resolving this issu"
   "e.\r\n\r\n"
   "Best regards,\r\n"
   "Hazrat A. | OneColib"
   "ri IT Service Desk A"
   "gent\r\n\r\n"
   "Service Desk Phone: "
   "817-659-2470\r\n\r\n"
   "Service Desk Chat: h"
   "ttps://sdchat.colibr"
   "igroup.com\r\n\r\n"
   "Self-Service Portal:"
   " https://sd.colibrig"
   "roup.com﻿")])
cbclbri1btn.place(relx=0.152, rely=0.57, anchor=CENTER, width=80, height=18)

tsclbri1btn = tk.Button(clbrpg, border=0, borderwidth=0, relief="sunken", image=tsbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "OneColibri IT Servic"
   "e Desk, contacting y"
   "ou regarding ticket "
   "number [ticket] refe"
   "rencing [issue]. Unf"
   "ortunately, after th"
   "ree attempts to reac"
   "h you via phone and "
   "email, we have been "
   "unable to obtain a r"
   "esponse. As a result"
   ", we will need to cl"
   "ose this ticket for "
   "the time being. Howe"
   "ver, if the problem "
   "is still ongoing, pl"
   "ease do not hesitate"
   " to get back in touc"
   "h so we can reopen t"
   "he ticket and contin"
   "ue working to resolv"
   "e this matter. Our t"
   "eam is happy to assi"
   "st. We appreciate yo"
   "ur patience and unde"
   "rstanding.\r\n\r\n"
   "Best regards,\r\n"
   "Hazrat A. | OneColib"
   "ri IT Service Desk A"
   "gent\r\n\r\n"
   "Service Desk Phone: "
   "817-659-2470\r\n\r\n"
   "Service Desk Chat: h"
   "ttps://sdchat.colibr"
   "igroup.com\r\n\r\n"
   "Self-Service Portal:"
   " https://sd.colibrig"
   "roup.com﻿")])
tsclbri1btn.place(relx=0.839, rely=0.57, anchor=CENTER, width=99, height=18)

snclbri1btn = tk.Button(clbrpg, border=0, borderwidth=0, relief="sunken", image=snbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Best regards,\r\n"
   "Hazrat A. | OneColib"
   "ri IT Service Desk A"
   "gent\r\n\r\n"
   "Service Desk Phone: "
   "817-659-2470\r\n\r\n"
   "Service Desk Chat: h"
   "ttps://sdchat.colibr"
   "igroup.com\r\n\r\n"
   "Self-Service Portal:"
   " https://sd.colibrig"
   "roup.com")])
snclbri1btn.place(relx=0.152, rely=0.832, anchor=CENTER, width=83, height=18)

apclbri1btn = tk.Button(clbrpg, border=0, borderwidth=0, relief="sunken", image=apbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "OneColibri IT Servic"
   "e Desk reaching out "
   "in regards to ticket"
   " number [ticket], re"
   "ferencing [issue]. ["
   "EU] has requested to"
   " have their password"
   " reset. If you appro"
   "ve of this request, "
   "please reply to this"
   " email with your app"
   "roval.\r\n\r\n"
   "Best regards,\r\n"
   "Hazrat A.| OneColibr"
   "i IT Service Desk Ag"
   "ent\r\n\r\n"
   "Service Desk Phone: "
   "817-659-2470\r\n\r\n"
   "Service Desk Chat: h"
   "ttps://sdchat.colibr"
   "igroup.com\r\n\r\n"
   "Self-Service Portal:"
   " https://sd.colibrig"
   "roup.com﻿")])
apclbri1btn.place(relx=0.384, rely=0.832, anchor=CENTER, width=80, height=18)

mirclbri1btn = tk.Button(clbrpg, border=0, borderwidth=0, relief="sunken", image=mirbr1photo, cursor="hand2",
                      compound="left", command=lambda: [webbrowser.open('https://btlsolutions.service-now.com/kb_view.do?sys_kb_id=3a3b00d8db212d90d59ea5bb139619a9&sysparm_rank=5&sysparm_tsqueryId=c4934a71db6bfd10d59ea5bb139619a2'), copy_clip("Description of the i"
   "ssue:\r\n"
   "Network, application"
   ", service?\r\n"
   "Name of the applicat"
   "ion or service:\r\n"
   "Error messages, if a"
   "vailable:\r\n"
   "Location affected:\r"
   "\n"
   "How many people are "
   "affected, if known?"
   "\r\n"
   "Is there a suitable "
   "work around?\r\n"
   "Troubleshooting atte"
   "mpted in detail:")])
mirclbri1btn.place(relx=0.61, rely=0.832, anchor=CENTER, width=80, height=18)

inclbri1btn = tk.Button(clbrpg, border=0, borderwidth=0, relief="sunken", image=inbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("EUs name:\r\n"
   "CB #:\r\n"
   "Asset tag:\r\n"
   "Issue:\r\n"
   "Error/ss:\r\n"
   "Location(Optional):"
   "\r\n\r\n"
   "TS:")])
inclbri1btn.place(relx=0.839, rely=0.832, anchor=CENTER, width=99, height=18)


# clbridefine


def grclbri1btn_hover(event):
    grclbri1btn.configure(image=grbr2photo)


def grclbri1btn_leave(event):
    grclbri1btn.configure(image=grbr1photo)


def clclbri1btn_hover(event):
    clclbri1btn.configure(image=clsbr2photo)


def clclbri1btn_leave(event):
    clclbri1btn.configure(image=clbr1photo)


def cbclbri1btn_hover(event):
    cbclbri1btn.configure(image=cbbr2photo)


def cbclbri1btn_leave(event):
    cbclbri1btn.configure(image=cbbr1photo)


def tsclbri1btn_hover(event):
    tsclbri1btn.configure(image=tsbr2photo)


def tsclbri1btn_leave(event):
    tsclbri1btn.configure(image=tsbr1photo)


def snclbri1btn_hover(event):
    snclbri1btn.configure(image=snbr2photo)


def snclbri1btn_leave(event):
    snclbri1btn.configure(image=snbr1photo)


def apclbri1btn_hover(event):
    apclbri1btn.configure(image=apbr2photo)


def apclbri1btn_leave(event):
    apclbri1btn.configure(image=apbr1photo)


def mirclbri1btn_hover(event):
    mirclbri1btn.configure(image=mirbr2photo)


def mirclbri1btn_leave(event):
    mirclbri1btn.configure(image=mirbr1photo)


def inclbri1btn_hover(event):
    inclbri1btn.configure(image=inbr2photo)


def inclbri1btn_leave(event):
    inclbri1btn.configure(image=inbr1photo)


grclbri1btn.bind("<Enter>", grclbri1btn_hover)
grclbri1btn.bind("<Leave>", grclbri1btn_leave)
clclbri1btn.bind("<Enter>", clclbri1btn_hover)
clclbri1btn.bind("<Leave>", clclbri1btn_leave)
cbclbri1btn.bind("<Enter>", cbclbri1btn_hover)
cbclbri1btn.bind("<Leave>", cbclbri1btn_leave)
tsclbri1btn.bind("<Enter>", tsclbri1btn_hover)
tsclbri1btn.bind("<Leave>", tsclbri1btn_leave)
snclbri1btn.bind("<Enter>", snclbri1btn_hover)
snclbri1btn.bind("<Leave>", snclbri1btn_leave)
apclbri1btn.bind("<Enter>", apclbri1btn_hover)
apclbri1btn.bind("<Leave>", apclbri1btn_leave)
mirclbri1btn.bind("<Enter>", mirclbri1btn_hover)
mirclbri1btn.bind("<Leave>", mirclbri1btn_leave)
inclbri1btn.bind("<Enter>", inclbri1btn_hover)
inclbri1btn.bind("<Leave>", inclbri1btn_leave)

#fi buttons221

grfi1btn = tk.Button(gif_FIPpg, border=0, borderwidth=0, relief="sunken", image=grbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hi, Thank you for re"
   "aching out!\r\n\r\n"
   "This is Hazrat with "
   "Flatiron IT Service "
   "Desk. In order to be"
   " of more assistance,"
   " could you kindly pr"
   "ovide me with your f"
   "irst name, last name"
   ", and preferred phon"
   "e number?")])
grfi1btn.place(relx=0.152, rely=0.307, anchor=CENTER, width=80, height=18)

clfi1btn = tk.Button(gif_FIPpg, border=0, borderwidth=0, relief="sunken", image=clbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("FlatIron IT Service "
   "Desk appreciates you"
   "r communication. If "
   "I have addressed you"
   "r needs, please enjo"
   "y the rest of your d"
   "ay. You may receive "
   "a survey regarding t"
   "his interaction. I w"
   "elcome your feedback"
   ". The ticket number "
   "is [ticket] if you n"
   "eed to follow up.\r"
   "\n\r\n"
   "Bye 😄")])
clfi1btn.place(relx=0.832, rely=0.307, anchor=CENTER, width=80, height=18)

cbfi1btn = tk.Button(gif_FIPpg, border=0, borderwidth=0, relief="sunken", image=cbbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "FlatIron IT Service "
   "Desk reaching out in"
   " regards to ticket n"
   "umber [ticket], refe"
   "rencing [issue]. Unf"
   "ortunately, we were "
   "unable to reach you "
   "via phone or email. "
   "Please call us back "
   "or start a chat at y"
   "our earliest conveni"
   "ence so we may furth"
   "er assist you with r"
   "esolving this issue."
   "\r\n\r\n"
   "Flatiron\r\n\r\n"
   "Thank you,\r\n\r\n"
   "Hazrat A.\r\n\r\n"
   "SupportCenter\r\n\r"
   "\n"
   "Flatiron Constructio"
   "n Corp.\r\n\r\n"
   "866 648 8838 PHONE\r"
   "\n\r\n"
   "supportcenter@flatir"
   "oncorp.com \r\n\r\n"
   "https://supportcente"
   "r.flatironcorp.com\r"
   "\n\r\n"
   "Need your password r"
   "eset?\r\n\r\n"
   "You can reset your p"
   "assword at https://a"
   "ccountinfo.flatironc"
   "orp.com.\r\n\r\n"
   "The other option is "
   "to call the Flatiron"
   " Support Center!")])
cbfi1btn.place(relx=0.152, rely=0.57, anchor=CENTER, width=80, height=18)

tsfi1btn = tk.Button(gif_FIPpg, border=0, borderwidth=0, relief="sunken", image=tsbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "FlatIron IT Service "
   "Desk, contacting you"
   " regarding ticket nu"
   "mber [ticket] refere"
   "ncing [issue]. Unfor"
   "tunately, after thre"
   "e attempts to reach "
   "you via phone and em"
   "ail, we have been un"
   "able to obtain a res"
   "ponse. As a result, "
   "we will need to clos"
   "e this ticket for th"
   "e time being. Howeve"
   "r, if the problem is"
   " still ongoing, plea"
   "se do not hesitate t"
   "o get back in touch "
   "so we can reopen the"
   " ticket and continue"
   " working to resolve "
   "this matter. Our tea"
   "m is happy to assist"
   ". We appreciate your"
   " patience and unders"
   "tanding.\r\n\r\n"
   "Flatiron\r\n\r\n"
   "Thank you,\r\n\r\n"
   "Hazrat A.\r\n\r\n"
   "SupportCenter\r\n\r"
   "\n"
   "Flatiron Constructio"
   "n Corp.\r\n\r\n"
   "866 648 8838 PHONE\r"
   "\n\r\n"
   "supportcenter@flatir"
   "oncorp.com \r\n\r\n"
   "https://supportcente"
   "r.flatironcorp.com\r"
   "\n\r\n"
   "Need your password r"
   "eset?\r\n\r\n"
   "You can reset your p"
   "assword at https://a"
   "ccountinfo.flatironc"
   "orp.com.\r\n\r\n"
   "The other option is "
   "to call the Flatiron"
   " Support Center!")])
tsfi1btn.place(relx=0.839, rely=0.57, anchor=CENTER, width=99, height=18)

snfi1btn = tk.Button(gif_FIPpg, border=0, borderwidth=0, relief="sunken", image=snbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Flatiron\r\n\r\n"
   " \r\n\r\n"
   "Thank you,\r\n"
   "Hazrat A.\r\n"
   "SupportCenter\r\n\r"
   "\n"
   "Flatiron Constructio"
   "n Corp \r\n\r\n"
   "866 648 8838 PHONE\r"
   "\n\r\n"
   "supportcenter@flatir"
   "oncorp.com \r\n\r\n"
   "https://supportcente"
   "r.flatironcorp.com\r"
   "\n\r\n"
   "Need your password r"
   "eset?\r\n\r\n"
   "You can reset your p"
   "assword at https://a"
   "ccountinfo.flatironc"
   "orp.com.\r\n\r\n"
   "The other option is "
   "you can call the Fla"
   "tiron SupportCenter!"
   "\r\n")])
snfi1btn.place(relx=0.152, rely=0.832, anchor=CENTER, width=83, height=18)

apfi1btn = tk.Button(gif_FIPpg, border=0, borderwidth=0, relief="sunken", image=apbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "FlatIron IT Service "
   "Desk reaching out in"
   " regards to ticket n"
   "umber [ticket], refe"
   "rencing [issue]. [EU"
   "] has requested to h"
   "ave their password r"
   "eset. If you approve"
   " of this request, pl"
   "ease reply to this e"
   "mail with your appro"
   "val.\r\n\r\n"
   "Flatiron\r\n\r\n"
   "Thank you,\r\n"
   "Hazrat A.\r\n"
   "SupportCenter\r\n\r"
   "\n"
   "Flatiron Constructio"
   "n Corp \r\n\r\n"
   "866 648 8838 PHONE\r"
   "\n\r\n"
   "supportcenter@flatir"
   "oncorp.com \r\n\r\n"
   "https://supportcente"
   "r.flatironcorp.com\r"
   "\n\r\n"
   "Need your password r"
   "eset?\r\n\r\n"
   "You can reset your p"
   "assword at https://a"
   "ccountinfo.flatironc"
   "orp.com.\r\n\r\n"
   "The other option is "
   "you can call the Fla"
   "tiron SupportCenter!")])
apfi1btn.place(relx=0.384, rely=0.832, anchor=CENTER, width=80, height=18)

mirfi1btn = tk.Button(gif_FIPpg, border=0, borderwidth=0, relief="sunken", image=mirbr1photo, cursor="hand2",
                      compound="left", command=lambda: [copy_clip("Employee Name:\r\n"
   "Employee ID (if know"
   "n):\r\n"
   "Assigned Job/Project"
   ":\r\n"
   "Job/Project Address:"
   "\r\n"
   "Call back number:\r"
   "\n"
   "Issue:\r\n"
   "Error/ss:\r\n\r\n"
   "TS:")])
mirfi1btn.place(relx=0.61, rely=0.832, anchor=CENTER, width=80, height=18)

infi1btn = tk.Button(gif_FIPpg, border=0, borderwidth=0, relief="sunken", image=inbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Employee Name:\r\n"
   "Employee ID (if know"
   "n):\r\n"
   "Assigned Job/Project"
   ":\r\n"
   "Job/Project Address:"
   "\r\n"
   "Call back number:\r"
   "\n"
   "Issue:\r\n"
   "Error/ss:\r\n\r\n"
   "TS:")])
infi1btn.place(relx=0.839, rely=0.832, anchor=CENTER, width=99, height=18)


# fidefine


def grfi1btn_hover(event):
    grfi1btn.configure(image=grbr2photo)


def grfi1btn_leave(event):
    grfi1btn.configure(image=grbr1photo)


def clfi1btn_hover(event):
    clfi1btn.configure(image=clsbr2photo)


def clfi1btn_leave(event):
    clfi1btn.configure(image=clbr1photo)


def cbfi1btn_hover(event):
    cbfi1btn.configure(image=cbbr2photo)


def cbfi1btn_leave(event):
    cbfi1btn.configure(image=cbbr1photo)


def tsfi1btn_hover(event):
    tsfi1btn.configure(image=tsbr2photo)


def tsfi1btn_leave(event):
    tsfi1btn.configure(image=tsbr1photo)


def snfi1btn_hover(event):
    snfi1btn.configure(image=snbr2photo)


def snfi1btn_leave(event):
    snfi1btn.configure(image=snbr1photo)


def apfi1btn_hover(event):
    apfi1btn.configure(image=apbr2photo)


def apfi1btn_leave(event):
    apfi1btn.configure(image=apbr1photo)


def mirfi1btn_hover(event):
    mirfi1btn.configure(image=mirbr2photo)


def mirfi1btn_leave(event):
    mirfi1btn.configure(image=mirbr1photo)


def infi1btn_hover(event):
    infi1btn.configure(image=inbr2photo)


def infi1btn_leave(event):
    infi1btn.configure(image=inbr1photo)


grfi1btn.bind("<Enter>", grfi1btn_hover)
grfi1btn.bind("<Leave>", grfi1btn_leave)
clfi1btn.bind("<Enter>", clfi1btn_hover)
clfi1btn.bind("<Leave>", clfi1btn_leave)
cbfi1btn.bind("<Enter>", cbfi1btn_hover)
cbfi1btn.bind("<Leave>", cbfi1btn_leave)
tsfi1btn.bind("<Enter>", tsfi1btn_hover)
tsfi1btn.bind("<Leave>", tsfi1btn_leave)
snfi1btn.bind("<Enter>", snfi1btn_hover)
snfi1btn.bind("<Leave>", snfi1btn_leave)
apfi1btn.bind("<Enter>", apfi1btn_hover)
apfi1btn.bind("<Leave>", apfi1btn_leave)
mirfi1btn.bind("<Enter>", mirfi1btn_hover)
mirfi1btn.bind("<Leave>", mirfi1btn_leave)
infi1btn.bind("<Enter>", infi1btn_hover)
infi1btn.bind("<Leave>", infi1btn_leave)

#jx buttons221

grjx1btn = tk.Button(jxpg, border=0, borderwidth=0, relief="sunken", image=grbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hi, Thank you for re"
   "aching out!\r\n\r\n"
   "This is Hazrat with "
   "JAX IT Service Desk."
   " In order to be of m"
   "ore assistance, coul"
   "d you kindly provide"
   " me with your first "
   "name, last name, and"
   " preferred phone num"
   "ber?")])
grjx1btn.place(relx=0.152, rely=0.307, anchor=CENTER, width=80, height=18)

cljx1btn = tk.Button(jxpg, border=0, borderwidth=0, relief="sunken", image=clbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("JAX IT Service Desk "
   "appreciates your com"
   "munication. If I hav"
   "e addressed your nee"
   "ds, please enjoy the"
   " rest of your day. Y"
   "ou may receive a sur"
   "vey regarding this i"
   "nteraction. I welcom"
   "e your feedback. The"
   " ticket number is [t"
   "icket] if you need t"
   "o follow up.\r\n\r\n"
   "Bye 😄")])
cljx1btn.place(relx=0.832, rely=0.307, anchor=CENTER, width=80, height=18)

cbjx1btn = tk.Button(jxpg, border=0, borderwidth=0, relief="sunken", image=cbbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "JAX IT Service Desk "
   "reaching out in rega"
   "rds to ticket number"
   " [ticket], referenci"
   "ng [issue]. Unfortun"
   "ately, we were unabl"
   "e to reach you via p"
   "hone or email. Pleas"
   "e call us back or st"
   "art a chat at your e"
   "arliest convenience "
   "so we may further as"
   "sist you with resolv"
   "ing this issue.\r\n"
   "\r\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n"
   "JAX IT Service Desk "
   "Agent\r\n\r\n"
   "Phone: 207-288-1414"
   "\r\n\r\n"
   "Service Portal\r\n\r"
   "\n"
   "The Jackson Laborato"
   "ry: Leading the sear"
   "ch for tomorrow\'s c"
   "ures\r\n\r\n"
   "www.jax.org﻿")])
cbjx1btn.place(relx=0.152, rely=0.57, anchor=CENTER, width=80, height=18)

tsjx1btn = tk.Button(jxpg, border=0, borderwidth=0, relief="sunken", image=tsbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "JAX IT Service Desk,"
   " contacting you rega"
   "rding ticket number "
   "[ticket] referencing"
   " [issue]. Unfortunat"
   "ely, after three att"
   "empts to reach you v"
   "ia phone and email, "
   "we have been unable "
   "to obtain a response"
   ". As a result, we wi"
   "ll need to close thi"
   "s ticket for the tim"
   "e being. However, if"
   " the problem is stil"
   "l ongoing, please do"
   " not hesitate to get"
   " back in touch so we"
   " can reopen the tick"
   "et and continue work"
   "ing to resolve this "
   "matter. Our team is "
   "happy to assist. We "
   "appreciate your pati"
   "ence and understandi"
   "ng.\r\n\r\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n"
   "JAX IT Service Desk "
   "Agent\r\n\r\n"
   "Phone: 207-288-1414"
   "\r\n\r\n"
   "Service Portal\r\n\r"
   "\n"
   "The Jackson Laborato"
   "ry: Leading the sear"
   "ch for tomorrow\'s c"
   "ures\r\n\r\n"
   "www.jax.org﻿")])
tsjx1btn.place(relx=0.839, rely=0.57, anchor=CENTER, width=99, height=18)

snjx1btn = tk.Button(jxpg, border=0, borderwidth=0, relief="sunken", image=snbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Best Regards,\r\n"
   "Hazrat A.\r\n\r\n"
   "JAX IT Service Desk "
   "Agent\r\n\r\n"
   "Phone: 207-288-1414"
   "\r\n\r\n"
   "Service Portal\r\n\r"
   "\n"
   "The Jackson Laborato"
   "ry: Leading the sear"
   "ch for tomorrow\'s c"
   "ures\r\n\r\n"
   "www.jax.org")])
snjx1btn.place(relx=0.152, rely=0.832, anchor=CENTER, width=83, height=18)

apjx1btn = tk.Button(jxpg, border=0, borderwidth=0, relief="sunken", image=apbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "JAX IT Service Desk "
   "reaching out in rega"
   "rds to ticket number"
   " [ticket], referenci"
   "ng [issue]. [EU] has"
   " requested to have t"
   "heir password reset."
   " If you approve of t"
   "his request, please "
   "reply to this email "
   "with your approval."
   "\r\n\r\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n"
   "JAX IT Service Desk "
   "Agent\r\n\r\n"
   "Phone: 207-288-1414"
   "\r\n\r\n"
   "Service Portal\r\n\r"
   "\n"
   "The Jackson Laborato"
   "ry: Leading the sear"
   "ch for tomorrow\'s c"
   "ures\r\n\r\n"
   "www.jax.org﻿")])
apjx1btn.place(relx=0.384, rely=0.832, anchor=CENTER, width=80, height=18)

mirjx1btn = tk.Button(jxpg, border=0, borderwidth=0, relief="sunken", image=mirbr1photo, cursor="hand2",
                      compound="left", command=lambda: [copy_clip("EUs name:\r\n"
   "CB #:\r\n"
   "Asset tag:\r\n"
   "Issue:\r\n"
   "Error/ss:\r\n"
   "Location(Optional):"
   "\r\n\r\n"
   "TS:")])
mirjx1btn.place(relx=0.61, rely=0.832, anchor=CENTER, width=80, height=18)

injx1btn = tk.Button(jxpg, border=0, borderwidth=0, relief="sunken", image=inbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("EUs name:\r\n"
   "CB #:\r\n"
   "Asset tag:\r\n"
   "Issue:\r\n"
   "Error/ss:\r\n"
   "Location(Optional):"
   "\r\n\r\n"
   "TS:")])
injx1btn.place(relx=0.839, rely=0.832, anchor=CENTER, width=99, height=18)


# jxdefine


def grjx1btn_hover(event):
    grjx1btn.configure(image=grbr2photo)


def grjx1btn_leave(event):
    grjx1btn.configure(image=grbr1photo)


def cljx1btn_hover(event):
    cljx1btn.configure(image=clsbr2photo)


def cljx1btn_leave(event):
    cljx1btn.configure(image=clbr1photo)


def cbjx1btn_hover(event):
    cbjx1btn.configure(image=cbbr2photo)


def cbjx1btn_leave(event):
    cbjx1btn.configure(image=cbbr1photo)


def tsjx1btn_hover(event):
    tsjx1btn.configure(image=tsbr2photo)


def tsjx1btn_leave(event):
    tsjx1btn.configure(image=tsbr1photo)


def snjx1btn_hover(event):
    snjx1btn.configure(image=snbr2photo)


def snjx1btn_leave(event):
    snjx1btn.configure(image=snbr1photo)


def apjx1btn_hover(event):
    apjx1btn.configure(image=apbr2photo)


def apjx1btn_leave(event):
    apjx1btn.configure(image=apbr1photo)


def mirjx1btn_hover(event):
    mirjx1btn.configure(image=mirbr2photo)


def mirjx1btn_leave(event):
    mirjx1btn.configure(image=mirbr1photo)


def injx1btn_hover(event):
    injx1btn.configure(image=inbr2photo)


def injx1btn_leave(event):
    injx1btn.configure(image=inbr1photo)


grjx1btn.bind("<Enter>", grjx1btn_hover)
grjx1btn.bind("<Leave>", grjx1btn_leave)
cljx1btn.bind("<Enter>", cljx1btn_hover)
cljx1btn.bind("<Leave>", cljx1btn_leave)
cbjx1btn.bind("<Enter>", cbjx1btn_hover)
cbjx1btn.bind("<Leave>", cbjx1btn_leave)
tsjx1btn.bind("<Enter>", tsjx1btn_hover)
tsjx1btn.bind("<Leave>", tsjx1btn_leave)
snjx1btn.bind("<Enter>", snjx1btn_hover)
snjx1btn.bind("<Leave>", snjx1btn_leave)
apjx1btn.bind("<Enter>", apjx1btn_hover)
apjx1btn.bind("<Leave>", apjx1btn_leave)
mirjx1btn.bind("<Enter>", mirjx1btn_hover)
mirjx1btn.bind("<Leave>", mirjx1btn_leave)
injx1btn.bind("<Enter>", injx1btn_hover)
injx1btn.bind("<Leave>", injx1btn_leave)

#qst buttons221

grqst1btn = tk.Button(qstpg, border=0, borderwidth=0, relief="sunken", image=grbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hi, Thank you for re"
   "aching out!\r\n\r\n"
   "This is Hazrat with "
   "Quest IT Service Des"
   "k. In order to be of"
   " more assistance, co"
   "uld you kindly provi"
   "de me with your firs"
   "t name, last name, a"
   "nd preferred phone n"
   "umber?")])
grqst1btn.place(relx=0.152, rely=0.307, anchor=CENTER, width=80, height=18)

clqst1btn = tk.Button(qstpg, border=0, borderwidth=0, relief="sunken", image=clbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Quest IT Service Des"
   "k appreciates your c"
   "ommunication. If I h"
   "ave addressed your n"
   "eeds, please enjoy t"
   "he rest of your day."
   " You may receive a s"
   "urvey regarding this"
   " interaction. I welc"
   "ome your feedback. T"
   "he ticket number is "
   "[ticket] if you need"
   " to follow up.\r\n\r"
   "\n"
   "Bye 😄")])
clqst1btn.place(relx=0.832, rely=0.307, anchor=CENTER, width=80, height=18)

cbqst1btn = tk.Button(qstpg, border=0, borderwidth=0, relief="sunken", image=cbbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "Quest IT Service Des"
   "k reaching out in re"
   "gards to ticket numb"
   "er [ticket], referen"
   "cing [issue]. Unfort"
   "unately, we were una"
   "ble to reach you via"
   " phone or email. Ple"
   "ase call us back or "
   "start a chat at your"
   " earliest convenienc"
   "e so we may further "
   "assist you with reso"
   "lving this issue.\r"
   "\n\r\n\r\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n"
   "Quest Diagnostics")])
cbqst1btn.place(relx=0.152, rely=0.57, anchor=CENTER, width=80, height=18)

tsqst1btn = tk.Button(qstpg, border=0, borderwidth=0, relief="sunken", image=tsbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "Quest IT Service Des"
   "k, contacting you re"
   "garding ticket numbe"
   "r [ticket] referenci"
   "ng [issue]. Unfortun"
   "ately, after three a"
   "ttempts to reach you"
   " via phone and email"
   ", we have been unabl"
   "e to obtain a respon"
   "se. As a result, we "
   "will need to close t"
   "his ticket for the t"
   "ime being. However, "
   "if the problem is st"
   "ill ongoing, please "
   "do not hesitate to g"
   "et back in touch so "
   "we can reopen the ti"
   "cket and continue wo"
   "rking to resolve thi"
   "s matter. Our team i"
   "s happy to assist. W"
   "e appreciate your pa"
   "tience and understan"
   "ding.\r\n\r\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n"
   "Quest Diagnostics")])
tsqst1btn.place(relx=0.839, rely=0.57, anchor=CENTER, width=99, height=18)

snqst1btn = tk.Button(qstpg, border=0, borderwidth=0, relief="sunken", image=snbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Thank you\r\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n"
   "Quest Diagnostics")])
snqst1btn.place(relx=0.152, rely=0.832, anchor=CENTER, width=83, height=18)

apqst1btn = tk.Button(qstpg, border=0, borderwidth=0, relief="sunken", image=apbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "Quest IT Service Des"
   "k reaching out in re"
   "gards to ticket numb"
   "er [ticket], referen"
   "cing [issue]. [EU] h"
   "as requested to have"
   " their password rese"
   "t. If you approve of"
   " this request, pleas"
   "e reply to this emai"
   "l with your approval"
   ".\r\n\r\n"
   "Best regards,\r\n\r"
   "\n"
   "Hazrat A.\r\n"
   "Quest Diagnostics")])
apqst1btn.place(relx=0.384, rely=0.832, anchor=CENTER, width=80, height=18)

mirqst1btn = tk.Button(qstpg, border=0, borderwidth=0, relief="sunken", image=mirbr1photo, cursor="hand2",
                      compound="left", command=lambda: [copy_clip("Name:\r\n"
   "Email:\r\n"
   "Employee ID:\r\n"
   "Callback #:\r\n"
   "Make of Mobile Devic"
   "e:\r\n"
   "Model of Mobile Devi"
   "ce:\r\n"
   "Description of Issue"
   ":\r\n"
   "Location/Site code:")])
mirqst1btn.place(relx=0.61, rely=0.832, anchor=CENTER, width=80, height=18)

inqst1btn = tk.Button(qstpg, border=0, borderwidth=0, relief="sunken", image=inbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Name:\r\n"
   "Email:\r\n"
   "Employee ID:\r\n"
   "Callback #:\r\n"
   "Make of Mobile Devic"
   "e:\r\n"
   "Model of Mobile Devi"
   "ce:\r\n"
   "Description of Issue"
   ":\r\n"
   "Location/Site code:")])
inqst1btn.place(relx=0.839, rely=0.832, anchor=CENTER, width=99, height=18)


# qstdefine


def grqst1btn_hover(event):
    grqst1btn.configure(image=grbr2photo)


def grqst1btn_leave(event):
    grqst1btn.configure(image=grbr1photo)


def clqst1btn_hover(event):
    clqst1btn.configure(image=clsbr2photo)


def clqst1btn_leave(event):
    clqst1btn.configure(image=clbr1photo)


def cbqst1btn_hover(event):
    cbqst1btn.configure(image=cbbr2photo)


def cbqst1btn_leave(event):
    cbqst1btn.configure(image=cbbr1photo)


def tsqst1btn_hover(event):
    tsqst1btn.configure(image=tsbr2photo)


def tsqst1btn_leave(event):
    tsqst1btn.configure(image=tsbr1photo)


def snqst1btn_hover(event):
    snqst1btn.configure(image=snbr2photo)


def snqst1btn_leave(event):
    snqst1btn.configure(image=snbr1photo)


def apqst1btn_hover(event):
    apqst1btn.configure(image=apbr2photo)


def apqst1btn_leave(event):
    apqst1btn.configure(image=apbr1photo)


def mirqst1btn_hover(event):
    mirqst1btn.configure(image=mirbr2photo)


def mirqst1btn_leave(event):
    mirqst1btn.configure(image=mirbr1photo)


def inqst1btn_hover(event):
    inqst1btn.configure(image=inbr2photo)


def inqst1btn_leave(event):
    inqst1btn.configure(image=inbr1photo)


grqst1btn.bind("<Enter>", grqst1btn_hover)
grqst1btn.bind("<Leave>", grqst1btn_leave)
clqst1btn.bind("<Enter>", clqst1btn_hover)
clqst1btn.bind("<Leave>", clqst1btn_leave)
cbqst1btn.bind("<Enter>", cbqst1btn_hover)
cbqst1btn.bind("<Leave>", cbqst1btn_leave)
tsqst1btn.bind("<Enter>", tsqst1btn_hover)
tsqst1btn.bind("<Leave>", tsqst1btn_leave)
snqst1btn.bind("<Enter>", snqst1btn_hover)
snqst1btn.bind("<Leave>", snqst1btn_leave)
apqst1btn.bind("<Enter>", apqst1btn_hover)
apqst1btn.bind("<Leave>", apqst1btn_leave)
mirqst1btn.bind("<Enter>", mirqst1btn_hover)
mirqst1btn.bind("<Leave>", mirqst1btn_leave)
inqst1btn.bind("<Enter>", inqst1btn_hover)
inqst1btn.bind("<Leave>", inqst1btn_leave)


#sbr buttons221

grsbr1btn = tk.Button(sbrpg, border=0, borderwidth=0, relief="sunken", image=grbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hi, Thank you for re"
   "aching out!\r\n\r\n"
   "This is Hazrat with "
   "Sabra & Obela IT Ser"
   "vice Desk. In order "
   "to be of more assist"
   "ance, could you kind"
   "ly provide me with y"
   "our first name, last"
   " name, and preferred"
   " phone number?")])
grsbr1btn.place(relx=0.152, rely=0.307, anchor=CENTER, width=80, height=18)

clsbr1btn = tk.Button(sbrpg, border=0, borderwidth=0, relief="sunken", image=clbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Sabra & Obela IT Ser"
   "vice Desk appreciate"
   "s your communication"
   ". If I have addresse"
   "d your needs, please"
   " enjoy the rest of y"
   "our day. You may rec"
   "eive a survey regard"
   "ing this interaction"
   ". I welcome your fee"
   "dback. The ticket nu"
   "mber is [ticket] if "
   "you need to follow u"
   "p.\r\n\r\n"
   "Bye 😄")])
clsbr1btn.place(relx=0.832, rely=0.307, anchor=CENTER, width=80, height=18)

cbsbr1btn = tk.Button(sbrpg, border=0, borderwidth=0, relief="sunken", image=cbbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "Sabra & Obela IT Ser"
   "vice Desk reaching o"
   "ut in regards to tic"
   "ket number [ticket],"
   " referencing [issue]"
   ". Unfortunately, we "
   "were unable to reach"
   " you via phone or em"
   "ail. Please call us "
   "back or start a chat"
   " at your earliest co"
   "nvenience so we may "
   "further assist you w"
   "ith resolving this i"
   "ssue.\r\n\r\n\r\n"
   "Best regards,\r\n"
   "Sabra/Obela\r\n"
   "Hazrat A.\r\n"
   "Sabra & Obela Servic"
   "e Desk\r\n"
   "Phone: Toll Free: +1"
   ".844.767.2272       "
   "   (+1 844 SOSABRA)"
   "\r\n"
   "Outside U.S.: +1.317"
   ".608.5966\r\n"
   "Chat: http://Chat.sa"
   "bra.com﻿")])
cbsbr1btn.place(relx=0.152, rely=0.57, anchor=CENTER, width=80, height=18)

tssbr1btn = tk.Button(sbrpg, border=0, borderwidth=0, relief="sunken", image=tsbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "Sabra & Obela IT Ser"
   "vice Desk, contactin"
   "g you regarding tick"
   "et number [ticket] r"
   "eferencing [issue]. "
   "Unfortunately, after"
   " three attempts to r"
   "each you via phone a"
   "nd email, we have be"
   "en unable to obtain "
   "a response. As a res"
   "ult, we will need to"
   " close this ticket f"
   "or the time being. H"
   "owever, if the probl"
   "em is still ongoing,"
   " please do not hesit"
   "ate to get back in t"
   "ouch so we can reope"
   "n the ticket and con"
   "tinue working to res"
   "olve this matter. Ou"
   "r team is happy to a"
   "ssist. We appreciate"
   " your patience and u"
   "nderstanding.\r\n\r"
   "\n"
   "Best regards,\r\n"
   "Sabra/Obela\r\n"
   "Hazrat A.\r\n"
   "Sabra & Obela Servic"
   "e Desk\r\n"
   "Phone: Toll Free: +1"
   ".844.767.2272       "
   "   (+1 844 SOSABRA)"
   "\r\n"
   "Outside U.S.: +1.317"
   ".608.5966\r\n"
   "Chat: http://Chat.sa"
   "bra.com﻿")])
tssbr1btn.place(relx=0.839, rely=0.57, anchor=CENTER, width=99, height=18)

snsbr1btn = tk.Button(sbrpg, border=0, borderwidth=0, relief="sunken", image=snbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Sabra/Obela\r\n"
   "Hazrat A.\r\n"
   "Sabra & Obela Servic"
   "e Desk\r\n"
   "Phone: Toll Free: +1"
   ".844.767.2272       "
   "   (+1 844 SOSABRA)"
   "\r\n"
   "Outside U.S.: +1.317"
   ".608.5966\r\n"
   "Chat: http://Chat.sa"
   "bra.com")])
snsbr1btn.place(relx=0.152, rely=0.832, anchor=CENTER, width=83, height=18)

apsbr1btn = tk.Button(sbrpg, border=0, borderwidth=0, relief="sunken", image=apbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "Sabra & Obela IT Ser"
   "vice Desk reaching o"
   "ut in regards to tic"
   "ket number [ticket],"
   " referencing [issue]"
   ". [EU] has requested"
   " to have their passw"
   "ord reset. If you ap"
   "prove of this reques"
   "t, please reply to t"
   "his email with your "
   "approval.\r\n\r\n"
   "Best regards,\r\n"
   "Sabra/Obela\r\n"
   "Hazrat A.\r\n"
   "Sabra & Obela Servic"
   "e Desk\r\n"
   "Phone: Toll Free: +1"
   ".844.767.2272       "
   "   (+1 844 SOSABRA)"
   "\r\n"
   "Outside U.S.: +1.317"
   ".608.5966\r\n"
   "Chat: http://Chat.sa"
   "bra.com﻿")])
apsbr1btn.place(relx=0.384, rely=0.832, anchor=CENTER, width=80, height=18)

mirsbr1btn = tk.Button(sbrpg, border=0, borderwidth=0, relief="sunken", image=mirbr1photo, cursor="hand2",
                      compound="left", command=lambda: [copy_clip("EUs name:\r\n"
   "CB #:\r\n"
   "Asset tag:\r\n"
   "Issue:\r\n"
   "Error/ss:\r\n"
   "Location(Optional):"
   "\r\n\r\n"
   "TS:")])
mirsbr1btn.place(relx=0.61, rely=0.832, anchor=CENTER, width=80, height=18)

insbr1btn = tk.Button(sbrpg, border=0, borderwidth=0, relief="sunken", image=inbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("EUs name:\r\n"
   "CB #:\r\n"
   "Asset tag:\r\n"
   "Issue:\r\n"
   "Error/ss:\r\n"
   "Location(Optional):"
   "\r\n\r\n"
   "TS:")])
insbr1btn.place(relx=0.839, rely=0.832, anchor=CENTER, width=99, height=18)


# sbrdefine


def grsbr1btn_hover(event):
    grsbr1btn.configure(image=grbr2photo)


def grsbr1btn_leave(event):
    grsbr1btn.configure(image=grbr1photo)


def clsbr1btn_hover(event):
    clsbr1btn.configure(image=clsbr2photo)


def clsbr1btn_leave(event):
    clsbr1btn.configure(image=clbr1photo)


def cbsbr1btn_hover(event):
    cbsbr1btn.configure(image=cbbr2photo)


def cbsbr1btn_leave(event):
    cbsbr1btn.configure(image=cbbr1photo)


def tssbr1btn_hover(event):
    tssbr1btn.configure(image=tsbr2photo)


def tssbr1btn_leave(event):
    tssbr1btn.configure(image=tsbr1photo)


def snsbr1btn_hover(event):
    snsbr1btn.configure(image=snbr2photo)


def snsbr1btn_leave(event):
    snsbr1btn.configure(image=snbr1photo)


def apsbr1btn_hover(event):
    apsbr1btn.configure(image=apbr2photo)


def apsbr1btn_leave(event):
    apsbr1btn.configure(image=apbr1photo)


def mirsbr1btn_hover(event):
    mirsbr1btn.configure(image=mirbr2photo)


def mirsbr1btn_leave(event):
    mirsbr1btn.configure(image=mirbr1photo)


def insbr1btn_hover(event):
    insbr1btn.configure(image=inbr2photo)


def insbr1btn_leave(event):
    insbr1btn.configure(image=inbr1photo)


grsbr1btn.bind("<Enter>", grsbr1btn_hover)
grsbr1btn.bind("<Leave>", grsbr1btn_leave)
clsbr1btn.bind("<Enter>", clsbr1btn_hover)
clsbr1btn.bind("<Leave>", clsbr1btn_leave)
cbsbr1btn.bind("<Enter>", cbsbr1btn_hover)
cbsbr1btn.bind("<Leave>", cbsbr1btn_leave)
tssbr1btn.bind("<Enter>", tssbr1btn_hover)
tssbr1btn.bind("<Leave>", tssbr1btn_leave)
snsbr1btn.bind("<Enter>", snsbr1btn_hover)
snsbr1btn.bind("<Leave>", snsbr1btn_leave)
apsbr1btn.bind("<Enter>", apsbr1btn_hover)
apsbr1btn.bind("<Leave>", apsbr1btn_leave)
mirsbr1btn.bind("<Enter>", mirsbr1btn_hover)
mirsbr1btn.bind("<Leave>", mirsbr1btn_leave)
insbr1btn.bind("<Enter>", insbr1btn_hover)
insbr1btn.bind("<Leave>", insbr1btn_leave)

#us buttons221

grus1btn = tk.Button(uspg, border=0, borderwidth=0, relief="sunken", image=grbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hi, Thank you for re"
   "aching out!\r\n\r\n"
   "This is Hazrat with "
   "USP IT Service Desk."
   " In order to be of m"
   "ore assistance, coul"
   "d you kindly provide"
   " me with your first "
   "name, last name, and"
   " preferred phone num"
   "ber?")])
grus1btn.place(relx=0.152, rely=0.307, anchor=CENTER, width=80, height=18)

clus1btn = tk.Button(uspg, border=0, borderwidth=0, relief="sunken", image=clbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("USP IT Service Desk "
   "appreciates your com"
   "munication. If I hav"
   "e addressed your nee"
   "ds, please enjoy the"
   " rest of your day. Y"
   "ou may receive a sur"
   "vey regarding this i"
   "nteraction. I welcom"
   "e your feedback. The"
   " ticket number is [t"
   "icket] if you need t"
   "o follow up.\r\n\r\n"
   "Bye 😄")])
clus1btn.place(relx=0.832, rely=0.307, anchor=CENTER, width=80, height=18)

cbus1btn = tk.Button(uspg, border=0, borderwidth=0, relief="sunken", image=cbbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "USP IT Service Desk "
   "reaching out in rega"
   "rds to ticket number"
   " [ticket], referenci"
   "ng [issue]. Unfortun"
   "ately, we were unabl"
   "e to reach you via p"
   "hone or email. Pleas"
   "e call us back or st"
   "art a chat at your e"
   "arliest convenience "
   "so we may further as"
   "sist you with resolv"
   "ing this issue.\r\n"
   "\r\n\r\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n"
   "USP Service Desk\r\n"
   "\r\n"
   "We are here to servi"
   "ce you 24x7! If you "
   "need help, we can be"
   " reached in any of t"
   "he following ways:\r"
   "\n\r\n"
   "Toll free at 866-714"
   "-3622\r\n\r\n"
   "Self-service Portal:"
   " https://uspprod.ser"
   "vicenowservices.com/"
   " \r\n\r\n"
   "Chat URL: https://it"
   "chat.usp.org\r\n\r\n"
   "Email: https://ithel"
   "p@usp.org﻿")])
cbus1btn.place(relx=0.152, rely=0.57, anchor=CENTER, width=80, height=18)

tsus1btn = tk.Button(uspg, border=0, borderwidth=0, relief="sunken", image=tsbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "USP IT Service Desk,"
   " contacting you rega"
   "rding ticket number "
   "[ticket] referencing"
   " [issue]. Unfortunat"
   "ely, after three att"
   "empts to reach you v"
   "ia phone and email, "
   "we have been unable "
   "to obtain a response"
   ". As a result, we wi"
   "ll need to close thi"
   "s ticket for the tim"
   "e being. However, if"
   " the problem is stil"
   "l ongoing, please do"
   " not hesitate to get"
   " back in touch so we"
   " can reopen the tick"
   "et and continue work"
   "ing to resolve this "
   "matter. Our team is "
   "happy to assist. We "
   "appreciate your pati"
   "ence and understandi"
   "ng.\r\n\r\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n"
   "USP Service Desk\r\n"
   "\r\n"
   "We are here to servi"
   "ce you 24x7! If you "
   "need help, we can be"
   " reached in any of t"
   "he following ways:\r"
   "\n\r\n"
   "Toll free at 866-714"
   "-3622\r\n\r\n"
   "Self-service Portal:"
   " https://uspprod.ser"
   "vicenowservices.com/"
   " \r\n\r\n"
   "Chat URL: https://it"
   "chat.usp.org\r\n\r\n"
   "Email: https://ithel"
   "p@usp.org﻿")])
tsus1btn.place(relx=0.839, rely=0.57, anchor=CENTER, width=99, height=18)

snus1btn = tk.Button(uspg, border=0, borderwidth=0, relief="sunken", image=snbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Best Regards,\r\n"
   "Hazrat A.\r\n"
   "USP Service Desk\r\n"
   "\r\n"
   "We are here to servi"
   "ce you 24x7! If you "
   "need help, we can be"
   " reached in any of t"
   "he following ways:\r"
   "\n\r\n"
   "Toll free at 866-714"
   "-3622\r\n\r\n"
   "Self-service Portal:"
   " https://uspprod.ser"
   "vicenowservices.com/"
   " \r\n\r\n"
   "Chat URL: https://it"
   "chat.usp.org\r\n\r\n"
   "Email: https://ithel"
   "p@usp.org")])
snus1btn.place(relx=0.152, rely=0.832, anchor=CENTER, width=83, height=18)

apus1btn = tk.Button(uspg, border=0, borderwidth=0, relief="sunken", image=apbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "USP IT Service Desk "
   "reaching out in rega"
   "rds to ticket number"
   " [ticket], referenci"
   "ng [issue]. [EU] has"
   " requested to have t"
   "heir password reset."
   " If you approve of t"
   "his request, please "
   "reply to this email "
   "with your approval."
   "\r\n\r\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n"
   "USP Service Desk\r\n"
   "\r\n"
   "We are here to servi"
   "ce you 24x7! If you "
   "need help, we can be"
   " reached in any of t"
   "he following ways:\r"
   "\n\r\n"
   "Toll free at 866-714"
   "-3622\r\n\r\n"
   "Self-service Portal:"
   " https://uspprod.ser"
   "vicenowservices.com/"
   " \r\n\r\n"
   "Chat URL: https://it"
   "chat.usp.org\r\n\r\n"
   "Email: https://ithel"
   "p@usp.org﻿")])
apus1btn.place(relx=0.384, rely=0.832, anchor=CENTER, width=80, height=18)

mirus1btn = tk.Button(uspg, border=0, borderwidth=0, relief="sunken", image=mirbr1photo, cursor="hand2",
                      compound="left", command=lambda: [webbrowser.open('https://uspprod.service-now.com/kb_view.do?sys_kb_id=ae0d26221bfd75104431eca2604bcb7e&sysparm_rank=3&sysparm_tsqueryId=9c05ce7d87eb3514dbf484cd0ebb350b'), copy_clip("The name of the appl"
   "ication or system:\r"
   "\n\r\n"
   "Set the “Application"
   "” field to the appli"
   "cable application*\r"
   "\n\r\n"
   "Number of users impa"
   "cted and location:\r"
   "\n\r\n"
   "If multiple users ar"
   "e impacted, identify"
   " if it is the entire"
   " department/location"
   " and provide example"
   "s of User ID(s) or A"
   "pplication Specific "
   "ID(s) as applicable*"
   "\r\n\r\n"
   "Explanation of issue"
   ", including impact:"
   "\r\n\r\n"
   "Process/function use"
   "r is performing:\r\n"
   "\r\n"
   "Error message, if ap"
   "plicable:\r\n\r\n"
   "If this was identifi"
   "ed as a critical app"
   "lication in the bull"
   "et above, ask if the"
   " URL/application is "
   "accessible.\r\n\r\n"
   "When was the last ti"
   "me this worked prope"
   "rly?")])
mirus1btn.place(relx=0.61, rely=0.832, anchor=CENTER, width=80, height=18)

inus1btn = tk.Button(uspg, border=0, borderwidth=0, relief="sunken", image=inbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("EUs name:\r\n"
   "CB #:\r\n"
   "Asset tag:\r\n"
   "Issue:\r\n"
   "Error/ss:\r\n"
   "Location(Optional):"
   "\r\n\r\n"
   "TS:")])
inus1btn.place(relx=0.839, rely=0.832, anchor=CENTER, width=99, height=18)


# usdefine


def grus1btn_hover(event):
    grus1btn.configure(image=grbr2photo)


def grus1btn_leave(event):
    grus1btn.configure(image=grbr1photo)


def clus1btn_hover(event):
    clus1btn.configure(image=clsbr2photo)


def clus1btn_leave(event):
    clus1btn.configure(image=clbr1photo)


def cbus1btn_hover(event):
    cbus1btn.configure(image=cbbr2photo)


def cbus1btn_leave(event):
    cbus1btn.configure(image=cbbr1photo)


def tsus1btn_hover(event):
    tsus1btn.configure(image=tsbr2photo)


def tsus1btn_leave(event):
    tsus1btn.configure(image=tsbr1photo)


def snus1btn_hover(event):
    snus1btn.configure(image=snbr2photo)


def snus1btn_leave(event):
    snus1btn.configure(image=snbr1photo)


def apus1btn_hover(event):
    apus1btn.configure(image=apbr2photo)


def apus1btn_leave(event):
    apus1btn.configure(image=apbr1photo)


def mirus1btn_hover(event):
    mirus1btn.configure(image=mirbr2photo)


def mirus1btn_leave(event):
    mirus1btn.configure(image=mirbr1photo)


def inus1btn_hover(event):
    inus1btn.configure(image=inbr2photo)


def inus1btn_leave(event):
    inus1btn.configure(image=inbr1photo)


grus1btn.bind("<Enter>", grus1btn_hover)
grus1btn.bind("<Leave>", grus1btn_leave)
clus1btn.bind("<Enter>", clus1btn_hover)
clus1btn.bind("<Leave>", clus1btn_leave)
cbus1btn.bind("<Enter>", cbus1btn_hover)
cbus1btn.bind("<Leave>", cbus1btn_leave)
tsus1btn.bind("<Enter>", tsus1btn_hover)
tsus1btn.bind("<Leave>", tsus1btn_leave)
snus1btn.bind("<Enter>", snus1btn_hover)
snus1btn.bind("<Leave>", snus1btn_leave)
apus1btn.bind("<Enter>", apus1btn_hover)
apus1btn.bind("<Leave>", apus1btn_leave)
mirus1btn.bind("<Enter>", mirus1btn_hover)
mirus1btn.bind("<Leave>", mirus1btn_leave)
inus1btn.bind("<Enter>", inus1btn_hover)
inus1btn.bind("<Leave>", inus1btn_leave)


#bell buttons221

grbl1btn = tk.Button(blpg, border=0, borderwidth=0, relief="sunken", image=grbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hi, Thank you for re"
   "aching out!\r\n\r\n"
   "This is Hazrat with "
   "Bell Internal IT"
   " Service Desk. In or"
   "der to be of more as"
   "sistance, could you "
   "kindly provide me wi"
   "th your first name, "
   "last name, and prefe"
   "rred phone number?")])
grbl1btn.place(relx=0.152, rely=0.307, anchor=CENTER, width=80, height=18)

clbl1btn = tk.Button(blpg, border=0, borderwidth=0, relief="sunken", image=clbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Bell Internal IT Ser"
   "vice Desk appreciate"
   "s your communication"
   ". If I have addresse"
   "d your needs, please"
   " enjoy the rest of y"
   "our day. You may rec"
   "eive a survey regard"
   "ing this interaction"
   ". I welcome your fee"
   "dback. The ticket nu"
   "mber is [ticket] if "
   "you need to follow u"
   "p.\r\n\r\n"
   "Bye 😄")])
clbl1btn.place(relx=0.832, rely=0.307, anchor=CENTER, width=80, height=18)

cbbl1btn = tk.Button(blpg, border=0, borderwidth=0, relief="sunken", image=cbbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "Bell Internal IT Ser"
   "vice Desk reaching o"
   "ut in regards to tic"
   "ket number [ticket],"
   " referencing [issue]"
   ". Unfortunately, we "
   "were unable to reach"
   " you via phone or em"
   "ail. Please call us "
   "back or start a chat"
   " at your earliest co"
   "nvenience so we may "
   "further assist you w"
   "ith resolving this i"
   "ssue.\r\n\r\n\r\n\r"
   "\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n"
   "EUS Level 1 Analyst"
   "\r\n"
   "Bell Techlogix\r\n"
   "Service Desk Office "
   "no: +1.317.333.7700"
   "\r\n"
   "HAlkozai@belltechlog"
   "ix.com\r\n"
   "www.belltechlogix.co"
   "m\r\n"
   "Deliver. Transform. "
   "Exceed.")])
cbbl1btn.place(relx=0.152, rely=0.57, anchor=CENTER, width=80, height=18)

tsbl1btn = tk.Button(blpg, border=0, borderwidth=0, relief="sunken", image=tsbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "Bell Internal IT Ser"
   "vice Desk, contactin"
   "g you regarding tick"
   "et number [ticket] r"
   "eferencing [issue]. "
   "Unfortunately, after"
   " three attempts to r"
   "each you via phone a"
   "nd email, we have be"
   "en unable to obtain "
   "a response. As a res"
   "ult, we will need to"
   " close this ticket f"
   "or the time being. H"
   "owever, if the probl"
   "em is still ongoing,"
   " please do not hesit"
   "ate to get back in t"
   "ouch so we can reope"
   "n the ticket and con"
   "tinue working to res"
   "olve this matter. Ou"
   "r team is happy to a"
   "ssist. We appreciate"
   " your patience and u"
   "nderstanding.\r\n\r"
   "\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n"
   "EUS Level 1 Analyst"
   "\r\n"
   "Bell Techlogix\r\n"
   "Service Desk Office "
   "no: +1.317.333.7700"
   "\r\n"
   "HAlkozai@belltechlog"
   "ix.com\r\n"
   "www.belltechlogix.co"
   "m\r\n"
   "Deliver. Transform. "
   "Exceed.")])
tsbl1btn.place(relx=0.839, rely=0.57, anchor=CENTER, width=99, height=18)

snbl1btn = tk.Button(blpg, border=0, borderwidth=0, relief="sunken", image=snbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Best Regards,\r\n"
   "Hazrat A.\r\n"
   "EUS Level 1 Analyst"
   "\r\n\r\n"
   "Bell Techlogix\r\n\r"
   "\n"
   "Service Desk Office "
   "no: +1.317.333.7700"
   "\r\n\r\n"
   "HAlkozai@belltechlog"
   "ix.com\r\n\r\n"
   "www.belltechlogix.co"
   "m\r\n\r\n"
   "Deliver. Transform. "
   "Exceed.")])
snbl1btn.place(relx=0.152, rely=0.832, anchor=CENTER, width=83, height=18)

apbl1btn = tk.Button(blpg, border=0, borderwidth=0, relief="sunken", image=apbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "Bell Internal IT Ser"
   "vice Desk reaching o"
   "ut in regards to tic"
   "ket number [ticket],"
   " referencing [issue]"
   ". [EU] has requested"
   " to have their passw"
   "ord reset. If you ap"
   "prove of this reques"
   "t, please reply to t"
   "his email with your "
   "approval.\r\n\r\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n"
   "EUS Level 1 Analyst"
   "\r\n\r\n"
   "Bell Techlogix\r\n\r"
   "\n"
   "Service Desk Office "
   "no: +1.317.333.7700"
   "\r\n\r\n"
   "HAlkozai@belltechlog"
   "ix.com\r\n\r\n"
   "www.belltechlogix.co"
   "m\r\n\r\n"
   "Deliver. Transform. "
   "Exceed.")])
apbl1btn.place(relx=0.384, rely=0.832, anchor=CENTER, width=80, height=18)

mirbl1btn = tk.Button(blpg, border=0, borderwidth=0, relief="sunken", image=mirbr1photo, cursor="hand2",
                      compound="left", command=lambda: [copy_clip("EUs name:\r\n"
   "CB #:\r\n"
   "Asset tag:\r\n"
   "Issue:\r\n"
   "Error/ss:\r\n"
   "Location(Optional):"
   "\r\n\r\n"
   "TS:")])
mirbl1btn.place(relx=0.61, rely=0.832, anchor=CENTER, width=80, height=18)

inbl1btn = tk.Button(blpg, border=0, borderwidth=0, relief="sunken", image=inbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("EUs name:\r\n"
   "CB #:\r\n"
   "Asset tag:\r\n"
   "Issue:\r\n"
   "Error/ss:\r\n"
   "Location(Optional):"
   "\r\n\r\n"
   "TS:")])
inbl1btn.place(relx=0.839, rely=0.832, anchor=CENTER, width=99, height=18)


# belldefine


def grbl1btn_hover(event):
    grbl1btn.configure(image=grbr2photo)


def grbl1btn_leave(event):
    grbl1btn.configure(image=grbr1photo)


def clbl1btn_hover(event):
    clbl1btn.configure(image=clsbr2photo)


def clbl1btn_leave(event):
    clbl1btn.configure(image=clbr1photo)


def cbbl1btn_hover(event):
    cbbl1btn.configure(image=cbbr2photo)


def cbbl1btn_leave(event):
    cbbl1btn.configure(image=cbbr1photo)


def tsbl1btn_hover(event):
    tsbl1btn.configure(image=tsbr2photo)


def tsbl1btn_leave(event):
    tsbl1btn.configure(image=tsbr1photo)


def snbl1btn_hover(event):
    snbl1btn.configure(image=snbr2photo)


def snbl1btn_leave(event):
    snbl1btn.configure(image=snbr1photo)


def apbl1btn_hover(event):
    apbl1btn.configure(image=apbr2photo)


def apbl1btn_leave(event):
    apbl1btn.configure(image=apbr1photo)


def mirbl1btn_hover(event):
    mirbl1btn.configure(image=mirbr2photo)


def mirbl1btn_leave(event):
    mirbl1btn.configure(image=mirbr1photo)


def inbl1btn_hover(event):
    inbl1btn.configure(image=inbr2photo)


def inbl1btn_leave(event):
    inbl1btn.configure(image=inbr1photo)


grbl1btn.bind("<Enter>", grbl1btn_hover)
grbl1btn.bind("<Leave>", grbl1btn_leave)
clbl1btn.bind("<Enter>", clbl1btn_hover)
clbl1btn.bind("<Leave>", clbl1btn_leave)
cbbl1btn.bind("<Enter>", cbbl1btn_hover)
cbbl1btn.bind("<Leave>", cbbl1btn_leave)
tsbl1btn.bind("<Enter>", tsbl1btn_hover)
tsbl1btn.bind("<Leave>", tsbl1btn_leave)
snbl1btn.bind("<Enter>", snbl1btn_hover)
snbl1btn.bind("<Leave>", snbl1btn_leave)
apbl1btn.bind("<Enter>", apbl1btn_hover)
apbl1btn.bind("<Leave>", apbl1btn_leave)
mirbl1btn.bind("<Enter>", mirbl1btn_hover)
mirbl1btn.bind("<Leave>", mirbl1btn_leave)
inbl1btn.bind("<Enter>", inbl1btn_hover)
inbl1btn.bind("<Leave>", inbl1btn_leave)


#vera buttons221

grvr1btn = tk.Button(vrpg, border=0, borderwidth=0, relief="sunken", image=grbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hi, Thank you for re"
   "aching out!\r\n\r\n"
   "This is Hazrat with "
   "VeraBradley IT Servi"
   "ce Desk. In order to"
   " be of more assistan"
   "ce, could you kindly"
   " provide me with you"
   "r first name, last n"
   "ame, and preferred p"
   "hone number?")])
grvr1btn.place(relx=0.152, rely=0.307, anchor=CENTER, width=80, height=18)

clvr1btn = tk.Button(vrpg, border=0, borderwidth=0, relief="sunken", image=clbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("VeraBradley IT Servi"
   "ce Desk appreciates "
   "your communication. "
   "If I have addressed "
   "your needs, please e"
   "njoy the rest of you"
   "r day. You may recei"
   "ve a survey regardin"
   "g this interaction. "
   "I welcome your feedb"
   "ack. The ticket numb"
   "er is [ticket] if yo"
   "u need to follow up."
   "\r\n\r\n"
   "Bye 😄")])
clvr1btn.place(relx=0.832, rely=0.307, anchor=CENTER, width=80, height=18)

cbvr1btn = tk.Button(vrpg, border=0, borderwidth=0, relief="sunken", image=cbbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "VeraBradley IT Servi"
   "ce Desk reaching out"
   " in regards to ticke"
   "t number [ticket], r"
   "eferencing [issue]. "
   "Unfortunately, we we"
   "re unable to reach y"
   "ou via phone or emai"
   "l. Please call us ba"
   "ck or start a chat a"
   "t your earliest conv"
   "enience so we may fu"
   "rther assist you wit"
   "h resolving this iss"
   "ue.\r\n\r\n\r\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n"
   "Help Desk Support\r"
   "\n\r\n"
   "12420 Stonebridge Ro"
   "ad\r\n\r\n"
   "Roanoke, IN 46783\r"
   "\n\r\n"
   "260.207.5300\r\n\r\n"
   "helpdesk@verabradley"
   ".com﻿")])
cbvr1btn.place(relx=0.152, rely=0.57, anchor=CENTER, width=80, height=18)

tsvr1btn = tk.Button(vrpg, border=0, borderwidth=0, relief="sunken", image=tsbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "VeraBradley IT Servi"
   "ce Desk, contacting "
   "you regarding ticket"
   " number [ticket] ref"
   "erencing [issue]. Un"
   "fortunately, after t"
   "hree attempts to rea"
   "ch you via phone and"
   " email, we have been"
   " unable to obtain a "
   "response. As a resul"
   "t, we will need to c"
   "lose this ticket for"
   " the time being. How"
   "ever, if the problem"
   " is still ongoing, p"
   "lease do not hesitat"
   "e to get back in tou"
   "ch so we can reopen "
   "the ticket and conti"
   "nue working to resol"
   "ve this matter. Our "
   "team is happy to ass"
   "ist. We appreciate y"
   "our patience and und"
   "erstanding.\r\n\r\n"
   "Best regards,\r\n"
   "Hazrat A.\r\n"
   "Help Desk Support\r"
   "\n\r\n"
   "12420 Stonebridge Ro"
   "ad\r\n\r\n"
   "Roanoke, IN 46783\r"
   "\n\r\n"
   "260.207.5300\r\n\r\n"
   "helpdesk@verabradley"
   ".com")])
tsvr1btn.place(relx=0.839, rely=0.57, anchor=CENTER, width=99, height=18)

snvr1btn = tk.Button(vrpg, border=0, borderwidth=0, relief="sunken", image=snbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Best Regards,\r\n"
   "Hazrat A\r\n"
   "Help Desk Support\r"
   "\n\r\n"
   "12420 Stonebridge Ro"
   "ad\r\n\r\n"
   "Roanoke, IN 46783\r"
   "\n\r\n"
   "260.207.5300\r\n\r\n"
   "helpdesk@verabradley"
   ".com")])
snvr1btn.place(relx=0.152, rely=0.832, anchor=CENTER, width=83, height=18)

apvr1btn = tk.Button(vrpg, border=0, borderwidth=0, relief="sunken", image=apbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Hello,\r\n\r\n"
   "This is Hazrat from "
   "VeraBradley IT Servi"
   "ce Desk reaching out"
   " in regards to ticke"
   "t number [ticket], r"
   "eferencing [issue]. "
   "[EU] has requested t"
   "o have their passwor"
   "d reset. If you appr"
   "ove of this request,"
   " please reply to thi"
   "s email with your ap"
   "proval.\r\n\r\n"
   "Best regards,\r\n\r"
   "\n"
   "Hazrat A.\r\n\r\n"
   "Help Desk Support\r"
   "\n\r\n"
   "12420 Stonebridge Ro"
   "ad\r\n\r\n"
   "Roanoke, IN 46783\r"
   "\n\r\n"
   "260.207.5300\r\n\r\n"
   "helpdesk@verabradley"
   ".com﻿")])
apvr1btn.place(relx=0.384, rely=0.832, anchor=CENTER, width=80, height=18)

mirvr1btn = tk.Button(vrpg, border=0, borderwidth=0, relief="sunken", image=mirbr1photo, cursor="hand2",
                      compound="left", command=lambda: [webbrowser.open('https://verabradley.service-now.com/kb_view.do?sysparm_article=KB0041599&sysparm_rank=1&sysparm_tsqueryId=61a546f597afb59070eab82bf253af71'), copy_clip("Operator ID:\r\n"
   "Employee Name:\r\n"
   "CB:\r\n"
   "Store Number:\r\n"
   "Error they are recei"
   "ving:\r\n"
   "TS:\r\n\r\n"
   "Contacted oncall:\r"
   "\n"
   "Left Message: Y / N"
   "\r\n"
   "User Name:\r\n"
   "Callback :\r\n"
   "Ticket :\r\n"
   "Analyst Name:")])
mirvr1btn.place(relx=0.61, rely=0.832, anchor=CENTER, width=80, height=18)

invr1btn = tk.Button(vrpg, border=0, borderwidth=0, relief="sunken", image=inbr1photo, cursor="hand2",
                     compound="left", command=lambda: [copy_clip("Operator ID:\r\n"
   "Employee Name:\r\n"
   "CB:\r\n"
   "Store Number:\r\n"
   "Error they are recei"
   "ving:\r\n"
   "TS:\r\n")])
invr1btn.place(relx=0.839, rely=0.832, anchor=CENTER, width=99, height=18)


# veradefine


def grvr1btn_hover(event):
    grvr1btn.configure(image=grbr2photo)


def grvr1btn_leave(event):
    grvr1btn.configure(image=grbr1photo)


def clvr1btn_hover(event):
    clvr1btn.configure(image=clsbr2photo)


def clvr1btn_leave(event):
    clvr1btn.configure(image=clbr1photo)


def cbvr1btn_hover(event):
    cbvr1btn.configure(image=cbbr2photo)


def cbvr1btn_leave(event):
    cbvr1btn.configure(image=cbbr1photo)


def tsvr1btn_hover(event):
    tsvr1btn.configure(image=tsbr2photo)


def tsvr1btn_leave(event):
    tsvr1btn.configure(image=tsbr1photo)


def snvr1btn_hover(event):
    snvr1btn.configure(image=snbr2photo)


def snvr1btn_leave(event):
    snvr1btn.configure(image=snbr1photo)


def apvr1btn_hover(event):
    apvr1btn.configure(image=apbr2photo)


def apvr1btn_leave(event):
    apvr1btn.configure(image=apbr1photo)


def mirvr1btn_hover(event):
    mirvr1btn.configure(image=mirbr2photo)


def mirvr1btn_leave(event):
    mirvr1btn.configure(image=mirbr1photo)


def invr1btn_hover(event):
    invr1btn.configure(image=inbr2photo)


def invr1btn_leave(event):
    invr1btn.configure(image=inbr1photo)


grvr1btn.bind("<Enter>", grvr1btn_hover)
grvr1btn.bind("<Leave>", grvr1btn_leave)
clvr1btn.bind("<Enter>", clvr1btn_hover)
clvr1btn.bind("<Leave>", clvr1btn_leave)
cbvr1btn.bind("<Enter>", cbvr1btn_hover)
cbvr1btn.bind("<Leave>", cbvr1btn_leave)
tsvr1btn.bind("<Enter>", tsvr1btn_hover)
tsvr1btn.bind("<Leave>", tsvr1btn_leave)
snvr1btn.bind("<Enter>", snvr1btn_hover)
snvr1btn.bind("<Leave>", snvr1btn_leave)
apvr1btn.bind("<Enter>", apvr1btn_hover)
apvr1btn.bind("<Leave>", apvr1btn_leave)
mirvr1btn.bind("<Enter>", mirvr1btn_hover)
mirvr1btn.bind("<Leave>", mirvr1btn_leave)
invr1btn.bind("<Enter>", invr1btn_hover)
invr1btn.bind("<Leave>", invr1btn_leave)



# Assigned functions


def show_frame(frame):
    frame.tkraise()


# Show page 1 first
show_frame(intro_pg)


# GIF to MP4 https://cloudconvert.com/gif-to-mp4 set CRF=0 Vid enc = 265

def play_video(video_path, lb, playback_speed):
    vid = cv2.VideoCapture(video_path)

    def play():
        ret, frame = vid.read()
        if not ret:
            vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = vid.read()

        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        imgtk = ImageTk.PhotoImage(img)
        lb.imgtk = imgtk
        lb.configure(image=imgtk)

        # If video should play at 60 FPS, delay would be ~ 1000ms / 60 = ~ 17ms.
        # For different playback speed adjust this value
        delay = int((1 / 1) * 1000 / playback_speed)
        root.after(delay, play)

    delay = int((1 / 1) * 1000 / playback_speed)
    root.after(delay, play)





play_video('C:/Users/Administrator/Desktop/Main.py/mp2.mp4', gif_lb, 18)
play_video('C:/Users/Administrator/Desktop/Main.py/intro.mp4', intro_lb, 18)
play_video('C:/Users/Administrator/Desktop/Main.py/fi.mp4', gifFIP_lb, 18)
play_video('C:/Users/Administrator/Desktop/Main.py/main2.mp4', mp2lb, 18)
play_video('C:/Users/Administrator/Desktop/Main.py/cpi.mp4', gifcpi_lb, 18)
play_video('C:/Users/Administrator/Desktop/Main.py/br.mp4', gifbr_lb, 18)
play_video('C:/Users/Administrator/Desktop/Main.py/clbr.mp4', clbr_lb, 18)
play_video('C:/Users/Administrator/Desktop/Main.py/jx.mp4', jx_lb, 18)
play_video('C:/Users/Administrator/Desktop/Main.py/qst.mp4', qst_lb, 18)
play_video('C:/Users/Administrator/Desktop/Main.py/sbr.mp4', sbr_lb, 18)
play_video('C:/Users/Administrator/Desktop/Main.py/usp.mp4', us_lb, 18)
play_video('C:/Users/Administrator/Desktop/Main.py/bell.mp4', bl_lb, 18)
play_video('C:/Users/Administrator/Desktop/Main.py/vera.mp4', vr_lb, 18)

root.mainloop()