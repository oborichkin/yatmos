PROJECT_NAME = yatmos

.PHONY = test build push clean hooks

run: venv
	$(VENV)/uvicorn yatmos.main:app --reload

install: venv hooks

test: venv
	ENVIRONMENT=testing $(VENV)/pytest --cov=$(PROJECT_NAME) --cov-report=html --cov-report=term tests/

hooks: venv
	$(VENV)/pre-commit install

image:
	docker build -t $(PROJECT_NAME) .

build: venv clean
	$(VENV)/python setup.py sdist bdist_wheel

sphinx: venv
	. $(VENV)/activate && cd docs && $(MAKE) html

clean:
	rm -rf build dist *.egg-info

include Makefile.venv
Makefile.venv:
	curl \
		-o Makefile.fetched \
		-L "https://github.com/sio/Makefile.venv/raw/v2020.08.14/Makefile.venv"
	echo "5afbcf51a82f629cd65ff23185acde90ebe4dec889ef80bbdc12562fbd0b2611 *Makefile.fetched" \
		| sha256sum --check - \
		&& mv Makefile.fetched Makefile.venv
