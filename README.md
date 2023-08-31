# OpenClassrooms Projet P10

## Objectif
The young startup LITReview aims to market a product that allows a community of users to access or request book reviews on demand. The project's goal is to develop this web application using Django.

## Local Configuration
## Installation
SoftDesk, a collaborative software publishing company, has embarked on a new venture by introducing an application designed to efficiently address and track technical issues. This innovative solution, named SoftDesk Support, is tailored for B2B enterprises (Business to Business).
### Getting the project on your local machine.
1. Clone the repository to your local machine.
```bash
git clone https://github.com/xrobotzyh/OpenClassRoomsProjet_10.git
```
2.Navigate to the cloned directory.
```bash
cd OpenClassRoomsProjet_10
```

### Create a virtual environment
1.Create a virtual environment named "env".
```bash
python3 -m venv env
```

### Activate and install your virtual environment
Activate the newly created virtual environment "env".
```bash
source env/bin/activate
```
Install the packages listed in requirements.txt.
```bash
pip install -r requirements.txt
```

### Initialize the database
Perform a search for migrations.
```bash
python manage.py makemigrations
```
Apply the migrations.
```bash
python manage.py migrate
```

## Usage
### Start the serveur
```bash
python manage.py runserver
```
### Navigation
Access the site on your browser using the URL http://127.0.0.1:8000/

## Test
Use the following information to test
```bash
| User name             | password      |
|-----------------------|---------------|
| helpful               | 123456789/    | 

```

## Thanks!