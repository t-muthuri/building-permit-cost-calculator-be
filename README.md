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

```mysql -u root -p```

```python manage.py makemigrations```

```python manage.py migrate```

```python manage.py populate_counties```


# How to set up the application
Clone the application from github

```git clone url```

Activate your virtual environment

```source venv/bin/activate```

Install the app requirements

```pip install -r requirements.txt```

Run the application

```python manage.py runserver```

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
* [] Set up formatter for a homogenous code syntax
* [] Calculate the cost of approvals in Nairobi county for a residential unit
* [] set up an automated build server - research on how to do this first
 *[] Estimate the cost of materials needed for a simple one bedroom house in Kenya - post the quantities with estimated prices (table)


# To research on
* [] setting up mysql and django

# Notes
[Setting up Docker and CircleCI](https://circleci.com/blog/continuous-integration-for-django-projects/)
[Connect ReactJs and Django](https://medium.com/@devsumitg/how-to-connect-reactjs-django-framework-c5ba268cb8be)


# References
- [working with mysql db](https://blog.devart.com/mysql-command-line-client.html#How-to-use-MySQL-command-line-client?)

# Overview of the project
- Building approvals in Kenya vary based on factors like project type, size, estimated expenses, and location. Counties operate their own system for reviewing and [granting permits](https://www.buyrentkenya.com/discover/step-by-step-process-of-obtaining-building-permits-in-kenya#:~:text=There%20are%20four%20mandatory%20construction,EIA%20license%2FNEMA%20approval), adding complexity to the process.
- Construction approvals' procedures, regulations, and associated costs vary significantly depending on factors such as the type of structure, its size, estimated expenses, and its geographical location.
- There are four mandatory construction approvals in Kenya:
    - Architectural plan approval
    - Structural plan approval
    - EIA license/NEMA approval
    - NCA project registration

- This list is not exhaustive but represents the standard prerequisites for most building developments across Kenyan counties before construction begins.

- [Nairobi County Approvals](https://integrum.co.ke/construction-permits-in-kenya-nairobi-building-approval-costs/#Building_Approval_Costs_In_Nairobi)

# Authors

**Sharon Korir**
- website
- contact information

**Tressie Muthuri**
- website
- contact information