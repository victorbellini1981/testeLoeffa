# testeLoeffa
É preciso ter o python instalado e o django, caso não tenha vc pode baixar o python no site: https://www.python.org/downloads/ e
logo após baixá-lo abra o cmd do computador e rode o comando pip install django.
Crie uma conexão localhost mysql na porta 3306 e nessa conexão crie um database chamado loeffa com o usuário root e a senha 123456.
Clone este repositório em uma pasta em seu computador, abra o cmd, entre na pasta do projeto e rode os seguintes comandos para criar as tabelas no banco de dados:
python manage.py makemigrations 
python manage.py migrate
Agora rode esse comando para executar o servidor:
python manage.py runserver
Acesse o aplicativo digitando localhost:8000/mostrar
Não terá nenhum registro, porém é só clicar em cadastrar que aparecerá a tela de cadastro e após efetuar o cadastro aparecerá na lista de funcionários e também aparecerá um botão para editar ou excluir o cadastro.
