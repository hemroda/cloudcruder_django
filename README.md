CloudCruder
===

## Setting up the app

Clone the repo.  

First run `$ docker-compose build`  


## Running the app

Run `$ docker-compose up` then open a browser to `http://127.0.0.1:8000/`  


Enjoy the headaches 😁


## How to

#### Create apps

Create an empty folder with the apps name first in `backend/apps/name_of_the_app` then run:  
`$ docker-compose run --rm app sh -c "python manage.py startapp name_of_the_app ./apps/name_of_the_app"`


#### Makemigrations 

`$ docker-compose run --rm app sh -c "python manage.py makemigrations"`


#### Run Migrations

`$ docker-compose run --rm app sh -c "python manage.py migrate"`