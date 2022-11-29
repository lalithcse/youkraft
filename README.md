# README #

Youkraft's tasks of Django Rest API


## Get the application ##
To get the application, please pull this repo and checkout to master branch 
which is default. 

    > git clone https://github.com/lalithcse/youkraft.git
    
#### Setup project

To run the django project, first we need to create virtualenv and 
activate it. Install all the packages with requirements.txt. Then we 
need to apply the migrations. 
I have done this already for the given database connection. Below steps are 
required only if the database connection is different.

    > python manage.py makemigrations
    > python manage.py migrate
    
Once complete above steps, then we can run the django server.
 
    > python manage.py runserver
