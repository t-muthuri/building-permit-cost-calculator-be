# Building-plans-approvals-be
Building plans approval application with ReactJs and Python

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [building-plans-approvals-be](#building-plans-approvals-be)
- [table of contents](#table-of-contents)
- [about](#about)
- [prerequisites](#prerequisites)
- [project structure](#project-structure)
- [available scripts](#available-scripts)
- [how to set up the application](#how-to-set-up-the-application)
- [features](#features)
- [usage](#usage)
- [authors](#authors)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# About

# Prerequisites
Django
MySQL db

# Project structure
```
└── 📁building-plans-approvals-be
    └── LICENSE
    └── PROJECT.md
    └── README.md
    └── 📁approvals
        └── __init__.py
        └── 📁__pycache__
            └── ...
        └── asgi.py
        └── settings.py
        └── urls.py
        └── wsgi.py
    └── 📁authorization
        └── ...
    └── 📁calc
        └── ...
    └── db.sqlite3
    └── manage.py
    └── requirements.txt
    └── 📁venv
        └── ...
```

# Available scripts

### `mysql -u root -p`

### `python manage.py makemigrations`

### `python manage.py migrate`

### `python manage.py populate_counties`

### `python manage.py migrate <Django app name> zero`
Rollback migrations.\
Replace with the actual name of the Django app

### `python manage.py flush`
Remove all data from the database and re-exectes any post-synchronization handlers


# How to set up the application

### `git clone url`
Clone the application from github

### `source venv/bin/activate`
Activate your virtual environment

### `pip install -r requirements.txt`
Install the app requirements

### `python manage.py runserver`
Run the application

# Dependencies
- [django-rest-framework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)


# Features

* [] Approvals cost calculator
* [] Scrape building construction articles (AAK, NCA)
* [] Upload documents for approval
* [] Materials cost calculator

# Usage

# To do
* [] Authorization - two users (client, the county approver)
* [] Models - related to uploading documents for approval feature
* [x] Set up the backend
* [x] Set up MySQL db ... confirm
* [] Set up circleci for tracking changes and deploying
* [x] Set up formatter for a homogenous code syntax - using autopep 8 extension atm
* [] Set up files for formatting the code syntax
* [x] Calculate the cost of approvals in Nairobi county for a residential unit
* [] use the county data to calculate cost of approvals successfully (rough estimate)
* [] set up an automated build server - research on how to do this first
* [] Estimate the cost of materials needed for a simple one bedroom house in Kenya - post the quantities with estimated prices (table)
* [] thoroughly research on how you have populated the counties and project types and prices
* [] Post calculator data from the fe
    * [x] Create django models
    * [x] Create django views to receive data from the fe (POST)
    * [x] Restful APIs for react to fetch and modify data
    * [x] Validation logic using serializers
    * [x] Handle errors gracefully 
    * [] implement security measures


# To research on
* [] setting up mysql and django
* [] what is jazzmin

# Notes
[Setting up Docker and CircleCI](https://circleci.com/blog/continuous-integration-for-django-projects/)
[Connect ReactJs and Django](https://medium.com/@devsumitg/how-to-connect-reactjs-django-framework-c5ba268cb8be)


# References
- [working with mysql db](https://blog.devart.com/mysql-command-line-client.html#How-to-use-MySQL-command-line-client?)

# Overview of the project
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
    

# Authors

**Sharon Korir**
- website
- contact information

**Tressie Muthuri**
- website
- contact information