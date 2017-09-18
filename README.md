# Boi na linha desafio tecnico
technical challenge.
***
[ONLINE VERSION, CHECK OUT!](https://boi-na-linha.herokuapp.com/ "click to see more")

# Instructions for online version
##### to access site admin [admin page](https://boi-na-linha.herokuapp.com/admin "click to see more")
###  obs: only users with staff / superuser status can access the admin page
##### to create a user on the site access [register page](https://boi-na-linha.herokuapp.com/register/ "click to see more")

###  obs'': it is only possible to add new items and list the items that already exist on the site being logged in
***
***
##### preparing the environment to run the project locally


1. If virtualenv has not installed install using:
 ```
sudo pip install -U pip setuptools virtualenv
 ```
2. Creating virtualenv:
 ```
virtualenv <venvs_path>/boiEnv/ -p python2.7
 ```
 
 - *venvs_path* - This is the directory where all your virtual environments have been, for example: / opt / venvs /
 
 
3. Clone the repository:
 ```
 git clone https://github.com/henriquemsouza/Boi-na-linha-desafio.git
 ```
 
 4. Activate your virtualenv with the command:
 ```
 source <venvs_path/boiEnv/bin/activate
 ```
 5. Inside the <projects_path> / Boi na Linha Desafio / folder, install all dependencies:
 ```
 pip install -U pip && pip install -r requirements.txt
 ```
## create postgres database
 
* sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
* sudo su - postgres
*createdb mydb
*createuser -P myuser
*pass 12345678
*psql mydb
The following command defines access rights for the new user.
* GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;

* \q
 ```
 put postgres database in settings.py>DATABASES
  ```
