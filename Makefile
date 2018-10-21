default:
	echo "nothing"

clean:
	rm -rf .eggs .mypy_cache .pytest_cache .tox beckonjira.egg-info build .coverage

release:
	python3 setup.py sdist bdist_wheel

format:
	isort --recursive src -y
	black .

test: format
	tox
