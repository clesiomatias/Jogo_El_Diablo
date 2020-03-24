#-*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from keyboard import *
from random import *
from pynput.keyboard import Listener, Key, Controller


janela = Tk()
janela.geometry('800x600')
janela.title('El DiablO')
janela.iconbitmap('ico.ico')
janela.resizable(width=False, height=False)


image2 = Image.open("diablo.gif")

image1 = ImageTk.PhotoImage(image2)
background_label = Label(janela, image=image1)
background_label.image1=image1
background_label.place(x=0, y=20, height=600, width=800)

label_text_head = ttk.Label(
	janela, 
	text='Faça suas perguntas... Se puder!',
	font = 'Buffied 40 normal',
	)
label_text_head.place(x=150,y=-10)

with open ('elogios.txt','r', encoding='utf-8') as elogios:
	elogio = choice(elogios.readlines())
	print(elogio)
hot = Entry(janela, width=0)
hot.pack()
hot.place(x=-20,y=-100)
hot.focus()
x = hot.get()
print(x)



pergunta = Entry(janela,width=100,fg= 'red',justify ='center',state = 'disable')
pergunta.pack()
pergunta.place(x=100,y=120)

def avalia(x):
	print (x)
	
		
b_perg = Button(janela, text='Quero Perguntar', command=avalia(x))
b_perg.pack()
b_perg.place(x=350, y=80)



janela.mainloop()


