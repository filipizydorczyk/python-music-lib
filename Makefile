init:
	pip install -r requirements.txt

test:
	py.test

develop:
	python setup.py develop

install:
	python setup.py install