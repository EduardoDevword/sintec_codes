from tkinter import *

window =  Tk() # objeto janela classe TK 

val = " "
show = StringVar()  # para passar variaveis no tk deve se declarar o tipo dela 
cal= StringVar()


def get_value(num):
    global val 

    val = val + str(num)
    show.set(val)

def clean_screen():
    global val 

    val = " "
    show.set(val)

def calculate():
    global val 

    result = val 
    show.set(eval(result))


window.geometry("245x332") # primeira medida sera horizontal e a segunda vertical com 1920x1080 o valor maximo da tela
window.title("Calculadora")

icon = PhotoImage(file = "icon.png") # funcao que transforma imagem externa compaativel para a biblioteca TK

window.iconphoto(True, icon)
window.config(background= "#8F9696")

#style da calculadora 
screen= Label(window, textvariable= show, width=34, height= 2, bg="white")
screen.grid(row= 0, column=0)

div_corp=Frame(window, width= 245, height=283)
div_corp.grid(row=1, column=0)

# botoes 

# botoes das operacoes

clear=b1=Button(div_corp, command= clean_screen, text="C", width=27, height=3, bg='Red')  
clear.place(x=0 ,y=0)

div=  Button(div_corp, command= lambda : get_value("/"), text="/", width=5, height=3, bg='Orange')  # o comando lambda funciona como um def invisivel que o usuario não precisa definila 

div.place(x= 199,y=0) 

mult= Button(div_corp, command= lambda : get_value("*") ,text="*", width=5, height=3, bg='Orange')
mult.place(x= 199 ,y=57)

soma= Button(div_corp, command= lambda : get_value("+") ,text="+", width=5, height=3, bg='Orange')
soma.place(x= 199 ,y=113)

sub= Button(div_corp, command= lambda : get_value("-") ,text="-", width=5, height=3, bg='Orange')
sub.place(x= 199 ,y=169)

igual= Button(div_corp, command= calculate ,text="=", width=5, height=3, bg='Orange')
igual.place(x= 199 ,y=225)


# botoes numeros

b1=Button(div_corp, command= lambda : get_value("1") ,text="1", width=8, height=3)
b1.place(x= 0 ,y= 55)

b2=Button(div_corp, command= lambda : get_value("2") ,text="2", width=8, height=3)
b2.place(x=66, y=55)

b3=Button(div_corp, command= lambda : get_value("3") ,text="3", width=8, height=3)
b3.place(x=133, y=55)

b4=Button(div_corp, command= lambda : get_value("4") ,text="4", width=8, height=3)
b4.place(x=0, y=111)

b5=Button(div_corp, command= lambda : get_value("5") ,text="5", width=8, height=3)
b5.place(x=66, y=111)

b6=Button(div_corp, command= lambda : get_value("6") ,text="6", width=8, height=3)
b6.place(x=133, y=111)

b7=Button(div_corp, command= lambda : get_value("7") ,text="7", width=8, height=3)
b7.place(x=0, y=167)

b8=Button(div_corp, command= lambda : get_value("8") ,text="8", width=8, height=3)
b8.place(x=66, y=167)

b9=Button(div_corp, command= lambda : get_value("9") ,text="9", width=8, height=3)
b9.place(x=133  ,y=167)

b0=Button(div_corp, command= lambda : get_value("0") ,text="0", width=27, height=3)
b0.place(x=0, y=224)


window.mainloop() # funcao procipal para abrir a janela 