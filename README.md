
# SMC Annotator

Samsung Medical Center (SMC) Annotator is an open-source text annotation tool for humans. It provides annotation features for text classification, sequence labeling, and sequence to sequence tasks. You can create labeled data for sentiment analysis, named entity recognition, text summarization, and so on. Just create a project, upload data, and start annotating. You can build a dataset in hours.

<div align="center" style="height:150px; width=200px">
  <img src="https://github.com/javiagu13/SMC-Annotator/blob/main/frontend/assets/icon.png">
</div>

## Features

- Collaborative annotation
- Multi-language support
- Mobile support
- Emoji :smile: support
- Dark theme
- RESTful API

## Requirements:

- Anaconda installed
- Node installed (Node 16.20.1 has been proven to work, untested for other versions)

## Installation and running guide:

Since SMC Annotator is a fullstack software we will need to install backend and frontend separately as well as celery for file handling:

#### Anaconda Prompt #1 AS ADMIN
```
cd backend
poetry install
poetry shell

python manage.py migrate
python manage.py create_roles
python manage.py create_admin --noinput --username "admin" --email "admin@example.com" --password "password"
python manage.py runserver
```

#### Anaconda Prompt #2 AS ADMIN
```
cd backend 
pip install eventlet
celery --app=config worker --loglevel=INFO --concurrency=1 -P eventlet
```

#### Node Prompt #1 AS ADMIN
```
cd frontend
yarn install
yarn dev
```

## Running guide:

After installation in case you want to simply running follow the next steps:

#### Anaconda Prompt #1 AS ADMIN
```
cd backend 
poetry shell
python manage.py runserver 
```

#### Anaconda Prompt #2 AS ADMIN
```
cd backend
poetry shell
celery --app=config worker --loglevel=INFO --concurrency=1 -P eventlet
```

#### Node Prompt #1 AS ADMIN
```
cd frontend
yarn dev
```

## Troubleshooting

- If you cannot login, check with F12 the error you are getting if it is CSRF related its almost sure django backend is prohibiting the entrance to the site therefore go to the following file:

```
backend/config/settings/base.py
```

Look for CSRF trusted origins and add the frontend and backend IPs to allow it.

-If you are not getting allowed to upload files chances are celery is not running properly or runing at all, so, make sure Anaconda Prompt #2 is running


## Documentation
This tool has been built on top of the open source software doccano. For further documentation please visit:
<https://doccano.github.io/doccano/>.