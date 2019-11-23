from tkinter import *
from tkinter import ttk
import os
from PIL import ImageTk,Image

main_screen=Tk()
main_screen.geometry("800x600")
main_screen.title("Health Monitoring System")


global login_screen
login_screen = Toplevel(main_screen)
login_screen.title("Health Monitoring System")
login_screen.geometry("800x600")
  
c1=Canvas(login_screen,width=800,height=600)
c1.pack()
image=PhotoImage(file=r"F:\Namratha\5th-Sem-Project\globe.png")
background_label = Label(login_screen, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
c1.create_image(400,300,anchor="center",image=image)
   
        
button11=Button(login_screen, text="DOCTOR LOGIN",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL)
button11.configure(width=20,height=2)
button_window11=c1.create_window(480,250,anchor=SE,window=button11)

button12=Button(login_screen, text="PATIENT LOGIN",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL)
button12.configure(width=20,height=2)
button_window12=c1.create_window(480,350,anchor=SE,window=button12)

button13=Button(login_screen, text="Back",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL)
button13.configure(width=12,height=2)
button_window13=c1.create_window(100,50,anchor=SE,window=button13)
    







main_screen.mainloop()