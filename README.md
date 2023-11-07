# skillbasedroleportal

Skill Based Role Portal: IS212 G2T2 - Ais Kachang

## Table of Contents

- [Description](#description)
  - [Built with](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Frontend](#frontend)
  - [Backend](#backend)
- [Development](#development)
- [Testing](#testing)
- [Roadmap](#roadmap)
- [Acknowledgements](#acknowledgements)
- [Authors](#authors)

## Description

![Homepage](images/Home.png)

This project aims to be a skill based role portal that allows users to upskill themselves by searching and applying for company-internal roles based on their skills and experience. HR/admins of the portal will be able to add new role listings. It is built with the frontend using Vue.JS and the backend using Python Flask. The database used is MySQL.

### Built With

- <a href="https://vuejs.org/"><img src="images/vue.png" alt="Vue" width="50"></a>
- <a href="https://flask.palletsprojects.com/en/3.0.x/"><img src="images/flask.png" alt="Python Flask" width="50"></a>
- <a href="https://www.mysql.com/"><img src="images/sql.png" alt="MySQL" width="50"></a>
- <a href="https://getbootstrap.com/"><img src="images/bootstrap.png" alt="Bootstrap" width="50"></a>
- <a href="https://tailwindcss.com/"><img src="images/tailwind.png" alt="TailwindCSS" width="50"></a>

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/en/) (v18.x)
- [MySQL](https://dev.mysql.com/downloads/mysql/) (v8.0)
- [Python](https://www.python.org/downloads/) (v3.11)

### Frontend

For the frontend, simply run the commands below.

```bash
# In root directory
cd frontend
npm install

```

### Backend

For the backend, we will be using Python Flask and a local MySQL server. No API keys are required for this application.

```bash
# In root directory
cd backend
pip/pip3 install -r requirements.txt
```

Next, create a .env file with the following contents:

```python
# In backend directory
DB_USER=root
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=3306
```

### Local MySQL database

For the sample data, it is not stored in the repo, but you may use execute [init.sql](https://github.com/darylcwx/skillbasedroleportal/blob/main/init.sql) as the schema for the database, then load a .csv with their respective SQL table columns like so:

```bash
# In root directory
python load_init_sql.py
```

## Development

For development, you may run both the frontend and backend concurrently on separate terminals.

```bash
# In frontend directory
npm run dev

# In backend directory
flask run
```

**OR**

```bash
# In root directory
python startServices.py
```

On frontend you should see this:

```bash
  VITE v4.4.9  ready in XXX ms

  ➜  Local:   http://127.0.0.1:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help
```

And on the backend you should see this:

```bash
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

This means that once you load the data in correctly, the application will be fully functional.

### Testing

Up your frontend and backend [manually](#development)

**OR**

```bash
# In root directory
python startServices.py
```

#### Manual

You may run frontend Selenium testing like so:
([pytest docs](https://docs.pytest.org/en/6.2.x/usage.html))

```bash
# In root/selenium_tests/
pytest -k "positive or negative or boundary" --html=report.html —self-contained-html
```

You may run backend unit and integration tests like so:

```bash
# In root/backend/tests/
python unit_tests.py
```

#### CI/CD

A [Github Actions Workflow](https://github.com/darylcwx/skillbasedroleportal/blob/main/.github/workflows/actions.yml) has been setup to run the above tests.

### Style

- [/frontend/vite.config.js](https://github.com/darylcwx/skillbasedroleportal/blob/main/frontend/vite.config.js)
- [/frontend/src/scss/custom.scss](https://github.com/darylcwx/skillbasedroleportal/blob/main/frontend/src/scss/custom.scss)

## Roadmap

Tentatively, this application was done up for a school project and will possibly not be maintained in the future.

- [ ] First release (v1.0.0 - 07/11/23)
- [ ] Upcoming release (TBC 😢)

## Acknowledgements

- [Chris Poskitt](https://cposkitt.github.io/)
- [Lee Kok Khing](https://www.linkedin.com/in/lee-kok-khing-b074b69/)
- [SQL Alchemy](https://www.sqlalchemy.org/)
- [Vue 3 Datepicker](https://vue3datepicker.com/)
- [Hero icons](https://heroicons.dev/)

## Authors

- [Xavier Low](https://github.com/xavierlowjunjie)
- [Yoo Jia Ler](https://github.com/ninjachicken100)
- [Jada Tan](https://github.com/jadatanjq)
- [Oh Wen Hai](https://github.com/wenhai-smu)
- [Lem Wai Soon](https://waisoon123.github.io/)
- [Daryl Chua](https://darylchua.vercel.app)
