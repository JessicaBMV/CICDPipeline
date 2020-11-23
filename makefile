setup:
	python3 -m venv ~/.CICDPipline 

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb


lint:
	#hadolint Dockerfile
	pylint --disable=R,C,W1203,E0611,W0702,W0612,W0311 app.py

all: install lint test
