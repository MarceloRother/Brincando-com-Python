import tkinter as tk
from tkinter import ttk, PhotoImage

##* PARTE 1

#janela = tk.Tk()
#janela.geometry("300x200")
#janela.title("Uso de Labels")

## Criar um label
#label = tk.Label(janela, text="Aula de Labels")

## Empacotar o Label na janela
#label.pack()

## Loop principal
#janela.mainloop()

##* PARTE 2

# janela = tk.Tk()
# janela.geometry("300x200")
# janela.title("Uso de Labels")

## Mostrar um Label comum

# label1 = ttk.Label(
#     janela,
#     text= "Texto do Label 1",
#     font=("Arial", 18)
# )

# label1.pack(ipadx=10, ipady=30)

# # Segundo Label

# label2 = ttk.Label(
#     janela,
#     text="Texto do Label 2",
#     font=("Helvetica", 20),
#     foreground="blue"
# )

# label2.pack(ipadx=10, ipady=20)

# janela.mainloop()

##* PARTE 3 (Carregando Imagem)

def centralizar_imagem(event):
    largura_janela = janela.winfo_width()
    altura_janela = janela.winfo_height()
    largura_imagem = imagem.width()
    altura_imagem = imagem.height()

    posicao_x = (largura_janela - largura_imagem) // 2
    posicao_y = (altura_janela - altura_imagem) // 2

    lbl_imagem.place(x=posicao_x, y=posicao_y)

# Criar janela

janela = tk.Tk()
janela.title("Exibir Imagem")
#janela.geometry("400x250")

# Carregar Imagem
imagem = PhotoImage(file="gui/duck_life.png")

# Criar o Label e exibir a imagem
lbl_imagem = ttk.Label(janela, image=imagem)

# Centralizar imagem ao redirecionar janela
janela.bind("<Configure>", centralizar_imagem)

# Inserir o label na janela
lbl_imagem.pack()

# Adicionar Label comum
lbl_boson = ttk.Label(
    janela,
    text="Boson Treinamentos",
    foreground="purple",
    background="lightgreen",
    anchor="center",
    borderwidth=3,
    relief="groove"
)

# Loop principal
janela.mainloop()
