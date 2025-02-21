# Meu Blog

![Badge MIT License](https://img.shields.io/badge/License-MIT-green.svg)

Um sistema de blog simples desenvolvido com Flask e MySQL.

## 📌 Tecnologias Utilizadas

- Python (Flask)
- HTML, CSS e Bootstrap
- MySQL

## 🚀 Como Executar o Projeto

### 1. Clone o Repositório
```bash
git clone https://github.com/seuusuario/meu-blog.git
cd meu-blog
```

### 2. Configure o Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o Banco de Dados
- Crie um banco de dados MySQL chamado `blog`.
- Atualize as configurações do banco de dados no arquivo `config.py` se necessário.

### 5. Execute a Aplicação
```bash
python app.py
```
Acesse em [http://127.0.0.1:5000](http://127.0.0.1:5000).

## 📂 Estrutura do Projeto

```
meu-blog/
│-- templates/            # Arquivos HTML
│   ├── index.html        # Página inicial
│   ├── login.html        # Tela de login
│   ├── modelo.html       # Template base
│   ├── novopost.html     # Formulário para novo post
│   ├── novousuario.html  # Cadastro de usuários
│   ├── error404.html     # Página de erro 404
│-- static/               # Arquivos CSS, JS e imagens
│-- app.py                # Código principal do Flask
│-- config.py             # Configurações do banco de dados
│-- requirements.txt      # Dependências do projeto
│-- README.md             # Documentação do projeto
```

## 🔑 Autenticação
- O projeto possui autenticação de usuários.
- O administrador pode gerenciar usuários e postagens.
- Credenciais padrão do admin:
  - **E-mail:** adm@adm
  - **Senha:** Blog@dm123

## 📜 Licença
Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

