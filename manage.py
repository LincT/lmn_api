#!/usr/bin/env python
import os
import sys

from django.contrib.auth.hashers import make_password

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lmn_project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # generate password   at terminal execute 'python manage.py runserver'  will exit before running server
    # excrypt = make_password('qwerqwer')
    # print(excrypt)
    # exit()

    execute_from_command_line(sys.argv)
