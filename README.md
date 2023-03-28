## Install / Develope
```
sudo apt-get install python3 python3-venv

python3 -m venv env
source env/bin/activate

## Install
python3 -m pip install -r requirements.txt

## Run
export SECRET_KEY="your secret key"
export DATABASE_URI="postgresql://username:password@host:port/database_name"
export FLASK_APP=app_name
flask run

## Create Requirements.txt
python3 -m pip install pip-tools
pip-compile --resolver=backtracking pyproject.toml
```

## Run
```
python3 -m pip install waitress
waitress-serve --port=5000 --call 'app:create_app'
```