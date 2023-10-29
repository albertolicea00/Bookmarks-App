#!/bin/bash

# Activar el entorno virtual de tu proyecto Django
source env/Scripts/activate

# Ejecutar el back-end
cd api
python manage.py migrate
python manage.py runserver
cd ..

# Ejecutar el front-end
cd app
npm run serve
cd..
