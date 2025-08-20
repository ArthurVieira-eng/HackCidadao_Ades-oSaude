# 🏥 Hack Cidadão - Adesão à Saúde

**HackCidadao_Ades-oSaude** é um sistema desenvolvido em Python com interface gráfica (Tkinter) e banco de dados MySQL, criado para promover **a adesão correta de idosos com doenças crônicas ao uso de medicações**. 

O projeto nasceu no contexto de um **evento de inovação cívica**, com foco em **saúde pública** e **inclusão digital**, buscando facilitar o acompanhamento do tratamento de idosos por meio de registros organizados e lembretes personalizados. Além disso, o sistema prevê a ideia de **benefícios e recompensas** como incentivo para quem segue corretamente os horários e prescrições médicas.

---

## 🎯 Objetivo

- Facilitar o acompanhamento do uso de medicamentos por **idosos com doenças crônicas**
- **Motivar a adesão correta ao tratamento** por meio de feedbacks e registros
- Criar um **ambiente digital acessível e funcional**, que possa ser usado por agentes de saúde ou familiares
- Registrar informações médicas essenciais de forma segura e estruturada
- Permitir **benefícios sociais** (como descontos em farmácias ou bônus em programas de saúde pública) baseados na adesão comprovada

---

## 🧠 Funcionalidades

- **Cadastro Completo de Pacientes:** Nome, idade, telefone, CPF, e-mail, doenças preexistentes e senha (com hash).
- **Validações Automáticas:** CPF, telefone, e-mail e campos obrigatórios são verificados.
- **Interface Gráfica com Tkinter:** Simples e acessível, pensada para usabilidade por pessoas com pouca familiaridade com tecnologia.
- **Registro de Remédios e Horários:** O usuário informa quais medicamentos está tomando e os respectivos horários.
- **Consulta e Edição de Dados:** Visualização completa dos dados e possibilidade de alterá-los com facilidade.
- **Sistema de Benefícios (em proposta):** Usuários que mantiverem o controle atualizado e correto podem ser premiados com recompensas sociais ou comunitárias.

---

## 💻 Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Interface Gráfica:** Tkinter
- **Banco de Dados:** MySQL (via MySQL Connector)
- **Bibliotecas Extras:** `hashlib`, `re`, `messagebox`

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/ArthurVieira-eng/HackCidadao_Ades-oSaude.git
   cd HackCidadao_Ades-oSaude
2. **Instale as dependências:**

pip install mysql-connector-python

3. **Configure o banco de dados MySQL:**

Crie o banco de dados MySQL ou de sua preferência: 

4. **Execute o sistema:** 

python nome_do_arquivo.py 

## 🦴 Estrutura de Dados

Paciente:

telefone:

idade:

doenças:

cpf:

email:

senha (com hash SHA-256):

remédio(s):

horário(s):

## 👓 Interface Gráfica

Tela de cadastro com validação dos campos

Menu principal com opções de:

Adicionar/remover remédios

Definir horários

Visualizar dados cadastrados

Editar informações pessoais

Feedback ao usuário com messagebox 

## 📖 Sobre o Projeto

Este projeto foi desenvolvido por estudantes e entusiastas de tecnologia durante o Hack Cidadão, com o intuito de criar uma ferramenta útil para a inclusão social na saúde. Ele propõe um modelo funcional que pode ser expandido futuramente com:

Notificações automáticas por SMS ou e-mail

Integração com sistemas de saúde pública

Painéis de monitoramento para agentes de saúde

Gamificação ou ranking por adesão 

## 💎 Contatos: 

**Email:** arthurv.o.2507@gmail.com

**LinkedIn:** Link: https://www.linkedin.com/in/arthur-vieira-arruda-de-oliveira-769461312/
