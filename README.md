# Connect 4 Map Renderer

## Installation

pip3 install flask pillow

## Start

FLASK_APP=map python3 -m flask run

## Heroku: Preparing to Deploy

brew tap heroku/brew && brew install heroku
heroku login
heroku git:remote -a connect4-map

## Deploy to Heroku

git push heroku main
