# quem-foi-para-o-mar

Projet with details of fisherman that left to work in the sea.


# Demo:

- https://quem-esta-no-mar.herokuapp.com/index/

## Running the project


- Docker on linux

Open prompt in the root of project and execute the following commands:

```
docker-compose build
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
docker-compose up
```

- Available in http://127.0.0.1:8000/admin/
- Login with created user

- Without docker:

- Install requirements-dev.txt
- In root of project run:

- Without docker:

**better run this project inside virtualenv**
- Install requirements.txt
- In root of project run:

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
- Available in http://127.0.0.1:8000/index/

## Tests

- In root DIR, open console and run:

```
python manage.py test
```

