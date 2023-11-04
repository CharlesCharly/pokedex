# Pokedex

## Summary

- [App information](#app-information)
- [Installation Backend](#installation-backend)
  - [Prerequisites](#prerequisites)
  - [Install dependencies](#install-dependencies)
  - [Django commands](#django-commands)
- [Installation Frontend](#installation-frontend)
  - [Install modules](#install-modules)
  - [Nuxt commands](#nuxt-commands)
- [Resources](#resources)

## App information

- App name : Pokedex
- Description : Scroll through Pokemons, filter them and display the detail of one
- App links :
  - [Repo](https://github.com/CharlesCharly/pokedex)

## Installation backend

### Prerequisites

Populate your `.env` file with secret values as below

```sh
DEBUG=True
# Setup a secret key
SECRET_KEY=

# Database config
DB_NAME=pokedex
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=5432

```

### Install dependencies

```sh
# Set up your python virtual env
python.exe -m venv venv

# Activate it
.\venv\Scripts\Activate

# Install modules and packages
pip install -r requirements. txt

# Get the migrations
python manage.py migrate

# Import the CSV data into your DB
python manage.py import_data
```

### Django commands

```sh
# Run the Django server
python .\manage.py runserver

# Run the tests
python manage.py test
```

Open [http://localhost:8000](http://localhost:8000) if you need to

## Installation frontend

### Install modules

```sh
# Install node modules
npm install
```

### Nuxt commands

```sh
# Run the Nuxt.js server
npm run dev

# Build the project
npm run build
```

## Resources

Backend

- [Django](https://www.djangoproject.com/) - Python Framework
- [Dotenv](https://github.com/theskumar/python-dotenv) - Reads value from .env file

Frontend

- [Vue 2](https://v2.vuejs.org/) - JS Framework
- [Nuxt 2](https://v2.nuxt.com/) - Vue Framework
- [Axios](https://github.com/axios/axios) - Promise based HTTP client
- [Vuex-map-fields](https://github.com/maoberlehner/vuex-map-fields) - 2-way data binding
- [ApexCharts](https://apexcharts.com/) - Opensource charts
- [Tailwind CSS](https://tailwindcss.com/) - CSS Framework
