import tkinter as tk

janela = tk.Tk()

janela.title("Janela Principal")

## Tamanho de inicializacao da janela
##janela.geometry("500x400+200+100")

## Cor de fundo da janela
janela.config(bg="lightblue")

## Tamanho maximo
##janela.maxsize(800,600)

## Tamanho minimo
##janela.minsize(300,200)

## Impossibilitar mudanca de tamanho
## janela.resizable(False, False)

## Janela em tela cheia
##janela.state('zoomed')

## Transparencia da janela
##janela.attributes('-alpha', 0.6)

## Mudar o icone da janela (obrigatorio ser .ico)
janela.iconbitmap('gui/python_94570.ico')

janela.mainloop()