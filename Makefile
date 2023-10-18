.PHONY: dev init test

test:
	pytest -sv

# Initialize development environment
init:
	pip install --upgrade pip
	pip install --upgrade pip-tools
	test -e requirements.in || touch requirements.in

# Add required Python dependencies
dev: requirements.txt
	pip install -r $<

# Compile dependencies and lock versions
requirements.txt: requirements.in
	pip-compile
