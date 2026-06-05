# -*- coding: utf-8 -*-
"""Prepare the app before Render starts Gunicorn."""

import os

from app import app, get_db, init_db


def table_count(table_name):
    return get_db().execute(f"SELECT COUNT(*) AS total FROM {table_name}").fetchone()["total"]


def should_seed_on_empty():
    value = os.environ.get("LINGO_SEED_ON_EMPTY", "").strip().lower()
    return value in {"1", "true", "yes", "on"}


def main():
    with app.app_context():
        init_db()
        if should_seed_on_empty() and table_count("materials") == 0 and table_count("courses") == 0:
            from seed_real_data import main as seed_real_data

            seed_real_data()


if __name__ == "__main__":
    main()
