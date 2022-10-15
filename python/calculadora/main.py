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

# 1° Linha
btnClean = Button(frame_corpo, text="C", width=11, height=2)
btnClean.place(x=0, y=0)

btnPorcentagem = Button(frame_corpo, text="%", width=5, height=2)
btnPorcentagem.place(x=88)

btnDivisao = Button(frame_corpo, text="÷", width=5, height=2)
btnDivisao.place(x=177)

# 2° Linha
btn7 = Button(frame_corpo, text="7", width=5, height=2)
btn7.place(x=0, y=52)

btn8 = Button(frame_corpo, text="8", width=5, height=2)
btn8.place(x=59, y=52)

btn9 = Button(frame_corpo, text="9", width=5, height=2)
btn9.place(x=118, y=52)

btnMultiplicacao = Button(frame_corpo, text="x", width=5, height=2)
btnMultiplicacao.place(x=177, y=52)

# 3° Linha

btn4 = Button(frame_corpo, text="4", width=5, height=2)
btn4.place(x=0, y=104)

btn5 = Button(frame_corpo, text="5", width=5, height=2)
btn5.place(x=59, y=104)

btn6 = Button(frame_corpo, text="6", width=5, height=2)
btn6.place(x=118, y=104)

btnSubtracao = Button(frame_corpo, text="-", width=5, height=2)
btnSubtracao.place(x=177, y=104)


# 4° Linha

btn1 = Button(frame_corpo, text="1", width=5, height=2)
btn2 = Button(frame_corpo, text="2", width=5, height=2)
btn3 = Button(frame_corpo, text="3", width=5, height=2)
btnSoma = Button(frame_corpo, text="+", width=5, height=2)

# 5° Linha

btn0 = Button(frame_corpo, text="0", width=5, height=2)
btnPonto = Button(frame_corpo, text=".", width=5, height=2)
btnResultado = Button(frame_corpo, text="=", width=5, height=2)

janela.mainloop()