import tkinter as tk
from tkinter import messagebox
import re

# Função para validar CPF
def validar_cpf(cpf):
    # Verificar se o CPF tem 11 dígitos e é composto apenas por números
    if len(cpf) == 11 and cpf.isdigit():
        return True
    else:
        return False

# Função para verificar e validar os dados do formulário
def verificar_login():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    idade = entry_idade.get()
    doencas = entry_doencas.get()
    cpf = entry_cpf.get()

    # Verificando se todos os campos obrigatórios estão preenchidos
    if nome and telefone and idade and cpf:
        # Validando o CPF
        if not validar_cpf(cpf):
            messagebox.showerror("Erro", "CPF inválido! O CPF deve ter 11 dígitos numéricos.")
            return
        # Se os dados forem válidos, abre a próxima interface
        abrir_proxima_tela(nome, telefone, idade, doencas, cpf)
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

# Função para abrir a próxima tela após o login
def abrir_proxima_tela(nome, telefone, idade, doencas, cpf):
    # Cria a janela da próxima tela
    proxima_tela = tk.Toplevel()  # Toplevel cria uma nova janela
    proxima_tela.title("Bem-vindo ao Evento")
    proxima_tela.geometry("500x400")
    
    # Adicionando uma mensagem simples de boas-vindas
    mensagem = f"Bem-vindo, {nome}!\nTelefone: {telefone}\nIdade: {idade}\nDoenças: {doencas}\nCPF: {cpf}"
    label_bem_vindo = tk.Label(proxima_tela, text=mensagem, font=("Arial", 14), justify="left")
    label_bem_vindo.pack(pady=20)

    # Botões para editar as informações
    btn_editar = tk.Button(proxima_tela, text="Editar Informações", font=("Arial", 14), bg="#FFD700", command=lambda: editar_informacoes(proxima_tela, nome, telefone, idade, doencas, cpf))
    btn_editar.pack(pady=10)

    # Botão para sair
    btn_sair = tk.Button(proxima_tela, text="Sair", font=("Arial", 14), bg="#FF6347", command=proxima_tela.destroy)
    btn_sair.pack(pady=10)

# Função para permitir a edição das informações
def editar_informacoes(proxima_tela, nome, telefone, idade, doencas, cpf):
    # Remover todos os widgets da tela anterior
    for widget in proxima_tela.winfo_children():
        widget.destroy()

    # Criar campos para edição das informações
    label_nome = tk.Label(proxima_tela, text="Nome:", font=("Arial", 14))
    label_nome.pack(pady=5)
    entry_nome = tk.Entry(proxima_tela, font=("Arial", 14))
    entry_nome.insert(0, nome)
    entry_nome.pack(pady=5)

    label_telefone = tk.Label(proxima_tela, text="Telefone:", font=("Arial", 14))
    label_telefone.pack(pady=5)
    entry_telefone = tk.Entry(proxima_tela, font=("Arial", 14))
    entry_telefone.insert(0, telefone)
    entry_telefone.pack(pady=5)

    label_idade = tk.Label(proxima_tela, text="Idade:", font=("Arial", 14))
    label_idade.pack(pady=5)
    entry_idade = tk.Entry(proxima_tela, font=("Arial", 14))
    entry_idade.insert(0, idade)
    entry_idade.pack(pady=5)

    label_doencas = tk.Label(proxima_tela, text="Doenças (se tiver):", font=("Arial", 14))
    label_doencas.pack(pady=5)
    entry_doencas = tk.Entry(proxima_tela, font=("Arial", 14))
    entry_doencas.insert(0, doencas)
    entry_doencas.pack(pady=5)

    label_cpf = tk.Label(proxima_tela, text="CPF:", font=("Arial", 14))
    label_cpf.pack(pady=5)
    entry_cpf = tk.Entry(proxima_tela, font=("Arial", 14))
    entry_cpf.insert(0, cpf)
    entry_cpf.pack(pady=5)

    # Botão para salvar as edições
    btn_salvar = tk.Button(proxima_tela, text="Salvar Alterações", font=("Arial", 14), bg="#4CAF50", command=lambda: salvar_alteracoes(proxima_tela, entry_nome, entry_telefone, entry_idade, entry_doencas, entry_cpf))
    btn_salvar.pack(pady=20)

# Função para salvar as edições
def salvar_alteracoes(proxima_tela, entry_nome, entry_telefone, entry_idade, entry_doencas, entry_cpf):
    # Obter os dados alterados
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    idade = entry_idade.get()
    doencas = entry_doencas.get()
    cpf = entry_cpf.get()

    # Validar novamente o CPF
    if not validar_cpf(cpf):
        messagebox.showerror("Erro", "CPF inválido! O CPF deve ter 11 dígitos numéricos.")
        return

    # Atualizar a tela com as novas informações
    mensagem = f"Bem-vindo, {nome}!\nTelefone: {telefone}\nIdade: {idade}\nDoenças: {doencas}\nCPF: {cpf}"
    label_bem_vindo = tk.Label(proxima_tela, text=mensagem, font=("Arial", 14), justify="left")
    label_bem_vindo.pack(pady=20)

    # Recriar botões
    btn_editar = tk.Button(proxima_tela, text="Editar Informações", font=("Arial", 14), bg="#FFD700", command=lambda: editar_informacoes(proxima_tela, nome, telefone, idade, doencas, cpf))
    btn_editar.pack(pady=10)
    btn_sair = tk.Button(proxima_tela, text="Sair", font=("Arial", 14), bg="#FF6347", command=proxima_tela.destroy)
    btn_sair.pack(pady=10)

# Criação da interface de login
root = tk.Tk()
root.title("Tela de Login - Evento para Idosos")
root.geometry("500x400")
root.config(bg="#f0f0f0")  # Cor de fundo suave para tornar a interface mais amigável

# Adicionando campos de entrada para os dados
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

label_doencas = tk.Label(root, text="Doenças (se tiver):", font=("Arial", 14))
label_doencas.pack(pady=10)
entry_doencas = tk.Entry(root, font=("Arial", 14))
entry_doencas.pack(pady=5)

label_cpf = tk.Label(root, text="CPF:", font=("Arial", 14))
label_cpf.pack(pady=10)
entry_cpf = tk.Entry(root, font=("Arial", 14))
entry_cpf.pack(pady=5)

# Botão para validar login e abrir a próxima tela
btn_entrar = tk.Button(root, text="Entrar", font=("Arial", 16), bg="#4CAF50", fg="white", command=verificar_login)
btn_entrar.pack(pady=20)

# Iniciar a interface gráfica
root.mainloop()