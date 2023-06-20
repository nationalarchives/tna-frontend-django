# The National Archives Frontend Django Templates

Django templates implementation of [TNA components](https://github.com/nationalarchives/tna-frontend) for inclusion in Python applications.

```sh
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
python manage.py runserver 8080
```

```sh
python3 -m build
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*
```
