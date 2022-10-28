Maavita
===

## Setting up the app

Clone the repo.  

Make sure you have python3.10 installed. If not, run: `$ brew install python@3.10`  

Create virtual env `$ python3.10 -m venv .venv`  
Activate the virtual env `$ source .venv/bin/activate`  
Install the dependencies `$ pip3.10 install -r requirements.txt`  


## Running the app

To start your servers:  
`$ cd backend`  
`$ python manage.py runserver` to run the django server.  

Open a new tab, make sure you are in `src/` then:  
`$ python manage.py tailwind start`  

Enjoy the headaches 😁
