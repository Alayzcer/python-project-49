install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 brain_games
