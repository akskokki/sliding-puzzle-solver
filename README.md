# sliding-puzzle-solver
Data structures and algorithms student project

## Documentation
[Project specification](https://github.com/akskokki/sliding-puzzle-solver/blob/main/docs/specification.md)
#### Weekly progress reports
[Week 1](https://github.com/akskokki/sliding-puzzle-solver/blob/main/docs/week1.md)  
[Week 2](https://github.com/akskokki/sliding-puzzle-solver/blob/main/docs/week2.md)

## Installation

1. Install dependencies with

```
poetry install
```

2. Launch the game with

```
poetry run invoke start
```

## Testing
Unit tests:

```
poetry run invoke test
```

Coverage report (found in `/htmlcov/index.html`):

```
poetry run invoke coverage-report
```

Pylint static code analysis:

```
poetry run invoke lint
```
