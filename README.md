## Did you install git client on your machine?
## How to clone the repository
	git clone <repository>
## How to install virtualenv
	pip install virtualenv
## How to make the env by virtualenv in project.
	cd {project_folder}
	virtualenv env
## How to activate the env
	# case of Linux
	source env/bin/activate
	# case of windows
	env/scripts/activate
## How to install packages
	pip install -r requirements.txt
## Run server

	python manage.py run

Bydefault Flask dev server run on host `127.0.0.1` (`localhost`) and port `5000`. You configure default port and host in `config.py`.

You can also specify `port` and `host` as a commandline params while running the dev server.

	python manage.py run --host 0.0.0.0 --port 9000
![ScreenShot](https://raw.githubusercontent.com/app-generator/flask-mongo-binance-api/main/static/Capture.PNG?raw=true "Demo")
![screenshot](https://github.com/dipendrabaidawa/flask-mongo-binance-api/main/static/Capture.PNG?raw=true)
