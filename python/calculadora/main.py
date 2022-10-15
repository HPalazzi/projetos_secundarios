from tkinter import *
from tkinter import ttk

## Cores:
cor1 = "#000000" #Preto 
cor2 = "#fcfafa" #Branco 
cor3 = "#5F6368" #Cinza
cor4 = "#3C4043" #Laranja
cor5 = "#63E000" #Verde

janela =  Tk()
janela.title("Calculadora Python")
janela.geometry("235x340")
janela.config(bg=cor1)

## Dividindo a tela em Frames
frame_resultado = Frame(janela, width=235, height=80, bg=cor1)
frame_resultado.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=cor1)
frame_corpo.grid(row=1, column=0)

## Criando Labels

app_label = Label(frame_resultado, text="0", width=16, height=3, padx=20, pady=5, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 16'), bg=cor1, fg=cor5)
app_label.place(x=0, y=0)

## Criando Btn
# 1° Linha
btnClean = Button(frame_corpo, text="C", width=11, height=2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE, bg=cor3)
btnClean.place(x=0, y=0)

btnPorcentagem = Button(frame_corpo, text="%", width=5, height=2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE, bg=cor3)
btnPorcentagem.place(x=118)

btnDivisao = Button(frame_corpo, text="÷", width=5, height=2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE, bg=cor4)
btnDivisao.place(x=177)

# 2° Linha
btn7 = Button(frame_corpo, text="7", width=5, height=2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE, bg=cor3)
btn7.place(x=0, y=52)

btn8 = Button(frame_corpo, text="8", width=5, height=2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE, bg=cor3)
btn8.place(x=59, y=52)

btn9 = Button(frame_corpo, text="9", width=5, height=2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE, bg=cor3)
btn9.place(x=118, y=52)

btnMultiplicacao = Button(frame_corpo, text="x", width=5, height=2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE, bg=cor4)
btnMultiplicacao.place(x=177, y=52)

# 3° Linha

btn4 = Button(frame_corpo, text="4", width=5, height=2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE, bg=cor3)
btn4.place(x=0, y=104)

btn5 = Button(frame_corpo, text="5", width=5, height=2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE, bg=cor3)
btn5.place(x=59, y=104)

btn6 = Button(frame_corpo, text="6", width=5, height=2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE, bg=cor3)
btn6.place(x=118, y=104)

btnSubtracao = Button(frame_corpo, text="-", width=5, height=2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE, bg=cor4)
btnSubtracao.place(x=177, y=104)


# 4° Linha

btn1 = Button(frame_corpo, text="1", width=5, height=2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE, bg=cor3)
btn1.place(x=0, y=156)

btn2 = Button(frame_corpo, text="2", width=5, height=2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE, bg=cor3)
btn2.place(x=59, y=156)

btn3 = Button(frame_corpo, text="3", width=5, height=2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE, bg=cor3)
btn3.place(x=118, y=156)

btnSoma = Button(frame_corpo, text="+", width=5, height=2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE, bg=cor4)
btnSoma.place(x=177, y=156)

# 5° Linha

btn0 = Button(frame_corpo, text="0", width=11, height=2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE, bg=cor3)
btn0.place(x=0, y=208)

btnPonto = Button(frame_corpo, text=".", width=5, height=2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE, bg=cor3)
btnPonto.place(x=118, y=208)

btnResultado = Button(frame_corpo, text="=", width=5, height=2, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE, bg=cor4)
btnResultado.place(x=177, y=208)

janela.mainloop()