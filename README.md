# The National Archives Frontend Django Templates

[![Main build status](https://github.com/nationalarchives/tna-frontend-django/actions/workflows/test.yml/badge.svg?branch=main&event=push)](https://github.com/nationalarchives/tna-frontend-django/actions/workflows/test.yml?query=branch%3Amain)
[![Latest release](https://img.shields.io/github/v/release/nationalarchives/tna-frontend-django?style=flat-square&logo=github&logoColor=white&sort=semver)](https://github.com/nationalarchives/tna-frontend-django/releases)
[![PyPi version](https://img.shields.io/pypi/v/nationalarchives-frontend-django?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/nationalarchives-frontend-django/)
![Python version](https://img.shields.io/pypi/pyversions/nationalarchives-frontend-django?style=flat-square&logo=python&logoColor=white)
[![Licence](https://img.shields.io/github/license/nationalarchives/tna-frontend-django?style=flat-square)](https://github.com/nationalarchives/tna-frontend-django/blob/main/LICENCE)

Django templates implementation of [TNA components](https://github.com/nationalarchives/tna-frontend) for inclusion in Python applications.

```sh
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
npm install
python manage.py runserver 8080
node tasks/test.mjs
```

http://localhost:8080/components/

```sh
flake8 . --max-complexity=10 --max-line-length=120
isort .
black .
```

```sh
python3 -m build
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*
```

## How to use in your own Django project

### Templates

1. Install the `nationalarchives-frontend-django` package from PyPi

```python
from distutils.sysconfig import get_python_lib

TEMPLATES = [
    {
        "DIRS": [
            os.path.join(get_python_lib(), "nationalarchives-frontend-django/templates")
        ],
    }
]
```

### Styles

Install the `@nationalarchives/frontend` package from npm with `npm install @nationalarchives/frontend`

Add the config to enable you to use the static files:

```py
STATICFILES_DIRS = [
    "node_modules/@nationalarchives/frontend"
]
```

Import the stylesheet with:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'nationalarchives/all.css' %}">
```

The `@nationalarchives/frontend` package also includes the SCSS if you wish to compile the CSS yourself.
