#!/bin/bash

source "$PYTHONPATH/activate" && {
# log which migrations have already been applied
# migrate
python manage.py collectstatic --noinput;
}

