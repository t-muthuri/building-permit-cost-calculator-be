# to do
* [] Authorization - two users (client, the county approver)
* [] Models - related to uploading documents for approval feature
* [x] Set up the backend
* [x] Set up MySQL db ... confirm
* [] Set up circleci for tracking changes and deploying
* [] Set up formatter for a homogenous code syntax

# to research on
* [] setting up mysql and django

# Notes
[Setting up Docker and CircleCI](https://circleci.com/blog/continuous-integration-for-django-projects/)

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


# references
- [working with mysql db](https://blog.devart.com/mysql-command-line-client.html#How-to-use-MySQL-command-line-client?)