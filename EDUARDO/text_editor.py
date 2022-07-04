import os 
import tkinter as tk
from tkinter import YView, ttk
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

# import tkinter.font as tkFont
from ttkthemes import ThemedStyle 

def changue_color():
    color = colorchooser.askcolor()[1]
    text_area.config(fg = color)

def changue_font(*args):
    text_area.config(font = (name_font.get(), font_size.get()))
    
def new_file(): 
    pass

def open_file():
    text_area.delete(1.0, tk.END)
    file = filedialog.askopenfilename(initialdir= "C:\\Users\\Eduardo Marmentini\\Desktop\\arquivos")
    file=open(file,"r")
    text_area.insert(1.0, file.read())
    file.close()

def save_file():

    txt = text_area.get(1.0, tk.END)
    filepath= filedialog.asksaveasfilename(defaultextension = ".txt",
                                           filetypes = [("Arquivo TXT",".txt"),("Arquivo HTML", ".html"),
                                           ("Arquivo TIFF",".tiff"),
                                           ("Arquivo CSV", ".csv"),
                                           ("Arquivo WORD", ".doc")])


    file = open(filepath, "w")
    file.write(txt)
    file.close()

def copy():
    text_area.event_generate("<<Copy>>")

def cut ():
    text_area.event_generate("<<Cut>>")

def paste():
    text_area.event_generate("<<Paste>>")

def help():
    showinfo("Creditos do programa","Esse editor de texto foi desenvolvido pelos alunos do SINTEC")

root = tk.Tk()
root.title("SINTEC Text Editor")

style = ThemedStyle(root)
style.set_theme('breeze')

# root_width = 500
# root_height = 500

# screen_width = root.winfo_screenwidth()
# screen_heigth = root.winfo_screenheight()

# x = int((screen_width/2)-(root_width/2))
# y = int((screen_heigth/2)-(root_height/2))

root.geometry("500x500")

# #lista de fontes
# list_fontes = list(tkFont.families())
# print(list_fontes)

#definindo a fonte do texto do editor
name_font = tk.StringVar(root)
name_font.set("Arial")

#definindo tamanho do texto do editor
font_size = tk.StringVar(root)
font_size.set("25")

#area para o texto do editor
text_area = tk.Text(root, font = (name_font.get(),font_size.get()))

#barra de rolagem
scrool_bar = ttk.Scrollbar(text_area)
scrool_bar.configure(command = text_area.yview)
root.grid_rowconfigure(0, weight = 1)
root.grid_columnconfigure(0, weight = 1)

text_area.grid(sticky = tk.N+tk.E+tk.S+tk.W)
scrool_bar.pack(side = tk.RIGHT, fill = tk.Y)
text_area.config(yscrollcommand=scrool_bar.set)

#criando frames 
frame = ttk.Frame(root)
frame.grid()

#criando botoes
button_color = ttk.Button(frame, text = "Changue color", command = changue_color)
button_color.grid(row = 0, column = 0)

#menu das fontes
fonts_menu = ttk.OptionMenu(frame, name_font, *font.families(), command= changue_font)
fonts_menu.grid(row = 0, column = 1)

#manipulador de tamanho
spinbox = ttk.Spinbox(frame, text= font_size, from_= 1, to = 100, command= changue_font)
spinbox.grid(row = 0, column = 2)


#barra para os menus
bar_menu = tk.Menu(root)

#menu de novo arquivo
files_menu = tk.Menu(bar_menu, tearoff=0)
files_menu.add_command(label="New", command = new_file)
files_menu.add_command(label="Open", command= open_file)
files_menu.add_command(label="Save", command= save_file)

files_menu.add_separator()

files_menu.add_command(label="Exit", command= root.destroy)
bar_menu.add_cascade(label = "File", menu=files_menu)

root.config(menu=bar_menu)  

#menu de editar 
editmenu = tk.Menu(bar_menu, tearoff=0)
editmenu.add_command(label="Cut", command= cut)
editmenu.add_command(label="Copy", command= copy)
editmenu.add_command(label="Paste", command= paste)
bar_menu.add_cascade(label="Edit", menu= editmenu)

#menu de help
helpmenu = tk.Menu(bar_menu, tearoff=0)
bar_menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Information", command= help)

root.mainloop()