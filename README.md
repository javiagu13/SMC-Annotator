<div align="center" style="height:150px; width=200px">
  <img src="https://github.com/javiagu13/SMC-Annotator/blob/main/frontend/assets/icon.png">
</div>

# SMC Annotator

Samsung Medical Center (SMC) Annotator is an open-source text annotation tool for humans. It provides annotation features for text classification, sequence labeling, and sequence to sequence tasks. You can create labeled data for sentiment analysis, named entity recognition, text summarization, and so on. Just create a project, upload data, and start annotating. You can build a dataset in hours.

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

## Installation guide:

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
celery --app=config worker --loglevel=INFO --concurrency=1 -P eventlet
```

#### Node Prompt #1 AS ADMIN
```
cd frontend
yarn dev
```


## Documentation
This tool has been built on top of the open source software doccano. For further documentation please visit:
<https://doccano.github.io/doccano/>.