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

# building-plans-approvals-be
Building plans approval application with ReactJs and Python

# table of contents


# about

# prerequisites
Django
MySQL db

# project structure
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

# available scripts

```mysql -u root -p```

```python manage.py makemigrations```

```python manage.py migrate```


# how to set up the application
Clone the application from github

```git clone url```

Activate your virtual environment

```source venv/bin/activate```

Install the app requirements

```pip install -r requirements.txt```

Run the application

```python manage.py runserver```

# features

* [] Approvals cost calculator
* [] Scrape building construction articles (AAK, NCA)
* [] Upload documents for approval

# usage
# authors

**Sharon Korir**
- website
- contact information

**Tressie Muthuri**
- website
- contact information