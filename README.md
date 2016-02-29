# Sample python project to build web apps (using MySQL database)

### Setup instruction

1- Wamp/Lamp should be installed 

2- Open PhpMyAdmin, create new database named "test", import "db.sql" into newly created database

3- Install Python MySQL connector

Linux:

    $ sudo apt-get install python-mysql.connector
 
 Windows: follow [here](http://www.mysqltutorial.org/getting-started-mysql-python-connector)

4- Install werkzeug
 
 Linux:

    $ sudo apt-get install python-werkzeug
 
 Windows:
 
    easy_install Werkzeug or pip install Werkzeug
 
5- Install Jinja
 
 Linux:

    $ sudo apt-get install python-jinja2

 Windows:
 
    easy_install Jinja2 or pip install Jinja2

6- run main.py

then enter: "http://127.0.0.1:5000" in your web browser