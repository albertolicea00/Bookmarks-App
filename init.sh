#!/bin/bash

# Activar el entorno virtual de tu proyecto Django
if [[ "$OSTYPE" == "linux-gnu" ]]; then
    source env/bin/activate
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    source env/Scripts/activate
else
    echo "Sistema operativo o shell incompatible."
    exit 1
fi

# Inicia el servidor de Django
cd api
python manage.py runserver &

# Espera unos segundos para asegurarte de que el servidor de Django esté en funcionamiento
sleep 5

# Inicia el servidor de React
cd ../app
npm start
