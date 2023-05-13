# Inventario-TI
Proyecto para Codigo facilito. inventario para área de informática y e intranet en el cual se integrara ademas un  servicio de tickets Helpdesk (en construcción)


Instrucciones para la ejecucion del programa
Cuentas de login:
 login: admin 
password: admin

Instrucciones:
descomprimir el archivo en el escritorio.
abrir una consola en cmd o terminal en linux
instalar virtualenv
pip install virtualenv env

digitar para abrir entorno virtual enviroment

env\Script\activate

instalar django en entorno virtual

pip install django

Realizar makemigrations y migrate

python manage.py makemigrations python manage.py migrate

Instalar las librerias necesarias en archivo "requeriments.txt"

pip install -r requirements.txt

Levantar el server

python manage.py runserver

Si desea ejecutar la aplicacion en algun IDE o editor de texto, debe realizar lo mismo.
Vistas URL (LOCAL)

http://127.0.0.1:8000/home

http://127.0.0.1:8000/accounts/login

http://127.0.0.1:8000/panel

http://127.0.0.1:8000/listarmonitores

http://127.0.0.1:8000/listarperifericos

http://127.0.0.1:8000/registro

