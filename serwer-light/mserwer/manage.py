#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from datetime import date
from django.conf import settings


def main():
    """Run administrative tasks."""
    try:
        file = open("lol.txt", 'w')
        file.write("xd")
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mserwer.settings')
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        today = date.today()
        author = "Bartosz Kędziorek"
        port = settings.SERVER_PORT
        print("Autor: {}".format(author))
        print("Port: {}".format(port))
        print("Data: {}".format(today))
        execute_from_command_line(sys.argv)
    except Exception as e:
        file = open("error.txt", 'w')
        file.write(e)
        raise e


if __name__ == '__main__':
    main()
