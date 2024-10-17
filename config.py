ambiente = "teste"
#CONFIG BANCO DE DADOS
if ambiente == "teste":
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'senai'
    DB_NAME = 'blog'

if ambiente == "produção":
    DB_HOST = 'PedroV1510.mysql.pythonanywhere-services.com'
    DB_USER = 'PedroV1510'
    DB_PASSWORD = 'Senai@2024'
    DB_NAME = 'PedroV1510$blog'

#CONFIG CHAVE SECRETA DE SESSÃO
SECRET_KEY = 'blog'

#SENHA DO ADM
MASTER_PASSWORD = 'Blog@dm123'
MASTER_EMAIL = 'adm@adm'


