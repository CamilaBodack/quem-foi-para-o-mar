# quem-foi-para-o-mar

Projet with details of fisherman that left to work in the sea.


## Running the project

- Docker on linux

Open prompt in the root of project and execute the following commands:

```
docker-compose build
docker-compose run web python manage.py createsuperuser
docker-compose up
``

- Available in http://127.0.0.1:8000/admin/
- Login with created user


## Demo da aplicação:

-  Demo disponível em:

- https://obscure-sands-75237.herokuapp.com/

- Without docker:

- Install requirements-dev.txt
- In root of project run:

```python manage.py runserver
``

- Available in http://127.0.0.1:8000/index/
