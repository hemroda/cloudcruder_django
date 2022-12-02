CloudCruder
===

## Setting up the app

Clone the repo.  

Make sure you have python3.11 installed. If not, run: `$ brew install python@3.11`  

Create virtual env `$ python3.11 -m venv .venv`  
Activate the virtual env `$ source .venv/bin/activate`  
Install the dependencies `$ pip install -r requirements.txt`  


## Running the app

### Running the servers
To start your servers:  
`$ python manage.py runserver` to run the django server.  


## Testing

Run `$ python manage.py test apps/*` . 
or `$ python manage.py test apps/name_of_th_app`  


Enjoy the headaches 😁
