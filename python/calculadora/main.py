from tkinter import *
from tkinter import ttk

# Cores:
cor1 = "#04080F" #Preto 
cor2 = "#EAF2EF" #Branco 
cor3 = "#6B818C" #Cinza

janela =  Tk()
janela.title("Calculadora Python")
janela.geometry("450x400")
janela.config(bg=cor1)

# Dividindo a tela em Frames
frame_resultado = Frame(janela, width=450, height=80, bg=cor1)
frame_resultado.grid(row=0, column=0)

frame_corpo = Frame(janela, width=450, height=320)
frame_corpo.grid(row=1, column=0)

# Criando btn

btnClean = Button(frame_corpo, text="C", width=18, height=2)
btnClean.place(x=0, y=0)
btnSoma = Button(frame_corpo, text="+")
btnSubtracao = Button(frame_corpo, text="-")
btnDivisao = Button(frame_corpo, text="÷")
btnMultiplicacao = Button(frame_corpo, text="X")
btnPorcentagem = Button(frame_corpo, text="%")
btnResultado = Button(frame_corpo, text="=")

btn1 = Button(frame_corpo, text="1")
btn2 = Button(frame_corpo, text="2")
btn3 = Button(frame_corpo, text="3")
btn4 = Button(frame_corpo, text="4")
btn5 = Button(frame_corpo, text="5")
btn6 = Button(frame_corpo, text="6")
btn7 = Button(frame_corpo, text="7")
btn8 = Button(frame_corpo, text="8")
btn9 = Button(frame_corpo, text="9")

janela.mainloop()