#!/usr/bin/bash

export DJANGO_SETTINGS_MODULE=goodsshop.settings.local
cd ./goodsshop
python3 manage.py runserver
