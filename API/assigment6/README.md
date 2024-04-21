# FastAPI - Docker - SQLALCHEMY

# Description : 

FastAPI works with any database and any style of library to talk to the database.A common pattern is to use an "ORM": an "object-relational mapping" library.
Common ORMs are for example: Django-ORM (part of the Django framework), SQLAlchemy ORM (part of SQLAlchemy, independent of framework) and Peewee (independent of framework), among others.
in this priject we use SQLAlchemy.

# How to run :
+ ## Beginner mode : 
```
uvicorn main:app --reload
```
then open ``` http://127.0.0.1:8000/docs ``` in your browser and test all of it's methods .

+ ## Expert mode :

+ 1- docker pull postgres
+ 2- docker run :
```
docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=ramze_akbar_agha -e POSTGRES_USER=akbar_agha -e POSTGRES_DB=database_akbar_agha -d postgres

```
+ 3_ test in local system : ``` uvicorn university:app --reload ```


+ ## Deploy-liara :

+ 1- upload database in liara : 
<br> first we create a [postgres database](https://console.liara.ir/databases/create) 

SQLALCHEMY_DATABASE_URL  =  "postgresql://root:VNBfwH6bUSEcOi8PyWzi3LLb@university-db:5432/postgres"

+ 2- upload docker in project : https://assigment6.liara.run
<br> :

![img](image/result1.png)














+


