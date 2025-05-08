import tkinter as tk
from tkinter import messagebox
from MenuPrincipal import abrir_menu, validar_cpf

def verificar_login():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    idade = entry_idade.get()
    cpf = entry_cpf.get()

    if nome and telefone and idade and cpf:
        if not validar_cpf(cpf):  # Aqui o CPF já é validado corretamente
            messagebox.showerror("Erro", "CPF inválido! O CPF deve ter 11 dígitos numéricos.")
            return
        
        # Fecha a janela de login antes de abrir o menu
        root.destroy()
        
        # Chama a função para abrir o menu principal
        abrir_menu(nome, telefone, idade, cpf)
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

# Criação da interface de login
root = tk.Tk()
root.title("Tela de Login - Evento para Idosos")
root.geometry("500x350")
root.config(bg="#f0f0f0")

# Campos de entrada
label_nome = tk.Label(root, text="Nome:", font=("Arial", 14))
label_nome.pack(pady=10)
entry_nome = tk.Entry(root, font=("Arial", 14))
entry_nome.pack(pady=5)

label_telefone = tk.Label(root, text="Telefone:", font=("Arial", 14))
label_telefone.pack(pady=10)
entry_telefone = tk.Entry(root, font=("Arial", 14))
entry_telefone.pack(pady=5)

label_idade = tk.Label(root, text="Idade:", font=("Arial", 14))
label_idade.pack(pady=10)
entry_idade = tk.Entry(root, font=("Arial", 14))
entry_idade.pack(pady=5)

label_cpf = tk.Label(root, text="CPF:", font=("Arial", 14))
label_cpf.pack(pady=10)
entry_cpf = tk.Entry(root, font=("Arial", 14))
entry_cpf.pack(pady=5)

btn_entrar = tk.Button(root, text="Entrar", font=("Arial", 16), bg="#4CAF50", fg="white", command=verificar_login)
btn_entrar.pack(pady=20)

root.mainloop()