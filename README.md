# Compiler Exploter

## Roadmap

- [x] Create the roadmap
- [x] Choose a good lightweight HTTP framework: FastAPI
- [x] Choose useful packages to work with Git, cmake, zip from Python
- [x] Create POST endpoint accepting a git URL
- [x] Clone repo
- [x] Compile code
- [x] Zip code and return back

Took: 1h 12' to be functional

### Extras

- [x] Add possibility of selecting git branch
- [x] Caching strategies
- [x] Improve code and architecture quality
- [x] Sanitizers / Linter / Formatter
Took: 3h 50'

- [ ] Accept git token if private repository is given
- [ ] Add support for downloading dependencies
- [ ] Track user -> keep stats
- [ ] Login / Register -> token
- [ ] Return progress (websocket)

- [x] Add git hooks
- [ ] Create a CI on GitHub


## Set Up

This project uses `poetry` ([download page](https://python-poetry.org/docs/#installation))

Install dependencies:

```sh
poetry install
```

### Pass formatter and linters

```sh
poetry run black --check .
poetry run ruff check .
poetry run mypy compiler_exploter
```

## Run

```sh
poetry run start
```
