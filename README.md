Maavita
===

## Setting up the app

Clone the repo.  

Make sure you have python3.10 installed. If not, run: `$ brew install python@3.10`  

Create virtual env `$ python3.10 -m venv .venv`  
Activate the virtual env `$ source .venv/bin/activate`  
Install the dependencies `$ pip install -r requirements.txt`  

cd into `/backend` folder and run `$ python manage.py tailwind install`


## Running the app

### Running the servers
To start your servers:  
`$ cd backend`  
`$ python manage.py runserver` to run the django server.  

Open a new tab, make sure you are in `backend/` then:  
`$ python manage.py tailwind start`  


### Environment variables

Make sure you are in `backend/` then:  
`$ cp .env-sample .env`  
After adding in the correct values you need to source the `.env` file to make those values available to the app:  
`$ source .env`  


Enjoy the headaches 😁
