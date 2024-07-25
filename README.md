# Building-plans-approvals-be
Building plans approval application with ReactJs and Python

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Project description

**Overview of the project**
- Obtaining a [building permit](https://buildhub.aak.or.ke/approval)
- Building approvals in Kenya vary based on factors like project type, size, estimated expenses, and location. Counties operate their own system for reviewing and [granting permits](https://www.buyrentkenya.com/discover/step-by-step-process-of-obtaining-building-permits-in-kenya#:~:text=There%20are%20four%20mandatory%20construction,EIA%20license%2FNEMA%20approval), adding complexity to the process.
- Construction approvals' procedures, regulations, and associated costs vary significantly depending on factors such as the type of structure, its size, estimated expenses, and its geographical location.
- There are four mandatory construction approvals in Kenya:
    - Architectural plan approval
    - Structural plan approval
    - EIA license/NEMA approval
    - NCA project registration

- This list is not exhaustive but represents the standard prerequisites for most building developments across Kenyan counties before construction begins.

**Documents Required**

- Copy of ownership documents
- Application for development permission (PPA 1 form) (original)
- PPA1 payment receipt
- Survey plan- from Survey Kenya
- Rates clearance certificate(copy)
- Architectural drawings 
- Structural drawings 
- Structural design calculations 
- Official land search 
- Architect's practicing certificate (copy)
- Engineer's practicing certificate (copy)

**Fees charged**

* [x] Building approval application form – Kshs. 1,000
* [x] Architectural plans (plinth area per m2)
    Customization of drawing for ABT – Kshs. 5,000
* [] Structural plans
    Commercial – Kshs. 10,000
    Residential – Kshs. 7,000
    Industrial – Kshs. 20,000
    Educational – Kshs. 5,000
    Religious – Kshs. 2,500
    Petrol station – Kshs. 10,000
    Application fee for containers – Kshs. 20,000
* [] Alteration of building plans – Kshs. 5,000
* [x] Site board 
    Application  – Kshs. 1,500
    License fee  – Kshs. 15,000

# Project status
* [x] Deployment status: Hosted on Railway [Approvals APIs](https://approvals-api.up.railway.app/)

# Project structure
```
└── 📁building-plans-approvals-be
    └── .gitignore
    └── 📁.venv
    └── LICENSE
    └── README.md
    └── 📁approvals
        └── .env
        └── Dockerfile
        └── Procfile
        └── 📁approvals
        └── 📁authorization
        └── 📁calculator
        └── db.sqlite3
        └── manage.py
        └── railway.toml
        └── requirements.txt
        └── runtime.txt
        └── 📁upload
```

# Prerequisites
Django
Postgres db


# Project setup
## Local setup
How to set up the application

**`git clone url`**
Clone the application from github

**`source venv/bin/activate`**
Activate your virtual environment

**`pip install -r requirements.txt`**
Install the app requirements

**`python manage.py runserver`**
Run the application

## Available scripts

**`mysql -u root -p`**

**`python manage.py makemigrations`**

**`python manage.py migrate`**

**`python manage.py populate_counties`**

**`python manage.py populate_project_types`**

**`python manage.py migrate <Django app name> zero`**
Rollback migrations.\
Replace with the actual name of the Django app

**`python manage.py flush`**
Remove all data from the database and re-executes any post-synchronization handlers

**This project needs to have**
* [x] A Frontend
* [x] An (API)[https://approvals-api.up.railway.app/]
* [x] [Database](https://www.meetgor.com/django-deploy-railway/#google_vignette)
* [] A blog post about what is built and why.
* [] Documentation which includes system diagrams, API specs etc.
* [] Monitoring and Logging (for extra credit)

# Authors

**Tressie Muthuri**
- website
- contact information

# Collaborators

**Sharon Korir**
- website
- contact information

# References
[working with mysql db](https://blog.devart.com/mysql-command-line-client.html#How-to-use-MySQL-command-line-client?)

[Setting up Docker and CircleCI](https://circleci.com/blog/continuous-integration-for-django-projects/)

[Connect ReactJs and Django](https://medium.com/@devsumitg/how-to-connect-reactjs-django-framework-c5ba268cb8be)
