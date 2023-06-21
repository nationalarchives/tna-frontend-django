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
python manage.py runserver 8080
node tasks/test.mjs
```

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
