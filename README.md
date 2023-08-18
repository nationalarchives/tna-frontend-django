# The National Archives Frontend Django Templates

[![Main build status](https://img.shields.io/github/actions/workflow/status/nationalarchives/tna-frontend-django/ci.yml?style=flat-square&event=push&branch=main)](https://github.com/nationalarchives/tna-frontend-django/actions/workflows/ci.yml?query=branch%3Amain)
[![Latest release](https://img.shields.io/github/v/release/nationalarchives/tna-frontend-django?style=flat-square&logo=github&logoColor=white&sort=semver)](https://github.com/nationalarchives/tna-frontend-django/releases)
[![PyPi version](https://img.shields.io/pypi/v/nationalarchives-frontend-django?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/nationalarchives-frontend-django/)
![Python version](https://img.shields.io/pypi/pyversions/nationalarchives-frontend-django?style=flat-square&logo=python&logoColor=white)
[![Licence](https://img.shields.io/github/license/nationalarchives/tna-frontend-django?style=flat-square)](https://github.com/nationalarchives/tna-frontend-django/blob/main/LICENCE)

Django templates implementation of [TNA components](https://github.com/nationalarchives/tna-frontend) for inclusion in Python Django applications.

```sh
# Create a virtual environment
python3 -m venv venv
. ./venv/bin/activate

# Install the dependencies
pip install -r requirements.txt
npm install

# Run the server
python manage.py runserver 8080
```

http://localhost:8080/

```sh
# Run the tests against the running server
node tasks/test.mjs
```

<!--
```sh
python3 -m build
python3 -m pip install --upgrade twine
# python3 -m twine upload --repository testpypi dist/*
python3 -m twine upload dist/*
```
-->

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
