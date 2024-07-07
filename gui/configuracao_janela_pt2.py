import tkinter as tk

def abrir_segunda_janela():
    segunda_janela = tk.Toplevel()
    segunda_janela.title("Segunda Janela")
    segunda_janela.config(bg='red')

    # Tamanho da janela
    largura_janela = 300
    altura_janela = 200

    # Obter dimensoes da tela do monitor
    largura_tela = segunda_janela.winfo_screenwidth()
    altura_tela = segunda_janela.winfo_screenwidth()

    # Calcular as coordenadas para centralizar a janela 2
    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2

    # Definir a geometria da janela 2
    segunda_janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

# Criar janela principal
janela_principal = tk.Tk()
janela_principal.title("Janela Principal")
janela_principal.geometry("600x500")

# Configurar evento de clique na janela principal
janela_principal.bind("<Button-1>", lambda event: abrir_segunda_janela())

# MainLoop
janela_principal.mainloop()