from tkinter import *
from tkinter import ttk

# Cores:
cor1 = "#04080F" #Preto 
cor2 = "#EAF2EF" #Branco 
cor3 = "#6B818C" #Cinza

janela =  Tk()
janela.title("Calculadora Python")
janela.geometry("235x318")
janela.config(bg=cor1)

# Dividindo a tela em Frames
frame_resultado = Frame(janela, width=235, height=50, bg=cor1)
frame_resultado.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Criando btn

btnClean = Button(frame_corpo, text="C", width=11, height=2)
btnClean.place(x=0, y=0)

btnPorcentagem = Button(frame_corpo, text="%", width=11, height=2)
btnPorcentagem.place(x=118,y=0)

btnDivisao = Button(frame_corpo, text="÷", width=11, height=2)
btnDivisao.place(x=177)

btnSoma = Button(frame_corpo, text="+")
btnSubtracao = Button(frame_corpo, text="-")
btnMultiplicacao = Button(frame_corpo, text="X")
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