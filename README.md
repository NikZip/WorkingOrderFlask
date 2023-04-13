<p align="center">
      <img src="https://res.cloudinary.com/practicaldev/image/fetch/s--ukvXO23M--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9o96xdyd1m0arnk1gq9k.png" width="500">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/App%20Version-v1.0-red" alt="App Version">
   <img src="https://img.shields.io/badge/Flask%20Version-2.2-red" alt="Flask Version">
   <img src="https://img.shields.io/badge/License-MIT-red" alt="License">
</p>

# About

This is simple flask app that i did while doing an internship in the company. It supposed to run on terminals in IPOPAT company.

In this project:
+ Factory flask app
+ SQLAlchemy + PostgreSQL
+ Testing app and models with pytest
+ Running app with Docker


# Install

0. Before doing all of this you need:

+ Installed Docker and some database

1. Clone the repository or download the zip file

```
git clone https://github.com/NikZip/WorkingOrderFlask
```

2. Setup **`.env`** by renaming .env_template file and setting up params

**`SECRET_KEY`** - your secret key for app

**`FLASK_DEBUG`** - set it to 0 to use production config and to 1 if you wanna use dev config

**`DATABASE`** - set your database options: engine, user, pass and etc 


3. Docker:

```
docker-compose up --build
```
4. Without Docker
```
pip install -r requirements.txt
```

5. To run test start **`run_test.py`** file
**``**

# Documentation

## File structure 
```
Project/
├─ FlaskApp/
│  ├─ blueprint-folder/
│  │  ├─ blueprint-templates/
│  ├─ templates/
│  ├─ static/
│  ├─ tests/
├─ run.py
├─ run_tests.py
```

## Flask Blueprints

### **`site_bp`** - main blueprint that responsible for the main page of the application

Blueprint functions:

**`main`** - get function. Renders main page

**`render_order`** - post function. 
It takes in a form object containing personal_n and date fields and validates it. 
If the form's data is valid, it retrieves the corresponding WorkingOrder data from the database and renders it on the web page. 
Otherwise, it just renders an empty web page.

## Models

### **`WorkingOrder`** model

Model functions:

**`get_by_personal_n`** - Retrieving all WorkingOrder records from the database that match the provided personal_n and date. 
It then orders the results by departure_time and returns all of the results as a list.

## Configs

**`Config`** - base config class 

**`ProductionConfig`** - config will be used if in **`.env`**  is **`FLASK_DEBUG=0`**.
You can set different **`SQLALCHEMY_DATABASE_URI`** for prod database

**`DevelopmentConfig`** -  config will be used if in **`.env`**  is **`FLASK_DEBUG=1`**. 
Use this config for dev

**`TestingConfig`** - config will be used when testing app with pytest.


## Tests

### All tests documentation is in tests func files, but TL;DR im testing:
1. Model method **`get_be_personal_n`**
2. Right config conf and if there is **`.env`** file
3. App functions

## Other functions 

**`create_app`** - Factory app function

**`create_database_url`** - creates url from **`.env`** params


# Developers

- [NikZip](https://github.com/NikZip)

# License
This app is distributed under the MIT license.
