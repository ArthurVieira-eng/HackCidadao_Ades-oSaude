import tkinter as tk
from tkinter import messagebox

# Função para validar CPF
def validar_cpf(cpf):
    return len(cpf) == 11 and cpf.isdigit()

# Função para abrir o menu principal após o login
def abrir_menu(nome, telefone, idade, cpf):
    menu_tela = tk.Toplevel()
    menu_tela.title("Menu Principal")
    menu_tela.geometry("600x400")
    
    # Exibir as informações do usuário (sem doenças)
    label_info_usuario = tk.Label(menu_tela, text=f"Nome: {nome}\nIdade: {idade}\nTelefone: {telefone}\nCPF: {cpf}",
                                  font=("Arial", 14), justify="left")
    label_info_usuario.pack(pady=20)

    # Botões do menu
    btn_remedios = tk.Button(menu_tela, text="Adicionar Remédios", font=("Arial", 14), bg="#4CAF50", fg="white",
                             command=lambda: adicionar_remedios(menu_tela, nome, telefone, idade, cpf))
    btn_remedios.pack(pady=10)

    btn_horarios = tk.Button(menu_tela, text="Horários dos Remédios", font=("Arial", 14), bg="#4CAF50", fg="white",
                             command=lambda: adicionar_horarios(menu_tela, nome, telefone, idade, cpf))
    btn_horarios.pack(pady=10)

    btn_sair = tk.Button(menu_tela, text="Sair", font=("Arial", 14), bg="#FF6347", command=menu_tela.destroy)
    btn_sair.pack(pady=10)

# Função para adicionar remédios
def adicionar_remedios(menu_tela, nome, telefone, idade, cpf):
    for widget in menu_tela.winfo_children():
        widget.destroy()

    label_titulo = tk.Label(menu_tela, text="Adicionar Remédios", font=("Arial", 16))
    label_titulo.pack(pady=20)

    label_remedio = tk.Label(menu_tela, text="Digite seus remédios (separados por vírgula):", font=("Arial", 14))
    label_remedio.pack(pady=10)
    entry_remedios = tk.Entry(menu_tela, font=("Arial", 14))
    entry_remedios.pack(pady=5)

    def salvar_remedios():
        remedios = entry_remedios.get()
        messagebox.showinfo("Sucesso", f"Remédios adicionados: {remedios}")
        abrir_menu(nome, telefone, idade, cpf)

    btn_salvar = tk.Button(menu_tela, text="Salvar Remédios", font=("Arial", 14), bg="#4CAF50", fg="white",
                           command=salvar_remedios)
    btn_salvar.pack(pady=20)

# Função para adicionar horários aos remédios
def adicionar_horarios(menu_tela, nome, telefone, idade, cpf):
    for widget in menu_tela.winfo_children():
        widget.destroy()

    label_titulo = tk.Label(menu_tela, text="Horários dos Remédios", font=("Arial", 16))
    label_titulo.pack(pady=20)

    label_horarios = tk.Label(menu_tela, text="Defina os horários para seus remédios:", font=("Arial", 14))
    label_horarios.pack(pady=10)

    label_remedios = tk.Label(menu_tela, text="Digite os horários correspondentes a cada remédio (separados por vírgula):", font=("Arial", 14))
    label_remedios.pack(pady=10)
    entry_horarios = tk.Entry(menu_tela, font=("Arial", 14))
    entry_horarios.pack(pady=5)

    def salvar_horarios():
        horarios = entry_horarios.get()
        messagebox.showinfo("Sucesso", f"Horários definidos: {horarios}")
        abrir_menu(nome, telefone, idade, cpf)

    btn_salvar = tk.Button(menu_tela, text="Salvar Horários", font=("Arial", 14), bg="#4CAF50", fg="white",
                           command=salvar_horarios)
    btn_salvar.pack(pady=20)