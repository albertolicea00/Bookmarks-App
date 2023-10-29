# Gestor de Marcadores

Este proyecto es un gestor de marcadores que te permite guardar y organizar tus enlaces favoritos. Proporciona una interfaz de usuario web desarrollada con React para consumir una API de Django Rest.

## Características

- Agregar nuevos marcadores con título, URL y descripción.
- Organizar marcadores en categorías.
- Buscar marcadores por título o categoría.
- Editar y eliminar marcadores existentes.
- Interfaz intuitiva y fácil de usar.

## Requisitos previos

- Node.js: [Instalar Node.js](https://nodejs.org/)
- Python: [Instalar Python](https://www.python.org/)

## Configuración del proyecto

1. Clona este repositorio: `git clone <URL_DEL_REPOSITORIO>`
2. Ve al directorio del proyecto: `cd <NOMBRE_DEL_DIRECTORIO>`
3. Instalar las dependencias de python: `pip install -r requirements.txt`
4. Instala las dependencias de nodejs: `npm install`
5. Configura la conexión a la base de datos en el archivo `.env`.
6. Inicia la aplicación back-end: `python manage.py run server`
7. Inicia la aplicación front-end: `npm start`

## Uso
- Accede a la aplicación React a través de tu navegador en [http://localhost:3000](http://localhost:3000).
- La API Django Rest estará disponible en [http://localhost:8000](http://localhost:8000).
- Regístrate e inicia sesión para comenzar a utilizar el gestor de marcadores.
- Agrega, organiza, busca y administra tus marcadores desde la interfaz de usuario.

## Contribución

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Crea un fork del repositorio.
2. Crea una nueva rama para tus cambios: `git checkout -b nombre-de-la-rama`
3. Realiza tus modificaciones y realiza commits: `git commit -m "Descripción de los cambios"`
4. Haz push a la rama: `git push origin nombre-de-la-rama`
5. Crea un pull request en el repositorio original.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.