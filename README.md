# Boi-na-linha-desafio
d

sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
sudo su - postgres

createdb mydb
createuser -P myuser
pass 12345678

acess
psql mydb

 comando a seguir define direito de acesso ao novo usuário.
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;

\q

https://boi-na-linha.herokuapp.com/
