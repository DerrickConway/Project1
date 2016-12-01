ID G00328406

Project1 for Data Representation and Querying.

Project Overview

I have created a Single-Page Web Application (SPA) that lets users log into the application and register themselves to the application. This application was selected for a Hit training program application:

download PostgreSQL http://www.enterprisedb.com/products-services-training/pgdownload#windows here is the link above to download, I installed the 32bit virsion when installed you must run it. You must make a password and username after installing serch for pgAdmin4 click on it under the browser section it will say PostgreSQL click on it then click on databases it will then prompt you to enter your password and username, then click on flaskIngo then Schemas then public then Tables then right click on user then View data and click on first 100 row

Flask Security Install flask security into your command prompt this is the command “pip install flask-security flask-sqlalchemy”

User guide To run application

you need to install Pycharm here is the web link to Pycharm
https://www.jetbrains.com/pycharm/specials/pycharm/pycharm.html?&gclid=CjwKEAiAjvrBBRDxm_nRusW3q1QSJAAzRI1t9dfzGn7L1nLY3VGVW03Xturb5mKzr_Q8Jc_hTHonaBoCs1_w_wcB&gclsrc=aw.ds.ds&dclid=CJyA28yc0dACFUyKdwodmI4EWQ and the latest version of python 3.5.2, you need virtual environment this come with python when installed, to do this you must use you command prompt, for me it was “virtualenv env” To get to this env file I need to go through PycharmProjects then into my project name in Pycharm for me it was Project1 from there you need to go into the directory just type the command dir and inside you will see the env you need to go into the env diredtory by just typing cd env then type dir after that to go into directory in there you should see a Scripts directory you need to go into that directory my typing cd scripts then dir in this directory you should see activate now just type activate to activate the env this is what it should look like on the left hand side is the environment that was created (env) C:\Users\User\PycharmProjects\Project1\env\Scripts>activate (env) C:\Users\User\PycharmProjects\Project1\env\Scripts>

Now install flask You should now install flask, use this command to install flask “pip install flask” Now you need to install flask SQLAlchemy just enter in your command prompt pip install Flask-SQLAlchemy in the command prompt you need to import the database, this is the command you need to enter into the command line “from Project1 import db” and then type “db.create_all()” if this does not work you need to install a database adapter next you’re going to need to download a wheel file, it is a database adapter, use this website http://www.lfd.uci.edu/~gohlke/pythonlibs/ and select psycopg2-2.6.2-cp35-cp35m-win32, copy the file and put it into the project file and go to the eventual averment file for me it’s the env file then go to lib, site-packages and past it in there, then from there go into your command prompt and cd into env, lib, site-pakages, and then “pip install psycopg2-2.6.2-cp35-cp35m-win32.whl” now go back to project file in command prompt and enter command “from project1 import db” and then enter “db.create_all()” and that should work you need to now install flask security in your command prompt wright, “pip install flask-security flask-sqlalchemy” but you might not need to install flask-sqlalchemy as it should already be installed.

To run application 
Now to run the application in the command prompt enter “python Project1.py” this activates web application, if you want to kill the web application you just enter into the command prompt Ctrl c to stop it, if it freezes then Ctrl c and then enter “python Project1.py”

In this application the user must register to use this HIT Workout application, after you enter your email address and password once you register it will be saved to the database. This is the web address URL http://127.0.0.1:5000/register to register. After that the user is logged in, to check your login works just enter into the web address URL http://127.0.0.1:5000/logout then enter http://127.0.0.1:5000/login and it will ask you to enter your user email address and password. And for the home page http://127.0.0.1:5000 where all the information is for your three week work out plan From there it gives you the information for the 3 week plan you should try out. Images,About, and how to contact me but could not get the contact me working properly so I hade to take it out last min, You can check the database to make sure it saved correctly. To check database follow these steps. Click on the following pgAdmin4, PostgreSQL 9.6 enter your password continue on to Databases my password is declanconn1 for database password , FlaskInfo, Schemas, Public, Tables, and right click on user, View data and select first 100 rows and your data should be there of your email address and password.

Problems with the project

Problems I encountered with the project is that when I register on the application it would give me a send error after I entered my details and would not send me back to the home page, I also had an error on contact form that I tried to design I could not get the data to send to my email database so at the last min I decided to delete it and leave it out.

Research for project 

I did a good bit of research for the project looking up tutorials on YouTube on how to connect database with a data base and and how to use bootstrap and what software to use in the end I decided to use Pycharm for my text and postgresql as my database as it was recommending in my research.
Here is where I found most of my research that helped me put the application together that I found on YouTube and on websites for database, bootstrap and flask
https://www.youtube.com/watch?v=PJK950Gp780
http://flask.pocoo.org/docs/0.11/patterns/sqlalchemy/
http://flask.pocoo.org/
http://getbootstrap.com/
http://www.w3schools.com/bootstrap/default.asp
https://pythonhosted.org/Flask-Security/




