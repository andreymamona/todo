# todo

About
-----

Simpliest web app for making notes

[![License](https://img.shields.io/badge/license-BSD-blue.svg)](https://raw.githubusercontent.com/manti-by/Manti.by/master/LICENSE)

Author: Andrey Mamona <andrey.jbjv@gmail.com>

Source link: https://github.com/andreymamona/todo

Setup dev environment
---------------------

1. Download 'todo' dir to your machine
2. install Python3
3. install, configure and run virtual environment

    $ cd ~/todo/
    $ virtualenv -p python3 --prompt=todo .venv/
    $ python3 -m venv --prompt=todo .venv/
    $ source .venv/bin/activate

4. install framework and libraries (in a virtual environment)

    $ pip install django crispy-bootstrap5 psycopg2-binary

5. change SECRET_KEY in /todo/todo/settings.py
6. change settings for DB in /todo/todo/settings.py
7. run django server and enjoy it on 127.0.0.1

    $ python manage.py runserver