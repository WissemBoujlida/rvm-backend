# rvm-backend - Academic project

A simple API consumed through a mobile app to help users track their recycling history and rewards. The API is also used to send recycling data even when users are not logged in. This allows us to collect data and build real-time dashboards and statistics.

# Technologies used to build the project

Python, Django, PostgreSQL

# Running the application

First, install all the required python packages (always use a virtual environment).

```shell
pip install -r requirements.txt
```

To run the application on your local machine, make sure to change directory to the `project directory` and simply execute: 

```shell
python manage.py runserver 0.0.0.0:8000
```

Notes: Make sure to change the database configuration at `api/settings.py`. 
