#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management import execute_from_command_line
from django_redis import get_redis_connection


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news.settings")
    try:
        cacheCon = get_redis_connection("default")
        cacheCon.flushall()
        print("Redis cache cleared.")
    except Exception as e:
        print(f"Error clearing Redis cache: {e}")

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
