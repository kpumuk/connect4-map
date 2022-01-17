# Connect 4 Map Renderer

## Installation

```bash
pip3 install -r requirements.txt
```

## Start

```bash
python3 -m flask run
```

Now you can open http://127.0.0.1:5000/map/000000000000000000000000000000100000200000 to test

## Deployment to Heroku

### Pre-Requisites

```bash
brew tap heroku/brew && brew install heroku
heroku login
heroku git:remote -a connect4-map
```

### Deployment

Commit your changes to the repository, then run:

```bash
git push heroku main
```
