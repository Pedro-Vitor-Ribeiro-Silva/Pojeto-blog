ambiente = "teste"
#CONFIG BANCO DE DADOS
if ambiente == "teste":
    DB_HOST = 'localhost'
    DB_USER = 'ENDEREÇO DA HOST DO BANCO'
    DB_PASSWORD = 'SENHA DO BANCO'
    DB_NAME = 'NOME DO BANCO'

if ambiente == "produção":
    DB_HOST = 'ENDEREÇO DA HOST DO BANCO'
    DB_USER = 'NOME USUARIO'
    DB_PASSWORD = 'SENHA DO BANCO'
    DB_NAME = 'NOME DO BANCO'

#CONFIG CHAVE SECRETA DE SESSÃO
SECRET_KEY = 'blog'

#SENHA DO ADM
MASTER_PASSWORD = 'Blog@dm123'
MASTER_EMAIL = 'adm@adm'


