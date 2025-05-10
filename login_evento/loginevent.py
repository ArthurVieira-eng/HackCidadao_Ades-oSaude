import tkinter as tk
from tkinter import messagebox
import mysql.connector
import re
import hashlib  # Usaremos hashlib para o exemplo de hashing (não é a melhor prática em produção)

# Função para validar número de telefone
def validar_telefone(telefone):
    padrao = r"^\d{10,11}$"  # Aceita números com 10 ou 11 dígitos
    return re.match(padrao, telefone)

# Função para validar email
def validar_email(email):
    padrao = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(padrao, email)

# Função para conectar ao banco de dados MySQL
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="teste10",  # Substitua se necessário
        database="registros"
    )

# Função para validar CPF
def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

# Função para hash da senha (usando SHA256 por simplicidade)
def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Função para salvar os dados no banco MySQL
def salvar_usuario(nome, telefone, idade, doencas, cpf, email, senha, remedio, horarios):
    try:
        conn = conectar()
        cursor = conn.cursor()

        # Verifica se o CPF já existe
        cursor.execute("SELECT * FROM usuarios WHERE cpf = %s", (cpf,))
        if cursor.fetchone():
            messagebox.showerror("Erro", "CPF já cadastrado!")
            return

        senha_hash = hash_senha(senha)  # Aqui estamos aplicando o hash na senha

        sql = """
        INSERT INTO usuarios (nome, telefone, idade, doencas, cpf, email, senha, remedio, horarios)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (nome, telefone, int(idade), doencas, cpf, email, senha_hash, remedio, horarios)
        cursor.execute(sql, valores)
        conn.commit()
        cursor.close()
        conn.close()
        print("Usuário salvo com sucesso!")
    except Exception as e:
        print("Erro ao salvar no banco:", e)
        messagebox.showerror("Erro", f"Erro ao salvar no banco de dados:\n{e}")

# Função para validar e processar os dados do formulário
def verificar_login():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    idade = entry_idade.get()
    doencas = entry_doencas.get()
    cpf = entry_cpf.get()
    email = entry_email.get()
    senha = entry_senha.get()  # Novo campo para senha
    remedio = entry_remedio.get()
    horarios = entry_horarios.get()

    if nome and telefone and idade and cpf and email and senha:
        if not validar_cpf(cpf):
            messagebox.showerror("Erro", "CPF inválido! O CPF deve ter 11 dígitos numéricos.")
            return
        
        if not validar_telefone(telefone):
            messagebox.showerror("Erro", "Telefone inválido! Insira um número com 10 ou 11 dígitos.")
            return
        
        if not validar_email(email):
            messagebox.showerror("Erro", "E-mail inválido! Insira um e-mail válido.")
            return

        # Garantir que "remedio" e "horarios" não estejam vazios
        if not remedio:
            remedio = "Não especificado"
        
        if not horarios:
            horarios = "Não especificado"
        
        salvar_usuario(nome, telefone, idade, doencas, cpf, email, senha, remedio, horarios)
        cadastro_concluido(nome, telefone, idade, doencas, cpf, email, remedio, horarios)
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios!")

# Função para exibir mensagem de cadastro concluído e perguntar sobre editar dados
def cadastro_concluido(nome, telefone, idade, doencas, cpf, email, remedio, horarios):
    messagebox.showinfo("Cadastro Concluído", f"Cadastro de {nome} realizado com sucesso!")
    
    resposta = messagebox.askyesno("Deseja Editar os Dados?", "Gostaria de editar seus dados?")
    if resposta:
        editar_informacoes(nome, telefone, idade, doencas, cpf, email, remedio, horarios)
    else:
        mostrar_dados(nome, telefone, idade, doencas, cpf, email, remedio, horarios)

# Função para exibir os dados em uma lista
def mostrar_dados(nome, telefone, idade, doencas, cpf, email, remedio, horarios):
    dados_tela = tk.Toplevel()
    dados_tela.title("Dados Cadastrados")
    dados_tela.geometry("500x400")
    dados_tela.config(bg="#f0f0f0")

    lista_dados = [
        f"Nome: {nome}",
        f"Telefone: {telefone}",
        f"Idade: {idade}",
        f"Doenças: {doencas}",
        f"CPF: {cpf}",
        f"E-mail: {email}",
        f"Remédio: {remedio}",
        f"Horário do Remédio: {horarios}"
    ]

    listbox = tk.Listbox(dados_tela, font=("Arial", 12), height=10, width=50)
    for item in lista_dados:
        listbox.insert(tk.END, item)
    listbox.pack(pady=20)

    tk.Button(dados_tela, text="Fechar", font=("Arial", 14), bg="#FF6347", command=dados_tela.destroy).pack(pady=10)

# Função para editar os dados
def editar_informacoes(nome, telefone, idade, doencas, cpf, email, remedio, horarios):
    proxima_tela = tk.Toplevel()
    proxima_tela.title("Editar Dados")
    proxima_tela.geometry("500x600")
    proxima_tela.config(bg="#f0f0f0")

    def salvar_alteracoes():
        novo_nome = entry_nome.get()
        novo_telefone = entry_telefone.get()
        nova_idade = entry_idade.get()
        novas_doencas = entry_doencas.get()
        novo_cpf = entry_cpf.get()
        novo_email = entry_email.get()
        novo_remedio = entry_remedio.get()
        novo_horario = entry_horarios.get()

        if not validar_cpf(novo_cpf):
            messagebox.showerror("Erro", "CPF inválido! O CPF deve ter 11 dígitos numéricos.")
            return

        mensagem = (
            f"Dados atualizados:\n{novo_nome}\nTelefone: {novo_telefone}\nIdade: {nova_idade}\n"
            f"Doenças: {novas_doencas}\nCPF: {novo_cpf}\nRemédio: {novo_remedio}\nHorário: {novo_horario}"
        )
        messagebox.showinfo("Dados Atualizados", mensagem)
        mostrar_dados(novo_nome, novo_telefone, nova_idade, novas_doencas, novo_cpf, novo_email, novo_remedio, novo_horario)

    # Campos editáveis
    entry_nome = criar_campo_rotulado("Nome:", nome)
    entry_telefone = criar_campo_rotulado("Telefone:", telefone)
    entry_idade = criar_campo_rotulado("Idade:", idade)
    entry_doencas = criar_campo_rotulado("Doenças (se tiver):", doencas)
    entry_cpf = criar_campo_rotulado("CPF:", cpf)
    entry_email = criar_campo_rotulado("E-mail:", email)
    entry_remedio = criar_campo_rotulado("Remédio:", remedio)
    entry_horarios = criar_campo_rotulado("Horário do Remédio:", horarios)

    tk.Button(proxima_tela, text="Salvar Alterações", font=("Arial", 14), bg="#4CAF50", fg="white", command=salvar_alteracoes).pack(pady=20)

# Interface principal
root = tk.Tk()
root.title("Tela de Cadastro - Evento de Saúde")
root.geometry("500x600")
root.config(bg="#f0f0f0")

# Função para criar o campo rotulado
def criar_campo_rotulado(texto):
    label = tk.Label(root, text=texto, font=("Arial", 12), bg="#f0f0f0")
    label.grid(sticky="w", padx=20, pady=5)
    entrada = tk.Entry(root, font=("Arial", 12))
    entrada.grid(sticky="w", padx=20, pady=5)
    return entrada

# Campos do formulário
entry_nome = criar_campo_rotulado("Nome:")
entry_telefone = criar_campo_rotulado("Telefone:")
entry_idade = criar_campo_rotulado("Idade:")
entry_doencas = criar_campo_rotulado("Doenças (se tiver):")
entry_cpf = criar_campo_rotulado("CPF:")
entry_email = criar_campo_rotulado("E-mail:")
entry_senha = criar_campo_rotulado("Senha:")
entry_remedio = criar_campo_rotulado("Remédio:")
entry_horarios = criar_campo_rotulado("Horário do Remédio:")

# Botão de cadastro
tk.Button(root, text="Cadastrar", font=("Arial", 16), bg="#4CAF50", fg="white", command=verificar_login).grid(padx=20, pady=20)

root.mainloop() 

